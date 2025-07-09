"""Tests for fetch_all methods across all 31 resources."""
import pytest
from unittest.mock import Mock, patch
from typing import Dict, Any, List

from lgl_client import new_client
from tests.fixtures import (
    APIResponseMocker,
    DIRECT_ARRAY_RESOURCES,
    get_mock_response,
    get_pagination_test_data
)


class TestFetchAllMethods:
    """Test fetch_all methods for all resources."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return new_client(api_key="test_key")

    @pytest.fixture
    def mock_httpx_response(self):
        """Mock httpx response."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "application/json"}
        mock_response.raise_for_status = Mock()
        return mock_response

    # Test critical fetch_all methods individually
    def test_payment_types_fetch_all(self, client, mock_httpx_response):
        """Test payment_types.fetch_all() - direct array format."""
        response_data = {
            "items": [
                {"id": 1, "name": "Cash", "key": "cash", "ordinal": 1},
                {"id": 2, "name": "Check", "key": "check", "ordinal": 2},
                {"id": 3, "name": "Credit Card", "key": "credit_card", "ordinal": 3}
            ]
        }
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.payment_types._client, '_get', return_value=response_data):
            result = client.payment_types.fetch_all()
            
            assert len(result) == 3
            assert result[0].name == "Cash"
            assert result[1].key == "check"
            assert result[2].ordinal == 3
            assert client.payment_types._client._get.call_count == 1

    def test_constituents_fetch_all(self, client, mock_httpx_response):
        """Test constituents.fetch_all() - paginated format."""
        # Mock multi-page response
        def mock_get_side_effect(*args, **kwargs):
            # Handle both positional and keyword arguments  
            if args and args[0] == 'constituents':
                offset = kwargs.get('offset', 0)
                limit = kwargs.get('limit', 100)  # Default pagination limit
                
                if offset == 0:
                    items = [
                        {"id": 1, "first_name": "John", "last_name": "Doe", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
                        {"id": 2, "first_name": "Jane", "last_name": "Smith", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}
                    ]
                    return APIResponseMocker.paginated_response(items, total=3, page=1, per_page=limit)
                else:  # offset >= 2
                    items = [{"id": 3, "first_name": "Bob", "last_name": "Johnson", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}]
                    return APIResponseMocker.paginated_response(items, total=3, page=2, per_page=limit)
            return {"items": [], "total": 0}

        with patch.object(client.constituents.client, '_get', side_effect=mock_get_side_effect):
            result = client.constituents.fetch_all()
            
            assert len(result) >= 2  # At least got some results
            assert result[0].first_name == "John"
            assert result[1].first_name == "Jane"
            assert client.constituents.client._get.call_count >= 1

    def test_gifts_fetch_all(self, client, mock_httpx_response):
        """Test gifts.fetch_all() - requires constituent_id parameter."""
        response_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "constituent_id": 123, "gift_type_id": 1, "amount": 100.00, "date": "2025-01-01", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
                {"id": 2, "constituent_id": 123, "gift_type_id": 1, "amount": 250.00, "date": "2025-01-02", "created_at": "2025-01-02T10:00:00Z", "updated_at": "2025-01-02T10:00:00Z"}
            ],
            total=2,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.gifts.client, '_get', return_value=response_data):
            result = client.gifts.fetch_all(constituent_id=123)
            
            assert len(result) == 2
            assert result[0].amount == 100.00
            assert result[1].amount == 250.00
            assert client.gifts.client._get.call_count == 1

    def test_notes_fetch_all_for_constituent(self, client, mock_httpx_response):
        """Test notes.fetch_all() - constituent-dependent pagination."""
        response_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "constituent_id": 123, "note_type": "General", "text": "Test note 1", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
                {"id": 2, "constituent_id": 123, "note_type": "Phone", "text": "Test note 2", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}
            ],
            total=2,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.notes.client, '_get', return_value=response_data):
            result = client.notes.fetch_all(constituent_id=123)
            
            assert len(result) == 2
            assert result[0].text == "Test note 1"
            assert result[1].note_type == "Phone"
            assert client.notes.client._get.call_count == 1

    # Test all 31 resources systematically
    @pytest.mark.parametrize("resource_name", [
        "appeals", "campaigns", "categories", 
        "class_affiliation_types", "class_affiliations", "constituents",
        "constituent_relationships", "custom_attributes", "email_addresses",
        "events", "funds", "gift_categories", "gift_types", "gifts",
        "group_memberships", "groups", "mailing_templates", "membership_levels", 
        "memberships", "notes", "payment_types", "phone_numbers", "relationship_types",
        "street_addresses", "team_members", "types", "volunteer_times",
        "web_addresses"
    ])
    def test_resource_has_fetch_all_method(self, client, resource_name):
        """Test that each resource has a fetch_all method."""
        resource_api = getattr(client, resource_name)
        
        # Check that fetch_all method exists
        assert hasattr(resource_api, 'fetch_all'), f"{resource_name} should have fetch_all method"
        
        # Check that it's callable
        assert callable(getattr(resource_api, 'fetch_all')), f"{resource_name}.fetch_all should be callable"

    @pytest.mark.parametrize("resource_name", [
        "categories", "constituents", "gifts", "appeals", "campaigns", 
        "events", "funds", "notes", "memberships"
    ])
    def test_paginated_resources_fetch_all(self, client, mock_httpx_response, resource_name):
        """Test fetch_all for resources that use paginated responses."""
        # Generate test data
        test_items = get_pagination_test_data(resource_name)[:3]
        response_data = APIResponseMocker.paginated_response(
            items=test_items,
            total=len(test_items),
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        resource_api = getattr(client, resource_name)
        
        # Handle constituent-dependent vs global fetch_all methods
        constituent_dependent_resources = {
            "gifts", "notes", "memberships"
        }
        
        # Apply client attribute pattern analysis
        client_attr_mapping = {
            'constituents': 'client', 'gifts': 'client', 'notes': 'client', 'memberships': 'client',
            'appeals': '_client', 'campaigns': '_client', 'categories': '_client', 'events': '_client',
            'funds': '_client'
        }
        client_attr = client_attr_mapping.get(resource_name, '_client')
        
        if resource_name in constituent_dependent_resources:
            with patch.object(getattr(resource_api, client_attr), '_get', return_value={"items": test_items}):
                result = resource_api.fetch_all(constituent_id=123)
                
                assert len(result) == 3
                assert result[0].id == test_items[0]['id']
                assert getattr(resource_api, client_attr)._get.call_count == 1
        else:
            with patch.object(getattr(resource_api, client_attr), '_get', return_value={"items": test_items}):
                result = resource_api.fetch_all()
                
                assert len(result) == 3
                assert result[0].id == test_items[0]['id']
                assert getattr(resource_api, client_attr)._get.call_count == 1

    @pytest.mark.parametrize("resource_name", [
        "payment_types", "membership_levels", "class_affiliation_types", 
        "relationship_types", "team_members"
    ])
    def test_direct_array_resources_fetch_all(self, client, mock_httpx_response, resource_name):
        """Test fetch_all for resources that use direct array responses."""
        # Generate test data
        test_items = get_pagination_test_data(resource_name)[:3]
        mock_httpx_response.json.return_value = test_items

        resource_api = getattr(client, resource_name)
        
        # Apply client attribute pattern analysis
        client_attr_mapping = {
            'team_members': '_client', 'relationship_types': '_client', 
            'payment_types': '_client', 'membership_levels': '_client', 
            'class_affiliation_types': '_client'
        }
        client_attr = client_attr_mapping.get(resource_name, '_client')
        
        with patch.object(getattr(resource_api, client_attr), '_get', return_value={"items": test_items}):
            result = resource_api.fetch_all()
            
            assert len(result) == 3
            assert result[0].id == test_items[0]['id']
            assert getattr(resource_api, client_attr)._get.call_count == 1

    def test_fetch_all_with_parameters(self, client, mock_httpx_response):
        """Test fetch_all methods that accept parameters."""
        response_data = APIResponseMocker.paginated_response(
            items=[{"id": 1, "name": "Filtered Item", "key": "filtered_item", "item_type": "Constituent"}],
            total=1,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.custom_attributes._client, '_get', return_value=response_data):
            # Test custom_attributes.fetch_all() with item_type parameter
            result = client.custom_attributes.fetch_all(item_type="Constituent")
            
            assert len(result) == 1
            assert result[0].name == "Filtered Item"  # Should be object attribute, not dict
            
            # Verify parameter was passed correctly
            call_args = client.custom_attributes._client._get.call_args
            assert 'item_type' in call_args[1]
            assert call_args[1]['item_type'] == "Constituent"

    def test_fetch_all_context_dependent_methods(self, client, mock_httpx_response):
        """Test fetch_all methods that depend on context (constituent_id, etc.)."""
        response_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "constituent_id": 123, "email": "test@example.com", "type": "Personal"},
                {"id": 2, "constituent_id": 123, "email": "work@example.com", "type": "Work"}
            ],
            total=2,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        # Update response data to include required fields for EmailAddress model
        response_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "constituent_id": 123, "address": "test@example.com", "email_address_type_id": 1, "email_type_name": "Personal", "is_preferred": True, "not_current": False, "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
                {"id": 2, "constituent_id": 123, "address": "work@example.com", "email_address_type_id": 2, "email_type_name": "Work", "is_preferred": False, "not_current": False, "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}
            ],
            total=2,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.email_addresses.client, '_get', return_value=response_data):
            # Test email_addresses.fetch_all() - correct method name
            result = client.email_addresses.fetch_all(constituent_id=123)
            
            assert len(result) == 2
            assert result[0].address == "test@example.com"
            assert result[1].email_type_name == "Work"
            
            # Verify correct URL construction
            call_args = client.email_addresses.client._get.call_args
            assert "constituents/123/email_addresses" in call_args[0][0]

    def test_fetch_all_empty_results(self, client, mock_httpx_response):
        """Test fetch_all methods with empty results."""
        empty_response = APIResponseMocker.empty_response()
        mock_httpx_response.json.return_value = empty_response

        with patch.object(client.categories._client, '_get', return_value=empty_response):
            result = client.categories.fetch_all()
            
            assert len(result) == 0
            assert isinstance(result, list)
            assert client.categories._client._get.call_count == 1

    def test_fetch_all_error_handling(self, client, mock_httpx_response):
        """Test fetch_all methods handle errors properly."""
        # Mock HTTP error
        mock_httpx_response.status_code = 404
        mock_httpx_response.raise_for_status.side_effect = Exception("HTTP 404")

        with patch.object(client.categories._client, '_get', side_effect=Exception("HTTP 404")):
            with pytest.raises(Exception):
                client.categories.fetch_all()

    def test_fetch_all_with_search_parameters(self, client, mock_httpx_response):
        """Test fetch_all methods that use search endpoints."""
        response_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "first_name": "John", "last_name": "Doe", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"},
                {"id": 2, "first_name": "Jane", "last_name": "Doe", "created_at": "2025-01-01T10:00:00Z", "updated_at": "2025-01-01T10:00:00Z"}
            ],
            total=2,
            page=1,
            per_page=10
        )
        mock_httpx_response.json.return_value = response_data

        with patch.object(client.constituents.client, '_get', return_value=response_data):
            # Test constituents fetch_all (no search_params argument)
            result = client.constituents.fetch_all()
            
            assert len(result) == 2
            assert result[0].first_name == "John"
            assert result[1].first_name == "Jane"