"""Custom Attributes API for LGL client."""

from typing import Any, List, Literal, Optional

from ..models.custom_attribute import CustomAttributeDefinition
from .client import LGLClient


class CustomAttributesAPI:
    """API for managing custom attributes in Little Green Light.
    
    Custom attributes define additional fields that can be associated
    with constituents or invitations beyond the standard fields.
    """
    
    _resource = "attributes"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Custom Attributes API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(
        self, 
        *, 
        item_type: Optional[Literal["Constituent", "Invitation"]] = None,
        limit: int = 25, 
        offset: int = 0
    ) -> List[CustomAttributeDefinition]:
        """List custom attribute definitions for the account.
        
        Args:
            item_type: Filter by item type (default: Constituent)
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of CustomAttributeDefinition objects
        """
        params = {"limit": limit, "offset": offset}
        if item_type is not None:
            params["item_type"] = item_type
        
        data = self._client._get(self._resource, **params)
        return [CustomAttributeDefinition.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(
        self, 
        *, 
        item_type: Optional[Literal["Constituent", "Invitation"]] = None
    ) -> List[CustomAttributeDefinition]:
        """Fetch all custom attribute definitions using automatic pagination.
        
        Args:
            item_type: Filter by item type (default: Constituent)
            
        Returns:
            List of all CustomAttributeDefinition objects
        """
        def _list_page(**kwargs: Any) -> List[CustomAttributeDefinition]:
            return self.list(**kwargs)
        
        kwargs = {}
        if item_type is not None:
            kwargs["item_type"] = item_type
            
        items = list(self._client._paginate(_list_page, **kwargs))
        return [CustomAttributeDefinition.from_dict(item) if isinstance(item, dict) else item for item in items]