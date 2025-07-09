"""LGL API Exception Classes."""

from typing import Any, Dict, Optional


class LGLAPIError(Exception):
    """Base exception for LGL API errors."""
    
    def __init__(
        self, 
        message: str, 
        *, 
        status_code: int, 
        url: str, 
        payload: Optional[Dict[str, Any]] = None
    ) -> None:
        """Initialize LGL API error.
        
        Args:
            message: Error message
            status_code: HTTP status code
            url: Request URL that caused the error
            payload: Request payload (if applicable) - will be sanitized for security
        """
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.url = self._sanitize_url(url)
        self.payload = self._sanitize_payload(payload) if payload else None
    
    def _sanitize_url(self, url: str) -> str:
        """Sanitize URL to remove potential sensitive query parameters."""
        # Remove query parameters that might contain sensitive data
        if '?' in url:
            base_url = url.split('?')[0]
            return f"{base_url}?[QUERY_PARAMS_REMOVED]"
        return url
    
    def _sanitize_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Sanitize payload to mask sensitive information."""
        if not isinstance(payload, dict):
            return {"payload": "[SANITIZED]"}
        
        # List of field names that may contain sensitive information
        sensitive_fields = {
            'password', 'passwd', 'secret', 'token', 'key', 'api_key',
            'ssn', 'social_security_number', 'credit_card', 'cc_number', 'card_number',
            'email', 'email_address', 'phone', 'phone_number', 'mobile', 'tel',
            'address', 'street_address', 'home_address', 'billing_address',
            'birth_date', 'dob', 'date_of_birth', 'birthday',
            'account_number', 'routing_number', 'bank_account'
        }
        
        def sanitize_value(key: str, value: Any) -> Any:
            """Sanitize individual field values."""
            key_lower = str(key).lower()
            
            # Check if field name suggests sensitive data
            if any(sensitive in key_lower for sensitive in sensitive_fields):
                if isinstance(value, str) and len(value) > 4:
                    return f"{value[:2]}***{value[-2:]}"
                else:
                    return "***"
            elif isinstance(value, dict):
                # Recursively sanitize nested dictionaries
                return {k: sanitize_value(k, v) for k, v in value.items()}
            elif isinstance(value, list):
                # Sanitize list items
                return [sanitize_value(f"{key}_item", item) for item in value]
            else:
                return value
        
        return {k: sanitize_value(k, v) for k, v in payload.items()}
    
    def __str__(self) -> str:
        """String representation of the error."""
        return f"{self.message} (HTTP {self.status_code} at {self.url})"


class UnauthorizedError(LGLAPIError):
    """Raised when API returns 401 Unauthorized."""
    pass


class NotFoundError(LGLAPIError):
    """Raised when API returns 404 Not Found."""
    pass


class ValidationError(LGLAPIError):
    """Raised when API returns 422 Unprocessable Entity."""
    pass