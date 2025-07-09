"""Campaigns API for LGL client."""

from typing import Any, List

from ..models.campaign import Campaign
from .client import LGLClient


class CampaignsAPI:
    """API for managing campaigns in Little Green Light.
    
    Campaigns represent fundraising initiatives or drives
    that span multiple appeals and activities.
    """
    
    _resource = "campaigns"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Campaigns API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(self, *, limit: int = 25, offset: int = 0) -> List[Campaign]:
        """List campaigns for the account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of Campaign objects
        """
        data = self._client._get(self._resource, limit=limit, offset=offset)
        return [Campaign.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self) -> List[Campaign]:
        """Fetch all campaigns using automatic pagination.
        
        Returns:
            List of all Campaign objects
        """
        def _list_page(**kwargs: Any) -> List[Campaign]:
            return self.list(**kwargs)
            
        items = list(self._client._paginate(_list_page))
        return [Campaign.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def retrieve(self, campaign_id: int) -> Campaign:
        """Retrieve a specific campaign by ID.
        
        Args:
            campaign_id: Campaign ID
            
        Returns:
            Campaign object
        """
        data = self._client._get(f"{self._resource}/{campaign_id}")
        return Campaign.from_dict(data)
    
    def create(self, campaign: Campaign) -> Campaign:
        """Create a new campaign.
        
        Args:
            campaign: Campaign object with data to create
            
        Returns:
            Created Campaign object
        """
        data = self._client._post(self._resource, campaign.to_dict())
        return Campaign.from_dict(data)
    
    def update(self, campaign_id: int, campaign: Campaign) -> Campaign:
        """Update an existing campaign.
        
        Args:
            campaign_id: Campaign ID to update
            campaign: Campaign object with updated data
            
        Returns:
            Updated Campaign object
        """
        data = self._client._patch(f"{self._resource}/{campaign_id}", campaign.to_dict())
        return Campaign.from_dict(data)
    
    def delete(self, campaign_id: int) -> None:
        """Delete a campaign.
        
        Args:
            campaign_id: Campaign ID to delete
        """
        self._client._delete(f"{self._resource}/{campaign_id}")