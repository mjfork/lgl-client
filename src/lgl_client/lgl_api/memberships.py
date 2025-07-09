"""Memberships API for LGL client."""

from typing import Dict, List, Optional
from datetime import date

from ..lgl_api.client import LGLClient
from ..models.constituent import Membership


class MembershipsAPI:
    """API for managing constituent memberships."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def list(
        self, 
        constituent_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all memberships for a constituent.
        
        Args:
            constituent_id: The constituent ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with membership items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'constituents/{constituent_id}/memberships', **params)
    
    def fetch_all(self, constituent_id: int) -> List[Membership]:
        """Fetch all memberships for a constituent with automatic pagination.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of all Membership objects
        """
        def _list_page(**kwargs):
            return self.list(constituent_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [Membership(**item) for item in items]
    
    def retrieve(self, membership_id: int) -> Membership:
        """Retrieve a specific membership by ID.
        
        Args:
            membership_id: The membership ID
        
        Returns:
            Membership object
        """
        response = self.client._get(f'memberships/{membership_id}')
        return Membership(**response)
    
    def create(self, constituent_id: int, membership_data: Dict) -> Membership:
        """Create a new membership for a constituent.
        
        Args:
            constituent_id: The constituent ID
            membership_data: Dictionary containing membership data:
                - membership_level_id (optional): Membership level ID
                - membership_level_name (optional): Membership level name
                - date_start (optional): Start date (YYYY-MM-DD)
                - finish_date (optional): End date (YYYY-MM-DD)
                - note (optional): Membership notes
        
        Returns:
            Created Membership object
        """
        response = self.client._post(f'constituents/{constituent_id}/memberships', membership_data)
        return Membership(**response)
    
    def update(self, membership_id: int, membership_data: Dict) -> Membership:
        """Update an existing membership.
        
        Args:
            membership_id: The membership ID
            membership_data: Dictionary containing updated membership data
        
        Returns:
            Updated Membership object
        """
        response = self.client._patch(f'memberships/{membership_id}', membership_data)
        return Membership(**response)
    
    def delete(self, membership_id: int) -> Dict:
        """Delete a membership.
        
        Args:
            membership_id: The membership ID
        
        Returns:
            Success response
        """
        self.client._delete(f'memberships/{membership_id}')
        return {"result": "success"}
    
    # Helper methods for common operations
    
    def create_membership_by_level_id(
        self, 
        constituent_id: int, 
        membership_level_id: int,
        start_date: date,
        end_date: Optional[date] = None,
        note: Optional[str] = None
    ) -> Membership:
        """Create a membership using membership level ID.
        
        Args:
            constituent_id: The constituent ID
            membership_level_id: The membership level ID
            start_date: Membership start date
            end_date: Membership end date (optional)
            note: Membership notes (optional)
        
        Returns:
            Created Membership object
        """
        data = {
            "membership_level_id": membership_level_id,
            "date_start": start_date.strftime('%Y-%m-%d')
        }
        
        if end_date:
            data["finish_date"] = end_date.strftime('%Y-%m-%d')
        if note:
            data["note"] = note
        
        return self.create(constituent_id, data)
    
    def create_membership_by_level_name(
        self, 
        constituent_id: int, 
        membership_level_name: str,
        start_date: date,
        end_date: Optional[date] = None,
        note: Optional[str] = None
    ) -> Membership:
        """Create a membership using membership level name.
        
        Args:
            constituent_id: The constituent ID
            membership_level_name: The membership level name
            start_date: Membership start date
            end_date: Membership end date (optional)
            note: Membership notes (optional)
        
        Returns:
            Created Membership object
        """
        data = {
            "membership_level_name": membership_level_name,
            "date_start": start_date.strftime('%Y-%m-%d')
        }
        
        if end_date:
            data["finish_date"] = end_date.strftime('%Y-%m-%d')
        if note:
            data["note"] = note
        
        return self.create(constituent_id, data)
    
    def extend_membership(self, membership_id: int, new_end_date: date) -> Membership:
        """Extend a membership to a new end date.
        
        Args:
            membership_id: The membership ID
            new_end_date: New end date for the membership
        
        Returns:
            Updated Membership object
        """
        return self.update(membership_id, {
            "finish_date": new_end_date.strftime('%Y-%m-%d')
        })
    
    def add_note(self, membership_id: int, note: str) -> Membership:
        """Add or update a note on a membership.
        
        Args:
            membership_id: The membership ID
            note: Note text to add
        
        Returns:
            Updated Membership object
        """
        return self.update(membership_id, {"note": note})
    
    def change_level(self, membership_id: int, new_level_id: int) -> Membership:
        """Change the membership level.
        
        Args:
            membership_id: The membership ID
            new_level_id: New membership level ID
        
        Returns:
            Updated Membership object
        """
        return self.update(membership_id, {"membership_level_id": new_level_id})
    
    def get_active_memberships(self, constituent_id: int) -> List[Membership]:
        """Get all active memberships for a constituent.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of active Membership objects (no end date or future end date)
        """
        from datetime import date
        
        all_memberships = self.fetch_all(constituent_id)
        today = date.today()
        
        active_memberships = []
        for membership in all_memberships:
            # Active if no finish date or finish date is in the future
            if membership.finish_date is None or membership.finish_date > today:
                active_memberships.append(membership)
        
        return active_memberships