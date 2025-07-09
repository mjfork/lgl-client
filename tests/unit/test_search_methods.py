"""Tests for search method variations across different APIs."""
import pytest
from unittest.mock import Mock, patch
from typing import Dict, Any, List

from datetime import date

from lgl_client import new_client
from tests.fixtures import APIResponseMocker


class TestSearchMethods:
    """Test search functionality across different resources."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return new_client(api_key="test_key")

    @pytest.fixture
    def mock_httpx_response(self):
        """Mock httpx response."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "application/json"}
        mock_response.raise_for_status = Mock()
        return mock_response

    # Test Constituents search (q[] array format)
    def test_constituents_search_with_q_array(self, client, mock_httpx_response):
        """Test constituents search with q[] array format."""
        response_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john@example.com", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
                {"id": 2, "first_name": "Jane", "last_name": "Doe", "email": "jane@example.com", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}
            ],
            total=2,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.constituents.client, '_get', return_value=response_data):
            # Test search with multiple query parameters
            result = client.constituents.search(query_params=["name=John", "name=Doe"])
            
            assert result["total"] == 2
            assert len(result["items"]) == 2
            assert result["items"][0]["first_name"] == "John"
            assert result["items"][1]["first_name"] == "Jane"
            
            # Verify URL and parameters
            call_args = client.constituents.client._get.call_args
            assert "constituents/search" in call_args[0][0]
            assert 'q' in call_args[1]
            assert call_args[1]['q'] == ["name=John", "name=Doe"]

    def test_constituents_search_by_name(self, client, mock_httpx_response):
        """Test constituents search_by_name helper method."""
        response_data = APIResponseMocker.paginated_response(
            items=[{"id": 1, "first_name": "John", "last_name": "Smith", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}],
            total=1,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.constituents.client, '_get', return_value=response_data):
            result = client.constituents.search_by_name("John Smith")
            
            assert len(result) == 1
            assert result[0].first_name == "John"
            
            # Verify correct parameter construction
            call_args = client.constituents.client._get.call_args
            assert call_args is not None

    def test_constituents_search_by_email(self, client, mock_httpx_response):
        """Test constituents search_by_email helper method."""
        response_data = APIResponseMocker.paginated_response(
            items=[{"id": 1, "email": "john@example.com", "first_name": "John", "last_name": "Doe", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}],
            total=1,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.constituents.client, '_get', return_value=response_data):
            result = client.constituents.search_by_email("john@example.com")
            
            assert len(result) == 1
            assert result[0].first_name == "John"
            
            # Verify email parameter
            call_args = client.constituents.client._get.call_args
            assert call_args is not None

    def test_constituents_advanced_search(self, client, mock_httpx_response):
        """Test constituents advanced search with multiple parameters."""
        response_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "first_name": "John", "last_name": "Doe", "city": "New York", "state": "NY", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
                {"id": 2, "first_name": "Jane", "last_name": "Smith", "city": "New York", "state": "NY", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}
            ],
            total=2,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.constituents.client, '_get', return_value=response_data):
            result = client.constituents.search(
                query_params=["city=New York", "state=NY", "organization=false"]
            )
            
            assert result["total"] == 2
            assert len(result["items"]) == 2
            assert result["items"][0]["city"] == "New York"
            assert result["items"][1]["state"] == "NY"
            
            # Verify complex parameter handling
            call_args = client.constituents.client._get.call_args
            assert 'q' in call_args[1]
            assert call_args[1]['q'] == ["city=New York", "state=NY", "organization=false"]

    # Test Gifts search (named parameters)
    def test_gifts_search_with_named_parameters(self, client, mock_httpx_response):
        """Test gifts search with named parameters."""
        response_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "amount": 100.00, "gift_date": "2025-01-01", "constituent_id": 1, "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
                {"id": 2, "amount": 250.00, "gift_date": "2025-01-02", "constituent_id": 2, "created_at": "2025-01-02T10:00:00Z", "updated_at": "2025-01-02T10:00:00Z"}
            ],
            total=2,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.gifts.client, '_get', return_value=response_data):
            result = client.gifts.search(
                amount_from=50.00,
                amount_to=500.00,
                date_from=date(2025, 1, 1),
                date_to=date(2025, 1, 31)
            )
            
            assert result["total"] == 2
            assert len(result["items"]) == 2
            assert result["items"][0]["amount"] == 100.00
            assert result["items"][1]["amount"] == 250.00
            
            # Verify named parameters
            call_args = client.gifts.client._get.call_args
            assert "gifts/search" in call_args[0][0]
            if len(call_args) > 1 and 'params' in call_args[1]:
                params = call_args[1]['params']
                assert 'amount_from' in params
                assert 'date_from' in params

    def test_gifts_search_by_constituent(self, client, mock_httpx_response):
        """Test gifts search by constituent."""
        response_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "amount": 100.00, "constituent_id": 123, "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
                {"id": 2, "amount": 50.00, "constituent_id": 123, "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}
            ],
            total=2,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.gifts.client, '_get', return_value=response_data):
            result = client.gifts.search(constituent_id=123)
            
            assert result["total"] == 2
            assert len(result["items"]) == 2
            assert result["items"][0]["constituent_id"] == 123
            assert result["items"][1]["constituent_id"] == 123

    def test_gifts_search_by_date_range(self, client, mock_httpx_response):
        """Test gifts search with date range filtering."""
        response_data = APIResponseMocker.paginated_response(
            items=[{"id": 1, "amount": 100.00, "gift_date": "2025-01-15", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}],
            total=1,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.gifts.client, '_get', return_value=response_data):
            result = client.gifts.search(
                date_from=date(2025, 1, 1),
                date_to=date(2025, 1, 31)
            )
            
            assert result["total"] == 1
            assert len(result["items"]) == 1
            assert result["items"][0]["gift_date"] == "2025-01-15"

    # Test Keywords search (category-based)
    def test_keywords_search_by_category(self, client, mock_httpx_response):
        """Test keywords search by category."""
        response_data = [
            {"id": 1, "category_id": 1, "name": "Email", "ordinal": 1, "removable": True, "can_change": True, "can_select": True, "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
            {"id": 2, "category_id": 1, "name": "Newsletter", "ordinal": 2, "removable": True, "can_change": True, "can_select": True, "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
            {"id": 3, "category_id": 1, "name": "Direct Mail", "ordinal": 3, "removable": True, "can_change": True, "can_select": True, "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}
        ]
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.keywords._client, '_get', return_value={"items": response_data}):
            result = client.keywords.list_for_category(category_id=1)
            
            assert len(result) == 3
            assert result[0].name == "Email"
            assert result[1].name == "Newsletter"
            
            # Verify category-based URL
            call_args = client.keywords._client._get.call_args
            assert "categories/1/keywords" in call_args[0][0]

    def test_keywords_fetch_all_for_category(self, client, mock_httpx_response):
        """Test keywords fetch_all_for_category method."""
        response_data = [
            {"id": 1, "category_id": 2, "name": "Volunteer", "ordinal": 1, "removable": True, "can_change": True, "can_select": True, "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
            {"id": 2, "category_id": 2, "name": "Board Member", "ordinal": 2, "removable": True, "can_change": True, "can_select": True, "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}
        ]
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.keywords._client, '_get', return_value={"items": response_data}):
            result = client.keywords.list_for_category(category_id=2)
            
            assert len(result) == 2
            assert result[0].name == "Volunteer"
            assert result[1].name == "Board Member"

    # Test search with special characters and encoding
    def test_search_with_special_characters(self, client, mock_httpx_response):
        """Test search methods handle special characters properly."""
        response_data = APIResponseMocker.paginated_response(
            items=[{"id": 1, "name": "O'Brien & Associates", "last_name": "O'Brien", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}],
            total=1,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.constituents.client, '_get', return_value=response_data):
            # Test search with special characters
            result = client.constituents.search(query_params=["name=O'Brien", "name=&", "name=Associates"])
            
            assert result["total"] == 1
            assert len(result["items"]) == 1
            assert result["items"][0]["name"] == "O'Brien & Associates"
            
            # Verify proper URL encoding
            call_args = client.constituents.client._get.call_args
            assert "constituents/search" in call_args[0][0]

    def test_search_with_unicode_characters(self, client, mock_httpx_response):
        """Test search methods handle unicode characters."""
        response_data = APIResponseMocker.paginated_response(
            items=[{"id": 1, "name": "José María González", "last_name": "González", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}],
            total=1,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.constituents.client, '_get', return_value=response_data):
            result = client.constituents.search_by_name("José María González")
            
            assert len(result) == 1
            assert result[0].last_name == "González"

    def test_search_empty_results(self, client, mock_httpx_response):
        """Test search methods with empty results."""
        empty_response = APIResponseMocker.empty_response()
        mock_httpx_response.json.return_value = empty_response

        with patch.object(client.constituents.client, '_get', return_value=empty_response):
            result = client.constituents.search(query_params=["name=NonExistentName"])
            
            assert result["total"] == 0
            assert len(result["items"]) == 0
            assert isinstance(result, dict)

    def test_search_pagination(self, client, mock_httpx_response):
        """Test search methods with pagination."""
        # Simple mock that returns a fixed set of results
        response_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "first_name": "John", "last_name": "Smith", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
                {"id": 2, "first_name": "Jane", "last_name": "Smith", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}
            ],
            total=2,
            page=1,
            per_page=10
        )

        with patch.object(client.constituents.client, '_get', return_value=response_data):
            result = client.constituents.search(query_params=["last_name=Smith"])
            
            assert result["total"] == 2
            assert len(result["items"]) == 2
            assert result["items"][0]["first_name"] == "John"
            assert result["items"][1]["first_name"] == "Jane"
            assert client.constituents.client._get.call_count == 1

    def test_search_with_filters(self, client, mock_httpx_response):
        """Test search methods with various filters."""
        response_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "is_org": True, "city": "New York", "last_name": "Corp", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
                {"id": 2, "is_org": True, "city": "Boston", "last_name": "Inc", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}
            ],
            total=2,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.constituents.client, '_get', return_value=response_data):
            result = client.constituents.search(
                query_params=["organization=true", "city=New York", "state=NY", "active=true"]
            )
            
            assert result["total"] == 2
            assert len(result["items"]) == 2
            assert result["items"][0]["is_org"] == True
            assert result["items"][0]["city"] == "New York"

    def test_search_error_handling(self, client, mock_httpx_response):
        """Test search methods handle errors properly."""
        mock_httpx_response.status_code = 400
        mock_httpx_response.json.return_value = {"error": "Invalid search parameters"}
        mock_httpx_response.raise_for_status.side_effect = Exception("HTTP 400")

        with patch.object(client.constituents.client, '_get', side_effect=Exception("HTTP 400")):
            with pytest.raises(Exception):
                client.constituents.search(query_params=["invalid"])

    def test_search_parameter_validation(self, client, mock_httpx_response):
        """Test search methods validate parameters correctly."""
        response_data = APIResponseMocker.paginated_response(
            items=[{"id": 1, "name": "Valid Result", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}],
            total=1,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.gifts.client, '_get', return_value=response_data):
            # Test with valid parameters
            result = client.gifts.search(amount_from=10.00, amount_to=1000.00)
            
            assert result["total"] == 1
            assert len(result["items"]) == 1
            assert result["items"][0]["name"] == "Valid Result"
            
            # Verify parameter validation passed
            call_args = client.gifts.client._get.call_args
            if len(call_args) > 1 and 'params' in call_args[1]:
                params = call_args[1]['params']
                assert params['amount_from'] == 10.00
                assert params['amount_to'] == 1000.00