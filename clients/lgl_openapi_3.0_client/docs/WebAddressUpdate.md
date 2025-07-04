# WebAddressUpdate

A WebAddress object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**url** | **str** | Web Address | [optional] 
**web_address_type_id** | **int** | Web Address Type ID | [optional] 
**web_address_type_name** | **str** | Web Address Type Name | [optional] 
**is_preferred** | **bool** | Make this the preferred email address | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.web_address_update import WebAddressUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WebAddressUpdate from a JSON string
web_address_update_instance = WebAddressUpdate.from_json(json)
# print the JSON string representation of the object
print(WebAddressUpdate.to_json())

# convert the object into a dict
web_address_update_dict = web_address_update_instance.to_dict()
# create an instance of WebAddressUpdate from a dict
web_address_update_from_dict = WebAddressUpdate.from_dict(web_address_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


