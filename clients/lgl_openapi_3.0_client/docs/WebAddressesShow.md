# WebAddressesShow

web_address object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | Email Address ID | 
**item_id** | **int** | Owner ID | 
**item_type** | **str** | Owner Type | 
**url** | **str** | Web Address | [optional] 
**web_address_type_id** | **int** | Web Address Type ID | [optional] 
**web_address_type_name** | **str** | Web Address Type Name | [optional] 
**is_preferred** | **bool** | Make this the preferred email address | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.web_addresses_show import WebAddressesShow

# TODO update the JSON string below
json = "{}"
# create an instance of WebAddressesShow from a JSON string
web_addresses_show_instance = WebAddressesShow.from_json(json)
# print the JSON string representation of the object
print(WebAddressesShow.to_json())

# convert the object into a dict
web_addresses_show_dict = web_addresses_show_instance.to_dict()
# create an instance of WebAddressesShow from a dict
web_addresses_show_from_dict = WebAddressesShow.from_dict(web_addresses_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


