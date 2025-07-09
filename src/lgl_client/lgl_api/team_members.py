"""Team Members API for LGL client."""

from typing import Any, List

from ..models.team_member import TeamMember
from .client import LGLClient


class TeamMembersAPI:
    """API for managing team members in Little Green Light.
    
    Team members represent users who have access to the LGL account
    with various roles and permission levels.
    """
    
    _resource = "team_members"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Team Members API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(self, *, limit: int = 25, offset: int = 0) -> List[TeamMember]:
        """List team members for the account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of TeamMember objects
        """
        data = self._client._get(self._resource, limit=limit, offset=offset)
        return [TeamMember.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self) -> List[TeamMember]:
        """Fetch all team members using automatic pagination.
        
        Returns:
            List of all TeamMember objects
        """
        def _list_page(**kwargs: Any) -> List[TeamMember]:
            return self.list(**kwargs)
        
        items = list(self._client._paginate(_list_page))
        return [TeamMember.from_dict(item) if isinstance(item, dict) else item for item in items]