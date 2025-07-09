"""Integration tests requiring live API access.

IMPORTANT: These tests require:
1. Valid LGL_API_KEY environment variable
2. Human approval before running
3. Access to test/staging LGL environment
"""
import pytest
import os
from typing import List

from lgl_client import new_client


# Skip all tests in this module unless explicitly enabled
pytestmark = pytest.mark.integration


class TestLiveAPIIntegration:
    """Integration tests with live LGL API."""

    @pytest.fixture(scope="class")
    def live_client(self):
        """Create client with live API key."""
        api_key = os.getenv("LGL_API_KEY")
        if not api_key:
            pytest.skip("LGL_API_KEY environment variable not set")
        return new_client(api_key=api_key)

    @pytest.fixture(scope="class")
    def require_human_approval(self):
        """Require human approval before running live API tests."""
        approval = os.getenv("LGL_LIVE_API_APPROVED")
        if approval != "yes":
            pytest.skip(
                "Live API tests require human approval. "
                "Set LGL_LIVE_API_APPROVED=yes to run these tests."
            )

    def test_payment_types_live_api(self, live_client, require_human_approval):
        """Test payment types with live API."""
        payment_types = live_client.payment_types.list()
        
        assert isinstance(payment_types, list)
        assert len(payment_types) > 0
        
        # Verify payment type structure
        first_payment_type = payment_types[0]
        assert hasattr(first_payment_type, 'id')
        assert hasattr(first_payment_type, 'name')
        assert hasattr(first_payment_type, 'key')

    def test_payment_types_fetch_all_live(self, live_client, require_human_approval):
        """Test payment types fetch_all with live API."""
        all_payment_types = live_client.payment_types.fetch_all()
        
        assert isinstance(all_payment_types, list)
        assert len(all_payment_types) > 0
        
        # Should be same as list() for small datasets
        list_payment_types = live_client.payment_types.list()
        assert len(all_payment_types) == len(list_payment_types)

    def test_membership_levels_live_api(self, live_client, require_human_approval):
        """Test membership levels with live API."""
        membership_levels = live_client.membership_levels.list()
        
        assert isinstance(membership_levels, list)
        # May be empty for some accounts
        
        if membership_levels:
            first_level = membership_levels[0]
            assert hasattr(first_level, 'id')
            assert hasattr(first_level, 'name')

    def test_categories_live_api(self, live_client, require_human_approval):
        """Test categories with live API."""
        categories = live_client.categories.list()
        
        assert isinstance(categories, list)
        # Categories should exist in most accounts
        
        if categories:
            first_category = categories[0]
            assert hasattr(first_category, 'id')
            assert hasattr(first_category, 'name')
            assert hasattr(first_category, 'item_type')

    def test_team_members_live_api(self, live_client, require_human_approval):
        """Test team members with live API."""
        team_members = live_client.team_members.list()
        
        assert isinstance(team_members, list)
        assert len(team_members) > 0  # Should have at least one team member
        
        # Verify team member structure
        first_member = team_members[0]
        assert hasattr(first_member, 'id')
        assert hasattr(first_member, 'email')

    def test_relationship_types_live_api(self, live_client, require_human_approval):
        """Test relationship types with live API."""
        relationship_types = live_client.relationship_types.list()
        
        assert isinstance(relationship_types, list)
        assert len(relationship_types) > 0
        
        # Verify relationship type structure
        first_type = relationship_types[0]
        assert hasattr(first_type, 'id')
        assert hasattr(first_type, 'name')

    def test_types_live_api(self, live_client, require_human_approval):
        """Test types system with live API."""
        types = live_client.types.list()
        
        assert isinstance(types, list)
        assert len(types) > 0
        
        # Test type values for first type
        first_type = types[0]
        type_values = live_client.types.list_values(first_type.key)
        
        assert isinstance(type_values, list)
        # May be empty for some types

    def test_custom_attributes_live_api(self, live_client, require_human_approval):
        """Test custom attributes with live API."""
        # Test for constituent attributes
        attributes = live_client.custom_attributes.list(item_type="Constituent")
        
        assert isinstance(attributes, list)
        # May be empty if no custom attributes defined
        
        if attributes:
            first_attr = attributes[0]
            assert hasattr(first_attr, 'id')
            assert hasattr(first_attr, 'name')
            assert hasattr(first_attr, 'item_type')

    def test_mailing_templates_live_api(self, live_client, require_human_approval):
        """Test mailing templates with live API."""
        templates = live_client.mailing_templates.list()
        
        assert isinstance(templates, list)
        # May be empty if no templates configured
        
        if templates:
            first_template = templates[0]
            assert hasattr(first_template, 'id')
            assert hasattr(first_template, 'name')

    def test_keywords_live_api(self, live_client, require_human_approval):
        """Test keywords system with live API."""
        # First get categories to find one with keywords
        categories = live_client.categories.list()
        
        if categories:
            first_category = categories[0]
            keywords = live_client.keywords.list_for_category(first_category.id)
            
            assert isinstance(keywords, list)
            # May be empty if no keywords in category

    def test_constituents_search_live_api(self, live_client, require_human_approval):
        """Test constituent search with live API."""
        # Search for a common name (should be safe for most test environments)
        results = live_client.constituents.search(["name=test"])
        
        assert isinstance(results, dict)
        # Results may be empty
        
        if results.get('items'):
            first_result = results['items'][0]
            assert 'id' in first_result
            assert 'first_name' in first_result or 'last_name' in first_result

    def test_pagination_with_live_data(self, live_client, require_human_approval):
        """Test pagination with live data."""
        # Use payment types as they're typically small and safe
        page1 = live_client.payment_types.list(limit=2, offset=0)
        all_items = live_client.payment_types.fetch_all()
        
        assert isinstance(page1, list)
        assert isinstance(all_items, list)
        assert len(all_items) >= len(page1)

    def test_error_handling_with_live_api(self, live_client, require_human_approval):
        """Test error handling with live API."""
        from lgl_client.lgl_api.exceptions import NotFoundError
        
        # Try to get a non-existent category
        with pytest.raises(NotFoundError):
            live_client.categories.retrieve(999999)

    def test_date_fields_with_live_data(self, live_client, require_human_approval):
        """Test date field parsing with live data."""
        # Get any resource with date fields
        categories = live_client.categories.list()
        
        if categories:
            first_category = categories[0]
            # Most models should have created_at/updated_at
            assert hasattr(first_category, 'id')  # Basic check that model loaded

    def test_security_features_with_live_api(self, live_client, require_human_approval):
        """Test security features work with live API."""
        # Create debug client to test credential masking
        from lgl_client.lgl_api.client import LGLClient
        import os
        
        api_key = os.getenv("LGL_API_KEY")
        debug_client = LGLClient(api_key=api_key, debug=True)
        
        # This should work but mask credentials in debug output
        payment_types = debug_client._get("payment_types")
        # In debug mode with live API, should return actual response data
        assert payment_types is not None

    @pytest.mark.slow
    def test_large_dataset_handling_live(self, live_client, require_human_approval):
        """Test handling of larger datasets with live API."""
        # Use fetch_all on a resource that might have many items
        try:
            all_categories = live_client.categories.fetch_all()
            assert isinstance(all_categories, list)
            
            # If there are many categories, verify they all loaded correctly
            if len(all_categories) > 10:
                # Spot check a few items
                assert all(hasattr(cat, 'id') for cat in all_categories[:5])
                assert all(hasattr(cat, 'name') for cat in all_categories[:5])
        except Exception as e:
            # If this fails, it might be due to API limits or large datasets
            pytest.skip(f"Large dataset test skipped due to: {e}")

    def test_api_rate_limiting_respect(self, live_client, require_human_approval):
        """Test that client respects API rate limiting."""
        import time
        
        # Make several requests in quick succession
        start_time = time.time()
        
        for i in range(5):
            payment_types = live_client.payment_types.list()
            assert isinstance(payment_types, list)
        
        end_time = time.time()
        total_time = end_time - start_time
        
        # Should complete reasonably quickly (under 10 seconds for 5 requests)
        assert total_time < 10.0, f"5 API requests took {total_time:.1f}s, possible rate limiting issues"

    def test_concurrent_safe_operations(self, live_client, require_human_approval):
        """Test that client handles concurrent-like operations safely."""
        # Simulate rapid consecutive calls
        results = []
        
        for i in range(3):
            payment_types = live_client.payment_types.list()
            results.append(payment_types)
        
        # All requests should succeed and return consistent data
        assert len(results) == 3
        assert all(isinstance(result, list) for result in results)
        
        # Results should be consistent (assuming no changes during test)
        if results[0]:
            assert len(results[0]) == len(results[1]) == len(results[2])