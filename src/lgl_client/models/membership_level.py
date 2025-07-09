"""Membership Level model for LGL API."""

from typing import Optional

from ..models import LGLModel


class MembershipLevel(LGLModel):
    """Membership Level resource model.
    
    Membership levels define different tiers of membership
    for constituents (e.g., General, Friend, Gold, Silver, Diamond, Bronze).
    """
    
    id: int
    name: str
    ordinal: Optional[int] = None