# CustomAttrIndex

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
**items** | [**List[CustomField]**](CustomField.md) | CustomFields | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.custom_attr_index import CustomAttrIndex

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttrIndex from a JSON string
custom_attr_index_instance = CustomAttrIndex.from_json(json)
# print the JSON string representation of the object
print(CustomAttrIndex.to_json())

# convert the object into a dict
custom_attr_index_dict = custom_attr_index_instance.to_dict()
# create an instance of CustomAttrIndex from a dict
custom_attr_index_from_dict = CustomAttrIndex.from_dict(custom_attr_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


