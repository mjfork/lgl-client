# TeamMemberAggregatedResponse

A TeamMember object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**first_name** | **str** | First Name | 
**last_name** | **str** | Last Name | 
**email** | **str** | Email | 
**role_id** | **int** | Role Id | 
**is_primary_contact** | **bool** | Is Primary Contact? | 
**is_billing_contact** | **bool** | Is Billing Contact? | 

## Example

```python
from lgl_openapi_3_0_client.models.team_member_aggregated_response import TeamMemberAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMemberAggregatedResponse from a JSON string
team_member_aggregated_response_instance = TeamMemberAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(TeamMemberAggregatedResponse.to_json())

# convert the object into a dict
team_member_aggregated_response_dict = team_member_aggregated_response_instance.to_dict()
# create an instance of TeamMemberAggregatedResponse from a dict
team_member_aggregated_response_from_dict = TeamMemberAggregatedResponse.from_dict(team_member_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


