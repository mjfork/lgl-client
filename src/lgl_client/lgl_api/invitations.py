"""Invitations API for LGL client."""

from typing import Any, List

from ..models.invitation import Invitation
from .client import LGLClient


class InvitationsAPI:
    """API for managing invitations in Little Green Light.
    
    Invitations represent event invitations sent to constituents
    and track RSVP status, attendance, and related details.
    """
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Invitations API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list_for_constituent(
        self, 
        constituent_id: int, 
        *, 
        limit: int = 25, 
        offset: int = 0
    ) -> List[Invitation]:
        """List invitations for a specific constituent.
        
        Args:
            constituent_id: Constituent ID
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of Invitation objects
        """
        data = self._client._get(
            f"constituents/{constituent_id}/invitations",
            limit=limit,
            offset=offset
        )
        return [Invitation.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all_for_constituent(self, constituent_id: int) -> List[Invitation]:
        """Fetch all invitations for a constituent using automatic pagination.
        
        Args:
            constituent_id: Constituent ID
            
        Returns:
            List of all Invitation objects for the constituent
        """
        def _list_page(**kwargs: Any) -> List[Invitation]:
            return self.list_for_constituent(constituent_id, **kwargs)
        
        items = list(self._client._paginate(_list_page))
        return [Invitation.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def list_for_event(
        self, 
        event_id: int, 
        *, 
        limit: int = 25, 
        offset: int = 0
    ) -> List[Invitation]:
        """List invitations for a specific event.
        
        Args:
            event_id: Event ID
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of Invitation objects
        """
        data = self._client._get(
            f"events/{event_id}/invitations",
            limit=limit,
            offset=offset
        )
        return [Invitation.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all_for_event(self, event_id: int) -> List[Invitation]:
        """Fetch all invitations for an event using automatic pagination.
        
        Args:
            event_id: Event ID
            
        Returns:
            List of all Invitation objects for the event
        """
        def _list_page(**kwargs: Any) -> List[Invitation]:
            return self.list_for_event(event_id, **kwargs)
        
        items = list(self._client._paginate(_list_page))
        return [Invitation.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def create_for_constituent(self, constituent_id: int, invitation: Invitation) -> Invitation:
        """Create a new invitation for a constituent.
        
        Args:
            constituent_id: Constituent ID
            invitation: Invitation object with data to create
            
        Returns:
            Created Invitation object
        """
        data = self._client._post(f"constituents/{constituent_id}/invitations", invitation.to_dict())
        return Invitation.from_dict(data)