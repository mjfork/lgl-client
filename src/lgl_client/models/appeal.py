"""Appeal model for LGL API."""

import datetime
from decimal import Decimal
from typing import Optional

from pydantic import field_validator

from ..models import LGLModel
from .common import parse_date


class Appeal(LGLModel):
    """Appeal resource model.
    
    Appeals represent fundraising campaigns or solicitation efforts
    targeting specific groups of constituents.
    """
    
    id: int
    name: str
    description: Optional[str] = None
    date: Optional[datetime.date] = None
    financial_goal: Optional[Decimal] = None
    projected_amount: Optional[Decimal] = None
    code: Optional[str] = None
    
    @field_validator('date', mode='before')
    @classmethod
    def parse_date_field(cls, v):
        """Parse date string to date object."""
        return parse_date(v)