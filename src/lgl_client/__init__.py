"""Little Green Light Python API Client.

A modular, type-safe Python library for the Little Green Light (LGL) REST API.
"""

from .lgl_api import LGLClient
from .lgl_api.categories import CategoriesAPI
from .lgl_api.appeals import AppealsAPI
from .lgl_api.campaigns import CampaignsAPI
from .lgl_api.events import EventsAPI
from .lgl_api.funds import FundsAPI
from .lgl_api.groups import GroupsAPI
from .lgl_api.gift_types import GiftTypesAPI
from .lgl_api.gift_categories import GiftCategoriesAPI
from .lgl_api.payment_types import PaymentTypesAPI
from .lgl_api.membership_levels import MembershipLevelsAPI
from .lgl_api.relationship_types import RelationshipTypesAPI
from .lgl_api.class_affiliation_types import ClassAffiliationTypesAPI
from .lgl_api.team_members import TeamMembersAPI
from .lgl_api.keywords import KeywordsAPI
from .lgl_api.types import TypesAPI
from .lgl_api.mailing_templates import MailingTemplatesAPI
from .lgl_api.custom_attributes import CustomAttributesAPI
from .lgl_api.invitations import InvitationsAPI
from .lgl_api.constituents import ConstituentsAPI
from .lgl_api.email_addresses import EmailAddressesAPI
from .lgl_api.phone_numbers import PhoneNumbersAPI
from .lgl_api.street_addresses import StreetAddressesAPI
from .lgl_api.web_addresses import WebAddressesAPI
from .lgl_api.notes import NotesAPI
from .lgl_api.volunteer_times import VolunteerTimesAPI
from .lgl_api.memberships import MembershipsAPI
from .lgl_api.group_memberships import GroupMembershipsAPI
from .lgl_api.class_affiliations import ClassAffiliationsAPI
from .lgl_api.appeal_requests import AppealRequestsAPI
from .lgl_api.gifts import GiftsAPI
from .lgl_api.constituent_relationships import ConstituentRelationshipsAPI

__version__ = "0.1.0"

def new_client(api_key: str, *, timeout: float = 10.0, debug: bool = False) -> "LGL":
    """Create a new LGL API client instance.
    
    Args:
        api_key: LGL API bearer token
        timeout: Request timeout in seconds
        debug: Enable debug mode to log request details
        
    Returns:
        LGL client instance with all API resources
    """
    base_client = LGLClient(api_key, timeout=timeout, debug=debug)
    return LGL(base_client)


class LGL:
    """Main LGL API client aggregating all resource APIs.
    
    This class will be updated as we implement each resource API.
    """
    
    def __init__(self, client: LGLClient) -> None:
        """Initialize LGL client.
        
        Args:
            client: Base HTTP client instance
        """
        self._client = client
        
        # Resource APIs
        self.categories = CategoriesAPI(client)
        self.appeals = AppealsAPI(client)
        self.campaigns = CampaignsAPI(client)
        self.events = EventsAPI(client)
        self.funds = FundsAPI(client)
        self.groups = GroupsAPI(client)
        self.gift_types = GiftTypesAPI(client)
        self.gift_categories = GiftCategoriesAPI(client)
        self.payment_types = PaymentTypesAPI(client)
        self.membership_levels = MembershipLevelsAPI(client)
        self.relationship_types = RelationshipTypesAPI(client)
        self.class_affiliation_types = ClassAffiliationTypesAPI(client)
        self.team_members = TeamMembersAPI(client)
        self.keywords = KeywordsAPI(client)
        self.types = TypesAPI(client)
        self.mailing_templates = MailingTemplatesAPI(client)
        self.custom_attributes = CustomAttributesAPI(client)
        self.invitations = InvitationsAPI(client)
        self.constituents = ConstituentsAPI(client)
        self.email_addresses = EmailAddressesAPI(client)
        self.phone_numbers = PhoneNumbersAPI(client)
        self.street_addresses = StreetAddressesAPI(client)
        self.web_addresses = WebAddressesAPI(client)
        self.notes = NotesAPI(client)
        self.volunteer_times = VolunteerTimesAPI(client)
        self.memberships = MembershipsAPI(client)
        self.group_memberships = GroupMembershipsAPI(client)
        self.class_affiliations = ClassAffiliationsAPI(client)
        self.appeal_requests = AppealRequestsAPI(client)
        self.gifts = GiftsAPI(client)
        self.constituent_relationships = ConstituentRelationshipsAPI(client)
    
    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()
    
    def __enter__(self) -> "LGL":
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit."""
        self.close()


__all__ = [
    "new_client",
    "LGL", 
    "LGLClient",
    "__version__",
]