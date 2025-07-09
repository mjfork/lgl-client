"""Relationship Type model for LGL API."""

from typing import Optional

from ..models import LGLModel


class RelationshipType(LGLModel):
    """Relationship Type resource model.
    
    Relationship types define the different types of relationships between
    constituents (e.g., Parent, Mother, Father, Child, Spouse, Friend).
    """
    
    id: int
    name: str
    short_code: str
    type_code: str
    ordinal: Optional[int] = None
    removable: Optional[bool] = None
    reciprocal_id: Optional[int] = None
    auto_soft_credit: Optional[str] = None
    share_class_year: Optional[str] = None
    share_membership: Optional[bool] = None
    is_spouse_partner: Optional[bool] = None
    share_class_year_to: Optional[str] = None