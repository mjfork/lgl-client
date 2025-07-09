"""Groups API for LGL client."""

from typing import Any, List

from ..models.group import Group
from .client import LGLClient


class GroupsAPI:
    """API for managing groups in Little Green Light.
    
    Groups represent organizational categories for constituents,
    such as "Board Member", "Staff", "Volunteer", etc.
    """
    
    _resource = "groups"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Groups API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(self, *, limit: int = 25, offset: int = 0) -> List[Group]:
        """List groups for the account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of Group objects
        """
        data = self._client._get(self._resource, limit=limit, offset=offset)
        return [Group.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self) -> List[Group]:
        """Fetch all groups using automatic pagination.
        
        Returns:
            List of all Group objects
        """
        def _list_page(**kwargs: Any) -> List[Group]:
            return self.list(**kwargs)
            
        items = list(self._client._paginate(_list_page))
        return [Group.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def retrieve(self, group_id: int) -> Group:
        """Retrieve a specific group by ID.
        
        Args:
            group_id: Group ID
            
        Returns:
            Group object
        """
        data = self._client._get(f"{self._resource}/{group_id}")
        return Group.from_dict(data)
    
    def create(self, group: Group) -> Group:
        """Create a new group.
        
        Args:
            group: Group object with data to create
            
        Returns:
            Created Group object
        """
        data = self._client._post(self._resource, group.to_dict())
        return Group.from_dict(data)
    
    def update(self, group_id: int, group: Group) -> Group:
        """Update an existing group.
        
        Args:
            group_id: Group ID to update
            group: Group object with updated data
            
        Returns:
            Updated Group object
        """
        data = self._client._patch(f"{self._resource}/{group_id}", group.to_dict())
        return Group.from_dict(data)
    
    def delete(self, group_id: int) -> None:
        """Delete a group.
        
        Args:
            group_id: Group ID to delete
        """
        self._client._delete(f"{self._resource}/{group_id}")