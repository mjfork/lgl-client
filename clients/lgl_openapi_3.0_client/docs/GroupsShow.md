# GroupsShow

group object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | ID | 
**name** | **str** | Name | 
**key** | **str** | Key | [optional] 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.groups_show import GroupsShow

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsShow from a JSON string
groups_show_instance = GroupsShow.from_json(json)
# print the JSON string representation of the object
print(GroupsShow.to_json())

# convert the object into a dict
groups_show_dict = groups_show_instance.to_dict()
# create an instance of GroupsShow from a dict
groups_show_from_dict = GroupsShow.from_dict(groups_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


