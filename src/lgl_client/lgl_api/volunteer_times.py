"""Volunteer Times API for LGL client."""

from typing import Dict, List, Optional
from datetime import date

from ..lgl_api.client import LGLClient
from ..models.volunteer_time import VolunteerTime


class VolunteerTimesAPI:
    """API for managing volunteer time records."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def list(
        self, 
        constituent_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all volunteer times for a constituent.
        
        Args:
            constituent_id: The constituent ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with volunteer time items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'constituents/{constituent_id}/volunteer_times', **params)
    
    def list_all(
        self,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all volunteer times for the account.
        
        Args:
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with volunteer time items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get('volunteer_times', **params)
    
    def search(
        self,
        date_from: Optional[date] = None,
        date_to: Optional[date] = None,
        description: Optional[str] = None,
        volunteering_category_id: Optional[int] = None,
        constituent_id: Optional[int] = None,
        constituent_keyword: Optional[str] = None,
        updated_from: Optional[date] = None,
        updated_to: Optional[date] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> Dict:
        """Search for volunteer times with various criteria.
        
        Args:
            date_from: Start date for volunteer time records (YYYY-MM-DD)
            date_to: End date for volunteer time records (YYYY-MM-DD)
            description: Text to search in description field
            volunteering_category_id: Filter by volunteering category ID
            constituent_id: Filter by constituent ID
            constituent_keyword: Search constituents by keyword
            updated_from: Filter by update date from (YYYY-MM-DD)
            updated_to: Filter by update date to (YYYY-MM-DD)
            sort: Sort field (date, constituent_id) with optional '!' for reverse
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with volunteer time items
        """
        params = {}
        
        if date_from is not None:
            params['date_from'] = date_from.strftime('%Y-%m-%d')
        if date_to is not None:
            params['date_to'] = date_to.strftime('%Y-%m-%d')
        if description is not None:
            params['description'] = description
        if volunteering_category_id is not None:
            params['volunteering_category_id'] = volunteering_category_id
        if constituent_id is not None:
            params['constituent_id'] = constituent_id
        if constituent_keyword is not None:
            params['constituent_keyword'] = constituent_keyword
        if updated_from is not None:
            params['updated_from'] = updated_from.strftime('%Y-%m-%d')
        if updated_to is not None:
            params['updated_to'] = updated_to.strftime('%Y-%m-%d')
        if sort is not None:
            params['sort'] = sort
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get('volunteer_times/search', **params)
    
    def fetch_all(self, constituent_id: int) -> List[VolunteerTime]:
        """Fetch all volunteer times for a constituent with automatic pagination.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of all VolunteerTime objects
        """
        def _list_page(**kwargs):
            return self.list(constituent_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [VolunteerTime(**item) for item in items]
    
    def fetch_all_account_volunteer_times(self) -> List[VolunteerTime]:
        """Fetch all volunteer times for the account with automatic pagination.
        
        Returns:
            List of all VolunteerTime objects in the account
        """
        def _list_page(**kwargs):
            return self.list_all(**kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [VolunteerTime(**item) for item in items]
    
    def search_volunteer_times(
        self,
        date_from: Optional[date] = None,
        date_to: Optional[date] = None,
        description: Optional[str] = None,
        volunteering_category_id: Optional[int] = None,
        constituent_id: Optional[int] = None,
        sort: Optional[str] = None
    ) -> List[VolunteerTime]:
        """Search for volunteer times and return as VolunteerTime objects.
        
        Args:
            date_from: Start date for volunteer time records
            date_to: End date for volunteer time records
            description: Text to search in description field
            volunteering_category_id: Filter by volunteering category ID
            constituent_id: Filter by constituent ID
            sort: Sort field (date, constituent_id) with optional '!' for reverse
        
        Returns:
            List of VolunteerTime objects
        """
        def _search_page(**kwargs):
            return self.search(
                date_from=date_from,
                date_to=date_to,
                description=description,
                volunteering_category_id=volunteering_category_id,
                constituent_id=constituent_id,
                sort=sort,
                **kwargs
            )
        
        items = list(self.client._paginate(_search_page))
        return [VolunteerTime(**item) for item in items]
    
    def retrieve(self, volunteer_time_id: int) -> VolunteerTime:
        """Retrieve a specific volunteer time by ID.
        
        Args:
            volunteer_time_id: The volunteer time ID
        
        Returns:
            VolunteerTime object
        """
        response = self.client._get(f'volunteer_times/{volunteer_time_id}')
        return VolunteerTime(**response)
    
    def create(self, constituent_id: int, volunteer_time_data: Dict) -> VolunteerTime:
        """Create a new volunteer time record for a constituent.
        
        Args:
            constituent_id: The constituent ID
            volunteer_time_data: Dictionary containing volunteer time data:
                - volunteering_category_id (required): Category ID for the volunteer work
                - external_id (optional): External system reference
                - description (optional): Description of volunteer work
                - hours (optional): Planned hours
                - completed_hours (optional): Actual completed hours
                - date (optional): Date of volunteer work (YYYY-MM-DD)
                - end_date (optional): End date for multi-day volunteer work
                - custom_attrs (optional): Custom field data
        
        Returns:
            Created VolunteerTime object
        """
        response = self.client._post(f'constituents/{constituent_id}/volunteer_times', volunteer_time_data)
        return VolunteerTime(**response)
    
    def update(self, volunteer_time_id: int, volunteer_time_data: Dict) -> VolunteerTime:
        """Update an existing volunteer time record.
        
        Args:
            volunteer_time_id: The volunteer time ID
            volunteer_time_data: Dictionary containing updated volunteer time data
        
        Returns:
            Updated VolunteerTime object
        """
        response = self.client._patch(f'volunteer_times/{volunteer_time_id}', volunteer_time_data)
        return VolunteerTime(**response)
    
    def delete(self, volunteer_time_id: int) -> Dict:
        """Delete a volunteer time record.
        
        Args:
            volunteer_time_id: The volunteer time ID
        
        Returns:
            Success response
        """
        self.client._delete(f'volunteer_times/{volunteer_time_id}')
        return {"result": "success"}
    
    # Helper methods for common operations
    
    def create_volunteer_time(
        self, 
        constituent_id: int, 
        category_id: int,
        hours: float,
        volunteer_date: date,
        description: Optional[str] = None,
        completed_hours: Optional[float] = None
    ) -> VolunteerTime:
        """Create a volunteer time record with common parameters.
        
        Args:
            constituent_id: The constituent ID
            category_id: Volunteering category ID
            hours: Planned volunteer hours
            volunteer_date: Date of volunteer work
            description: Description of volunteer work
            completed_hours: Actual completed hours (defaults to planned hours)
        
        Returns:
            Created VolunteerTime object
        """
        data = {
            "volunteering_category_id": category_id,
            "hours": hours,
            "date": volunteer_date.strftime('%Y-%m-%d')
        }
        
        if description:
            data["description"] = description
        if completed_hours is not None:
            data["completed_hours"] = completed_hours
        else:
            data["completed_hours"] = hours  # Default completed to planned
        
        return self.create(constituent_id, data)
    
    def mark_completed(self, volunteer_time_id: int, completed_hours: float) -> VolunteerTime:
        """Mark a volunteer time record as completed with actual hours.
        
        Args:
            volunteer_time_id: The volunteer time ID
            completed_hours: Actual hours completed
        
        Returns:
            Updated VolunteerTime object
        """
        return self.update(volunteer_time_id, {"completed_hours": completed_hours})
    
    def search_by_category(self, category_id: int, **kwargs) -> List[VolunteerTime]:
        """Search volunteer times by category ID.
        
        Args:
            category_id: Volunteering category ID
            **kwargs: Additional search parameters
        
        Returns:
            List of matching VolunteerTime objects
        """
        return self.search_volunteer_times(volunteering_category_id=category_id, **kwargs)
    
    def search_by_date_range(self, start_date: date, end_date: date, **kwargs) -> List[VolunteerTime]:
        """Search volunteer times within a date range.
        
        Args:
            start_date: Start date for search
            end_date: End date for search
            **kwargs: Additional search parameters
        
        Returns:
            List of matching VolunteerTime objects
        """
        return self.search_volunteer_times(date_from=start_date, date_to=end_date, **kwargs)