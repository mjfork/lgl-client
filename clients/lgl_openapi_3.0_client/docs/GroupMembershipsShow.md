# GroupMembershipsShow

group_membership object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | Group ID | 
**constituent_id** | **int** | Constituent Id | 
**group_id** | **int** | Group Id | 
**group_name** | **str** | Group Name | [optional] 
**date_start** | **date** |  | [optional] 
**date_end** | **date** |  | [optional] 
**is_current** | **bool** | Current? | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.group_memberships_show import GroupMembershipsShow

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMembershipsShow from a JSON string
group_memberships_show_instance = GroupMembershipsShow.from_json(json)
# print the JSON string representation of the object
print(GroupMembershipsShow.to_json())

# convert the object into a dict
group_memberships_show_dict = group_memberships_show_instance.to_dict()
# create an instance of GroupMembershipsShow from a dict
group_memberships_show_from_dict = GroupMembershipsShow.from_dict(group_memberships_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


