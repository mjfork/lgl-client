"""Property-based tests using hypothesis for edge case generation."""
import pytest
from hypothesis import given, strategies as st, assume, settings, HealthCheck
from datetime import date, datetime, timezone
from typing import Dict, Any
from unittest.mock import patch

from lgl_client import new_client
from lgl_client.models.category import Category
from lgl_client.models.constituent import Constituent
from lgl_client.models.gift import Gift
from lgl_client.models.common import parse_date, parse_datetime
from tests.fixtures import APIResponseMocker


class TestPropertyBased:
    """Property-based tests for robust validation."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return new_client(api_key="test_key")

    # Test date parsing with generated data
    @given(st.dates(min_value=date(1900, 1, 1), max_value=date(2100, 12, 31)))
    def test_date_parsing_with_valid_dates(self, test_date):
        """Test date parsing with all possible valid dates."""
        date_string = test_date.isoformat()
        parsed = parse_date(date_string)
        assert parsed == test_date

    @given(st.datetimes(min_value=datetime(1900, 1, 1), max_value=datetime(2100, 12, 31)))
    def test_datetime_parsing_with_valid_datetimes(self, test_datetime):
        """Test datetime parsing with all possible valid datetimes."""
        # Convert to ISO format with Z suffix
        datetime_string = test_datetime.replace(microsecond=0).isoformat() + "Z"
        parsed = parse_datetime(datetime_string)
        expected = test_datetime.replace(microsecond=0, tzinfo=timezone.utc)
        assert parsed == expected

    @given(st.text(min_size=1, max_size=100))
    def test_date_parsing_with_invalid_strings(self, invalid_string):
        """Test date parsing handles arbitrary invalid strings gracefully."""
        # Assume the string is not a valid date format
        assume(not any(char.isdigit() for char in invalid_string[:4]))  # Skip year-like strings
        assume("-" not in invalid_string)  # Skip potential date formats
        
        parsed = parse_date(invalid_string)
        assert parsed is None

    # Test model validation with generated data
    @given(
        st.integers(min_value=1, max_value=1000000),
        st.text(min_size=1, max_size=255, alphabet=st.characters(blacklist_categories=['Cc', 'Cs'])),
        st.sampled_from(["Constituent", "Gift", "VolunteerTime"])
    )
    def test_category_model_with_generated_data(self, category_id, name, item_type):
        """Test Category model with generated valid data."""
        category = Category(
            id=category_id,
            name=name,
            item_type=item_type
        )
        assert category.id == category_id
        assert category.name == name
        assert category.item_type == item_type

    @given(
        st.integers(min_value=1, max_value=1000000),
        st.integers(min_value=1, max_value=1000000),
        st.floats(min_value=0.01, max_value=1000000.0, allow_nan=False, allow_infinity=False),
        st.dates(min_value=date(2000, 1, 1), max_value=date(2030, 12, 31))
    )
    def test_gift_model_with_generated_data(self, gift_id, constituent_id, amount, gift_date):
        """Test Gift model with generated valid data."""
        gift = Gift(
            id=gift_id,
            constituent_id=constituent_id,
            gift_type_id=1,  # Required field
            amount=round(amount, 2),  # Round to 2 decimal places
            date=gift_date.isoformat(),  # Required field
            gift_date=gift_date.isoformat(),
            created_at="2025-01-01T10:00:00Z",
            updated_at="2025-01-01T10:00:00Z"
        )
        assert gift.id == gift_id
        assert gift.constituent_id == constituent_id
        assert gift.amount == round(amount, 2)
        assert gift.gift_date == gift_date.isoformat()  # gift_date is stored as string
        assert gift.date == gift_date  # date field is parsed to date object

    # Test pagination with various data sizes
    @given(st.integers(min_value=0, max_value=1000))
    def test_pagination_response_generation(self, total_items):
        """Test pagination response generation with various total counts."""
        items = [
            {"id": i, "name": f"Item {i}", "item_type": "Constituent"}
            for i in range(1, min(total_items + 1, 101))  # Limit to 100 items per page
        ]
        
        response = APIResponseMocker.paginated_response(
            items=items,
            total=total_items,
            page=1,
            per_page=100
        )
        
        assert response["total"] == total_items
        assert response["total_items"] == total_items
        assert len(response["items"]) == min(total_items, 100)
        assert response["items_count"] == len(response["items"])

    @given(
        st.lists(
            st.dictionaries(
                st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=['Lu', 'Ll', 'Nd'])),
                st.one_of(
                    st.text(min_size=0, max_size=100),
                    st.integers(min_value=0, max_value=1000000),
                    st.floats(min_value=0.0, max_value=1000000.0, allow_nan=False, allow_infinity=False),
                    st.booleans()
                ),
                min_size=1,
                max_size=10
            ),
            min_size=0,
            max_size=50
        )
    )
    def test_api_response_with_generated_items(self, items):
        """Test API response handling with generated item data."""
        # Add required fields for Category model
        processed_items = []
        for i, item in enumerate(items):
            processed_item = {
                "id": i + 1,
                "name": f"Generated Item {i + 1}",
                "item_type": "Constituent",
                **item
            }
            processed_items.append(processed_item)
        
        response = APIResponseMocker.paginated_response(
            items=processed_items,
            total=len(processed_items),
            page=1,
            per_page=100
        )
        
        assert len(response["items"]) == len(processed_items)
        assert response["total"] == len(processed_items)

    # Test parameter validation with generated data
    @given(
        st.dictionaries(
            st.text(
                min_size=1, 
                max_size=50, 
                alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
            ),
            st.one_of(
                st.text(min_size=0, max_size=100),
                st.integers(min_value=0, max_value=1000),
                st.floats(min_value=0.0, max_value=1000.0, allow_nan=False, allow_infinity=False)
            ),
            min_size=1,
            max_size=10
        )
    )
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_parameter_validation_with_safe_data(self, client, params):
        """Test parameter validation with generated safe parameter data."""
        # Filter out potentially problematic parameter names
        safe_params = {}
        for key, value in params.items():
            # Only include parameters that look like legitimate API parameters
            if (key.replace('_', '').isalnum() and 
                not key.startswith('_') and 
                len(key) <= 50):
                safe_params[key] = value
        
        if safe_params:  # Only test if we have safe parameters
            # Should not raise exceptions for safe parameters
            validated = client.categories._client._validate_api_params(safe_params)
            assert isinstance(validated, dict)
            assert len(validated) <= len(safe_params)

    @given(st.text(min_size=1, max_size=20, alphabet=st.characters(whitelist_categories=['Lu', 'Ll'])))
    def test_constituent_name_validation(self, name):
        """Test constituent name handling with generated names."""
        constituent_data = {
            "id": 1,
            "first_name": name,
            "last_name": "TestLast",
            "created_at": "2025-01-01T10:00:00Z",
            "updated_at": "2025-01-01T10:00:00Z",
            "addresses": [],
            "phone_numbers": [],
            "email_addresses": [],
            "web_addresses": []
        }
        
        constituent = Constituent(**constituent_data)
        assert constituent.first_name == name
        assert constituent.last_name == "TestLast"

    # Test search functionality with generated queries
    @given(
        st.lists(
            st.text(min_size=1, max_size=50, alphabet=st.characters(whitelist_categories=['Lu', 'Ll', 'Nd', 'Zs'])),
            min_size=1,
            max_size=5
        )
    )
    @settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_search_query_handling(self, client, search_terms):
        """Test search query handling with generated search terms."""
        # Clean up search terms
        clean_terms = [term.strip() for term in search_terms if term.strip()]
        
        if clean_terms:
            with patch.object(client.constituents.client, '_get') as mock_get:
                mock_get.return_value = {
                    "items": [],
                    "total": 0,
                    "total_items": 0,
                    "items_count": 0
                }
                
                # Should handle search terms without errors
                result = client.constituents.search(clean_terms)
                assert isinstance(result, dict)

    # Test numeric edge cases
    @given(
        st.floats(
            min_value=0.0, 
            max_value=999999.99, 
            allow_nan=False, 
            allow_infinity=False
        )
    )
    def test_gift_amount_edge_cases(self, amount):
        """Test gift amount handling with various numeric values."""
        # Round to 2 decimal places for currency
        rounded_amount = round(amount, 2)
        
        gift_data = {
            "id": 1,
            "constituent_id": 123,
            "gift_type_id": 1,  # Required field
            "amount": rounded_amount,
            "date": "2025-01-15",  # Required field
            "gift_date": "2025-01-15",
            "created_at": "2025-01-15T14:30:00Z",
            "updated_at": "2025-01-15T14:30:00Z"
        }
        
        gift = Gift(**gift_data)
        assert gift.amount == rounded_amount

    @given(st.integers(min_value=1, max_value=10000))
    @settings(max_examples=20, suppress_health_check=[HealthCheck.function_scoped_fixture])  # Limit examples for performance
    def test_large_response_handling(self, client, item_count):
        """Test handling of responses with varying sizes."""
        # Generate items for testing
        items = [
            {"id": i, "name": f"Item {i}", "item_type": "Constituent"}
            for i in range(1, min(item_count + 1, 1001))  # Cap at 1000 items
        ]
        
        response_data = APIResponseMocker.paginated_response(
            items=items,
            total=item_count,
            page=1,
            per_page=len(items)
        )
        
        with patch.object(client.categories._client, '_get', return_value=response_data):
            result = client.categories.list(limit=len(items))
            assert len(result) == len(items)

    # Test string length variations
    @given(
        st.text(
            min_size=0, 
            max_size=500, 
            alphabet=st.characters(whitelist_categories=['Lu', 'Ll', 'Nd', 'Zs', 'Po'])
        )
    )
    def test_text_field_variations(self, text_value):
        """Test text field handling with various string lengths and characters."""
        if len(text_value.strip()) > 0:  # Only test non-empty strings
            category_data = {
                "id": 1,
                "name": text_value.strip(),
                "item_type": "Constituent"
            }
            
            category = Category(**category_data)
            assert category.name == text_value.strip()

    # Test date boundary conditions
    @given(st.integers(min_value=1900, max_value=2100))
    def test_year_boundary_conditions(self, year):
        """Test date parsing with various years."""
        try:
            test_date = date(year, 1, 1)
            date_string = test_date.isoformat()
            parsed = parse_date(date_string)
            assert parsed == test_date
        except ValueError:
            # Some years might be invalid, which is fine
            pass

    # Test pagination offset/limit combinations
    @given(
        st.integers(min_value=0, max_value=1000),
        st.integers(min_value=1, max_value=100)
    )
    def test_pagination_parameter_combinations(self, offset, limit):
        """Test pagination with various offset/limit combinations."""
        # Generate test data
        total_items = offset + limit + 10  # Ensure we have enough items
        items = [
            {"id": i, "name": f"Item {i}", "item_type": "Constituent"}
            for i in range(offset + 1, min(offset + limit + 1, total_items + 1))
        ]
        
        response = APIResponseMocker.paginated_response(
            items=items,
            total=total_items,
            page=(offset // limit) + 1,
            per_page=limit
        )
        
        assert len(response["items"]) <= limit
        assert response["total"] == total_items

    # Test error resilience
    @given(st.text(min_size=1, max_size=1000))
    def test_error_message_handling(self, error_message):
        """Test error message handling with various message contents."""
        from lgl_client.lgl_api.exceptions import LGLAPIError
        
        # Create error with generated message
        error = LGLAPIError(error_message, status_code=400, url="/test")
        
        # Should be able to convert to string without issues
        error_str = str(error)
        assert isinstance(error_str, str)
        assert len(error_str) > 0