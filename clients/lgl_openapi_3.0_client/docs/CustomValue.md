# CustomValue

A CustomValue object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **int** | Category Id | 
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**short_code** | **str** | Short Code | [optional] 
**ordinal** | **int** | Ordinal | [optional] 
**removable** | **bool** | Removable? | [optional] 
**can_change** | **bool** | Can Change? | [optional] 
**can_select** | **bool** | Can Select? | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.custom_value import CustomValue

# TODO update the JSON string below
json = "{}"
# create an instance of CustomValue from a JSON string
custom_value_instance = CustomValue.from_json(json)
# print the JSON string representation of the object
print(CustomValue.to_json())

# convert the object into a dict
custom_value_dict = custom_value_instance.to_dict()
# create an instance of CustomValue from a dict
custom_value_from_dict = CustomValue.from_dict(custom_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


