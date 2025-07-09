"""Class Affiliation Type model for LGL API."""

from typing import Optional

from ..models import LGLModel


class ClassAffiliationType(LGLModel):
    """Class Affiliation Type resource model.
    
    Class affiliation types define different types of relationships 
    to educational institutions (e.g., Student, Parent, Grandparent).
    """
    
    id: int
    name: str
    ordinal: Optional[int] = None