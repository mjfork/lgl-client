# CustomField

A CustomField object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Custom Field Id | [optional] 
**item_type** | **str** | Item Type | 
**name** | **str** | Name | 
**key** | **str** | Key | [optional] 
**facet_type** | **str** | Facet Type | [optional] 
**ordinal** | **int** | Ordinal | [optional] 
**removable** | **bool** | Removable? | [optional] 
**editable** | **bool** | Editable? | [optional] 
**values** | [**List[CustomValue]**](CustomValue.md) | Values | 

## Example

```python
from lgl_openapi_3_0_client.models.custom_field import CustomField

# TODO update the JSON string below
json = "{}"
# create an instance of CustomField from a JSON string
custom_field_instance = CustomField.from_json(json)
# print the JSON string representation of the object
print(CustomField.to_json())

# convert the object into a dict
custom_field_dict = custom_field_instance.to_dict()
# create an instance of CustomField from a dict
custom_field_from_dict = CustomField.from_dict(custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


