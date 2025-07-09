"""LGL API HTTP Client - Core HTTP functionality and pagination."""

import logging
import re
from typing import Any, Dict, Iterator, List, Optional, Union
from urllib.parse import urljoin

import httpx

from .exceptions import LGLAPIError, NotFoundError, UnauthorizedError, ValidationError

logger = logging.getLogger(__name__)


class LGLClient:
    """Base HTTP client for Little Green Light API.
    
    Provides core HTTP methods, error handling, and pagination support.
    """
    
    BASE_URL = "https://api.littlegreenlight.com/api/v1/"
    
    def __init__(self, api_key: str, *, timeout: float = 10.0, debug: bool = False) -> None:
        """Initialize the LGL API client.
        
        Args:
            api_key: LGL API bearer token
            timeout: Request timeout in seconds
            debug: Enable debug mode to log request details
        """
        self._client = httpx.Client(
            base_url=self.BASE_URL,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=timeout,
        )
        self.debug = debug
    
    def _debug_request(self, method: str, path: str, **kwargs) -> None:
        """Debug print request details if debug mode is enabled.
        
        WARNING: Debug mode may expose sensitive information. Never use in production.
        """
        if not self.debug:
            return
        
        from urllib.parse import urlencode
        
        # Build full URL
        full_url = str(self._client.base_url) + path.lstrip('/')
        
        # Add query parameters if present
        params = kwargs.get('params', {})
        if params:
            query_string = urlencode(params, doseq=True)
            full_url += f"?{query_string}"
        
        # Mask sensitive headers for security
        safe_headers = {}
        for key, value in self._client.headers.items():
            if key.lower() in ('authorization', 'x-api-key', 'api-key'):
                # Mask credentials - show only first/last few characters
                if isinstance(value, str) and len(value) > 10:
                    safe_headers[key] = f"{value[:8]}...{value[-4:]}"
                else:
                    safe_headers[key] = "***MASKED***"
            else:
                safe_headers[key] = value
        
        print(f"\n🔍 DEBUG REQUEST (⚠️  SENSITIVE DATA MASKED):")
        print(f"Method: {method.upper()}")
        print(f"URL: {full_url}")
        print(f"Headers: {safe_headers}")
        
        if 'json' in kwargs:
            # Sanitize request body for potential sensitive fields
            sanitized_body = self._sanitize_debug_data(kwargs['json'])
            print(f"Body: {sanitized_body}")
        
        if params:
            # Sanitize query parameters
            sanitized_params = self._sanitize_debug_data(params)
            print(f"Query Params: {sanitized_params}")
        print()
    
    def _sanitize_debug_data(self, data: Any) -> Any:
        """Sanitize data for debug output by masking sensitive fields."""
        if not isinstance(data, dict):
            return data
        
        # List of field names that may contain sensitive information
        sensitive_fields = {
            'password', 'passwd', 'secret', 'token', 'key', 'api_key',
            'ssn', 'social_security', 'credit_card', 'cc_number', 
            'email', 'phone', 'address', 'birth_date', 'dob'
        }
        
        sanitized = {}
        for key, value in data.items():
            key_lower = str(key).lower()
            
            # Check if field name suggests sensitive data
            if any(sensitive in key_lower for sensitive in sensitive_fields):
                if isinstance(value, str) and len(value) > 4:
                    sanitized[key] = f"{value[:2]}***{value[-2:]}"
                else:
                    sanitized[key] = "***"
            elif isinstance(value, dict):
                # Recursively sanitize nested dictionaries
                sanitized[key] = self._sanitize_debug_data(value)
            else:
                sanitized[key] = value
        
        return sanitized
    
    def _validate_api_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and sanitize API parameters for security."""
        if not isinstance(params, dict):
            raise ValueError("Parameters must be a dictionary")
        
        validated = {}
        for key, value in params.items():
            # Validate parameter names (prevent injection attempts)
            if not self._is_safe_param_name(key):
                raise ValueError(f"Invalid parameter name: {key}")
            
            # Validate parameter values
            validated[key] = self._sanitize_param_value(value)
        
        return validated
    
    def _is_safe_param_name(self, name: str) -> bool:
        """Check if parameter name is safe (alphanumeric, underscore, dash, square brackets only)."""
        if not isinstance(name, str):
            return False
        
        # Allow alphanumeric characters, underscores, dashes, and square brackets for API array parameters
        pattern = r'^[a-zA-Z0-9_\[\]-]+$'
        return bool(re.match(pattern, name)) and len(name) <= 100
    
    def _sanitize_param_value(self, value: Any) -> Any:
        """Sanitize parameter values to prevent injection attacks."""
        if value is None:
            return None
        elif isinstance(value, bool):
            return value
        elif isinstance(value, (int, float)):
            # Check for reasonable numeric ranges
            if isinstance(value, int) and abs(value) > 2**31:
                raise ValueError(f"Integer value too large: {value}")
            return value
        elif isinstance(value, str):
            # Limit string length and check for suspicious patterns
            if len(value) > 1000:
                raise ValueError(f"String parameter too long: {len(value)} characters")
            
            # Check for potential injection patterns
            suspicious_patterns = [
                r'<script',  # XSS
                r'javascript:',  # JavaScript injection
                r'[\'"];',  # SQL injection attempts
                r'<!--',  # HTML injection
                r'\\x[0-9a-fA-F]{2}',  # Hex-encoded characters
            ]
            
            value_lower = value.lower()
            for pattern in suspicious_patterns:
                if re.search(pattern, value_lower):
                    logger.warning(f"Suspicious pattern detected in parameter: {pattern}")
                    # Don't reject, but log for monitoring
            
            return value
        elif isinstance(value, list):
            # Validate list items
            if len(value) > 100:  # Reasonable list size limit
                raise ValueError(f"List parameter too long: {len(value)} items")
            return [self._sanitize_param_value(item) for item in value]
        else:
            # Convert other types to string and validate
            return self._sanitize_param_value(str(value))
    
    def _validate_json_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Validate JSON payload for security and size limits."""
        if not isinstance(payload, dict):
            raise ValueError("Payload must be a dictionary")
        
        # Check payload size (rough estimate)
        payload_str = str(payload)
        if len(payload_str) > 10000:  # 10KB limit for safety
            raise ValueError(f"Payload too large: {len(payload_str)} characters")
        
        # Recursively validate payload structure
        return self._validate_nested_dict(payload, max_depth=5, current_depth=0)
    
    def _validate_nested_dict(self, data: Any, max_depth: int, current_depth: int) -> Any:
        """Recursively validate nested dictionary structure."""
        if current_depth > max_depth:
            raise ValueError(f"Payload nesting too deep: {current_depth} levels")
        
        if isinstance(data, dict):
            if len(data) > 100:  # Reasonable key limit
                raise ValueError(f"Too many keys in dictionary: {len(data)}")
            
            validated = {}
            for key, value in data.items():
                if not self._is_safe_param_name(str(key)):
                    raise ValueError(f"Invalid key name: {key}")
                validated[key] = self._validate_nested_dict(value, max_depth, current_depth + 1)
            return validated
        elif isinstance(data, list):
            if len(data) > 100:  # Reasonable list size
                raise ValueError(f"List too long: {len(data)} items")
            return [self._validate_nested_dict(item, max_depth, current_depth + 1) for item in data]
        else:
            return self._sanitize_param_value(data)
    
    def __enter__(self) -> "LGLClient":
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """Context manager exit."""
        self.close()
    
    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()
    
    def _get(self, path: str, **params: Any) -> Dict[str, Any]:
        """Make a GET request to the LGL API.
        
        Args:
            path: API endpoint path (relative to base URL)
            **params: Query parameters
            
        Returns:
            JSON response data
            
        Raises:
            LGLAPIError: For API errors
            ValueError: For invalid parameters
        """
        # Validate input parameters for security
        validated_params = self._validate_api_params(params) if params else {}
        
        self._debug_request("GET", path, params=validated_params)
        try:
            response = self._client.get(path, params=validated_params)
            self._handle_response(response)
            return response.json()
        except ValueError as e:
            logger.error(f"JSON decode error during GET {path}: {e}")
            raise LGLAPIError(
                f"Invalid JSON response: {e}",
                status_code=response.status_code,
                url=str(self._client.base_url) + path,
            )
        except httpx.HTTPError as e:
            logger.error(f"HTTP error during GET {path}: {e}")
            raise LGLAPIError(
                f"HTTP error: {e}",
                status_code=getattr(e, 'response', {}).get('status_code', 0),
                url=str(self._client.base_url) + path,
            )
    
    def _post(self, path: str, json: Dict[str, Any]) -> Dict[str, Any]:
        """Make a POST request to the LGL API.
        
        Args:
            path: API endpoint path
            json: Request body data
            
        Returns:
            JSON response data
            
        Raises:
            LGLAPIError: For API errors
            ValueError: For invalid payload
        """
        # Validate JSON payload for security
        validated_json = self._validate_json_payload(json)
        
        self._debug_request("POST", path, json=validated_json)
        try:
            response = self._client.post(path, json=validated_json)
            self._handle_response(response)
            return response.json()
        except ValueError as e:
            logger.error(f"JSON decode error during POST {path}: {e}")
            raise LGLAPIError(
                f"Invalid JSON response: {e}",
                status_code=response.status_code,
                url=str(self._client.base_url) + path,
                payload=validated_json,
            )
        except httpx.HTTPError as e:
            logger.error(f"HTTP error during POST {path}: {e}")
            raise LGLAPIError(
                f"HTTP error: {e}",
                status_code=getattr(e, 'response', {}).get('status_code', 0),
                url=str(self._client.base_url) + path,
                payload=validated_json,
            )
    
    def _patch(self, path: str, json: Dict[str, Any]) -> Dict[str, Any]:
        """Make a PATCH request to the LGL API.
        
        Args:
            path: API endpoint path
            json: Request body data
            
        Returns:
            JSON response data
            
        Raises:
            LGLAPIError: For API errors
            ValueError: For invalid payload
        """
        # Validate JSON payload for security
        validated_json = self._validate_json_payload(json)
        
        self._debug_request("PATCH", path, json=validated_json)
        try:
            response = self._client.patch(path, json=validated_json)
            self._handle_response(response)
            return response.json()
        except ValueError as e:
            logger.error(f"JSON decode error during PATCH {path}: {e}")
            raise LGLAPIError(
                f"Invalid JSON response: {e}",
                status_code=response.status_code,
                url=str(self._client.base_url) + path,
                payload=validated_json,
            )
        except httpx.HTTPError as e:
            logger.error(f"HTTP error during PATCH {path}: {e}")
            raise LGLAPIError(
                f"HTTP error: {e}",
                status_code=getattr(e, 'response', {}).get('status_code', 0),
                url=str(self._client.base_url) + path,
                payload=validated_json,
            )
    
    def _delete(self, path: str) -> None:
        """Make a DELETE request to the LGL API.
        
        Args:
            path: API endpoint path
            
        Raises:
            LGLAPIError: For API errors
        """
        self._debug_request("DELETE", path)
        try:
            response = self._client.delete(path)
            self._handle_response(response)
        except httpx.HTTPError as e:
            logger.error(f"HTTP error during DELETE {path}: {e}")
            raise LGLAPIError(
                f"HTTP error: {e}",
                status_code=getattr(e, 'response', {}).get('status_code', 0),
                url=str(self._client.base_url) + path,
            )
    
    def _handle_response(self, response: httpx.Response) -> None:
        """Handle HTTP response and raise appropriate exceptions.
        
        Args:
            response: HTTP response object
            
        Raises:
            LGLAPIError: For various API error conditions
        """
        if response.is_success:
            return
        
        # Try to get error details from response body
        try:
            error_data = response.json()
            # LGL API returns 'error' and 'description' fields
            if 'error' in error_data:
                error_message = error_data['error']
                if 'description' in error_data:
                    error_message += f": {error_data['description']}"
            else:
                # Fallback to standard 'message' field or default
                error_message = error_data.get('message', f'HTTP {response.status_code}')
        except Exception:
            error_message = f'HTTP {response.status_code}'
        
        # Map status codes to specific exceptions
        if response.status_code == 401:
            raise UnauthorizedError(
                error_message,
                status_code=response.status_code,
                url=str(response.url),
            )
        elif response.status_code == 404:
            raise NotFoundError(
                error_message,
                status_code=response.status_code,
                url=str(response.url),
            )
        elif response.status_code == 422:
            raise ValidationError(
                error_message,
                status_code=response.status_code,
                url=str(response.url),
            )
        else:
            raise LGLAPIError(
                error_message,
                status_code=response.status_code,
                url=str(response.url),
            )
    
    @staticmethod
    def _paginate(
        call_func: Any, 
        *, 
        limit: int = 100, 
        **kwargs: Any
    ) -> Iterator[Dict[str, Any]]:
        """Paginate through API results.
        
        Args:
            call_func: Function to call for each page
            limit: Items per page
            **kwargs: Additional arguments to pass to call_func
            
        Yields:
            Individual items from paginated results
        """
        offset = 0
        while True:
            # Call the function with current offset
            result = call_func(limit=limit, offset=offset, **kwargs)
            
            # Handle different response formats
            if isinstance(result, dict) and 'items' in result:
                items = result['items']
            elif isinstance(result, list):
                items = result
            else:
                # If response doesn't have expected structure, yield as-is and stop
                if result:
                    yield result
                break
            
            # If no items, we're done
            if not items:
                break
            
            # Yield each item
            for item in items:
                yield item
            
            # Check if we have more pages
            if isinstance(result, dict):
                total_items = result.get('total_items', 0)
                items_count = result.get('items_count', len(items))
                
                # If we got fewer items than requested, or we've reached total, stop
                if items_count < limit or (offset + items_count >= total_items):
                    break
            else:
                # For list responses, if we got fewer than limit, we're done
                if len(items) < limit:
                    break
            
            # Move to next page
            offset += len(items)