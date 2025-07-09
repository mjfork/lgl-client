"""Global pytest configuration and fixtures."""
import pytest
import httpx
from unittest.mock import Mock, patch
from typing import Dict, Any, List
import json

from lgl_client import new_client
from lgl_client.lgl_api.client import LGLClient


@pytest.fixture
def mock_api_key():
    """Mock API key for testing."""
    return "test_api_key_12345"


@pytest.fixture  
def mock_client(mock_api_key):
    """Mock LGL client with test API key."""
    return new_client(api_key=mock_api_key)


@pytest.fixture
def mock_httpx_client():
    """Mock httpx client for HTTP requests."""
    mock = Mock(spec=httpx.Client)
    mock.headers = {}
    return mock


@pytest.fixture
def sample_pagination_response():
    """Sample paginated API response."""
    return {
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"}
        ],
        "total": 25,
        "page": 1,
        "per_page": 3,
        "total_pages": 9
    }


@pytest.fixture
def sample_direct_array_response():
    """Sample direct array API response."""
    return [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"}
    ]


@pytest.fixture
def sample_empty_response():
    """Sample empty API response."""
    return {
        "items": [],
        "total": 0,
        "page": 1,
        "per_page": 10,
        "total_pages": 0
    }


@pytest.fixture
def sample_single_page_response():
    """Sample single page API response."""
    return {
        "items": [{"id": 1, "name": "Only Item"}],
        "total": 1,
        "page": 1,
        "per_page": 10,
        "total_pages": 1
    }


@pytest.fixture
def sample_constituent_data():
    """Sample constituent data for testing."""
    return {
        "id": 12345,
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1-555-123-4567",
        "created_at": "2025-01-01T10:00:00Z",
        "updated_at": "2025-01-02T15:30:00Z",
        "addresses": [],
        "phone_numbers": [],
        "email_addresses": [],
        "web_addresses": []
    }


@pytest.fixture
def sample_gift_data():
    """Sample gift data for testing."""
    return {
        "id": 67890,
        "constituent_id": 12345,
        "amount": 100.00,
        "gift_date": "2025-01-01",
        "payment_type": "Check",
        "created_at": "2025-01-01T10:00:00Z",
        "updated_at": "2025-01-01T10:00:00Z"
    }


@pytest.fixture
def sample_search_response():
    """Sample search API response."""
    return {
        "items": [
            {"id": 1, "name": "Search Result 1"},
            {"id": 2, "name": "Search Result 2"}
        ],
        "total": 2,
        "page": 1,
        "per_page": 10,
        "total_pages": 1
    }


class MockResponse:
    """Mock HTTP response for testing."""
    
    def __init__(self, json_data: Dict[str, Any], status_code: int = 200):
        self.json_data = json_data
        self.status_code = status_code
        self.headers = {"content-type": "application/json"}
        self.text = json.dumps(json_data)
    
    def json(self):
        return self.json_data
    
    def raise_for_status(self):
        if self.status_code >= 400:
            raise httpx.HTTPStatusError(
                f"HTTP {self.status_code}",
                request=Mock(),
                response=self
            )


@pytest.fixture
def mock_response():
    """Factory for creating mock responses."""
    return MockResponse


@pytest.fixture
def api_resources():
    """List of all API resources for comprehensive testing."""
    return [
        "appeals", "appeal_requests", "campaigns", "categories", 
        "class_affiliation_types", "class_affiliations", "constituents",
        "constituent_relationships", "custom_attributes", "email_addresses",
        "events", "funds", "gift_categories", "gift_types", "gifts",
        "group_memberships", "groups", "invitations", "keywords",
        "mailing_templates", "membership_levels", "memberships", "notes",
        "payment_types", "phone_numbers", "relationship_types",
        "street_addresses", "team_members", "types", "volunteer_times",
        "web_addresses"
    ]


@pytest.fixture(autouse=True)
def disable_live_api():
    """Automatically disable live API calls in tests."""
    with patch('httpx.Client') as mock:
        yield mock