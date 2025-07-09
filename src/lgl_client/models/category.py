"""Category model for LGL API."""

from typing import List, Literal, Optional

from ..models import LGLModel
from .common import Keyword


class Category(LGLModel):
    """Category resource model.
    
    Categories are used to organize constituents, gifts, and volunteer time
    with custom fields and categorization.
    """
    
    id: int
    item_type: Literal["Constituent", "Gift", "VolunteerTime"]
    name: str
    key: Optional[str] = None
    facet_type: Optional[Literal["single", "list"]] = None
    ordinal: Optional[int] = None
    removable: Optional[bool] = None
    editable: Optional[bool] = None
    display_format: Optional[str] = None
    keywords: List[Keyword] = []