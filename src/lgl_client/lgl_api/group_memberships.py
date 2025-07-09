"""Group Memberships API for LGL client."""

from typing import Dict, List, Optional
from datetime import date

from ..lgl_api.client import LGLClient
from ..models.constituent import GroupMembership


class GroupMembershipsAPI:
    """API for managing constituent group memberships."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def list(
        self, 
        constituent_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all group memberships for a constituent.
        
        Args:
            constituent_id: The constituent ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with group membership items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'constituents/{constituent_id}/group_memberships', **params)
    
    def fetch_all(self, constituent_id: int) -> List[GroupMembership]:
        """Fetch all group memberships for a constituent with automatic pagination.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of all GroupMembership objects
        """
        def _list_page(**kwargs):
            return self.list(constituent_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [GroupMembership(**item) for item in items]
    
    def retrieve(self, group_membership_id: int) -> GroupMembership:
        """Retrieve a specific group membership by ID.
        
        Args:
            group_membership_id: The group membership ID
        
        Returns:
            GroupMembership object
        """
        response = self.client._get(f'group_memberships/{group_membership_id}')
        return GroupMembership(**response)
    
    def create(self, constituent_id: int, group_membership_data: Dict) -> GroupMembership:
        """Create a new group membership for a constituent.
        
        Args:
            constituent_id: The constituent ID
            group_membership_data: Dictionary containing group membership data:
                - group_id (required): Group ID
                - group_name (optional): Group name
                - date_start (optional): Start date (YYYY-MM-DD)
                - date_end (optional): End date (YYYY-MM-DD)
                - is_current (optional): Whether membership is currently active
        
        Returns:
            Created GroupMembership object
        """
        response = self.client._post(f'constituents/{constituent_id}/group_memberships', group_membership_data)
        return GroupMembership(**response)
    
    def update(self, group_membership_id: int, group_membership_data: Dict) -> GroupMembership:
        """Update an existing group membership.
        
        Args:
            group_membership_id: The group membership ID
            group_membership_data: Dictionary containing updated group membership data:
                - constituent_id (optional): Constituent ID
                - group_id (required): Group ID
                - group_name (optional): Group name
                - date_start (optional): Start date (YYYY-MM-DD)
                - date_end (optional): End date (YYYY-MM-DD)
                - is_current (optional): Whether membership is currently active
        
        Returns:
            Updated GroupMembership object
        """
        response = self.client._patch(f'group_memberships/{group_membership_id}', group_membership_data)
        return GroupMembership(**response)
    
    def delete(self, group_membership_id: int) -> Dict:
        """Delete a group membership.
        
        Args:
            group_membership_id: The group membership ID
        
        Returns:
            Success response
        """
        self.client._delete(f'group_memberships/{group_membership_id}')
        return {"result": "success"}
    
    # Helper methods for common operations
    
    def create_group_membership(
        self, 
        constituent_id: int, 
        group_id: int,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        is_current: bool = True
    ) -> GroupMembership:
        """Create a group membership with common parameters.
        
        Args:
            constituent_id: The constituent ID
            group_id: The group ID
            start_date: Membership start date (optional)
            end_date: Membership end date (optional)
            is_current: Whether membership is currently active
        
        Returns:
            Created GroupMembership object
        """
        data = {
            "group_id": group_id,
            "is_current": is_current
        }
        
        if start_date:
            data["date_start"] = start_date.strftime('%Y-%m-%d')
        if end_date:
            data["date_end"] = end_date.strftime('%Y-%m-%d')
        
        return self.create(constituent_id, data)
    
    def create_active_membership(self, constituent_id: int, group_id: int, start_date: date) -> GroupMembership:
        """Create an active group membership starting on a specific date.
        
        Args:
            constituent_id: The constituent ID
            group_id: The group ID
            start_date: Membership start date
        
        Returns:
            Created GroupMembership object
        """
        return self.create_group_membership(
            constituent_id=constituent_id,
            group_id=group_id,
            start_date=start_date,
            is_current=True
        )
    
    def end_membership(self, group_membership_id: int, end_date: date) -> GroupMembership:
        """End a group membership on a specific date.
        
        Args:
            group_membership_id: The group membership ID
            end_date: Date to end the membership
        
        Returns:
            Updated GroupMembership object
        """
        return self.update(group_membership_id, {
            "date_end": end_date.strftime('%Y-%m-%d'),
            "is_current": False
        })
    
    def reactivate_membership(self, group_membership_id: int, start_date: Optional[date] = None) -> GroupMembership:
        """Reactivate a group membership.
        
        Args:
            group_membership_id: The group membership ID
            start_date: New start date (optional, defaults to today)
        
        Returns:
            Updated GroupMembership object
        """
        from datetime import date
        
        data = {
            "is_current": True,
            "date_end": None  # Remove end date
        }
        
        if start_date:
            data["date_start"] = start_date.strftime('%Y-%m-%d')
        else:
            data["date_start"] = date.today().strftime('%Y-%m-%d')
        
        return self.update(group_membership_id, data)
    
    def get_active_memberships(self, constituent_id: int) -> List[GroupMembership]:
        """Get all active group memberships for a constituent.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of active GroupMembership objects
        """
        all_memberships = self.fetch_all(constituent_id)
        return [membership for membership in all_memberships if membership.is_current]
    
    def get_memberships_by_group(self, constituent_id: int, group_id: int) -> List[GroupMembership]:
        """Get all memberships for a constituent in a specific group.
        
        Args:
            constituent_id: The constituent ID
            group_id: The group ID
        
        Returns:
            List of GroupMembership objects for the specified group
        """
        all_memberships = self.fetch_all(constituent_id)
        return [membership for membership in all_memberships if membership.group_id == group_id]
    
    def change_group(self, group_membership_id: int, new_group_id: int) -> GroupMembership:
        """Change the group for an existing membership.
        
        Args:
            group_membership_id: The group membership ID
            new_group_id: New group ID
        
        Returns:
            Updated GroupMembership object
        """
        return self.update(group_membership_id, {"group_id": new_group_id})