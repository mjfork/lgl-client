# TeamMember

A TeamMember object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First Name | 
**last_name** | **str** | Last Name | 
**email** | **str** | Email | 
**role_id** | **int** | Role Id | 
**is_primary_contact** | **bool** | Is Primary Contact? | 
**is_billing_contact** | **bool** | Is Billing Contact? | 

## Example

```python
from lgl_openapi_3_0_client.models.team_member import TeamMember

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMember from a JSON string
team_member_instance = TeamMember.from_json(json)
# print the JSON string representation of the object
print(TeamMember.to_json())

# convert the object into a dict
team_member_dict = team_member_instance.to_dict()
# create an instance of TeamMember from a dict
team_member_from_dict = TeamMember.from_dict(team_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


