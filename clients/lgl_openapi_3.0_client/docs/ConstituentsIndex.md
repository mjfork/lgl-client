# ConstituentsIndex

List of Constituent Objects

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
**items** | [**List[ConstituentResponseIndex]**](ConstituentResponseIndex.md) | Constituent Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.constituents_index import ConstituentsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of ConstituentsIndex from a JSON string
constituents_index_instance = ConstituentsIndex.from_json(json)
# print the JSON string representation of the object
print(ConstituentsIndex.to_json())

# convert the object into a dict
constituents_index_dict = constituents_index_instance.to_dict()
# create an instance of ConstituentsIndex from a dict
constituents_index_from_dict = ConstituentsIndex.from_dict(constituents_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


