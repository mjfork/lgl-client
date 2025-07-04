# AttributesIndex

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
**items** | [**List[AttributeResponse]**](AttributeResponse.md) | Attributes Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.attributes_index import AttributesIndex

# TODO update the JSON string below
json = "{}"
# create an instance of AttributesIndex from a JSON string
attributes_index_instance = AttributesIndex.from_json(json)
# print the JSON string representation of the object
print(AttributesIndex.to_json())

# convert the object into a dict
attributes_index_dict = attributes_index_instance.to_dict()
# create an instance of AttributesIndex from a dict
attributes_index_from_dict = AttributesIndex.from_dict(attributes_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


