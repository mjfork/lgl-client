"""Invitation model for LGL API."""

from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from ..models import LGLModel
from .common import CustomAttribute, CustomField


class Attendance(LGLModel):
    """Attendance record for an invitation."""
    
    date: str  # Keep as string for now
    notes: Optional[str] = None


class Invitation(LGLModel):
    """Invitation resource model.
    
    Invitations represent event invitations sent to constituents
    and track RSVP status, attendance, and related details.
    """
    
    id: int
    constituent_id: int
    guest_name: str
    is_a_guest: bool
    parent_invitation_id: int
    parent_invitation_guest_name: Optional[str] = None
    event_id: int
    name: str
    notes: Optional[str] = None
    rsvp: int  # 0-Unknown, 1-Yes, 2-No, 3-Maybe
    attended: int
    raised: Decimal
    status: str
    donated: bool
    assigned_to: Optional[int] = None
    additional_guests: int
    attendees: int
    attendee_names: Optional[str] = None
    attend_count: int
    attendances: List[Attendance] = []
    custom_fields: List[CustomField] = []
    custom_attrs: List[CustomAttribute] = []
    created_at: datetime
    updated_at: datetime