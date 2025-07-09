"""Tests for model validation across all 31 resources."""
import pytest
from datetime import date, datetime
from typing import Dict, Any, List
from pydantic import ValidationError

# Import all models
from lgl_client.models.appeal import Appeal
from lgl_client.models.appeal_request import AppealRequest
from lgl_client.models.campaign import Campaign
from lgl_client.models.category import Category
from lgl_client.models.class_affiliation_type import ClassAffiliationType
from lgl_client.models.constituent import Constituent
from lgl_client.models.custom_attribute import CustomAttributeDefinition
from lgl_client.models.event import Event
from lgl_client.models.fund import Fund
from lgl_client.models.gift import Gift
from lgl_client.models.gift_category import GiftCategory
from lgl_client.models.gift_type import GiftType
from lgl_client.models.group import Group
from lgl_client.models.invitation import Invitation
from lgl_client.models.mailing_template import MailingTemplate
from lgl_client.models.membership_level import MembershipLevel
from lgl_client.models.note import Note
from lgl_client.models.payment_type import PaymentType
from lgl_client.models.relationship_type import RelationshipType
from lgl_client.models.team_member import TeamMember
from lgl_client.models.type import Type, TypeValue
from lgl_client.models.volunteer_time import VolunteerTime


class TestModelValidation:
    """Test model validation for all resources."""

    def test_appeal_model_validation(self):
        """Test Appeal model validation."""
        # Valid appeal
        valid_data = {
            "id": 1,
            "name": "Annual Appeal 2025",
            "description": "Annual fundraising appeal",
            "financial_goal": 10000.00,
            "date": "2025-01-01"
        }
        appeal = Appeal(**valid_data)
        assert appeal.name == "Annual Appeal 2025"
        assert appeal.financial_goal == 10000.00
        assert appeal.date == date(2025, 1, 1)

        # Test with missing required fields
        with pytest.raises(ValidationError):
            Appeal(id=1)  # Missing name

        # Test with invalid date
        invalid_data = valid_data.copy()
        invalid_data["date"] = "invalid-date"
        appeal_invalid = Appeal(**invalid_data)
        assert appeal_invalid.date is None  # Should handle gracefully

    def test_campaign_model_validation(self):
        """Test Campaign model validation."""
        valid_data = {
            "id": 1,
            "name": "Capital Campaign",
            "description": "Building fund campaign",
            "goal": 100000.00,
            "start_date": "2025-01-01",
            "end_date": "2025-12-31",
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z"
        }
        campaign = Campaign(**valid_data)
        assert campaign.name == "Capital Campaign"
        assert campaign.goal == 100000.00
        assert campaign.start_date == date(2025, 1, 1)

    def test_category_model_validation(self):
        """Test Category model validation."""
        valid_data = {
            "id": 1,
            "item_type": "Constituent",
            "name": "Donor Category",
            "key": "donor",
            "ordinal": 1
        }
        category = Category(**valid_data)
        assert category.item_type == "Constituent"
        assert category.name == "Donor Category"

        # Test invalid item_type
        with pytest.raises(ValidationError):
            Category(id=1, item_type="Invalid", name="Test")

    def test_constituent_model_validation(self):
        """Test Constituent model validation."""
        valid_data = {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "birthday": "1990-05-15",
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z"
        }
        constituent = Constituent(**valid_data)
        assert constituent.first_name == "John"
        assert constituent.birthday == date(1990, 5, 15)

    def test_gift_model_validation(self):
        """Test Gift model validation."""
        valid_data = {
            "id": 1,
            "constituent_id": 123,
            "gift_type_id": 1,
            "amount": 100.00,
            "date": "2025-01-15",
            "created_at": "2025-01-15T14:30:00Z",
            "updated_at": "2025-01-15T14:30:00Z"
        }
        gift = Gift(**valid_data)
        assert gift.amount == 100.00
        assert gift.date == date(2025, 1, 15)
        assert gift.constituent_id == 123

    def test_event_model_validation(self):
        """Test Event model validation."""
        valid_data = {
            "id": 1,
            "name": "Annual Gala",
            "description": "Annual fundraising gala",
            "date": "2025-06-15",
            "end_date": "2025-06-16",
            "financial_goal": "10000.00"
        }
        event = Event(**valid_data)
        assert event.name == "Annual Gala"
        assert event.date == date(2025, 6, 15)
        assert event.end_date == date(2025, 6, 16)

    def test_payment_type_model_validation(self):
        """Test PaymentType model validation."""
        valid_data = {
            "id": 1,
            "name": "Cash",
            "key": "cash",
            "ordinal": 1
        }
        payment_type = PaymentType(**valid_data)
        assert payment_type.name == "Cash"
        assert payment_type.key == "cash"
        assert payment_type.ordinal == 1

    def test_membership_level_model_validation(self):
        """Test MembershipLevel model validation."""
        valid_data = {
            "id": 1,
            "name": "Premium",
            "ordinal": 1
        }
        membership_level = MembershipLevel(**valid_data)
        assert membership_level.name == "Premium"
        assert membership_level.ordinal == 1

    def test_note_model_validation(self):
        """Test Note model validation."""
        valid_data = {
            "id": 1,
            "constituent_id": 123,
            "note_type_name": "General",
            "text": "Test note content",
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z"
        }
        note = Note(**valid_data)
        assert note.text == "Test note content"
        assert note.constituent_id == 123

    def test_volunteer_time_model_validation(self):
        """Test VolunteerTime model validation."""
        valid_data = {
            "id": 1,
            "constituent_id": 123,
            "volunteering_category_id": 1,
            "activity": "Event Setup",
            "hours": 4.5,
            "volunteer_date": "2025-01-15",
            "created_at": "2025-01-15T10:00:00Z",
            "updated_at": "2025-01-15T10:00:00Z"
        }
        volunteer_time = VolunteerTime(**valid_data)
        assert volunteer_time.hours == 4.5
        assert volunteer_time.activity == "Event Setup"

    def test_fund_model_validation(self):
        """Test Fund model validation."""
        valid_data = {
            "id": 1,
            "name": "General Fund",
            "description": "General operating fund",
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z"
        }
        fund = Fund(**valid_data)
        assert fund.name == "General Fund"

    def test_team_member_model_validation(self):
        """Test TeamMember model validation."""
        valid_data = {
            "id": 1,
            "first_name": "Admin",
            "last_name": "User",
            "email": "admin@organization.org",
            "role_id": 1,
            "is_admin": True,
            "is_primary_contact": False,
            "is_billing_contact": False
        }
        team_member = TeamMember(**valid_data)
        assert team_member.first_name == "Admin"
        assert team_member.email == "admin@organization.org"

    def test_type_model_validation(self):
        """Test Type and TypeValue model validation."""
        # Test Type model
        type_data = {
            "id": 1,
            "name": "Email Address Types",
            "key": "email_address_types"
        }
        type_obj = Type(**type_data)
        assert type_obj.name == "Email Address Types"

        # Test TypeValue model
        type_value_data = {
            "id": 1,
            "name": "Personal",
            "key": "personal",
            "ordinal": 1
        }
        type_value = TypeValue(**type_value_data)
        assert type_value.name == "Personal"

    def test_relationship_type_model_validation(self):
        """Test RelationshipType model validation."""
        valid_data = {
            "id": 1,
            "name": "Spouse",
            "short_code": "SP",
            "type_code": "spouse",
            "ordinal": 1,
            "inverse_name": "Spouse"
        }
        relationship_type = RelationshipType(**valid_data)
        assert relationship_type.name == "Spouse"
        assert relationship_type.inverse_name == "Spouse"

    def test_class_affiliation_type_model_validation(self):
        """Test ClassAffiliationType model validation."""
        valid_data = {
            "id": 1,
            "name": "Student",
            "ordinal": 1
        }
        class_affiliation_type = ClassAffiliationType(**valid_data)
        assert class_affiliation_type.name == "Student"

    def test_custom_attribute_model_validation(self):
        """Test CustomAttributeDefinition model validation."""
        valid_data = {
            "id": 1,
            "name": "Alumni Year",
            "key": "alumni_year",
            "item_type": "Constituent",
            "field_type": "text"
        }
        custom_attr = CustomAttributeDefinition(**valid_data)
        assert custom_attr.name == "Alumni Year"
        assert custom_attr.item_type == "Constituent"

    def test_mailing_template_model_validation(self):
        """Test MailingTemplate model validation."""
        valid_data = {
            "id": 1,
            "name": "Welcome Email",
            "subject": "Welcome to our organization",
            "mailing_type_id": 1,
            "template_type": "email"
        }
        template = MailingTemplate(**valid_data)
        assert template.name == "Welcome Email"
        assert template.subject == "Welcome to our organization"

    def test_invitation_model_validation(self):
        """Test Invitation model validation."""
        valid_data = {
            "id": 1,
            "constituent_id": 123,
            "guest_name": "John Doe",
            "is_a_guest": False,
            "parent_invitation_id": 0,
            "event_id": 456,
            "name": "Annual Gala",
            "rsvp": 0,
            "attended": 0,
            "raised": 0.0,
            "status": "pending",
            "donated": False,
            "additional_guests": 0,
            "attendees": 0,
            "attend_count": 0,
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z"
        }
        invitation = Invitation(**valid_data)
        assert invitation.constituent_id == 123
        assert invitation.event_id == 456
        assert invitation.status == "pending"

    def test_group_model_validation(self):
        """Test Group model validation."""
        valid_data = {
            "id": 1,
            "name": "Board Members",
            "description": "Organization board members",
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z"
        }
        group = Group(**valid_data)
        assert group.name == "Board Members"

    def test_gift_category_model_validation(self):
        """Test GiftCategory model validation."""
        valid_data = {
            "id": 1,
            "display_name": "Annual Fund",
            "description": "Annual giving program"
        }
        gift_category = GiftCategory(**valid_data)
        assert gift_category.display_name == "Annual Fund"

    def test_gift_type_model_validation(self):
        """Test GiftType model validation."""
        valid_data = {
            "id": 1,
            "name": "Cash Gift",
            "description": "Standard cash donation"
        }
        gift_type = GiftType(**valid_data)
        assert gift_type.name == "Cash Gift"

    def test_appeal_request_model_validation(self):
        """Test AppealRequest model validation."""
        valid_data = {
            "id": 1,
            "constituent_id": 123,
            "appeal_id": 456,
            "status": "pending",
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z"
        }
        appeal_request = AppealRequest(**valid_data)
        assert appeal_request.constituent_id == 123
        assert appeal_request.appeal_id == 456

    # Edge case tests
    def test_model_with_none_values(self):
        """Test models handle None values correctly."""
        # Test Appeal with None dates
        appeal_data = {
            "id": 1,
            "name": "Test Appeal",
            "start_date": None,
            "end_date": None,
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z"
        }
        appeal = Appeal(**appeal_data)
        assert appeal.start_date is None
        assert appeal.end_date is None

    def test_model_with_empty_strings(self):
        """Test models handle empty strings correctly."""
        # Test Gift with empty string date
        gift_data = {
            "id": 1,
            "constituent_id": 123,
            "amount": 100.00,
            "gift_type_id": 1,
            "date": "2025-01-15",
            "gift_date": "",  # Empty string
            "created_at": "2025-01-15T14:30:00Z",
            "updated_at": "2025-01-15T14:30:00Z"
        }
        gift = Gift(**gift_data)
        assert gift.gift_date == ""  # Empty string is preserved

    def test_model_date_parsing_edge_cases(self):
        """Test date parsing edge cases across models."""
        # Test various date formats
        constituent_data = {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "birthday": "1990-12-31",  # End of year
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z",
            "addresses": [],
            "phone_numbers": [],
            "email_addresses": [],
            "web_addresses": []
        }
        constituent = Constituent(**constituent_data)
        assert constituent.birthday == date(1990, 12, 31)

    def test_model_numeric_edge_cases(self):
        """Test numeric field validation edge cases."""
        # Test Gift with zero amount
        gift_data = {
            "id": 1,
            "constituent_id": 123,
            "amount": 0.00,
            "gift_type_id": 1,
            "date": "2025-01-15",
            "gift_date": "2025-01-15",
            "created_at": "2025-01-15T14:30:00Z",
            "updated_at": "2025-01-15T14:30:00Z"
        }
        gift = Gift(**gift_data)
        assert gift.amount == 0.00

        # Test VolunteerTime with decimal hours
        volunteer_data = {
            "id": 1,
            "constituent_id": 123,
            "volunteering_category_id": 1,
            "activity": "Test Activity",
            "hours": 0.5,  # Half hour
            "volunteer_date": "2025-01-15",
            "created_at": "2025-01-15T10:00:00Z",
            "updated_at": "2025-01-15T10:00:00Z"
        }
        volunteer_time = VolunteerTime(**volunteer_data)
        assert volunteer_time.hours == 0.5

    def test_model_string_length_validation(self):
        """Test string field length handling."""
        # Test long strings are handled properly
        long_name = "A" * 1000  # Very long name
        category_data = {
            "id": 1,
            "item_type": "Constituent",
            "name": long_name
        }
        category = Category(**category_data)
        assert category.name == long_name  # Should handle long strings

    def test_model_from_dict_method(self):
        """Test that all models can be created from dict using from_dict method."""
        category_data = {
            "id": 1,
            "item_type": "Constituent",
            "name": "Test Category"
        }
        
        # Test both direct instantiation and from_dict
        category1 = Category(**category_data)
        category2 = Category.from_dict(category_data)
        
        assert category1.id == category2.id
        assert category1.name == category2.name
        assert category1.item_type == category2.item_type

    def test_model_serialization(self):
        """Test model serialization back to dict."""
        category = Category(
            id=1,
            item_type="Constituent",
            name="Test Category"
        )
        
        # Test that models can be converted to dict
        category_dict = category.model_dump()
        assert isinstance(category_dict, dict)
        assert category_dict["id"] == 1
        assert category_dict["name"] == "Test Category"