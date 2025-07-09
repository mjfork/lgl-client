"""Events API for LGL client."""

from typing import Any, List

from ..models.event import Event
from .client import LGLClient


class EventsAPI:
    """API for managing events in Little Green Light.
    
    Events represent fundraising events, gatherings, or activities
    that may have associated volunteer time or gifts.
    """
    
    _resource = "events"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Events API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(self, *, limit: int = 25, offset: int = 0) -> List[Event]:
        """List events for the account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of Event objects
        """
        data = self._client._get(self._resource, limit=limit, offset=offset)
        return [Event.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self) -> List[Event]:
        """Fetch all events using automatic pagination.
        
        Returns:
            List of all Event objects
        """
        def _list_page(**kwargs: Any) -> List[Event]:
            return self.list(**kwargs)
            
        items = list(self._client._paginate(_list_page))
        return [Event.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def retrieve(self, event_id: int) -> Event:
        """Retrieve a specific event by ID.
        
        Args:
            event_id: Event ID
            
        Returns:
            Event object
        """
        data = self._client._get(f"{self._resource}/{event_id}")
        return Event.from_dict(data)
    
    def create(self, event: Event) -> Event:
        """Create a new event.
        
        Args:
            event: Event object with data to create
            
        Returns:
            Created Event object
        """
        data = self._client._post(self._resource, event.to_dict())
        return Event.from_dict(data)
    
    def update(self, event_id: int, event: Event) -> Event:
        """Update an existing event.
        
        Args:
            event_id: Event ID to update
            event: Event object with updated data
            
        Returns:
            Updated Event object
        """
        data = self._client._patch(f"{self._resource}/{event_id}", event.to_dict())
        return Event.from_dict(data)
    
    def delete(self, event_id: int) -> None:
        """Delete an event.
        
        Args:
            event_id: Event ID to delete
        """
        self._client._delete(f"{self._resource}/{event_id}")