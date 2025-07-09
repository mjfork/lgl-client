"""Categories API for LGL client."""

from typing import Any, Dict, Iterator, List, Literal, Optional

from ..models.category import Category
from .client import LGLClient


class CategoriesAPI:
    """API for managing categories in Little Green Light.
    
    Categories are used to organize constituents, gifts, and volunteer time
    with custom fields and categorization.
    """
    
    _resource = "categories"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Categories API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(
        self, 
        *, 
        item_type: Optional[Literal["Constituent", "Gift", "VolunteerTime"]] = None,
        limit: int = 25, 
        offset: int = 0
    ) -> List[Category]:
        """List categories for the account.
        
        Args:
            item_type: Filter by category type (default: Constituent)
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of Category objects
        """
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if item_type is not None:
            params["item_type"] = item_type
        
        data = self._client._get(self._resource, **params)
        return [Category.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(
        self, 
        *, 
        item_type: Optional[Literal["Constituent", "Gift", "VolunteerTime"]] = None
    ) -> List[Category]:
        """Fetch all categories using automatic pagination.
        
        Args:
            item_type: Filter by category type (default: Constituent)
            
        Returns:
            List of all Category objects
        """
        def _list_page(**kwargs: Any) -> List[Category]:
            return self.list(**kwargs)
        
        kwargs = {}
        if item_type is not None:
            kwargs["item_type"] = item_type
            
        items = list(self._client._paginate(_list_page, **kwargs))
        return [Category.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def retrieve(self, category_id: int) -> Category:
        """Retrieve a specific category by ID.
        
        Args:
            category_id: Category ID
            
        Returns:
            Category object
        """
        data = self._client._get(f"{self._resource}/{category_id}")
        return Category.from_dict(data)
    
    def create(self, category: Category) -> Category:
        """Create a new category.
        
        Args:
            category: Category object with data to create
            
        Returns:
            Created Category object
        """
        data = self._client._post(self._resource, category.to_dict())
        return Category.from_dict(data)
    
    def update(self, category_id: int, category: Category) -> Category:
        """Update an existing category.
        
        Args:
            category_id: Category ID to update
            category: Category object with updated data
            
        Returns:
            Updated Category object
        """
        data = self._client._patch(f"{self._resource}/{category_id}", category.to_dict())
        return Category.from_dict(data)
    
    def delete(self, category_id: int) -> None:
        """Delete a category.
        
        Args:
            category_id: Category ID to delete
        """
        self._client._delete(f"{self._resource}/{category_id}")
    
    def list_for_constituent(
        self, 
        constituent_id: int, 
        *, 
        limit: int = 25, 
        offset: int = 0
    ) -> List[Category]:
        """List categories for a specific constituent.
        
        Args:
            constituent_id: Constituent ID
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of Category objects
        """
        data = self._client._get(
            f"constituents/{constituent_id}/categories",
            limit=limit,
            offset=offset
        )
        return [Category.from_dict(item) for item in data.get("items", [])]