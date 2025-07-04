# CustomAttrCreate

A CustomField object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Custom Field Id | [optional] 
**key** | **str** | Key | [optional] 
**value** | **str** | Value | 

## Example

```python
from lgl_openapi_3_0_client.models.custom_attr_create import CustomAttrCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttrCreate from a JSON string
custom_attr_create_instance = CustomAttrCreate.from_json(json)
# print the JSON string representation of the object
print(CustomAttrCreate.to_json())

# convert the object into a dict
custom_attr_create_dict = custom_attr_create_instance.to_dict()
# create an instance of CustomAttrCreate from a dict
custom_attr_create_from_dict = CustomAttrCreate.from_dict(custom_attr_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


