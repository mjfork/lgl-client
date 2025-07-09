"""Type models for LGL API."""

from typing import List, Optional

from ..models import LGLModel


class TypeValue(LGLModel):
    """Type Value resource model.
    
    Individual type value within a type group (e.g., 'Home', 'Work', 'Mobile' 
    within 'phone_number_types').
    """
    
    id: int
    name: str
    display_name: Optional[str] = None
    code: Optional[str] = None
    ordinal: int


class Type(LGLModel):
    """Type resource model.
    
    Type groups that contain multiple type values 
    (e.g., 'email_address_types', 'phone_number_types').
    """
    
    name: str
    key: str
    values: List[TypeValue] = []