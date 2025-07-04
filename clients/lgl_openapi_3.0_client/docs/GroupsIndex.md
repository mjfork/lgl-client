# GroupsIndex

Index

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**items_count** | **int** | Items returned | 
**total_items** | **int** | Total items available | 
**limit** | **int** | Item return limit | 
**offset** | **int** | Start item | 
**next_item** | **int** | Next item in list | 
**next_link** | **str** | Link to next page of items | 
**item_type** | **str** | Type of items | 
**items** | [**List[GroupResponse]**](GroupResponse.md) | Groups Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.groups_index import GroupsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsIndex from a JSON string
groups_index_instance = GroupsIndex.from_json(json)
# print the JSON string representation of the object
print(GroupsIndex.to_json())

# convert the object into a dict
groups_index_dict = groups_index_instance.to_dict()
# create an instance of GroupsIndex from a dict
groups_index_from_dict = GroupsIndex.from_dict(groups_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


