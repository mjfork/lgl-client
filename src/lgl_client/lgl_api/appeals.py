"""Appeals API for LGL client."""

from typing import Any, List

from ..models.appeal import Appeal
from .client import LGLClient


class AppealsAPI:
    """API for managing appeals in Little Green Light.
    
    Appeals represent fundraising campaigns or solicitation efforts
    targeting specific groups of constituents.
    """
    
    _resource = "appeals"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Appeals API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(self, *, limit: int = 25, offset: int = 0) -> List[Appeal]:
        """List appeals for the account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of Appeal objects
        """
        data = self._client._get(self._resource, limit=limit, offset=offset)
        return [Appeal.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self) -> List[Appeal]:
        """Fetch all appeals using automatic pagination.
        
        Returns:
            List of all Appeal objects
        """
        def _list_page(**kwargs: Any) -> List[Appeal]:
            return self.list(**kwargs)
            
        items = list(self._client._paginate(_list_page))
        return [Appeal.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def retrieve(self, appeal_id: int) -> Appeal:
        """Retrieve a specific appeal by ID.
        
        Args:
            appeal_id: Appeal ID
            
        Returns:
            Appeal object
        """
        data = self._client._get(f"{self._resource}/{appeal_id}")
        return Appeal.from_dict(data)
    
    def create(self, appeal: Appeal) -> Appeal:
        """Create a new appeal.
        
        Args:
            appeal: Appeal object with data to create
            
        Returns:
            Created Appeal object
        """
        data = self._client._post(self._resource, appeal.to_dict())
        return Appeal.from_dict(data)
    
    def update(self, appeal_id: int, appeal: Appeal) -> Appeal:
        """Update an existing appeal.
        
        Args:
            appeal_id: Appeal ID to update
            appeal: Appeal object with updated data
            
        Returns:
            Updated Appeal object
        """
        data = self._client._patch(f"{self._resource}/{appeal_id}", appeal.to_dict())
        return Appeal.from_dict(data)
    
    def delete(self, appeal_id: int) -> None:
        """Delete an appeal.
        
        Args:
            appeal_id: Appeal ID to delete
        """
        self._client._delete(f"{self._resource}/{appeal_id}")