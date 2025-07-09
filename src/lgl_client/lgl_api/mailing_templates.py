"""Mailing Templates API for LGL client."""

from typing import Any, List, Optional

from ..models.mailing_template import MailingTemplate
from .client import LGLClient


class MailingTemplatesAPI:
    """API for managing mailing templates in Little Green Light.
    
    Mailing templates define pre-configured templates for different types 
    of mailings (acknowledgments, appeals, newsletters, etc.).
    """
    
    _resource = "mailing_templates"
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize Mailing Templates API.
        
        Args:
            client: LGL HTTP client instance
        """
        self._client = client
    
    def list(
        self, 
        *, 
        mailing_type_id: Optional[int] = None,
        limit: int = 25, 
        offset: int = 0
    ) -> List[MailingTemplate]:
        """List mailing templates for the account.
        
        Args:
            mailing_type_id: Filter by mailing type ID (optional)
            limit: Number of entries to return (default: 25)
            offset: Start at given entry (default: 0)
            
        Returns:
            List of MailingTemplate objects
        """
        params = {"limit": limit, "offset": offset}
        if mailing_type_id is not None:
            params["mailing_type_id"] = mailing_type_id
        
        data = self._client._get(self._resource, **params)
        return [MailingTemplate.from_dict(item) for item in data.get("items", [])]
    
    def fetch_all(self, *, mailing_type_id: Optional[int] = None) -> List[MailingTemplate]:
        """Fetch all mailing templates using automatic pagination.
        
        Args:
            mailing_type_id: Filter by mailing type ID (optional)
            
        Returns:
            List of all MailingTemplate objects
        """
        def _list_page(**kwargs: Any) -> List[MailingTemplate]:
            return self.list(**kwargs)
        
        kwargs = {}
        if mailing_type_id is not None:
            kwargs["mailing_type_id"] = mailing_type_id
        
        items = list(self._client._paginate(_list_page, **kwargs))
        return [MailingTemplate.from_dict(item) if isinstance(item, dict) else item for item in items]