"""Email Addresses API for LGL client."""

from typing import Dict, List, Optional

from ..lgl_api.client import LGLClient
from ..models.constituent import EmailAddress


class EmailAddressesAPI:
    """API for managing constituent email addresses."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def list(
        self, 
        constituent_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all email addresses for a constituent.
        
        Args:
            constituent_id: The constituent ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with email address items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'constituents/{constituent_id}/email_addresses', **params)
    
    def fetch_all(self, constituent_id: int) -> List[EmailAddress]:
        """Fetch all email addresses for a constituent with automatic pagination.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of all EmailAddress objects
        """
        def _list_page(**kwargs):
            return self.list(constituent_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [EmailAddress(**item) for item in items]
    
    def retrieve(self, email_address_id: int) -> EmailAddress:
        """Retrieve a specific email address by ID.
        
        Args:
            email_address_id: The email address ID
        
        Returns:
            EmailAddress object
        """
        response = self.client._get(f'email_addresses/{email_address_id}')
        return EmailAddress(**response)
    
    def create(self, constituent_id: int, email_data: Dict) -> EmailAddress:
        """Create a new email address for a constituent.
        
        Args:
            constituent_id: The constituent ID
            email_data: Dictionary containing email address data:
                - address (required): The email address
                - email_address_type_id (required): Type ID (1=Home, 2=Work, 3=Other, 4=Assistant)
                - email_type_name (optional): Type name
                - is_preferred (optional): Mark as preferred email
                - not_current (optional): Mark as inactive
        
        Returns:
            Created EmailAddress object
        """
        response = self.client._post(f'constituents/{constituent_id}/email_addresses', email_data)
        return EmailAddress(**response)
    
    def update(self, email_address_id: int, email_data: Dict) -> EmailAddress:
        """Update an existing email address.
        
        Args:
            email_address_id: The email address ID
            email_data: Dictionary containing updated email address data
        
        Returns:
            Updated EmailAddress object
        """
        response = self.client._patch(f'email_addresses/{email_address_id}', email_data)
        return EmailAddress(**response)
    
    def delete(self, email_address_id: int) -> Dict:
        """Delete an email address.
        
        Args:
            email_address_id: The email address ID
        
        Returns:
            Success response
        """
        self.client._delete(f'email_addresses/{email_address_id}')
        return {"result": "success"}
    
    # Helper methods for common operations
    
    def create_home_email(self, constituent_id: int, address: str, is_preferred: bool = False) -> EmailAddress:
        """Create a home email address for a constituent.
        
        Args:
            constituent_id: The constituent ID
            address: The email address
            is_preferred: Mark as preferred email
        
        Returns:
            Created EmailAddress object
        """
        return self.create(constituent_id, {
            "address": address,
            "email_address_type_id": 1,  # Home
            "email_type_name": "Home",
            "is_preferred": is_preferred
        })
    
    def create_work_email(self, constituent_id: int, address: str, is_preferred: bool = False) -> EmailAddress:
        """Create a work email address for a constituent.
        
        Args:
            constituent_id: The constituent ID
            address: The email address
            is_preferred: Mark as preferred email
        
        Returns:
            Created EmailAddress object
        """
        return self.create(constituent_id, {
            "address": address,
            "email_address_type_id": 2,  # Work
            "email_type_name": "Work",
            "is_preferred": is_preferred
        })
    
    def set_preferred(self, email_address_id: int) -> EmailAddress:
        """Set an email address as preferred.
        
        Args:
            email_address_id: The email address ID
        
        Returns:
            Updated EmailAddress object
        """
        return self.update(email_address_id, {"is_preferred": True})
    
    def mark_inactive(self, email_address_id: int) -> EmailAddress:
        """Mark an email address as inactive/not current.
        
        Args:
            email_address_id: The email address ID
        
        Returns:
            Updated EmailAddress object
        """
        return self.update(email_address_id, {"not_current": True})