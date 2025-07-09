"""Payment Types API for LGL client."""

from typing import Any, List

from ..models.payment_type import PaymentType
from .client import LGLClient


class PaymentTypesAPI:
    """API for managing payment types in Little Green Light.
    
    Payment types define the different methods of payment that can be used
    for gifts (e.g., Cash, Check, Credit Card, Stock).
    """
    
    _resource = "payment_types"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Payment Types API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(self, *, limit: int = 25, offset: int = 0) -> List[PaymentType]:
        """List payment types for the account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of PaymentType objects
        """
        data = self._client._get(self._resource, limit=limit, offset=offset)
        return [PaymentType.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self) -> List[PaymentType]:
        """Fetch all payment types using automatic pagination.
        
        Returns:
            List of all PaymentType objects
        """
        def _list_page(**kwargs: Any) -> List[PaymentType]:
            return self.list(**kwargs)
        
        items = list(self._client._paginate(_list_page))
        return [PaymentType.from_dict(item) if isinstance(item, dict) else item for item in items]