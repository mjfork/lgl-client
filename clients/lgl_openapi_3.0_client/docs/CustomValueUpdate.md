# CustomValueUpdate

A CustomValue object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
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
from lgl_openapi_3_0_client.models.custom_value_update import CustomValueUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomValueUpdate from a JSON string
custom_value_update_instance = CustomValueUpdate.from_json(json)
# print the JSON string representation of the object
print(CustomValueUpdate.to_json())

# convert the object into a dict
custom_value_update_dict = custom_value_update_instance.to_dict()
# create an instance of CustomValueUpdate from a dict
custom_value_update_from_dict = CustomValueUpdate.from_dict(custom_value_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


