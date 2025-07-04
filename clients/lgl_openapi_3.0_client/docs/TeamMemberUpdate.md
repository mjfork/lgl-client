# TeamMemberUpdate

A TeamMember object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**first_name** | **str** | First Name | 
**last_name** | **str** | Last Name | 
**email** | **str** | Email | 
**role_id** | **int** | Role Id | 
**is_primary_contact** | **bool** | Is Primary Contact? | 
**is_billing_contact** | **bool** | Is Billing Contact? | 

## Example

```python
from lgl_openapi_3_0_client.models.team_member_update import TeamMemberUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMemberUpdate from a JSON string
team_member_update_instance = TeamMemberUpdate.from_json(json)
# print the JSON string representation of the object
print(TeamMemberUpdate.to_json())

# convert the object into a dict
team_member_update_dict = team_member_update_instance.to_dict()
# create an instance of TeamMemberUpdate from a dict
team_member_update_from_dict = TeamMemberUpdate.from_dict(team_member_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


