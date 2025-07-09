"""Event model for LGL API."""

import datetime
from decimal import Decimal
from typing import Optional

from pydantic import field_validator

from ..models import LGLModel
from .common import parse_date


class Event(LGLModel):
    """Event resource model.
    
    Events represent fundraising events, gatherings, or activities
    that may have associated volunteer time or gifts.
    """
    
    id: int
    name: str
    description: Optional[str] = None
    date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None
    financial_goal: Optional[Decimal] = None
    projected_amount: Optional[Decimal] = None
    code: Optional[str] = None
    
    @field_validator('date', 'end_date', mode='before')
    @classmethod
    def validate_dates(cls, v):
        """Parse date fields from API responses."""
        return parse_date(v)