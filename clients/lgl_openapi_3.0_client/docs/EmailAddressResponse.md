# EmailAddressResponse

A EmailAddress object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from lgl_openapi_3_0_client.models.email_address_response import EmailAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAddressResponse from a JSON string
email_address_response_instance = EmailAddressResponse.from_json(json)
# print the JSON string representation of the object
print(EmailAddressResponse.to_json())

# convert the object into a dict
email_address_response_dict = email_address_response_instance.to_dict()
# create an instance of EmailAddressResponse from a dict
email_address_response_from_dict = EmailAddressResponse.from_dict(email_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


