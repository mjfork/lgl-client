"""Mock HTTP responses for API testing."""
from typing import Dict, Any, List
import json


class APIResponseMocker:
    """Factory for creating mock API responses."""
    
    @staticmethod
    def paginated_response(
        items: List[Dict[str, Any]], 
        total: int, 
        page: int = 1, 
        per_page: int = 10
    ) -> Dict[str, Any]:
        """Create a paginated response."""
        total_pages = (total + per_page - 1) // per_page
        return {
            "items": items,
            "total": total,
            "total_items": total,  # Field expected by pagination logic
            "items_count": len(items),  # Field expected by pagination logic
            "page": page,
            "per_page": per_page,
            "total_pages": total_pages
        }
    
    @staticmethod
    def direct_array_response(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Create a direct array response."""
        return items
    
    @staticmethod
    def empty_response() -> Dict[str, Any]:
        """Create an empty response."""
        return {
            "items": [],
            "total": 0,
            "total_items": 0,
            "items_count": 0,
            "page": 1,
            "per_page": 10,
            "total_pages": 0
        }
    
    @staticmethod
    def error_response(message: str, status_code: int = 400) -> Dict[str, Any]:
        """Create an error response."""
        return {
            "error": message,
            "status": status_code
        }


# Sample data for different resource types
SAMPLE_PAYMENT_TYPES = [
    {"id": 1, "name": "Cash", "key": "cash", "ordinal": 1},
    {"id": 2, "name": "Check", "key": "check", "ordinal": 2},
    {"id": 3, "name": "Credit Card", "key": "credit_card", "ordinal": 3},
    {"id": 4, "name": "Online", "key": "online", "ordinal": 4}
]

SAMPLE_CONSTITUENTS = [
    {
        "id": 1,
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
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@example.com",
        "phone": "+1-555-987-6543",
        "created_at": "2025-01-01T11:00:00Z",
        "updated_at": "2025-01-02T16:30:00Z",
        "addresses": [],
        "phone_numbers": [],
        "email_addresses": [],
        "web_addresses": []
    }
]

SAMPLE_GIFTS = [
    {
        "id": 1,
        "constituent_id": 1,
        "amount": 100.00,
        "gift_type_id": 1,
        "date": "2025-01-01",
        "gift_date": "2025-01-01",
        "payment_type": "Check",
        "created_at": "2025-01-01T10:00:00Z",
        "updated_at": "2025-01-01T10:00:00Z"
    },
    {
        "id": 2,
        "constituent_id": 2,
        "amount": 250.00,
        "gift_type_id": 1,
        "date": "2025-01-02",
        "gift_date": "2025-01-02",
        "payment_type": "Credit Card",
        "created_at": "2025-01-02T14:30:00Z",
        "updated_at": "2025-01-02T14:30:00Z"
    }
]

SAMPLE_CATEGORIES = [
    {"id": 1, "item_type": "Constituent", "name": "Donor", "key": "donor", "ordinal": 1},
    {"id": 2, "item_type": "Constituent", "name": "Volunteer", "key": "volunteer", "ordinal": 2},
    {"id": 3, "item_type": "Gift", "name": "Board Member", "key": "board_member", "ordinal": 3}
]

SAMPLE_MEMBERSHIP_LEVELS = [
    {"id": 1, "name": "General", "ordinal": 1},
    {"id": 2, "name": "Premium", "ordinal": 2},
    {"id": 3, "name": "VIP", "ordinal": 3}
]

SAMPLE_KEYWORDS = [
    {"id": 1, "name": "Newsletter", "category": "Communication"},
    {"id": 2, "name": "Email", "category": "Communication"},
    {"id": 3, "name": "Direct Mail", "category": "Communication"}
]

SAMPLE_NOTES = [
    {
        "id": 1,
        "constituent_id": 1,
        "note_type": "General",
        "text": "Test note content",
        "created_at": "2025-01-01T10:00:00Z",
        "updated_at": "2025-01-01T10:00:00Z"
    }
]

SAMPLE_APPEALS = [
    {
        "id": 1,
        "name": "Annual Appeal 2025",
        "description": "Annual fundraising appeal",
        "goal": 10000.00,
        "start_date": "2025-01-01",
        "end_date": "2025-12-31",
        "created_at": "2025-01-01T10:00:00Z",
        "updated_at": "2025-01-01T10:00:00Z"
    }
]

SAMPLE_CAMPAIGNS = [
    {
        "id": 1,
        "name": "Capital Campaign",
        "description": "Building fund campaign",
        "goal": 100000.00,
        "start_date": "2025-01-01",
        "end_date": "2025-12-31",
        "created_at": "2025-01-01T10:00:00Z",
        "updated_at": "2025-01-01T10:00:00Z"
    }
]

SAMPLE_EVENTS = [
    {
        "id": 1,
        "name": "Annual Gala",
        "description": "Annual fundraising gala",
        "event_date": "2025-06-15",
        "location": "Grand Ballroom",
        "created_at": "2025-01-01T10:00:00Z",
        "updated_at": "2025-01-01T10:00:00Z"
    }
]

SAMPLE_FUNDS = [
    {
        "id": 1,
        "name": "General Fund",
        "description": "General operating fund",
        "created_at": "2025-01-01T10:00:00Z",
        "updated_at": "2025-01-01T10:00:00Z"
    }
]

SAMPLE_MEMBERSHIPS = [
    {
        "id": 1,
        "constituent_id": 1,
        "membership_level_id": 1,
        "membership_level_name": "General",
        "created_at": "2025-01-01T10:00:00Z",
        "updated_at": "2025-01-01T10:00:00Z"
    }
]

SAMPLE_RELATIONSHIP_TYPES = [
    {
        "id": 1,
        "name": "Parent",
        "short_code": "P",
        "type_code": "parent",
        "ordinal": 1
    }
]

SAMPLE_TEAM_MEMBERS = [
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Admin",
        "email": "admin@example.com",
        "role_id": 1,
        "is_admin": True,
        "is_primary_contact": True,
        "is_billing_contact": False
    }
]

# Resource-specific mock response generators
RESOURCE_SAMPLES = {
    "payment_types": SAMPLE_PAYMENT_TYPES,
    "constituents": SAMPLE_CONSTITUENTS,
    "gifts": SAMPLE_GIFTS,
    "categories": SAMPLE_CATEGORIES,
    "membership_levels": SAMPLE_MEMBERSHIP_LEVELS,
    "keywords": SAMPLE_KEYWORDS,
    "notes": SAMPLE_NOTES,
    "appeals": SAMPLE_APPEALS,
    "campaigns": SAMPLE_CAMPAIGNS,
    "events": SAMPLE_EVENTS,
    "funds": SAMPLE_FUNDS,
    "memberships": SAMPLE_MEMBERSHIPS,
    "relationship_types": SAMPLE_RELATIONSHIP_TYPES,
    "team_members": SAMPLE_TEAM_MEMBERS
}

# Resources that use direct array format (not paginated)
DIRECT_ARRAY_RESOURCES = {
    "payment_types",
    "membership_levels",
    "class_affiliation_types",
    "relationship_types",
    "team_members",
    "types"
}


def get_mock_response(resource_name: str, count: int = 2) -> Dict[str, Any]:
    """Get a mock response for a specific resource."""
    if resource_name in RESOURCE_SAMPLES:
        items = RESOURCE_SAMPLES[resource_name][:count]
    else:
        # Generate generic items for resources without specific samples
        items = [
            {"id": i, "name": f"Sample {resource_name.title()} {i}"}
            for i in range(1, count + 1)
        ]
    
    if resource_name in DIRECT_ARRAY_RESOURCES:
        return APIResponseMocker.direct_array_response(items)
    else:
        return APIResponseMocker.paginated_response(items, len(items))


def get_pagination_test_data(resource_name: str) -> List[Dict[str, Any]]:
    """Get test data for pagination testing."""
    base_items = []
    for i in range(1, 26):  # 25 items for pagination testing
        if resource_name in RESOURCE_SAMPLES:
            # Use the first sample as a template
            sample = RESOURCE_SAMPLES[resource_name][0].copy()
            sample["id"] = i
            if "name" in sample:
                sample["name"] = f"{sample['name']} {i}"
            base_items.append(sample)
        else:
            base_items.append({
                "id": i,
                "name": f"Sample {resource_name.title()} {i}"
            })
    
    return base_items