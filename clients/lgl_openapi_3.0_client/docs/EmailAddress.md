# EmailAddress

A EmailAddress object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Email Address | [optional] 
**email_address_type_id** | **int** | Email Address Type ID | [optional] 
**email_type_name** | **str** | Email Address Type Name | [optional] 
**is_preferred** | **bool** | Make this the preferred email address | [optional] 
**not_current** | **bool** | No longer a current email address | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.email_address import EmailAddress

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAddress from a JSON string
email_address_instance = EmailAddress.from_json(json)
# print the JSON string representation of the object
print(EmailAddress.to_json())

# convert the object into a dict
email_address_dict = email_address_instance.to_dict()
# create an instance of EmailAddress from a dict
email_address_from_dict = EmailAddress.from_dict(email_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


