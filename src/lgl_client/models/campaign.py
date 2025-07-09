"""Campaign model for LGL API."""

import datetime
from decimal import Decimal
from typing import Optional

from pydantic import field_validator

from ..models import LGLModel
from .common import parse_date, parse_datetime


class Campaign(LGLModel):
    """Campaign resource model.
    
    Campaigns represent fundraising initiatives or drives
    that span multiple appeals and activities.
    """
    
    id: int
    name: str
    description: Optional[str] = None
    financial_goal: Optional[Decimal] = None
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None
    code: Optional[str] = None
    goal: Optional[Decimal] = None
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None
    
    @field_validator('start_date', 'end_date', mode='before')
    @classmethod
    def validate_dates(cls, v):
        """Parse date fields from API responses."""
        return parse_date(v)
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def validate_datetimes(cls, v):
        """Parse datetime fields from API responses."""
        return parse_datetime(v)