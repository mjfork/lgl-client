"""Web Addresses API for LGL client."""

from typing import Dict, List, Optional

from ..lgl_api.client import LGLClient
from ..models.constituent import WebAddress


class WebAddressesAPI:
    """API for managing constituent web addresses."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def list(
        self, 
        constituent_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all web addresses for a constituent.
        
        Args:
            constituent_id: The constituent ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with web address items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'constituents/{constituent_id}/web_addresses', **params)
    
    def fetch_all(self, constituent_id: int) -> List[WebAddress]:
        """Fetch all web addresses for a constituent with automatic pagination.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of all WebAddress objects
        """
        def _list_page(**kwargs):
            return self.list(constituent_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [WebAddress(**item) for item in items]
    
    def retrieve(self, web_address_id: int) -> WebAddress:
        """Retrieve a specific web address by ID.
        
        Args:
            web_address_id: The web address ID
        
        Returns:
            WebAddress object
        """
        response = self.client._get(f'web_addresses/{web_address_id}')
        return WebAddress(**response)
    
    def create(self, constituent_id: int, web_data: Dict) -> WebAddress:
        """Create a new web address for a constituent.
        
        Args:
            constituent_id: The constituent ID
            web_data: Dictionary containing web address data:
                - url (optional): The web address URL
                - web_address_type_id (optional): Web address type ID
                - web_address_type_name (optional): Type name (Website, Facebook, etc.)
                - is_preferred (optional): Mark as preferred web address
        
        Returns:
            Created WebAddress object
        """
        response = self.client._post(f'constituents/{constituent_id}/web_addresses', web_data)
        return WebAddress(**response)
    
    def update(self, web_address_id: int, web_data: Dict) -> WebAddress:
        """Update an existing web address.
        
        Args:
            web_address_id: The web address ID
            web_data: Dictionary containing updated web address data
        
        Returns:
            Updated WebAddress object
        """
        response = self.client._patch(f'web_addresses/{web_address_id}', web_data)
        return WebAddress(**response)
    
    def delete(self, web_address_id: int) -> Dict:
        """Delete a web address.
        
        Args:
            web_address_id: The web address ID
        
        Returns:
            Success response
        """
        self.client._delete(f'web_addresses/{web_address_id}')
        return {"result": "success"}
    
    # Helper methods for common operations
    
    def create_website(self, constituent_id: int, url: str, is_preferred: bool = False) -> WebAddress:
        """Create a website address for a constituent.
        
        Args:
            constituent_id: The constituent ID
            url: The website URL
            is_preferred: Mark as preferred web address
        
        Returns:
            Created WebAddress object
        """
        return self.create(constituent_id, {
            "url": url,
            "web_address_type_name": "Website",
            "is_preferred": is_preferred
        })
    
    def create_facebook(self, constituent_id: int, url: str, is_preferred: bool = False) -> WebAddress:
        """Create a Facebook address for a constituent.
        
        Args:
            constituent_id: The constituent ID
            url: The Facebook URL
            is_preferred: Mark as preferred web address
        
        Returns:
            Created WebAddress object
        """
        return self.create(constituent_id, {
            "url": url,
            "web_address_type_name": "Facebook",
            "is_preferred": is_preferred
        })
    
    def create_linkedin(self, constituent_id: int, url: str, is_preferred: bool = False) -> WebAddress:
        """Create a LinkedIn address for a constituent.
        
        Args:
            constituent_id: The constituent ID
            url: The LinkedIn URL
            is_preferred: Mark as preferred web address
        
        Returns:
            Created WebAddress object
        """
        return self.create(constituent_id, {
            "url": url,
            "web_address_type_name": "LinkedIn",
            "is_preferred": is_preferred
        })
    
    def create_twitter(self, constituent_id: int, url: str, is_preferred: bool = False) -> WebAddress:
        """Create a Twitter address for a constituent.
        
        Args:
            constituent_id: The constituent ID
            url: The Twitter URL
            is_preferred: Mark as preferred web address
        
        Returns:
            Created WebAddress object
        """
        return self.create(constituent_id, {
            "url": url,
            "web_address_type_name": "Twitter",
            "is_preferred": is_preferred
        })
    
    def set_preferred(self, web_address_id: int) -> WebAddress:
        """Set a web address as preferred.
        
        Args:
            web_address_id: The web address ID
        
        Returns:
            Updated WebAddress object
        """
        return self.update(web_address_id, {"is_preferred": True})