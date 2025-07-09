"""Funds API for LGL client."""

from typing import Any, List

from ..models.fund import Fund
from .client import LGLClient


class FundsAPI:
    """API for managing funds in Little Green Light.
    
    Funds represent designated accounts or purposes for donations,
    such as building funds, endowments, or special projects.
    """
    
    _resource = "funds"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Funds API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(self, *, limit: int = 25, offset: int = 0) -> List[Fund]:
        """List funds for the account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of Fund objects
        """
        data = self._client._get(self._resource, limit=limit, offset=offset)
        return [Fund.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self) -> List[Fund]:
        """Fetch all funds using automatic pagination.
        
        Returns:
            List of all Fund objects
        """
        def _list_page(**kwargs: Any) -> List[Fund]:
            return self.list(**kwargs)
            
        items = list(self._client._paginate(_list_page))
        return [Fund.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def retrieve(self, fund_id: int) -> Fund:
        """Retrieve a specific fund by ID.
        
        Args:
            fund_id: Fund ID
            
        Returns:
            Fund object
        """
        data = self._client._get(f"{self._resource}/{fund_id}")
        return Fund.from_dict(data)
    
    def create(self, fund: Fund) -> Fund:
        """Create a new fund.
        
        Args:
            fund: Fund object with data to create
            
        Returns:
            Created Fund object
        """
        data = self._client._post(self._resource, fund.to_dict())
        return Fund.from_dict(data)
    
    def update(self, fund_id: int, fund: Fund) -> Fund:
        """Update an existing fund.
        
        Args:
            fund_id: Fund ID to update
            fund: Fund object with updated data
            
        Returns:
            Updated Fund object
        """
        data = self._client._patch(f"{self._resource}/{fund_id}", fund.to_dict())
        return Fund.from_dict(data)
    
    def delete(self, fund_id: int) -> None:
        """Delete a fund.
        
        Args:
            fund_id: Fund ID to delete
        """
        self._client._delete(f"{self._resource}/{fund_id}")