"""GiftType model for LGL API."""

from typing import Optional

from ..models import LGLModel


class GiftType(LGLModel):
    """GiftType resource model.
    
    Gift types categorize donations by their nature,
    such as "Gift", "Pledge", "In Kind", "Soft Credit", etc.
    """
    
    id: int
    name: str
    ordinal: Optional[int] = None