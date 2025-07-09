"""Volunteer Time model for LGL API."""

from datetime import date, datetime
from typing import List, Optional

from pydantic import field_validator

from ..models import LGLModel
from .common import CustomAttribute, parse_date, parse_datetime


class VolunteerTime(LGLModel):
    """Volunteer Time resource model.
    
    Volunteer Time records track hours contributed by constituents
    for various volunteer activities and categories.
    """
    
    id: int
    constituent_id: int
    external_id: Optional[str] = None
    volunteering_category_id: int
    volunteering_category_name: Optional[str] = None
    description: Optional[str] = None
    hours: Optional[float] = None
    completed_hours: Optional[float] = None
    date: Optional[date] = None
    end_date: Optional[date] = None
    created_at: datetime
    updated_at: datetime
    
    # Custom attributes (populated when expanded)
    custom_attrs: List[CustomAttribute] = []
    
    @field_validator('date', 'end_date', mode='before')
    @classmethod
    def parse_date_fields(cls, v):
        """Parse date strings to date objects."""
        return parse_date(v)
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def parse_datetime_fields(cls, v):
        """Parse datetime strings to datetime objects."""
        return parse_datetime(v)