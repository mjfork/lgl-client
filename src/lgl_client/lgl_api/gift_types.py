"""Gift Types API for LGL client."""

from typing import Any, List

from ..models.gift_type import GiftType
from .client import LGLClient


class GiftTypesAPI:
    """API for managing gift types in Little Green Light.
    
    Gift types categorize donations by their nature,
    such as "Gift", "Pledge", "In Kind", "Soft Credit", etc.
    """
    
    _resource = "gift_types"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Gift Types API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(self, *, limit: int = 25, offset: int = 0) -> List[GiftType]:
        """List gift types for the account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of GiftType objects
        """
        data = self._client._get(self._resource, limit=limit, offset=offset)
        return [GiftType.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self) -> List[GiftType]:
        """Fetch all gift types using automatic pagination.
        
        Returns:
            List of all GiftType objects
        """
        def _list_page(**kwargs: Any) -> List[GiftType]:
            return self.list(**kwargs)
            
        items = list(self._client._paginate(_list_page))
        return [GiftType.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def retrieve(self, gift_type_id: int) -> GiftType:
        """Retrieve a specific gift type by ID.
        
        Args:
            gift_type_id: Gift Type ID
            
        Returns:
            GiftType object
        """
        data = self._client._get(f"{self._resource}/{gift_type_id}")
        return GiftType.from_dict(data)
    
    def create(self, gift_type: GiftType) -> GiftType:
        """Create a new gift type.
        
        Args:
            gift_type: GiftType object with data to create
            
        Returns:
            Created GiftType object
        """
        data = self._client._post(self._resource, gift_type.to_dict())
        return GiftType.from_dict(data)
    
    def update(self, gift_type_id: int, gift_type: GiftType) -> GiftType:
        """Update an existing gift type.
        
        Args:
            gift_type_id: Gift Type ID to update
            gift_type: GiftType object with updated data
            
        Returns:
            Updated GiftType object
        """
        data = self._client._patch(f"{self._resource}/{gift_type_id}", gift_type.to_dict())
        return GiftType.from_dict(data)
    
    def delete(self, gift_type_id: int) -> None:
        """Delete a gift type.
        
        Args:
            gift_type_id: Gift Type ID to delete
        """
        self._client._delete(f"{self._resource}/{gift_type_id}")