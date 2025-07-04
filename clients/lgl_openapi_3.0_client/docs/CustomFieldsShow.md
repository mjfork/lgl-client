# CustomFieldsShow

A CustomField object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | Custom Field Id | [optional] 
**item_type** | **str** | Item Type | 
**name** | **str** | Name | 
**key** | **str** | Key | [optional] 
**facet_type** | **str** | Facet Type | [optional] 
**ordinal** | **int** | Ordinal | [optional] 
**removable** | **bool** | Removable? | [optional] 
**editable** | **bool** | Editable? | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.custom_fields_show import CustomFieldsShow

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldsShow from a JSON string
custom_fields_show_instance = CustomFieldsShow.from_json(json)
# print the JSON string representation of the object
print(CustomFieldsShow.to_json())

# convert the object into a dict
custom_fields_show_dict = custom_fields_show_instance.to_dict()
# create an instance of CustomFieldsShow from a dict
custom_fields_show_from_dict = CustomFieldsShow.from_dict(custom_fields_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


