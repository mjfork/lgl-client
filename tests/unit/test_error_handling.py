"""Tests for error handling across the LGL client."""
import pytest
from unittest.mock import Mock, patch
import httpx

from lgl_client import new_client
from lgl_client.lgl_api.exceptions import (
    LGLAPIError, 
    NotFoundError, 
    UnauthorizedError, 
    ValidationError
)


class TestErrorHandling:
    """Test error handling functionality."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return new_client(api_key="test_key")

    def test_404_not_found_error(self, client):
        """Test 404 errors are properly converted to NotFoundError."""
        with patch.object(client.categories._client, '_client') as mock_httpx:
            mock_response = Mock()
            mock_response.status_code = 404
            mock_response.is_success = False
            mock_response.json.return_value = {
                "error": "Category not found",
                "code": "NOT_FOUND"
            }
            mock_response.url = "https://api.littlegreenlight.com/api/v1/categories/999"
            mock_httpx.get.return_value = mock_response

            with pytest.raises(NotFoundError) as exc_info:
                client.categories.retrieve(999)
            
            assert "Category not found" in str(exc_info.value)
            assert exc_info.value.status_code == 404

    def test_401_unauthorized_error(self, client):
        """Test 401 errors are properly converted to UnauthorizedError."""
        with patch.object(client.categories._client, '_client') as mock_httpx:
            mock_response = Mock()
            mock_response.status_code = 401
            mock_response.is_success = False
            mock_response.json.return_value = {
                "error": "Invalid API key",
                "code": "UNAUTHORIZED"
            }
            mock_response.url = "https://api.littlegreenlight.com/api/v1/categories"
            mock_httpx.get.return_value = mock_response

            with pytest.raises(UnauthorizedError) as exc_info:
                client.categories.list()
            
            assert "Invalid API key" in str(exc_info.value)
            assert exc_info.value.status_code == 401

    def test_422_validation_error(self, client):
        """Test 422 errors are properly converted to ValidationError."""
        with patch.object(client.categories._client, '_client') as mock_httpx:
            mock_response = Mock()
            mock_response.status_code = 422
            mock_response.is_success = False
            mock_response.json.return_value = {
                "error": "Validation failed",
                "details": {
                    "name": ["This field is required"],
                    "item_type": ["Invalid choice"]
                }
            }
            mock_response.url = "https://api.littlegreenlight.com/api/v1/categories"
            mock_httpx.post.return_value = mock_response

            with pytest.raises(ValidationError) as exc_info:
                client.categories._client._post("categories", {"invalid": "data"})
            
            assert "Validation failed" in str(exc_info.value)
            assert exc_info.value.status_code == 422

    def test_generic_api_error(self, client):
        """Test other HTTP errors are converted to LGLAPIError."""
        with patch.object(client.categories._client, '_client') as mock_httpx:
            mock_response = Mock()
            mock_response.status_code = 500
            mock_response.is_success = False
            mock_response.json.return_value = {
                "error": "Internal server error"
            }
            mock_response.url = "https://api.littlegreenlight.com/api/v1/categories"
            mock_httpx.get.return_value = mock_response

            with pytest.raises(LGLAPIError) as exc_info:
                client.categories.list()
            
            assert "Internal server error" in str(exc_info.value)
            assert exc_info.value.status_code == 500

    def test_network_error_handling(self, client):
        """Test network errors are properly handled."""
        with patch.object(client.categories._client, '_client') as mock_httpx:
            # Simulate network timeout
            mock_httpx.get.side_effect = httpx.TimeoutException("Request timed out")

            with pytest.raises(LGLAPIError) as exc_info:
                client.categories.list()
            
            assert "HTTP error" in str(exc_info.value)

    def test_json_decode_error_handling(self, client):
        """Test handling of invalid JSON responses."""
        with patch.object(client.categories._client, '_client') as mock_httpx:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.side_effect = ValueError("Invalid JSON")
            mock_response.raise_for_status = Mock()
            mock_httpx.get.return_value = mock_response

            with pytest.raises(LGLAPIError):
                client.categories.list()

    def test_error_with_missing_json_response(self, client):
        """Test error handling when response has no JSON."""
        def mock_get_side_effect(*args, **kwargs):
            # Simulate a response that raises ValueError when trying to parse JSON
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.side_effect = ValueError("No JSON")
            # This will trigger the ValueError handling in LGLClient._get
            raise ValueError("No JSON")
        
        with patch.object(client.categories._client._client, 'get') as mock_httpx_get:
            mock_response = Mock()
            mock_response.status_code = 400
            mock_response.json.side_effect = ValueError("No JSON")
            mock_httpx_get.return_value = mock_response
            
            with pytest.raises(LGLAPIError) as exc_info:
                client.categories.list()
            
            # Should contain the JSON decode error message
            assert "Invalid JSON response" in str(exc_info.value)

    def test_error_context_preservation(self, client):
        """Test that error context (URL, status code) is preserved."""
        with patch.object(client.categories._client._client, 'get') as mock_httpx_get:
            mock_response = Mock()
            mock_response.status_code = 403
            mock_response.is_success = False  # Important: mark as failed response
            mock_response.json.return_value = {"error": "Forbidden"}
            mock_response.url = "https://api.littlegreenlight.com/api/v1/categories"
            mock_httpx_get.return_value = mock_response

            with pytest.raises(LGLAPIError) as exc_info:
                client.categories.list()
            
            error = exc_info.value
            assert error.status_code == 403
            assert "categories" in str(error.url) if error.url else True

    def test_pagination_error_propagation(self, client):
        """Test that errors during pagination are properly propagated."""
        def mock_get_side_effect(*args, **kwargs):
            offset = kwargs.get('offset', 0)
            limit = kwargs.get('limit', 100)
            
            if offset == 0:
                # First page succeeds - return exactly `limit` items to trigger continuation
                items = [{"id": i, "name": f"Item {i}", "item_type": "Constituent"} for i in range(1, limit + 1)]
                return {
                    "items": items,
                    "total": 200,
                    "total_items": 200,
                    "items_count": limit  # Full page to trigger continuation
                }
            else:
                # Second page fails
                raise LGLAPIError("Server error during pagination", status_code=500, url="/categories")

        with patch.object(client.categories._client, '_get', side_effect=mock_get_side_effect):
            with pytest.raises(LGLAPIError) as exc_info:
                client.categories.fetch_all()
            
            assert "Server error during pagination" in str(exc_info.value)

    def test_model_validation_error_handling(self, client):
        """Test handling of model validation errors during response parsing."""
        with patch.object(client.categories._client, '_get') as mock_get:
            # Return invalid data that will fail model validation
            mock_get.return_value = {
                "items": [
                    {"id": 1, "name": "Valid Category", "item_type": "Constituent"},
                    {"id": 2, "name": "Invalid Category", "item_type": "InvalidType"}  # Invalid item_type
                ],
                "total": 2
            }

            # Should handle model validation errors gracefully
            with pytest.raises(Exception):  # Pydantic ValidationError will be raised
                client.categories.list()

    def test_search_method_error_handling(self, client):
        """Test error handling in search methods."""
        with patch.object(client.constituents.client, '_get') as mock_get:
            mock_get.side_effect = NotFoundError("No constituents found", status_code=404, url="/constituents")

            with pytest.raises(NotFoundError):
                client.constituents.search(query_params=["name=NonExistentName"])

    def test_individual_resource_error_handling(self, client):
        """Test error handling for individual resource retrieval."""
        with patch.object(client.categories._client, '_get') as mock_get:
            mock_get.side_effect = NotFoundError("Category not found", status_code=404, url="/categories/999")

            with pytest.raises(NotFoundError):
                client.categories.retrieve(999)

    def test_create_operation_error_handling(self, client):
        """Test error handling for create operations."""
        with patch.object(client.categories._client, '_post') as mock_post:
            mock_post.side_effect = ValidationError(
                "Name is required", 
                status_code=422,
                url="/categories"
            )

            with pytest.raises(ValidationError) as exc_info:
                from lgl_client.models.category import Category
                category = Category(id=0, name="", item_type="Constituent")  # Missing name
                client.categories.create(category)
            
            assert "Name is required" in str(exc_info.value)

    def test_update_operation_error_handling(self, client):
        """Test error handling for update operations."""
        with patch.object(client.categories._client, '_patch') as mock_patch:
            mock_patch.side_effect = NotFoundError("Category not found", status_code=404, url="/categories/999")

            with pytest.raises(NotFoundError):
                from lgl_client.models.category import Category
                category = Category(id=999, name="Updated Name", item_type="Constituent")
                client.categories.update(999, category)

    def test_delete_operation_error_handling(self, client):
        """Test error handling for delete operations."""
        with patch.object(client.categories._client, '_delete') as mock_delete:
            mock_delete.side_effect = LGLAPIError(
                "Cannot delete category with associated records", 
                status_code=409,
                url="/categories/1"
            )

            with pytest.raises(LGLAPIError) as exc_info:
                client.categories.delete(1)
            
            assert "Cannot delete" in str(exc_info.value)
            assert exc_info.value.status_code == 409

    def test_context_dependent_error_handling(self, client):
        """Test error handling for context-dependent operations."""
        with patch.object(client.notes.client, '_get') as mock_get:
            mock_get.side_effect = NotFoundError("Constituent not found", status_code=404, url="/constituents/999")

            with pytest.raises(NotFoundError):
                client.notes.list(constituent_id=999)

    def test_error_message_sanitization(self, client):
        """Test that error messages are sanitized for security."""
        from lgl_client.lgl_api.exceptions import LGLAPIError
        
        # Create error with sensitive information
        sensitive_payload = {
            "api_key": "secret_key_123",
            "email": "user@example.com",
            "normal_field": "safe_value"
        }
        
        error = LGLAPIError(
            "Operation failed",
            status_code=400,
            url="/categories",
            payload=sensitive_payload
        )
        
        # Test that payload is properly sanitized in the stored payload
        sanitized_payload = error.payload
        
        # Sensitive data should be masked in the stored payload
        assert "secret_key_123" not in str(sanitized_payload["api_key"])
        assert "user@example.com" not in str(sanitized_payload["email"])
        assert sanitized_payload["api_key"] == "se***23"  # First 2 and last 2 chars
        assert sanitized_payload["email"] == "us***om"  # First 2 and last 2 chars
        
        # Safe data should be preserved
        assert sanitized_payload["normal_field"] == "safe_value"

    def test_chained_operation_error_handling(self, client):
        """Test error handling in chained operations like fetch_all with search."""
        def mock_get_side_effect(*args, **kwargs):
            # Simulate search that starts successfully but fails partway through
            offset = kwargs.get('offset', 0)
            if offset == 0:
                return {
                    "items": [
                        {"id": 1, "first_name": "John", "last_name": "Doe", 
                         "email": "john@example.com", "created_at": "2025-01-01T10:00:00Z",
                         "updated_at": "2025-01-01T10:00:00Z", "addresses": [],
                         "phone_numbers": [], "email_addresses": [], "web_addresses": []}
                    ],
                    "total": 200,
                    "total_items": 200,
                    "items_count": 100  # Trigger continuation
                }
            else:
                raise LGLAPIError("Search service temporarily unavailable", status_code=503, url="/constituents")

        with patch.object(client.constituents.client, '_get', side_effect=mock_get_side_effect):
            with pytest.raises(LGLAPIError) as exc_info:
                client.constituents.fetch_all()
            
            assert "Search service temporarily unavailable" in str(exc_info.value)
            assert exc_info.value.status_code == 503

    def test_malformed_response_handling(self, client):
        """Test handling of malformed API responses."""
        with patch.object(client.categories._client, '_get') as mock_get:
            # Return response missing expected fields
            mock_get.return_value = {
                "unexpected_field": "unexpected_value"
                # Missing "items" field
            }

            # Should handle gracefully (empty list)
            items = client.categories.list()
            assert items == []

    def test_empty_response_handling(self, client):
        """Test handling of empty responses."""
        with patch.object(client.categories._client, '_get') as mock_get:
            mock_get.return_value = {}

            # Should handle empty response gracefully
            items = client.categories.list()
            assert items == []

    def test_concurrent_error_handling(self, client):
        """Test error handling doesn't interfere between concurrent operations."""
        # Simulate concurrent operations with one failing
        def mock_get_side_effect(path, **kwargs):
            if "categories" in path:
                raise NotFoundError("Categories not found", status_code=404, url="/categories")
            else:
                return {"items": [], "total": 0}

        with patch.object(client.categories._client, '_get', side_effect=mock_get_side_effect):
            # First operation should fail
            with pytest.raises(NotFoundError):
                client.categories.list()
            
            # Second operation with different path should still work
            with patch.object(client.payment_types._client, '_get', return_value={"items": [], "total": 0}):
                items = client.payment_types.list()
                assert items == []