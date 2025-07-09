"""Tests for date field parsing across all models."""
import pytest
from datetime import date, datetime
from typing import Dict, Any
from unittest.mock import Mock, patch

from lgl_client import new_client
from lgl_client.models.common import parse_date, parse_datetime
from lgl_client.models.campaign import Campaign
from lgl_client.models.fund import Fund
from lgl_client.models.event import Event
from lgl_client.models.appeal import Appeal
from lgl_client.models.gift import Gift
from lgl_client.models.constituent import Constituent


class TestDateParsing:
    """Test date parsing functionality."""

    def test_parse_date_valid_iso_format(self):
        """Test parse_date with valid ISO format."""
        result = parse_date("2025-01-15")
        assert result == date(2025, 1, 15)

    def test_parse_date_valid_datetime_format(self):
        """Test parse_date with datetime format (extracts date)."""
        result = parse_date("2025-01-15T10:30:00Z")
        assert result == date(2025, 1, 15)

    def test_parse_date_with_none(self):
        """Test parse_date with None input."""
        result = parse_date(None)
        assert result is None

    def test_parse_date_with_empty_string(self):
        """Test parse_date with empty string."""
        result = parse_date("")
        assert result is None

    def test_parse_date_with_invalid_format(self):
        """Test parse_date with invalid format."""
        result = parse_date("invalid-date")
        assert result is None

    def test_parse_date_with_date_object(self):
        """Test parse_date with existing date object."""
        input_date = date(2025, 1, 15)
        result = parse_date(input_date)
        assert result == input_date

    def test_parse_datetime_valid_iso_format(self):
        """Test parse_datetime with valid ISO format."""
        result = parse_datetime("2025-01-15T10:30:00Z")
        # Result should be timezone-aware UTC
        from datetime import timezone
        expected = datetime(2025, 1, 15, 10, 30, 0, tzinfo=timezone.utc)
        assert result == expected

    def test_parse_datetime_with_none(self):
        """Test parse_datetime with None input."""
        result = parse_datetime(None)
        assert result is None

    def test_parse_datetime_with_empty_string(self):
        """Test parse_datetime with empty string."""
        result = parse_datetime("")
        assert result is None

    def test_parse_datetime_with_invalid_format(self):
        """Test parse_datetime with invalid format."""
        result = parse_datetime("invalid-datetime")
        assert result is None

    def test_parse_datetime_with_datetime_object(self):
        """Test parse_datetime with existing datetime object."""
        input_datetime = datetime(2025, 1, 15, 10, 30, 0)
        result = parse_datetime(input_datetime)
        assert result == input_datetime

    # Test model date field parsing
    def test_campaign_date_parsing(self):
        """Test Campaign model date field parsing."""
        campaign_data = {
            "id": 1,
            "name": "Test Campaign",
            "description": "Test Description",
            "financial_goal": 10000.00,
            "start_date": "2025-01-01",
            "end_date": "2025-12-31"
        }
        
        campaign = Campaign(**campaign_data)
        
        assert campaign.start_date == date(2025, 1, 1)
        assert campaign.end_date == date(2025, 12, 31)
        assert campaign.financial_goal == 10000.00

    def test_campaign_date_parsing_with_nulls(self):
        """Test Campaign model with null date fields."""
        campaign_data = {
            "id": 1,
            "name": "Test Campaign",
            "description": "Test Description",
            "financial_goal": 10000.00,
            "start_date": None,
            "end_date": None
        }
        
        campaign = Campaign(**campaign_data)
        
        assert campaign.start_date is None
        assert campaign.end_date is None
        assert campaign.financial_goal == 10000.00

    def test_fund_date_parsing(self):
        """Test Fund model date field parsing."""
        fund_data = {
            "id": 1,
            "name": "Test Fund",
            "description": "Test Description",
            "start_date": "2025-01-01",
            "end_date": "2025-12-31"
        }
        
        fund = Fund(**fund_data)
        
        assert fund.start_date == date(2025, 1, 1)
        assert fund.end_date == date(2025, 12, 31)

    def test_event_date_parsing(self):
        """Test Event model date field parsing."""
        event_data = {
            "id": 1,
            "name": "Test Event",
            "description": "Test Description",
            "date": "2025-06-15",
            "end_date": "2025-06-16"
        }
        
        event = Event(**event_data)
        
        assert event.date == date(2025, 6, 15)
        assert event.end_date == date(2025, 6, 16)

    def test_event_date_parsing_with_null_date(self):
        """Test Event model with null date."""
        event_data = {
            "id": 1,
            "name": "Test Event",
            "description": "Test Description",
            "date": None,
            "end_date": None
        }
        
        event = Event(**event_data)
        
        assert event.date is None
        assert event.end_date is None

    def test_appeal_date_parsing(self):
        """Test Appeal model date field parsing."""
        appeal_data = {
            "id": 1,
            "name": "Test Appeal",
            "description": "Test Description",
            "date": "2025-01-01",
            "financial_goal": "5000.00"
        }
        
        appeal = Appeal(**appeal_data)
        
        assert appeal.name == "Test Appeal"
        assert appeal.date == date(2025, 1, 1)
        assert appeal.financial_goal == 5000.00

    def test_appeal_date_parsing_with_nulls(self):
        """Test Appeal model with null date fields."""
        appeal_data = {
            "id": 1,
            "name": "Test Appeal",
            "description": "Test Description",
            "date": None,
            "financial_goal": "5000.00"
        }
        
        appeal = Appeal(**appeal_data)
        
        assert appeal.name == "Test Appeal"
        assert appeal.date is None
        assert appeal.financial_goal == 5000.00

    def test_gift_date_parsing(self):
        """Test Gift model date field parsing."""
        gift_data = {
            "id": 1,
            "constituent_id": 123,
            "gift_type_id": 1,
            "amount": 100.00,
            "date": "2025-01-15",
            "created_at": "2025-01-15T14:30:00Z",
            "updated_at": "2025-01-15T14:30:00Z"
        }
        
        gift = Gift(**gift_data)
        
        assert gift.date == date(2025, 1, 15)
        assert gift.amount == 100.00
        from datetime import timezone
        assert gift.created_at == datetime(2025, 1, 15, 14, 30, 0, tzinfo=timezone.utc)
        assert gift.updated_at == datetime(2025, 1, 15, 14, 30, 0, tzinfo=timezone.utc)

    def test_gift_date_parsing_with_optional_dates(self):
        """Test Gift model with optional date fields."""
        gift_data = {
            "id": 1,
            "constituent_id": 123,
            "gift_type_id": 1,
            "amount": 100.00,
            "date": "2025-01-15",
            "check_date": "2025-01-16",
            "date_deposited": None,
            "created_at": "2025-01-15T14:30:00Z",
            "updated_at": "2025-01-15T14:30:00Z"
        }
        
        gift = Gift(**gift_data)
        
        assert gift.date == date(2025, 1, 15)
        assert gift.check_date == date(2025, 1, 16)
        assert gift.date_deposited is None
        from datetime import timezone
        assert gift.created_at == datetime(2025, 1, 15, 14, 30, 0, tzinfo=timezone.utc)

    def test_constituent_date_parsing(self):
        """Test Constituent model date field parsing."""
        constituent_data = {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "birthday": "1990-05-15",  # Fixed: use 'birthday' not 'birth_date'
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z"
        }
        
        constituent = Constituent(**constituent_data)
        
        assert constituent.birthday == date(1990, 5, 15)
        # Fixed: parse_datetime returns timezone-aware datetime
        from datetime import timezone
        assert constituent.created_at == datetime(2025, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
        assert constituent.updated_at == datetime(2025, 1, 1, 10, 0, 0, tzinfo=timezone.utc)

    def test_constituent_date_parsing_with_null_birth_date(self):
        """Test Constituent model with null birthday."""
        constituent_data = {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "birthday": None,  # Fixed: use 'birthday' not 'birth_date'
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z"
        }
        
        constituent = Constituent(**constituent_data)
        
        assert constituent.birthday is None
        # Fixed: parse_datetime returns timezone-aware datetime
        from datetime import timezone
        assert constituent.created_at == datetime(2025, 1, 1, 10, 0, 0, tzinfo=timezone.utc)

    # Test edge cases
    def test_date_parsing_edge_cases(self):
        """Test date parsing with various edge cases."""
        # Test different ISO formats
        assert parse_date("2025-01-01") == date(2025, 1, 1)
        assert parse_date("2025-12-31") == date(2025, 12, 31)
        
        # Test datetime string extraction
        assert parse_date("2025-01-15T00:00:00Z") == date(2025, 1, 15)
        assert parse_date("2025-01-15T23:59:59Z") == date(2025, 1, 15)
        
        # Test invalid formats
        assert parse_date("01/15/2025") is None  # US format not supported
        assert parse_date("15-01-2025") is None  # Non-ISO format
        assert parse_date("2025-13-01") is None  # Invalid month
        assert parse_date("2025-01-32") is None  # Invalid day

    def test_datetime_parsing_edge_cases(self):
        """Test datetime parsing with various edge cases."""
        # Test different ISO formats - parse_datetime returns timezone-aware datetime
        from datetime import timezone
        assert parse_datetime("2025-01-01T00:00:00Z") == datetime(2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        assert parse_datetime("2025-12-31T23:59:59Z") == datetime(2025, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
        
        # Test timezone handling (should parse as UTC)
        assert parse_datetime("2025-01-15T10:30:00Z") == datetime(2025, 1, 15, 10, 30, 0, tzinfo=timezone.utc)
        
        # Test different valid formats (fromisoformat is flexible)
        # Space separator is actually valid for fromisoformat
        assert parse_datetime("2025-01-15 10:30:00") == datetime(2025, 1, 15, 10, 30, 0)
        
        # Test truly invalid formats
        assert parse_datetime("2025-01-15T25:00:00Z") is None  # Invalid hour
        assert parse_datetime("2025-01-15T10:60:00Z") is None  # Invalid minute
        assert parse_datetime("invalid-datetime") is None  # Completely invalid

    def test_api_response_date_parsing_integration(self):
        """Test date parsing in API response processing."""
        client = new_client(api_key="test_key")
        
        # Mock API response with date fields
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": 1,
            "name": "Test Campaign",
            "description": "Test Description",
            "goal": 10000.00,
            "start_date": "2025-01-01",
            "end_date": "2025-12-31",
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z"
        }
        mock_response.raise_for_status = Mock()

        # Fixed: use '_get' instead of 'get'
        with patch.object(client.campaigns._client, '_get', return_value=mock_response.json.return_value):
            campaign = client.campaigns.retrieve(1)
            
            # Verify proper date parsing in real API response
            assert campaign.start_date == date(2025, 1, 1)
            assert campaign.end_date == date(2025, 12, 31)
            # Fixed: parse_datetime returns timezone-aware datetime
            from datetime import timezone
            assert campaign.created_at == datetime(2025, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
            assert campaign.updated_at == datetime(2025, 1, 1, 10, 0, 0, tzinfo=timezone.utc)

    def test_model_validation_with_invalid_dates(self):
        """Test model validation handles invalid date formats gracefully."""
        # Test with invalid date format - should not raise exception
        campaign_data = {
            "id": 1,
            "name": "Test Campaign",
            "description": "Test Description",
            "goal": 10000.00,
            "start_date": "invalid-date",
            "end_date": "2025-12-31",
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z"
        }
        
        campaign = Campaign(**campaign_data)
        
        # Invalid date should be parsed as None
        assert campaign.start_date is None
        assert campaign.end_date == date(2025, 12, 31)  # Valid date should parse correctly

    def test_date_parsing_performance(self):
        """Test date parsing performance with large datasets."""
        # Create 1000 date strings
        date_strings = [f"2025-01-{str(i).zfill(2)}" for i in range(1, 29)]  # 28 dates
        date_strings = date_strings * 36  # ~1000 total dates
        
        # Test parsing performance
        import time
        start_time = time.time()
        
        parsed_dates = [parse_date(date_str) for date_str in date_strings]
        
        end_time = time.time()
        parsing_time = end_time - start_time
        
        # Verify all dates parsed correctly
        assert len(parsed_dates) == len(date_strings)
        assert all(isinstance(d, date) for d in parsed_dates)
        
        # Performance should be reasonable (under 1 second for 1000 dates)
        assert parsing_time < 1.0, f"Date parsing took {parsing_time:.3f}s for {len(date_strings)} dates"