# LGL API Dependencies Analysis

This document maps all LGL API resources and their dependencies to determine the correct implementation order.

## Resource Dependency Map

### Level 0: Independent Resources (No Dependencies)
These resources have no foreign key dependencies and can be implemented first:

1. **Categories** → `/api/v1/categories`
   - Parameters: `item_type`, `limit`, `offset`
   - Response fields: `id`, `item_type`, `name`, `key`, `facet_type`, `ordinal`, `removable`, `editable`, `display_format`, `keywords[]`

2. **Appeals** → `/api/v1/appeals`
   - Parameters: `limit`, `offset`
   - Response fields: `id`, `name`, `description`, `date`, `financial_goal`, `projected_amount`, `code`

3. **Campaigns** → `/api/v1/campaigns`
   - Parameters: `limit`, `offset`
   - Response fields: `id`, `name`, `description`, `financial_goal`, `start_date`, `end_date`, `code`

4. **Events** → `/api/v1/events`
   - Parameters: `limit`, `offset`
   - Response fields: `id`, `name`, `description`, `date`, `end_date`, `financial_goal`, `projected_amount`, `code`

5. **Funds** → `/api/v1/funds`
   - Parameters: `limit`, `offset`
   - Response fields: `id`, `name`, `description`, `code`, `start_date`, `end_date`, `financial_goal`

6. **Groups** → `/api/v1/groups`
   - Parameters: `limit`, `offset`
   - Response fields: `id`, `name`, `key`, `ordinal`

7. **Gift Types** → `/api/v1/gift_types`
   - Parameters: `limit`, `offset`
   - Response fields: `id`, `name`, `ordinal`

8. **Gift Categories** → `/api/v1/gift_categories`
   - Parameters: `limit`, `offset`
   - Response fields: `id`, `name`, `ordinal`

9. **Payment Types** → `/api/v1/payment_types`
   - Parameters: `limit`, `offset`
   - Response fields: `id`, `name`, `key`, `ordinal`

10. **Membership Levels** → `/api/v1/membership_levels`
    - Parameters: `limit`, `offset`
    - Response fields: `id`, `name`, `ordinal`

11. **Relationship Types** → `/api/v1/relationship_types`
    - Parameters: `limit`, `offset`
    - Response fields: `id`, `name`, `ordinal`

12. **Class Affiliation Types** → `/api/v1/class_affiliation_types`
    - Parameters: `limit`, `offset`
    - Response fields: `id`, `name`, `ordinal`

13. **Team Members** → `/api/v1/team_members`
    - Parameters: `limit`, `offset`
    - Response fields: `id`, `first_name`, `last_name`, `email`, `admin`

14. **Keywords** → `/api/v1/keywords`
    - Parameters: `limit`, `offset`
    - Response fields: `id`, `category_id`, `name`, `description`, `short_code`, `ordinal`

15. **Types** → `/api/v1/types`
    - Parameters: `limit`, `offset`
    - Response fields: `id`, `name`, `ordinal`

16. **Mailing Templates** → `/api/v1/mailing_templates`
    - Parameters: `limit`, `offset`
    - Response fields: `id`, `name`, `template_type`

17. **Custom Attributes** (Type definitions) → `/api/v1/custom_attributes`
    - Parameters: `limit`, `offset`
    - Response fields: `id`, `name`, `key`, `field_type`

18. **Invitations** (Template level) → `/api/v1/invitations`
    - Parameters: `limit`, `offset`
    - Response fields: `id`, `name`, `event_id`, `template`

### Level 1: Core Entity
This is the fundamental entity that most other resources depend on:

19. **Constituents** → `/api/v1/constituents` & `/api/v1/constituents/search`
    - Parameters: `q[]`, `expand`, `sort`, `limit`, `offset`
    - Response fields: `id`, `first_name`, `last_name`, `email`, `external_id`, `lgl_id`, `date_created`, `date_updated`
    - Dependencies: Can reference Categories for custom fields

### Level 2: Single Dependencies
Resources that depend primarily on Constituents:

20. **Email Addresses** → `/api/v1/constituents/{constituent_id}/email_addresses`
    - Dependencies: Constituents
    - Response fields: `id`, `item_id`, `item_type`, `address`, `email_address_type_id`, `email_type_name`, `is_preferred`, `not_current`

21. **Phone Numbers** → `/api/v1/constituents/{constituent_id}/phone_numbers`
    - Dependencies: Constituents
    - Response fields: `id`, `item_id`, `item_type`, `number`, `phone_number_type_id`, `phone_type_name`, `is_preferred`, `not_current`, `normalized_number`

22. **Street Addresses** → `/api/v1/constituents/{constituent_id}/street_addresses`
    - Dependencies: Constituents
    - Response fields: `id`, `item_id`, `item_type`, `street`, `city`, `state`, `country`, `postal_code`, `county`, `street_address_type_id`, `street_type_name`, `is_preferred`, `not_current`, `seasonal_from`, `seasonal_to`, `seasonal`, `lat`, `lng`, `zip5`, `verified`, `verified_on`

23. **Web Addresses** → `/api/v1/constituents/{constituent_id}/web_addresses`
    - Dependencies: Constituents
    - Response fields: `id`, `item_id`, `item_type`, `url`, `web_address_type_id`, `web_type_name`, `is_preferred`, `not_current`

24. **Notes** → `/api/v1/constituents/{constituent_id}/notes`
    - Dependencies: Constituents
    - Response fields: `id`, `constituent_id`, `note`, `created_at`, `updated_at`

25. **Volunteer Time** → `/api/v1/constituents/{constituent_id}/volunteer_time`
    - Dependencies: Constituents + Events
    - Response fields: `id`, `constituent_id`, `event_id`, `event_name`, `hours`, `date`, `note`

### Level 3: Multiple Dependencies
Resources that depend on Constituents plus other Level 0 resources:

26. **Memberships** → `/api/v1/constituents/{constituent_id}/memberships`
    - Dependencies: Constituents + Membership Levels
    - Response fields: `id`, `constituent_id`, `membership_level_id`, `membership_level_name`, `date_start`, `finish_date`, `note`

27. **Group Memberships** → `/api/v1/constituents/{constituent_id}/group_memberships`
    - Dependencies: Constituents + Groups
    - Response fields: `id`, `constituent_id`, `group_id`, `group_name`, `date_start`, `date_end`, `is_current`

28. **Class Affiliations** → `/api/v1/constituents/{constituent_id}/class_affiliations`
    - Dependencies: Constituents + Class Affiliation Types
    - Response fields: `id`, `constituent_id`, `class_affiliation_type_id`, `class_affiliation_type_name`, `date_start`, `date_end`

29. **Appeal Requests** → `/api/v1/appeal_requests` & `/api/v1/appeals/{appeal_id}/appeal_requests` & `/api/v1/constituents/{constituent_id}/appeal_requests`
    - Dependencies: Constituents + Appeals
    - Response fields: `id`, `constituent_id`, `constituent_name`, `appeal_id`, `name`, `raised`, `status`, `ask_amount`, `assigned_to`, `custom_fields`, `custom_attrs`

### Level 4: Complex Dependencies
Resources with the most complex dependency relationships:

30. **Gifts** → `/api/v1/constituents/{constituent_id}/gifts`
    - Dependencies: Constituents + Multiple Optional (Gift Types, Gift Categories, Payment Types, Campaigns, Funds, Appeals, Events, Team Members)
    - Response fields: `id`, `constituent_id`, `gift_type_id`, `gift_type_name`, `gift_category_id`, `gift_category_name`, `campaign_id`, `campaign_name`, `fund_id`, `fund_name`, `appeal_id`, `appeal_name`, `event_id`, `event_name`, `amount`, `date`, `payment_type_id`, `payment_type_name`, `check_number`, `deductible_amount`, `note`, `team_member`

31. **Constituent Relationships** → `/api/v1/constituents/{constituent_id}/relationships`
    - Dependencies: 2 Constituents + Relationship Types
    - Response fields: `id`, `constituent_id`, `related_constituent_id`, `relationship_type_id`, `relationship_type_name`, `is_reciprocal`

## Implementation Order Summary

1. **Phase 1**: Implement all Level 0 resources (1-18)
2. **Phase 2**: Implement Constituents (19)
3. **Phase 3**: Implement Level 2 resources (20-25)
4. **Phase 4**: Implement Level 3 resources (26-29)
5. **Phase 5**: Implement Level 4 resources (30-31)

## Endpoint Patterns

### Standard List Endpoints
- `/api/v1/{resource}` - List all resources
- Standard parameters: `limit`, `offset`

### Constituent-Scoped Endpoints
- `/api/v1/constituents/{constituent_id}/{resource}` - List resources for a constituent
- Standard parameters: `limit`, `offset`

### Individual Resource Endpoints
- `/api/v1/{resource}/{id}` - Get individual resource
- `/api/v1/{resource}` (POST) - Create resource
- `/api/v1/{resource}/{id}` (PATCH) - Update resource
- `/api/v1/{resource}/{id}` (DELETE) - Delete resource

## Testing Strategy

### GET Method Testing Commands
For each resource, use the appropriate GET command:

**Level 0 Resources:**
```python
# Categories
python -c "import os; from src.lgl_client.lgl_api import new_client; client = new_client(os.environ['LGL_API_KEY']); print(client.categories.list())"

# Appeals
python -c "import os; from src.lgl_client.lgl_api import new_client; client = new_client(os.environ['LGL_API_KEY']); print(client.appeals.list())"
```

**Constituent-dependent Resources:**
```python
# Email Addresses (requires constituent_id)
python -c "import os; from src.lgl_client.lgl_api import new_client; client = new_client(os.environ['LGL_API_KEY']); constituents = client.constituents.list(limit=1); print(client.email_addresses.list(constituents[0].id) if constituents else 'No constituents found')"
```

## Error Handling Strategy

**Reasonable Defaults:**
- Return empty list if no data found
- Handle authentication errors gracefully (401)
- Handle permission errors gracefully (403)
- Handle not found errors gracefully (404)
- Validate required parameters before making requests
- Provide meaningful error messages with context

This analysis ensures proper implementation order and comprehensive API coverage.