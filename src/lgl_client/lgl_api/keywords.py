"""Keywords API for LGL client."""

from typing import Any, List

from ..models.common import Keyword
from .client import LGLClient


class KeywordsAPI:
    """API for managing keywords in Little Green Light.
    
    Keywords are labels that can be organized within categories and
    applied to constituents for tagging and organization.
    """
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Keywords API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list_for_category(self, category_id: int, *, limit: int = 25, offset: int = 0) -> List[Keyword]:
        """List keywords for a specific category.
        
        Args:
            category_id: Category ID to get keywords for
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of Keyword objects
        """
        data = self._client._get(f"categories/{category_id}/keywords", limit=limit, offset=offset)
        return [Keyword.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all_for_category(self, category_id: int) -> List[Keyword]:
        """Fetch all keywords for a category using automatic pagination.
        
        Args:
            category_id: Category ID to get keywords for
            
        Returns:
            List of all Keyword objects for the category
        """
        def _list_page(**kwargs: Any) -> List[Keyword]:
            return self.list_for_category(category_id, **kwargs)
        
        items = list(self._client._paginate(_list_page))
        return [Keyword.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def retrieve(self, keyword_id: int) -> Keyword:
        """Retrieve a specific keyword by ID.
        
        Args:
            keyword_id: Keyword ID
            
        Returns:
            Keyword object
        """
        data = self._client._get(f"keywords/{keyword_id}")
        return Keyword.from_dict(data)
    
    def create_for_category(self, category_id: int, keyword: Keyword) -> Keyword:
        """Create a new keyword for a category.
        
        Args:
            category_id: Category ID to create keyword in
            keyword: Keyword object with data to create
            
        Returns:
            Created Keyword object
        """
        data = self._client._post(f"categories/{category_id}/keywords", keyword.to_dict())
        return Keyword.from_dict(data)
    
    def update(self, keyword_id: int, keyword: Keyword) -> Keyword:
        """Update an existing keyword.
        
        Args:
            keyword_id: Keyword ID to update
            keyword: Keyword object with updated data
            
        Returns:
            Updated Keyword object
        """
        data = self._client._patch(f"keywords/{keyword_id}", keyword.to_dict())
        return Keyword.from_dict(data)
    
    def delete(self, keyword_id: int, *, permanent: bool = False) -> None:
        """Delete a keyword.
        
        Args:
            keyword_id: Keyword ID to delete
            permanent: Whether to delete permanently (default: False)
        """
        params = {"permanent": 1} if permanent else {}
        self._client._delete(f"keywords/{keyword_id}", **params)
    
    def add_to_constituent(self, constituent_id: int, keyword_id: int) -> None:
        """Add a keyword to a constituent.
        
        Args:
            constituent_id: Constituent ID
            keyword_id: Keyword ID to add
        """
        data = {"id": keyword_id}
        self._client._post(f"constituents/{constituent_id}/keywords", data)
    
    def remove_from_constituent(self, constituent_id: int, keyword_id: int) -> None:
        """Remove a keyword from a constituent.
        
        Args:
            constituent_id: Constituent ID
            keyword_id: Keyword ID to remove
        """
        self._client._delete(f"constituents/{constituent_id}/keywords/{keyword_id}")