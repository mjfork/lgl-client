# CustomAttr

A CustomField object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Custom Field Id | [optional] 
**classification** | **str** | Classification | 
**name** | **str** | Name | 
**key** | **str** | Key | [optional] 
**ordinal** | **int** | Ordinal | [optional] 
**value** | **str** | Value | 

## Example

```python
from lgl_openapi_3_0_client.models.custom_attr import CustomAttr

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttr from a JSON string
custom_attr_instance = CustomAttr.from_json(json)
# print the JSON string representation of the object
print(CustomAttr.to_json())

# convert the object into a dict
custom_attr_dict = custom_attr_instance.to_dict()
# create an instance of CustomAttr from a dict
custom_attr_from_dict = CustomAttr.from_dict(custom_attr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


