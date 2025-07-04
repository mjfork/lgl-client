# GroupMembershipUpdate

A GroupMembership object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**group_id** | **int** | Group Id | 
**group_name** | **str** | Group Name | [optional] 
**date_start** | **date** |  | [optional] 
**date_end** | **date** |  | [optional] 
**is_current** | **bool** | Current? | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.group_membership_update import GroupMembershipUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMembershipUpdate from a JSON string
group_membership_update_instance = GroupMembershipUpdate.from_json(json)
# print the JSON string representation of the object
print(GroupMembershipUpdate.to_json())

# convert the object into a dict
group_membership_update_dict = group_membership_update_instance.to_dict()
# create an instance of GroupMembershipUpdate from a dict
group_membership_update_from_dict = GroupMembershipUpdate.from_dict(group_membership_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


