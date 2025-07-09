"""Gift Categories API for LGL client."""

from typing import Any, Dict, List, Optional

from ..models.gift_category import GiftCategory
from .client import LGLClient


class GiftCategoriesAPI:
    """API for managing gift categories in Little Green Light.
    
    Gift categories provide sub-classifications within gift types,
    such as "Donation", "Matching Gift", "Standard Pledge", "Grant", etc.
    """
    
    _resource = "gift_categories"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Gift Categories API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(
        self, 
        *, 
        gift_type_id: Optional[int] = None,
        limit: int = 25, 
        offset: int = 0
    ) -> List[GiftCategory]:
        """List gift categories for the account.
        
        Args:
            gift_type_id: Filter by gift type ID
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of GiftCategory objects
        """
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if gift_type_id is not None:
            params["gift_type_id"] = str(gift_type_id)  # API expects string
        
        data = self._client._get(self._resource, **params)
        return [GiftCategory.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self, *, gift_type_id: Optional[int] = None) -> List[GiftCategory]:
        """Fetch all gift categories using automatic pagination.
        
        Args:
            gift_type_id: Filter by gift type ID
            
        Returns:
            List of all GiftCategory objects
        """
        def _list_page(**kwargs: Any) -> List[GiftCategory]:
            return self.list(**kwargs)
        
        kwargs = {}
        if gift_type_id is not None:
            kwargs["gift_type_id"] = gift_type_id
            
        items = list(self._client._paginate(_list_page, **kwargs))
        return [GiftCategory.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def retrieve(self, gift_category_id: int) -> GiftCategory:
        """Retrieve a specific gift category by ID.
        
        Args:
            gift_category_id: Gift Category ID
            
        Returns:
            GiftCategory object
        """
        data = self._client._get(f"{self._resource}/{gift_category_id}")
        return GiftCategory.from_dict(data)
    
    def create(self, gift_category: GiftCategory) -> GiftCategory:
        """Create a new gift category.
        
        Args:
            gift_category: GiftCategory object with data to create
            
        Returns:
            Created GiftCategory object
        """
        data = self._client._post(self._resource, gift_category.to_dict())
        return GiftCategory.from_dict(data)
    
    def update(self, gift_category_id: int, gift_category: GiftCategory) -> GiftCategory:
        """Update an existing gift category.
        
        Args:
            gift_category_id: Gift Category ID to update
            gift_category: GiftCategory object with updated data
            
        Returns:
            Updated GiftCategory object
        """
        data = self._client._patch(f"{self._resource}/{gift_category_id}", gift_category.to_dict())
        return GiftCategory.from_dict(data)
    
    def delete(self, gift_category_id: int) -> None:
        """Delete a gift category.
        
        Args:
            gift_category_id: Gift Category ID to delete
        """
        self._client._delete(f"{self._resource}/{gift_category_id}")