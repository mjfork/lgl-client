"""Fund model for LGL API."""

import datetime
from decimal import Decimal
from typing import Optional

from pydantic import field_validator

from ..models import LGLModel
from .common import parse_date


class Fund(LGLModel):
    """Fund resource model.
    
    Funds represent designated accounts or purposes for donations,
    such as building funds, endowments, or special projects.
    """
    
    id: int
    name: str
    description: Optional[str] = None
    code: Optional[str] = None
    start_date: Optional[datetime.date] = None
    end_date: Optional[datetime.date] = None
    financial_goal: Optional[Decimal] = None
    
    @field_validator('start_date', 'end_date', mode='before')
    @classmethod
    def validate_dates(cls, v):
        """Parse date fields from API responses."""
        return parse_date(v)