"""Team Member model for LGL API."""

from typing import Optional

from ..models import LGLModel


class TeamMember(LGLModel):
    """Team Member resource model.
    
    Team members represent users who have access to the LGL account
    with various roles and permission levels.
    """
    
    id: int
    first_name: str
    last_name: str
    email: str
    role_id: int
    is_admin: bool
    is_primary_contact: bool
    is_billing_contact: bool