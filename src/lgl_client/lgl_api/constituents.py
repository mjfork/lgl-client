"""Constituents API for LGL client."""

from typing import Dict, List, Optional, Union

from ..lgl_api.client import LGLClient
from ..models.constituent import Constituent


class ConstituentsAPI:
    """API for managing constituents."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def search(
        self,
        query_params: List[str],
        expand: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> Dict:
        """Search for constituents.
        
        Args:
            query_params: List of query strings (e.g., ["name=brady", "city=Seattle"])
            expand: Comma-separated list of data structures to expand:
                   'class_affiliations,relationships,street_addresses,phone_numbers,
                    email_addresses,web_addresses,categories,groups,memberships,custom_attrs'
            sort: Sort field with optional '!' for reverse order
                 (name, external_id, lgl_id, date_created, date_updated, 
                  membership_level, membership_end_date_from)
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
        
        Returns:
            Paginated response with constituent items
        """
        params = {}
        
        # Add query parameters - handle multiple q[] parameters
        if query_params:
            params['q'] = query_params
        
        if expand:
            params['expand'] = expand
        if sort:
            params['sort'] = sort
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get('constituents/search', **params)
    
    def search_constituents(
        self,
        query_params: List[str],
        expand: Optional[str] = None,
        sort: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> List[Constituent]:
        """Search for constituents and return as Constituent objects.
        
        Args:
            query_params: List of query strings (e.g., ["name=brady", "city=Seattle"])
            expand: Comma-separated list of data structures to expand
            sort: Sort field with optional '!' for reverse order
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
        
        Returns:
            List of Constituent objects
        """
        response = self.search(query_params, expand, sort, limit, offset)
        return [Constituent(**item) for item in response.get('items', [])]
    
    def search_all_constituents(
        self,
        query_params: List[str],
        expand: Optional[str] = None,
        sort: Optional[str] = None
    ) -> List[Constituent]:
        """Search for all matching constituents with automatic pagination.
        
        Args:
            query_params: List of query strings (e.g., ["name=brady", "city=Seattle"])
            expand: Comma-separated list of data structures to expand
            sort: Sort field with optional '!' for reverse order
        
        Returns:
            List of all matching Constituent objects
        """
        all_constituents = []
        offset = 0
        limit = 100
        
        while True:
            response = self.search(query_params, expand, sort, limit, offset)
            items = response.get('items', [])
            
            if not items:
                break
            
            all_constituents.extend([Constituent(**item) for item in items])
            
            # Check if there are more items
            if response.get('next_item') is None:
                break
            
            offset = response.get('next_item', 0)
        
        return all_constituents
    
    def list(self, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict:
        """List all constituents for an account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
        
        Returns:
            Paginated response with constituent items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get('constituents', **params)
    
    def fetch_all(self) -> List[Constituent]:
        """Fetch all constituents with automatic pagination.
        
        Returns:
            List of all Constituent objects
        """
        def _list_page(**kwargs):
            return self.list(**kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [Constituent(**item) for item in items]
    
    def retrieve(self, constituent_id: int) -> Constituent:
        """Retrieve a specific constituent by ID.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            Constituent object
        """
        response = self.client._get(f'constituents/{constituent_id}')
        return Constituent(**response)
    
    def create(self, constituent_data: Dict) -> Constituent:
        """Create a new constituent.
        
        Args:
            constituent_data: Dictionary containing constituent data including:
                - first_name (required): First name
                - last_name (required): Last name
                - email_addresses (required): List of email address objects
                - Optional fields: is_org, external_constituent_id, prefix, etc.
                - Related objects: class_affiliations, relationships, street_addresses,
                  phone_numbers, web_addresses, categories, groups, custom_attrs
        
        Returns:
            Created Constituent object
        """
        response = self.client._post('constituents', constituent_data)
        return Constituent(**response)
    
    def update(self, constituent_id: int, constituent_data: Dict) -> Constituent:
        """Update an existing constituent.
        
        Args:
            constituent_id: The constituent ID
            constituent_data: Dictionary containing updated constituent data
                Can include remove_previous_* flags to replace related objects
        
        Returns:
            Updated Constituent object
        """
        response = self.client._patch(f'constituents/{constituent_id}', constituent_data)
        return Constituent(**response)
    
    def delete(self, constituent_id: int) -> Dict:
        """Delete a constituent.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            Success response
        """
        self.client._delete(f'constituents/{constituent_id}')
        return {"result": "success"}
    
    # Helper methods for common search scenarios
    
    def search_by_name(self, name: str, **kwargs) -> List[Constituent]:
        """Search constituents by name.
        
        Args:
            name: Name to search for
            **kwargs: Additional search parameters (expand, sort, etc.)
        
        Returns:
            List of matching Constituent objects
        """
        return self.search_constituents([f"name={name}"], **kwargs)
    
    def search_by_email(self, email: str, **kwargs) -> List[Constituent]:
        """Search constituents by email address.
        
        Args:
            email: Email address to search for
            **kwargs: Additional search parameters (expand, sort, etc.)
        
        Returns:
            List of matching Constituent objects
        """
        return self.search_constituents([f"eaddr={email}"], **kwargs)
    
    def search_by_phone(self, phone: str, **kwargs) -> List[Constituent]:
        """Search constituents by phone number.
        
        Args:
            phone: Phone number to search for
            **kwargs: Additional search parameters (expand, sort, etc.)
        
        Returns:
            List of matching Constituent objects
        """
        return self.search_constituents([f"phone_number={phone}"], **kwargs)
    
    def search_by_external_id(self, external_id: str, **kwargs) -> List[Constituent]:
        """Search constituents by external ID.
        
        Args:
            external_id: External ID to search for
            **kwargs: Additional search parameters (expand, sort, etc.)
        
        Returns:
            List of matching Constituent objects
        """
        return self.search_constituents([f"external_id={external_id}"], **kwargs)
    
    def search_organizations(self, **kwargs) -> List[Constituent]:
        """Search for organization constituents only.
        
        Args:
            **kwargs: Additional search parameters (expand, sort, etc.)
        
        Returns:
            List of organization Constituent objects
        """
        return self.search_constituents(["constituent_type=1"], **kwargs)
    
    def search_individuals(self, **kwargs) -> List[Constituent]:
        """Search for individual constituents only.
        
        Args:
            **kwargs: Additional search parameters (expand, sort, etc.)
        
        Returns:
            List of individual Constituent objects
        """
        return self.search_constituents(["constituent_type=0"], **kwargs)
    
    def search_by_keyword(self, keyword_id: int, **kwargs) -> List[Constituent]:
        """Search constituents by keyword ID.
        
        Args:
            keyword_id: Keyword ID to search for
            **kwargs: Additional search parameters (expand, sort, etc.)
        
        Returns:
            List of matching Constituent objects
        """
        return self.search_constituents([f"keyword={keyword_id}"], **kwargs)
    
    def search_by_group(self, group_ids: Union[int, List[int]], **kwargs) -> List[Constituent]:
        """Search constituents by group membership.
        
        Args:
            group_ids: Single group ID or list of group IDs
            **kwargs: Additional search parameters (expand, sort, etc.)
        
        Returns:
            List of matching Constituent objects
        """
        if isinstance(group_ids, int):
            group_ids = [group_ids]
        group_param = ",".join(map(str, group_ids))
        return self.search_constituents([f"groups={group_param}"], **kwargs)
    
    def search_by_membership_level(self, level_ids: Union[int, List[int]], **kwargs) -> List[Constituent]:
        """Search constituents by membership level.
        
        Args:
            level_ids: Single membership level ID or list of level IDs
            **kwargs: Additional search parameters (expand, sort, etc.)
        
        Returns:
            List of matching Constituent objects
        """
        if isinstance(level_ids, int):
            level_ids = [level_ids]
        level_param = ",".join(map(str, level_ids))
        return self.search_constituents([f"membership_level={level_param}"], **kwargs)