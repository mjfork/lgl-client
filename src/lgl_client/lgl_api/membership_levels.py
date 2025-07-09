"""Membership Levels API for LGL client."""

from typing import Any, List

from ..models.membership_level import MembershipLevel
from .client import LGLClient


class MembershipLevelsAPI:
    """API for managing membership levels in Little Green Light.
    
    Membership levels define different tiers of membership
    for constituents (e.g., General, Friend, Gold, Silver, Diamond, Bronze).
    """
    
    _resource = "membership_levels"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Membership Levels API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(self, *, limit: int = 25, offset: int = 0) -> List[MembershipLevel]:
        """List membership levels for the account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of MembershipLevel objects
        """
        data = self._client._get(self._resource, limit=limit, offset=offset)
        return [MembershipLevel.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self) -> List[MembershipLevel]:
        """Fetch all membership levels using automatic pagination.
        
        Returns:
            List of all MembershipLevel objects
        """
        def _list_page(**kwargs: Any) -> List[MembershipLevel]:
            return self.list(**kwargs)
        
        items = list(self._client._paginate(_list_page))
        return [MembershipLevel.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def retrieve(self, membership_level_id: int) -> MembershipLevel:
        """Retrieve a specific membership level by ID.
        
        Args:
            membership_level_id: Membership level ID
            
        Returns:
            MembershipLevel object
        """
        data = self._client._get(f"{self._resource}/{membership_level_id}")
        return MembershipLevel.from_dict(data)
    
    def create(self, membership_level: MembershipLevel) -> MembershipLevel:
        """Create a new membership level.
        
        Args:
            membership_level: MembershipLevel object with data to create
            
        Returns:
            Created MembershipLevel object
        """
        data = self._client._post(self._resource, membership_level.to_dict())
        return MembershipLevel.from_dict(data)
    
    def update(self, membership_level_id: int, membership_level: MembershipLevel) -> MembershipLevel:
        """Update an existing membership level.
        
        Args:
            membership_level_id: Membership level ID to update
            membership_level: MembershipLevel object with updated data
            
        Returns:
            Updated MembershipLevel object
        """
        data = self._client._patch(f"{self._resource}/{membership_level_id}", membership_level.to_dict())
        return MembershipLevel.from_dict(data)
    
    def delete(self, membership_level_id: int) -> None:
        """Delete a membership level.
        
        Args:
            membership_level_id: Membership level ID to delete
        """
        self._client._delete(f"{self._resource}/{membership_level_id}")