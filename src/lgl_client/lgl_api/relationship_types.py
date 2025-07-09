"""Relationship Types API for LGL client."""

from typing import Any, List

from ..models.relationship_type import RelationshipType
from .client import LGLClient


class RelationshipTypesAPI:
    """API for managing relationship types in Little Green Light.
    
    Relationship types define the different types of relationships between
    constituents (e.g., Parent, Mother, Father, Child, Spouse, Friend).
    """
    
    _resource = "relationship_types"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Relationship Types API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(self, *, limit: int = 25, offset: int = 0) -> List[RelationshipType]:
        """List relationship types for the account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of RelationshipType objects
        """
        data = self._client._get(self._resource, limit=limit, offset=offset)
        return [RelationshipType.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self) -> List[RelationshipType]:
        """Fetch all relationship types using automatic pagination.
        
        Returns:
            List of all RelationshipType objects
        """
        def _list_page(**kwargs: Any) -> List[RelationshipType]:
            return self.list(**kwargs)
        
        items = list(self._client._paginate(_list_page))
        return [RelationshipType.from_dict(item) if isinstance(item, dict) else item for item in items]