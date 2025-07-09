"""Types API for LGL client."""

from typing import Any, List, Literal

from ..models.type import Type, TypeValue
from .client import LGLClient


class TypesAPI:
    """API for managing types in Little Green Light.
    
    Types define various categorization systems used throughout LGL
    (e.g., phone number types, email address types, mailing types).
    """
    
    _resource = "types"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Types API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(self, *, limit: int = 25, offset: int = 0) -> List[Type]:
        """List all type groups for the account.
        
        Args:
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of Type objects with their values
        """
        data = self._client._get(self._resource, limit=limit, offset=offset)
        
        types = []
        for item in data.get("items", []):
            # Convert values to TypeValue objects
            values = [TypeValue.from_dict(value) for value in item.get("values", [])]
            
            # Create Type object with values
            type_data = {
                "name": item["name"],
                "key": item["key"],
                "values": values
            }
            types.append(Type.from_dict(type_data))
        
        return types
    
    def fetch_all(self) -> List[Type]:
        """Fetch all type groups using automatic pagination.
        
        Returns:
            List of all Type objects
        """
        def _list_page(**kwargs: Any) -> List[Type]:
            return self.list(**kwargs)
        
        items = list(self._client._paginate(_list_page))
        return [Type.from_dict(item) if isinstance(item, dict) else item for item in items]
    
    def list_values(
        self, 
        type_key: Literal[
            "contact_report_types", "email_address_types", "mailing_types", 
            "street_address_types", "phone_number_types", "web_address_types", 
            "volunteering_categories", "appeal_types", "event_types", "note_types"
        ], 
        *, 
        limit: int = 25, 
        offset: int = 0
    ) -> List[TypeValue]:
        """List values for a specific type.
        
        Args:
            type_key: Type key to get values for
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of TypeValue objects
        """
        data = self._client._get(f"{self._resource}/{type_key}", limit=limit, offset=offset)
        return [TypeValue.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all_values(
        self, 
        type_key: Literal[
            "contact_report_types", "email_address_types", "mailing_types", 
            "street_address_types", "phone_number_types", "web_address_types", 
            "volunteering_categories", "appeal_types", "event_types", "note_types"
        ]
    ) -> List[TypeValue]:
        """Fetch all values for a type using automatic pagination.
        
        Args:
            type_key: Type key to get values for
            
        Returns:
            List of all TypeValue objects for the type
        """
        def _list_page(**kwargs: Any) -> List[TypeValue]:
            return self.list_values(type_key, **kwargs)
        
        items = list(self._client._paginate(_list_page))
        return [TypeValue.from_dict(item) if isinstance(item, dict) else item for item in items]