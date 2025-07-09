"""Appeal Request model for LGL API."""

from datetime import datetime
from typing import List, Optional

from pydantic import field_validator

from ..models import LGLModel
from .common import CustomAttribute, parse_datetime


class AppealRequest(LGLModel):
    """Appeal Request resource model.
    
    Appeal Requests represent solicitation attempts to individual constituents
    as part of broader fundraising appeals. They track ask amounts, response
    status, and assignment details.
    """
    
    id: int
    constituent_id: int
    constituent_name: Optional[str] = None
    appeal_id: int
    name: Optional[str] = None
    raised: Optional[float] = None
    ask_amount: Optional[float] = None
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    # Custom attributes (populated when expanded)
    custom_attrs: List[CustomAttribute] = []
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def parse_datetime_fields(cls, v):
        """Parse datetime strings to datetime objects."""
        return parse_datetime(v)