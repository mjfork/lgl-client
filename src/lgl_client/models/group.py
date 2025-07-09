"""Group model for LGL API."""

from typing import Optional

from ..models import LGLModel


class Group(LGLModel):
    """Group resource model.
    
    Groups represent organizational categories for constituents,
    such as "Board Member", "Staff", "Volunteer", etc.
    """
    
    id: int
    name: str
    key: Optional[str] = None
    ordinal: Optional[int] = None