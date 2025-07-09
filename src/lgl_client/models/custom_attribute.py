"""Custom Attribute model for LGL API."""

from typing import Literal, Optional

from ..models import LGLModel


class CustomAttributeDefinition(LGLModel):
    """Custom Attribute Definition resource model.
    
    Custom attribute definitions define the structure and type of custom
    attributes that can be associated with constituents or invitations.
    """
    
    id: int
    name: str
    key: str
    item_type: Literal["Constituent", "Invitation"]
    value_type: Optional[str] = None
    description: Optional[str] = None
    ordinal: Optional[int] = None
    required: Optional[bool] = None
    min_val: Optional[int] = None
    max_val: Optional[int] = None