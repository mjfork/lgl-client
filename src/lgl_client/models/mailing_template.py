"""Mailing Template model for LGL API."""

from typing import Optional

from ..models import LGLModel


class MailingTemplate(LGLModel):
    """Mailing Template resource model.
    
    Mailing templates define pre-configured templates for different types 
    of mailings (acknowledgments, appeals, newsletters, etc.).
    """
    
    id: int
    name: str
    code: Optional[str] = None
    mailing_type_id: Optional[int] = None
    mailing_type_name: Optional[str] = None
    template_type: str