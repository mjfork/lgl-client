"""GiftCategory model for LGL API."""

from typing import Optional

from ..models import LGLModel


class GiftCategory(LGLModel):
    """GiftCategory resource model.
    
    Gift categories provide sub-classifications within gift types,
    such as "Donation", "Matching Gift", "Standard Pledge", "Grant", etc.
    """
    
    id: int
    display_name: str
    gift_type_id: Optional[int] = None
    gift_type_name: Optional[str] = None