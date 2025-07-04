# TeamMembersShow

team_member object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | ID | 
**first_name** | **str** | First Name | 
**last_name** | **str** | Last Name | 
**email** | **str** | Email | 
**role_id** | **int** | Role Id | 
**is_primary_contact** | **bool** | Is Primary Contact? | 
**is_billing_contact** | **bool** | Is Billing Contact? | 

## Example

```python
from lgl_openapi_3_0_client.models.team_members_show import TeamMembersShow

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMembersShow from a JSON string
team_members_show_instance = TeamMembersShow.from_json(json)
# print the JSON string representation of the object
print(TeamMembersShow.to_json())

# convert the object into a dict
team_members_show_dict = team_members_show_instance.to_dict()
# create an instance of TeamMembersShow from a dict
team_members_show_from_dict = TeamMembersShow.from_dict(team_members_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


