"""Street Addresses API for LGL client."""

from typing import Dict, List, Optional

from ..lgl_api.client import LGLClient
from ..models.constituent import StreetAddress


class StreetAddressesAPI:
    """API for managing constituent street addresses."""
    
    def __init__(self, client: LGLClient):
        self.client = client
    
    def list(
        self, 
        constituent_id: int,
        limit: Optional[int] = None, 
        offset: Optional[int] = None
    ) -> Dict:
        """List all street addresses for a constituent.
        
        Args:
            constituent_id: The constituent ID
            limit: Number of entries to return
            offset: Start at given entry
        
        Returns:
            Paginated response with street address items
        """
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset
        
        return self.client._get(f'constituents/{constituent_id}/street_addresses', **params)
    
    def fetch_all(self, constituent_id: int) -> List[StreetAddress]:
        """Fetch all street addresses for a constituent with automatic pagination.
        
        Args:
            constituent_id: The constituent ID
        
        Returns:
            List of all StreetAddress objects
        """
        def _list_page(**kwargs):
            return self.list(constituent_id, **kwargs)
        
        items = list(self.client._paginate(_list_page))
        return [StreetAddress(**item) for item in items]
    
    def retrieve(self, street_address_id: int) -> StreetAddress:
        """Retrieve a specific street address by ID.
        
        Args:
            street_address_id: The street address ID
        
        Returns:
            StreetAddress object
        """
        response = self.client._get(f'street_addresses/{street_address_id}')
        return StreetAddress(**response)
    
    def create(self, constituent_id: int, address_data: Dict) -> StreetAddress:
        """Create a new street address for a constituent.
        
        Args:
            constituent_id: The constituent ID
            address_data: Dictionary containing street address data:
                - street (optional): Street address line
                - city (optional): City name
                - state (optional): State/province code
                - postal_code (optional): ZIP/postal code
                - country (optional): Country name
                - county (optional): County name
                - street_address_type_id (optional): Address type ID
                - street_type_name (optional): Address type name
                - is_preferred (optional): Mark as preferred address
                - not_current (optional): Mark as inactive
                - seasonal (optional): Mark as seasonal address
                - seasonal_from (optional): Seasonal start date
                - seasonal_to (optional): Seasonal end date
        
        Returns:
            Created StreetAddress object
        """
        response = self.client._post(f'constituents/{constituent_id}/street_addresses', address_data)
        return StreetAddress(**response)
    
    def update(self, street_address_id: int, address_data: Dict) -> StreetAddress:
        """Update an existing street address.
        
        Args:
            street_address_id: The street address ID
            address_data: Dictionary containing updated street address data
        
        Returns:
            Updated StreetAddress object
        """
        response = self.client._patch(f'street_addresses/{street_address_id}', address_data)
        return StreetAddress(**response)
    
    def delete(self, street_address_id: int) -> Dict:
        """Delete a street address.
        
        Args:
            street_address_id: The street address ID
        
        Returns:
            Success response
        """
        self.client._delete(f'street_addresses/{street_address_id}')
        return {"result": "success"}
    
    # Helper methods for common operations
    
    def create_home_address(
        self, 
        constituent_id: int, 
        street: str, 
        city: str, 
        state: str, 
        postal_code: str,
        country: str = "United States",
        is_preferred: bool = False
    ) -> StreetAddress:
        """Create a home address for a constituent.
        
        Args:
            constituent_id: The constituent ID
            street: Street address
            city: City name
            state: State/province code
            postal_code: ZIP/postal code
            country: Country name
            is_preferred: Mark as preferred address
        
        Returns:
            Created StreetAddress object
        """
        return self.create(constituent_id, {
            "street": street,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "country": country,
            "street_type_name": "Home",
            "is_preferred": is_preferred
        })
    
    def create_work_address(
        self, 
        constituent_id: int, 
        street: str, 
        city: str, 
        state: str, 
        postal_code: str,
        country: str = "United States",
        is_preferred: bool = False
    ) -> StreetAddress:
        """Create a work address for a constituent.
        
        Args:
            constituent_id: The constituent ID
            street: Street address
            city: City name
            state: State/province code
            postal_code: ZIP/postal code
            country: Country name
            is_preferred: Mark as preferred address
        
        Returns:
            Created StreetAddress object
        """
        return self.create(constituent_id, {
            "street": street,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "country": country,
            "street_type_name": "Work",
            "is_preferred": is_preferred
        })
    
    def create_seasonal_address(
        self, 
        constituent_id: int, 
        street: str, 
        city: str, 
        state: str, 
        postal_code: str,
        seasonal_from: str,
        seasonal_to: str,
        country: str = "United States"
    ) -> StreetAddress:
        """Create a seasonal address for a constituent.
        
        Args:
            constituent_id: The constituent ID
            street: Street address
            city: City name
            state: State/province code
            postal_code: ZIP/postal code
            seasonal_from: Seasonal start date (MM-DD format)
            seasonal_to: Seasonal end date (MM-DD format)
            country: Country name
        
        Returns:
            Created StreetAddress object
        """
        return self.create(constituent_id, {
            "street": street,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "country": country,
            "seasonal": True,
            "seasonal_from": seasonal_from,
            "seasonal_to": seasonal_to,
            "street_type_name": "Seasonal"
        })
    
    def set_preferred(self, street_address_id: int) -> StreetAddress:
        """Set a street address as preferred.
        
        Args:
            street_address_id: The street address ID
        
        Returns:
            Updated StreetAddress object
        """
        return self.update(street_address_id, {"is_preferred": True})
    
    def mark_inactive(self, street_address_id: int) -> StreetAddress:
        """Mark a street address as inactive/not current.
        
        Args:
            street_address_id: The street address ID
        
        Returns:
            Updated StreetAddress object
        """
        return self.update(street_address_id, {"not_current": True})