# TypeValue

A Type value object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Keyword Id | [optional] 
**name** | **str** | Name | 
**display_name** | **str** | Display Name | [optional] 
**code** | **str** | code | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.type_value import TypeValue

# TODO update the JSON string below
json = "{}"
# create an instance of TypeValue from a JSON string
type_value_instance = TypeValue.from_json(json)
# print the JSON string representation of the object
print(TypeValue.to_json())

# convert the object into a dict
type_value_dict = type_value_instance.to_dict()
# create an instance of TypeValue from a dict
type_value_from_dict = TypeValue.from_dict(type_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


