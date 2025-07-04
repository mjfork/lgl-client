# WebAddress

A WebAddress object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Web Address | [optional] 
**web_address_type_id** | **int** | Web Address Type ID | [optional] 
**web_address_type_name** | **str** | Web Address Type Name | [optional] 
**is_preferred** | **bool** | Make this the preferred email address | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.web_address import WebAddress

# TODO update the JSON string below
json = "{}"
# create an instance of WebAddress from a JSON string
web_address_instance = WebAddress.from_json(json)
# print the JSON string representation of the object
print(WebAddress.to_json())

# convert the object into a dict
web_address_dict = web_address_instance.to_dict()
# create an instance of WebAddress from a dict
web_address_from_dict = WebAddress.from_dict(web_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


