"""Phone Numbers API for LGL client."""

from typing import Dict, List, Optional

from ..lgl_api.client import LGLClient
from ..models.constituent import PhoneNumber


class PhoneNumbersAPI:
    """API for managing constituent phone numbers."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def list(
        self, 
        constituent_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all phone numbers for a constituent.
        
        Args:
            constituent_id: The constituent ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with phone number items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'constituents/{constituent_id}/phone_numbers', **params)
    
    def fetch_all(self, constituent_id: int) -> List[PhoneNumber]:
        """Fetch all phone numbers for a constituent with automatic pagination.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of all PhoneNumber objects
        """
        def _list_page(**kwargs):
            return self.list(constituent_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [PhoneNumber(**item) for item in items]
    
    def retrieve(self, phone_number_id: int) -> PhoneNumber:
        """Retrieve a specific phone number by ID.
        
        Args:
            phone_number_id: The phone number ID
        
        Returns:
            PhoneNumber object
        """
        response = self.client._get(f'phone_numbers/{phone_number_id}')
        return PhoneNumber(**response)
    
    def create(self, constituent_id: int, phone_data: Dict) -> PhoneNumber:
        """Create a new phone number for a constituent.
        
        Args:
            constituent_id: The constituent ID
            phone_data: Dictionary containing phone number data:
                - number (optional): The phone number
                - phone_number_type_id (optional): Type ID
                - phone_type_name (optional): Type name (Home, Work, Mobile, etc.)
                - is_preferred (optional): Mark as preferred phone
                - not_current (optional): Mark as inactive
        
        Returns:
            Created PhoneNumber object
        """
        response = self.client._post(f'constituents/{constituent_id}/phone_numbers', phone_data)
        return PhoneNumber(**response)
    
    def update(self, phone_number_id: int, phone_data: Dict) -> PhoneNumber:
        """Update an existing phone number.
        
        Args:
            phone_number_id: The phone number ID
            phone_data: Dictionary containing updated phone number data
        
        Returns:
            Updated PhoneNumber object
        """
        response = self.client._patch(f'phone_numbers/{phone_number_id}', phone_data)
        return PhoneNumber(**response)
    
    def delete(self, phone_number_id: int) -> Dict:
        """Delete a phone number.
        
        Args:
            phone_number_id: The phone number ID
        
        Returns:
            Success response
        """
        self.client._delete(f'phone_numbers/{phone_number_id}')
        return {"result": "success"}
    
    # Helper methods for common operations
    
    def create_home_phone(self, constituent_id: int, number: str, is_preferred: bool = False) -> PhoneNumber:
        """Create a home phone number for a constituent.
        
        Args:
            constituent_id: The constituent ID
            number: The phone number
            is_preferred: Mark as preferred phone
        
        Returns:
            Created PhoneNumber object
        """
        return self.create(constituent_id, {
            "number": number,
            "phone_type_name": "Home",
            "is_preferred": is_preferred
        })
    
    def create_work_phone(self, constituent_id: int, number: str, is_preferred: bool = False) -> PhoneNumber:
        """Create a work phone number for a constituent.
        
        Args:
            constituent_id: The constituent ID
            number: The phone number
            is_preferred: Mark as preferred phone
        
        Returns:
            Created PhoneNumber object
        """
        return self.create(constituent_id, {
            "number": number,
            "phone_type_name": "Work",
            "is_preferred": is_preferred
        })
    
    def create_mobile_phone(self, constituent_id: int, number: str, is_preferred: bool = False) -> PhoneNumber:
        """Create a mobile phone number for a constituent.
        
        Args:
            constituent_id: The constituent ID
            number: The phone number
            is_preferred: Mark as preferred phone
        
        Returns:
            Created PhoneNumber object
        """
        return self.create(constituent_id, {
            "number": number,
            "phone_type_name": "Mobile",
            "is_preferred": is_preferred
        })
    
    def set_preferred(self, phone_number_id: int) -> PhoneNumber:
        """Set a phone number as preferred.
        
        Args:
            phone_number_id: The phone number ID
        
        Returns:
            Updated PhoneNumber object
        """
        return self.update(phone_number_id, {"is_preferred": True})
    
    def mark_inactive(self, phone_number_id: int) -> PhoneNumber:
        """Mark a phone number as inactive/not current.
        
        Args:
            phone_number_id: The phone number ID
        
        Returns:
            Updated PhoneNumber object
        """
        return self.update(phone_number_id, {"not_current": True})