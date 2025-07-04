# EmailAddressesShow

email_address object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | Email Address ID | 
**item_id** | **int** | Owner ID | 
**item_type** | **str** | Owner Type | 
**address** | **str** | Email Address | [optional] 
**email_address_type_id** | **int** | Email Address Type ID | [optional] 
**email_type_name** | **str** | Email Address Type Name | [optional] 
**is_preferred** | **bool** | Make this the preferred email address | [optional] 
**not_current** | **bool** | No longer a current email address | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.email_addresses_show import EmailAddressesShow

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAddressesShow from a JSON string
email_addresses_show_instance = EmailAddressesShow.from_json(json)
# print the JSON string representation of the object
print(EmailAddressesShow.to_json())

# convert the object into a dict
email_addresses_show_dict = email_addresses_show_instance.to_dict()
# create an instance of EmailAddressesShow from a dict
email_addresses_show_from_dict = EmailAddressesShow.from_dict(email_addresses_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


