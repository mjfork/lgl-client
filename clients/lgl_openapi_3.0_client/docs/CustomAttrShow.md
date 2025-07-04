# CustomAttrShow

A CustomField object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | Custom Field Id | [optional] 
**classification** | **str** | Classification | 
**name** | **str** | Name | 
**key** | **str** | Key | [optional] 
**ordinal** | **int** | Ordinal | [optional] 
**value** | **str** | Value | 

## Example

```python
from lgl_openapi_3_0_client.models.custom_attr_show import CustomAttrShow

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttrShow from a JSON string
custom_attr_show_instance = CustomAttrShow.from_json(json)
# print the JSON string representation of the object
print(CustomAttrShow.to_json())

# convert the object into a dict
custom_attr_show_dict = custom_attr_show_instance.to_dict()
# create an instance of CustomAttrShow from a dict
custom_attr_show_from_dict = CustomAttrShow.from_dict(custom_attr_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


