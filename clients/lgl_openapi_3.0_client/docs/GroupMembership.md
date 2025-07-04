# GroupMembership

A GroupMembership object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** | Group Id | 
**group_name** | **str** | Group Name | [optional] 
**date_start** | **date** |  | [optional] 
**date_end** | **date** |  | [optional] 
**is_current** | **bool** | Current? | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.group_membership import GroupMembership

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMembership from a JSON string
group_membership_instance = GroupMembership.from_json(json)
# print the JSON string representation of the object
print(GroupMembership.to_json())

# convert the object into a dict
group_membership_dict = group_membership_instance.to_dict()
# create an instance of GroupMembership from a dict
group_membership_from_dict = GroupMembership.from_dict(group_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


