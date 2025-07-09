"""Note model for LGL API."""

from datetime import date, datetime
from typing import Optional

from pydantic import field_validator

from ..models import LGLModel
from .common import parse_date, parse_datetime


class Note(LGLModel):
    """Note resource model.
    
    Notes are text entries associated with constituents containing
    important information, communications, or observations.
    """
    
    id: int
    constituent_id: int
    note_type_id: Optional[int] = None
    note_type_name: Optional[str] = None
    text: str
    external_id: Optional[str] = None
    original_date: Optional[date] = None
    created_at: datetime
    updated_at: datetime
    
    @field_validator('original_date', mode='before')
    @classmethod
    def parse_date_fields(cls, v):
        """Parse date strings to date objects."""
        return parse_date(v)
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def parse_datetime_fields(cls, v):
        """Parse datetime strings to datetime objects."""
        return parse_datetime(v)