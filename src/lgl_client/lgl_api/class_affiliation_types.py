"""Class Affiliation Types API for LGL client."""

from typing import Any, List

from ..models.class_affiliation_type import ClassAffiliationType
from .client import LGLClient


class ClassAffiliationTypesAPI:
    """API for managing class affiliation types in Little Green Light.
    
    Class affiliation types define different types of relationships 
    to educational institutions (e.g., Student, Parent, Grandparent).
    """
    
    _resource = "class_affiliation_types"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Class Affiliation Types API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(self, *, limit: int = 25, offset: int = 0) -> List[ClassAffiliationType]:
        """List class affiliation types for the account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of ClassAffiliationType objects
        """
        data = self._client._get(self._resource, limit=limit, offset=offset)
        return [ClassAffiliationType.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self) -> List[ClassAffiliationType]:
        """Fetch all class affiliation types using automatic pagination.
        
        Returns:
            List of all ClassAffiliationType objects
        """
        def _list_page(**kwargs: Any) -> List[ClassAffiliationType]:
            return self.list(**kwargs)
        
        items = list(self._client._paginate(_list_page))
        return [ClassAffiliationType.from_dict(item) if isinstance(item, dict) else item for item in items]