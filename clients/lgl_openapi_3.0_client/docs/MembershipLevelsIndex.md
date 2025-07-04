# MembershipLevelsIndex

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
**items** | [**List[MembershipLevelResponse]**](MembershipLevelResponse.md) | MembershipLevels Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.membership_levels_index import MembershipLevelsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipLevelsIndex from a JSON string
membership_levels_index_instance = MembershipLevelsIndex.from_json(json)
# print the JSON string representation of the object
print(MembershipLevelsIndex.to_json())

# convert the object into a dict
membership_levels_index_dict = membership_levels_index_instance.to_dict()
# create an instance of MembershipLevelsIndex from a dict
membership_levels_index_from_dict = MembershipLevelsIndex.from_dict(membership_levels_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


