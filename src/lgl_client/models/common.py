"""Common model components and utilities."""

from datetime import date, datetime
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, field_validator

from . import LGLModel


def parse_date(value: Union[str, date, None]) -> Optional[date]:
    """Parse date string in YYYY-MM-DD format to date object."""
    if value is None:
        return None
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        if not value.strip():
            return None
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            # Try ISO format as fallback
            try:
                return datetime.fromisoformat(value).date()
            except ValueError:
                return None
    return None


def parse_datetime(value: Union[str, datetime, None]) -> Optional[datetime]:
    """Parse datetime string in ISO 8601 format to datetime object."""
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        if not value.strip():
            return None
        try:
            # Handle both with and without timezone
            if value.endswith('Z'):
                return datetime.fromisoformat(value.replace('Z', '+00:00'))
            return datetime.fromisoformat(value)
        except ValueError:
            return None
    return None


class CustomField(BaseModel):
    """Custom field structure used across multiple resources."""
    
    id: Optional[int] = None
    name: str
    key: Optional[str] = None
    remove_previous_values: Optional[bool] = None
    values: List["CustomValue"] = Field(default_factory=list)


class CustomValue(BaseModel):
    """Custom field value structure."""
    
    id: int
    name: str


class CustomAttribute(BaseModel):
    """Custom attribute structure used across multiple resources."""
    
    id: Optional[int] = None
    key: Optional[str] = None
    value: str


class Keyword(LGLModel):
    """Keyword structure used in categories."""
    
    id: int
    category_id: int
    name: str
    description: Optional[str] = None
    short_code: Optional[str] = None
    ordinal: int
    removable: bool
    can_change: bool
    can_select: bool
    created_at: datetime
    updated_at: datetime


class PaginatedResponse(BaseModel):
    """Standard paginated response structure from LGL API."""
    
    api_version: str
    items_count: int
    total_items: int
    limit: int
    offset: int
    next_item: Optional[int] = None
    next_link: Optional[str] = None
    item_type: str
    items: List[Dict[str, Any]] = Field(default_factory=list)


# Forward reference resolution
CustomField.model_rebuild()