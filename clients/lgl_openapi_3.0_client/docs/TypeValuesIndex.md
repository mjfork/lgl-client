# TypeValuesIndex

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
**items** | [**List[TypeValue]**](TypeValue.md) | Type Values | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.type_values_index import TypeValuesIndex

# TODO update the JSON string below
json = "{}"
# create an instance of TypeValuesIndex from a JSON string
type_values_index_instance = TypeValuesIndex.from_json(json)
# print the JSON string representation of the object
print(TypeValuesIndex.to_json())

# convert the object into a dict
type_values_index_dict = type_values_index_instance.to_dict()
# create an instance of TypeValuesIndex from a dict
type_values_index_from_dict = TypeValuesIndex.from_dict(type_values_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


