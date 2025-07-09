"""Gift model for LGL API."""

from datetime import date, datetime
from typing import List, Optional

from pydantic import field_validator

from ..models import LGLModel
from .common import CustomAttribute, parse_date, parse_datetime


class Tribute(LGLModel):
    """Tribute information associated with a gift."""
    
    tribute_name: str
    tribute_type: str
    tribute_note: Optional[str] = None


class Gift(LGLModel):
    """Gift resource model.
    
    Gifts represent financial contributions from constituents including
    donations, pledges, grants, and other forms of giving. They can be
    associated with campaigns, appeals, events, and funds.
    """
    
    id: int
    constituent_id: int
    constituent_name: Optional[str] = None
    external_gift_id: Optional[str] = None
    gift_type_id: int
    gift_type_name: Optional[str] = None
    gift_category_id: Optional[int] = None
    gift_category_name: Optional[str] = None
    payment_type_id: Optional[int] = None
    payment_type_name: Optional[str] = None
    campaign_id: Optional[int] = None
    campaign_name: Optional[str] = None
    fund_id: Optional[int] = None
    fund_name: Optional[str] = None
    appeal_id: Optional[int] = None
    appeal_name: Optional[str] = None
    event_id: Optional[int] = None
    event_name: Optional[str] = None
    
    # Financial information
    amount: float
    deductible_amount: Optional[float] = None
    check_number: Optional[str] = None
    check_date: Optional[date] = None
    
    # Dates
    date: date
    date_deposited: Optional[date] = None
    
    # Status and notes
    acknowledged: bool = False
    acknowledged_date: Optional[date] = None
    note: Optional[str] = None
    
    # Pledge information (for pledge gifts)
    parent_gift_id: Optional[int] = None
    installment_frequency: Optional[str] = None
    number_installments: Optional[int] = None
    
    # System fields
    created_at: datetime
    updated_at: datetime
    
    # Related objects (populated when expanded)
    custom_attrs: List[CustomAttribute] = []
    tribute: Optional[Tribute] = None
    
    @field_validator('date', 'check_date', 'date_deposited', 'acknowledged_date', mode='before')
    @classmethod
    def parse_date_fields(cls, v):
        """Parse date strings to date objects."""
        return parse_date(v)
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def parse_datetime_fields(cls, v):
        """Parse datetime strings to datetime objects."""
        return parse_datetime(v)