# CustomFieldsIndex

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
from lgl_openapi_3_0_client.models.custom_fields_index import CustomFieldsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldsIndex from a JSON string
custom_fields_index_instance = CustomFieldsIndex.from_json(json)
# print the JSON string representation of the object
print(CustomFieldsIndex.to_json())

# convert the object into a dict
custom_fields_index_dict = custom_fields_index_instance.to_dict()
# create an instance of CustomFieldsIndex from a dict
custom_fields_index_from_dict = CustomFieldsIndex.from_dict(custom_fields_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


