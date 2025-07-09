"""Tests for pagination functionality across all resources."""
import pytest
from unittest.mock import Mock, patch
from typing import Dict, Any, List

from lgl_client import new_client
from lgl_client.lgl_api.client import LGLClient
from lgl_client.models.category import Category
from tests.fixtures import (
    APIResponseMocker,
    DIRECT_ARRAY_RESOURCES,
    get_mock_response,
    get_pagination_test_data
)


class TestPaginationFramework:
    """Test pagination functionality."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        return new_client(api_key="test_key")

    def test_pagination_with_standard_format(self, client):
        """Test pagination with standard {items: [], total: X} format."""
        # Mock response data for 3 pages
        page1_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "name": "Item 1", "item_type": "Constituent"}, 
                {"id": 2, "name": "Item 2", "item_type": "Constituent"}
            ],
            total=5,
            page=1,
            per_page=2
        )
        page2_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 3, "name": "Item 3", "item_type": "Constituent"}, 
                {"id": 4, "name": "Item 4", "item_type": "Constituent"}
            ],
            total=5,
            page=2,
            per_page=2
        )
        page3_data = APIResponseMocker.paginated_response(
            items=[{"id": 5, "name": "Item 5", "item_type": "Constituent"}],
            total=5,
            page=3,
            per_page=2
        )

        def mock_get_side_effect(*args, **kwargs):
            # Extract offset from params to determine which page to return
            offset = kwargs.get('offset', 0)
            limit = kwargs.get('limit', 100)
            
            # Return exactly `limit` items per page to trigger pagination
            all_test_items = [
                {"id": 1, "name": "Item 1", "item_type": "Constituent"},
                {"id": 2, "name": "Item 2", "item_type": "Constituent"},
                {"id": 3, "name": "Item 3", "item_type": "Constituent"},
                {"id": 4, "name": "Item 4", "item_type": "Constituent"},
                {"id": 5, "name": "Item 5", "item_type": "Constituent"}
            ]
            
            # Get the slice for this page
            start = offset
            end = min(offset + limit, len(all_test_items))
            items = all_test_items[start:end]
            
            if not items:
                return APIResponseMocker.empty_response()
            
            return APIResponseMocker.paginated_response(
                items=items,
                total=len(all_test_items),
                page=(offset // limit) + 1,
                per_page=limit
            )

        with patch.object(client.categories._client, '_get', side_effect=mock_get_side_effect) as mock_get:
            # Test fetch_all method
            all_items = client.categories.fetch_all()
            
            # Verify all items were fetched
            assert len(all_items) == 5
            assert all_items[0].name == "Item 1"
            assert all_items[4].name == "Item 5"
            
            # Verify correct number of API calls (with limit=100, all items fit in one page)
            assert mock_get.call_count == 1

    def test_pagination_with_simple_resources(self, client):
        """Test pagination with simpler resources like payment_types."""
        # Mock response data - payment types still use paginated format
        response_data = APIResponseMocker.paginated_response(
            items=[
                {"id": 1, "name": "Cash", "key": "cash", "ordinal": 1},
                {"id": 2, "name": "Check", "key": "check", "ordinal": 2}
            ],
            total=2,
            page=1,
            per_page=100
        )

        with patch.object(client.payment_types._client, '_get', return_value=response_data):
            # Test fetch_all method
            all_items = client.payment_types.fetch_all()
            
            # Verify all items were fetched
            assert len(all_items) == 2
            assert all_items[0].name == "Cash"
            assert all_items[1].name == "Check"

    def test_pagination_empty_response(self, client):
        """Test pagination with empty response."""
        empty_data = APIResponseMocker.empty_response()

        with patch.object(client.categories._client, '_get', return_value=empty_data):
            all_items = client.categories.fetch_all()
            
            assert len(all_items) == 0

    def test_pagination_single_page(self, client):
        """Test pagination with single page response."""
        single_page_data = APIResponseMocker.paginated_response(
            items=[{"id": 1, "name": "Only Item", "item_type": "Constituent"}],
            total=1,
            page=1,
            per_page=10
        )

        with patch.object(client.categories._client, '_get', return_value=single_page_data):
            all_items = client.categories.fetch_all()
            
            assert len(all_items) == 1
            assert all_items[0].name == "Only Item"

    def test_pagination_exact_page_boundary(self, client):
        """Test pagination when total items exactly match page size."""
        # Exactly 10 items in one page
        page1_data = APIResponseMocker.paginated_response(
            items=[{"id": i, "name": f"Item {i}", "item_type": "Constituent"} for i in range(1, 11)],
            total=10,
            page=1,
            per_page=10
        )

        with patch.object(client.categories._client, '_get', return_value=page1_data):
            all_items = client.categories.fetch_all()
            
            assert len(all_items) == 10
            assert all_items[0].name == "Item 1"
            assert all_items[9].name == "Item 10"

    @pytest.mark.parametrize("resource_name", [
        "categories", "constituents", "gifts", "notes", "appeals", "campaigns"
    ])
    def test_pagination_across_paginated_resources(self, client, resource_name):
        """Test pagination works across different paginated resources."""
        # Get test data for this resource
        test_items = get_pagination_test_data(resource_name)[:5]  # Use 5 items
        
        paginated_data = APIResponseMocker.paginated_response(
            items=test_items,
            total=len(test_items),
            page=1,
            per_page=10
        )

        # Get the resource API from client
        resource_api = getattr(client, resource_name)
        
        # Apply client attribute pattern analysis
        client_attr_mapping = {
            'constituents': 'client', 'gifts': 'client', 'notes': 'client',
            'appeals': '_client', 'campaigns': '_client', 'categories': '_client'
        }
        client_attr = client_attr_mapping.get(resource_name, '_client')
        
        # Handle constituent-dependent resources
        constituent_dependent_resources = {'gifts', 'notes'}
        
        with patch.object(getattr(resource_api, client_attr), '_get', return_value=paginated_data):
            if resource_name in constituent_dependent_resources:
                all_items = resource_api.fetch_all(constituent_id=123)
            else:
                all_items = resource_api.fetch_all()
            
            assert len(all_items) == 5
            assert all_items[0].id == 1

    @pytest.mark.parametrize("resource_name", [
        "payment_types", "membership_levels", "class_affiliation_types", 
        "relationship_types", "team_members"
    ])
    def test_direct_array_across_resources(self, client, resource_name):
        """Test direct array format works across different resources."""
        # Get test data for this resource
        if resource_name in DIRECT_ARRAY_RESOURCES:
            test_items = get_pagination_test_data(resource_name)[:3]  # Use 3 items

            # Get the resource API from client
            resource_api = getattr(client, resource_name)
            
            # Apply client attribute pattern analysis - all these use _client
            client_attr_mapping = {
                'payment_types': '_client', 'membership_levels': '_client', 
                'class_affiliation_types': '_client', 'relationship_types': '_client', 
                'team_members': '_client'
            }
            client_attr = client_attr_mapping.get(resource_name, '_client')
            
            # For direct array resources, the _get should return {"items": test_items}
            mock_response = {"items": test_items}
            
            with patch.object(getattr(resource_api, client_attr), '_get', return_value=mock_response):
                all_items = resource_api.fetch_all()
                
                assert len(all_items) == 3
                assert all_items[0].id == 1

    def test_pagination_multiple_pages(self, client):
        """Test pagination with multiple pages by using smaller page size."""
        def mock_get_side_effect(*args, **kwargs):
            offset = kwargs.get('offset', 0)
            limit = kwargs.get('limit', 100)
            
            # Create 25 test items to ensure multiple pages
            all_test_items = [
                {"id": i, "name": f"Item {i}", "item_type": "Constituent"}
                for i in range(1, 26)
            ]
            
            # Get the slice for this page
            start = offset
            end = min(offset + limit, len(all_test_items))
            items = all_test_items[start:end]
            
            if not items:
                return APIResponseMocker.empty_response()
            
            return APIResponseMocker.paginated_response(
                items=items,
                total=len(all_test_items),
                page=(offset // limit) + 1,
                per_page=limit
            )

        # Test pagination by forcing smaller page size
        with patch.object(client.categories._client, '_get', side_effect=mock_get_side_effect):
            # Test by calling _paginate directly with smaller limit
            def _list_page(**kwargs):
                return client.categories.list(**kwargs)
            
            # Use smaller limit to force multiple pages
            items = list(client.categories._client._paginate(_list_page, limit=10))
            all_items = [Category.from_dict(item) if isinstance(item, dict) else item for item in items]
            
            # Should get all 25 items
            assert len(all_items) == 25
            assert all_items[0].name == "Item 1"
            assert all_items[24].name == "Item 25"

    def test_pagination_with_large_dataset(self, client):
        """Test pagination with larger dataset (memory usage consideration)."""
        # Mock function to simulate pages using offset/limit
        def mock_get_side_effect(*args, **kwargs):
            # Extract offset and limit from params
            offset = kwargs.get('offset', 0)
            limit = kwargs.get('limit', 100)
            
            # Generate 100 test items
            all_test_items = [
                {"id": i, "name": f"Item {i}", "item_type": "Constituent"}
                for i in range(1, 101)
            ]
            
            # Get the slice for this page
            start = offset
            end = min(offset + limit, len(all_test_items))
            items = all_test_items[start:end]
            
            if not items:
                return APIResponseMocker.empty_response()
                
            return APIResponseMocker.paginated_response(
                items=items,
                total=len(all_test_items),
                page=(offset // limit) + 1,
                per_page=limit
            )

        with patch.object(client.categories._client, '_get', side_effect=mock_get_side_effect):
            all_items = client.categories.fetch_all()
            
            # Verify all 100 items were fetched
            assert len(all_items) == 100
            assert all_items[0].id == 1
            assert all_items[99].id == 100

    def test_pagination_error_handling(self, client):
        """Test pagination handles errors gracefully."""
        # Create a scenario where pagination will definitely continue beyond first page
        # by having more total items than the limit with pagination logic
        def mock_get_side_effect(*args, **kwargs):
            offset = kwargs.get('offset', 0)
            limit = kwargs.get('limit', 100)
            
            if offset == 0:
                # First page succeeds but indicates more data exists
                # Return exactly `limit` items to trigger continuation
                items = [
                    {"id": i, "name": f"Item {i}", "item_type": "Constituent"}
                    for i in range(1, min(101, limit + 1))
                ]
                return APIResponseMocker.paginated_response(
                    items=items,
                    total=200,  # More than limit to ensure pagination continues
                    page=1,
                    per_page=limit
                )
            else:
                # Second page fails
                raise Exception("HTTP 500")

        with patch.object(client.categories._client, '_get', side_effect=mock_get_side_effect):
            with pytest.raises(Exception):
                client.categories.fetch_all()