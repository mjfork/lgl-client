"""Constituent model for LGL API."""

from datetime import date, datetime
from typing import List, Optional

from pydantic import field_validator

from ..models import LGLModel
from .common import CustomAttribute, parse_date, parse_datetime


class ClassAffiliation(LGLModel):
    """Class affiliation associated with a constituent."""
    
    id: int
    constituent_id: int
    class_affiliation_type_id: int
    year: Optional[int] = None
    note: Optional[str] = None


class ConstituentRelationship(LGLModel):
    """Relationship between constituents."""
    
    id: int
    relationship_type_id: int
    constituent_id: int
    related_constituent_id: int
    name: str
    description: Optional[str] = None
    auto_soft_credit: bool = False
    also_acknowledge: bool = False
    share_address: Optional[int] = None
    share_phone: Optional[int] = None


class EmailAddress(LGLModel):
    """Email address associated with a constituent."""
    
    id: int
    address: str
    email_address_type_id: int
    email_type_name: str
    is_preferred: bool = False
    not_current: bool = False
    parent_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def parse_datetime_fields(cls, v):
        """Parse datetime strings to datetime objects."""
        return parse_datetime(v)


class PhoneNumber(LGLModel):
    """Phone number associated with a constituent."""
    
    id: int
    number: str
    phone_number_type_id: int
    phone_type_name: str
    is_preferred: bool = False
    not_current: bool = False
    parent_id: Optional[int] = None
    normalized_number: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def parse_datetime_fields(cls, v):
        """Parse datetime strings to datetime objects."""
        return parse_datetime(v)


class StreetAddress(LGLModel):
    """Street address associated with a constituent."""
    
    id: int
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    county: Optional[str] = None
    street_address_type_id: int
    street_type_name: str
    is_preferred: bool = False
    not_current: bool = False
    parent_id: Optional[int] = None
    seasonal_from: Optional[str] = None
    seasonal_to: Optional[str] = None
    seasonal: Optional[bool] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    zip5: Optional[str] = None
    verified: bool = False
    verified_on: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    
    @field_validator('verified_on', 'created_at', 'updated_at', mode='before')
    @classmethod
    def parse_datetime_fields(cls, v):
        """Parse datetime strings to datetime objects."""
        return parse_datetime(v)


class WebAddress(LGLModel):
    """Web address associated with a constituent."""
    
    id: int
    url: str
    web_address_type_id: int
    web_address_type_name: str
    is_preferred: bool = False
    parent_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def parse_datetime_fields(cls, v):
        """Parse datetime strings to datetime objects."""
        return parse_datetime(v)


class ConstituentCategory(LGLModel):
    """Category with keywords associated with a constituent."""
    
    id: int
    item_type: str
    name: str
    key: str
    facet_type: str
    ordinal: int
    removable: bool
    editable: bool
    display_format: str
    keywords: List['ConstituentKeyword'] = []


class ConstituentKeyword(LGLModel):
    """Keyword within a constituent category."""
    
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
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def parse_datetime_fields(cls, v):
        """Parse datetime strings to datetime objects."""
        return parse_datetime(v)


class GroupMembership(LGLModel):
    """Group membership associated with a constituent."""
    
    id: int
    constituent_id: int
    group_id: int
    group_name: str
    date_start: Optional[date] = None
    date_end: Optional[date] = None
    is_current: bool = True
    created_at: datetime
    updated_at: datetime
    
    @field_validator('date_start', 'date_end', mode='before')
    @classmethod
    def parse_date_fields(cls, v):
        """Parse date strings to date objects."""
        return parse_date(v)
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def parse_datetime_fields(cls, v):
        """Parse datetime strings to datetime objects."""
        return parse_datetime(v)


class Membership(LGLModel):
    """Membership level association for a constituent."""
    
    id: int
    constituent_id: int
    membership_level_id: int
    membership_level_name: str
    date_start: Optional[date] = None
    finish_date: Optional[date] = None
    note: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    @field_validator('date_start', 'finish_date', mode='before')
    @classmethod
    def parse_date_fields(cls, v):
        """Parse date strings to date objects."""
        return parse_date(v)
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def parse_datetime_fields(cls, v):
        """Parse datetime strings to datetime objects."""
        return parse_datetime(v)


class Constituent(LGLModel):
    """Constituent resource model.
    
    Constituents are the core entity representing individuals or organizations
    in the LGL system. They can have associated contact information, relationships,
    memberships, and custom attributes.
    """
    
    id: int
    external_constituent_id: Optional[str] = None
    is_org: bool = False
    constituent_contact_type_id: Optional[int] = None
    constituent_contact_type_name: Optional[str] = None
    prefix: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: str
    suffix: Optional[str] = None
    spouse_name: Optional[str] = None
    org_name: Optional[str] = None
    job_title: Optional[str] = None
    addressee: Optional[str] = None
    salutation: Optional[str] = None
    sort_name: Optional[str] = None
    constituent_interest_level_id: Optional[int] = None
    constituent_interest_level_name: Optional[str] = None
    constituent_rating_id: Optional[int] = None
    constituent_rating_name: Optional[str] = None
    is_deceased: bool = False
    deceased_date: Optional[date] = None
    annual_report_name: Optional[str] = None
    birthday: Optional[date] = None
    gender: Optional[str] = None
    maiden_name: Optional[str] = None
    nick_name: Optional[str] = None
    spouse_nick_name: Optional[str] = None
    date_added: Optional[date] = None
    alt_salutation: Optional[str] = None
    alt_addressee: Optional[str] = None
    honorary_name: Optional[str] = None
    assistant_name: Optional[str] = None
    marital_status_id: Optional[int] = None
    marital_status_name: Optional[str] = None
    is_anon: bool = False
    created_at: datetime
    updated_at: datetime
    
    # Related objects (populated when expanded)
    class_affiliations: List[ClassAffiliation] = []
    relationships: List[ConstituentRelationship] = []
    street_addresses: List[StreetAddress] = []
    phone_numbers: List[PhoneNumber] = []
    email_addresses: List[EmailAddress] = []
    web_addresses: List[WebAddress] = []
    categories: List[ConstituentCategory] = []
    groups: List[GroupMembership] = []
    memberships: List[Membership] = []
    custom_attrs: List[CustomAttribute] = []
    
    @field_validator('deceased_date', 'birthday', 'date_added', mode='before')
    @classmethod
    def parse_date_fields(cls, v):
        """Parse date strings to date objects."""
        return parse_date(v)
    
    @field_validator('created_at', 'updated_at', mode='before')
    @classmethod
    def parse_datetime_fields(cls, v):
        """Parse datetime strings to datetime objects."""
        return parse_datetime(v)


# Forward reference resolution
ConstituentCategory.model_rebuild()