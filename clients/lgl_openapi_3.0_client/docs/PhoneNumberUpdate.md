# PhoneNumberUpdate

A PhoneNumber object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**number** | **str** | Phone Number | [optional] 
**phone_number_type_id** | **int** | Phone Number Type Id | [optional] 
**phone_type_name** | **str** | Phone Number Type Name | [optional] 
**is_preferred** | **bool** | Make this the preferred phone number | [optional] 
**not_current** | **bool** | No longer a current phone number | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.phone_number_update import PhoneNumberUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumberUpdate from a JSON string
phone_number_update_instance = PhoneNumberUpdate.from_json(json)
# print the JSON string representation of the object
print(PhoneNumberUpdate.to_json())

# convert the object into a dict
phone_number_update_dict = phone_number_update_instance.to_dict()
# create an instance of PhoneNumberUpdate from a dict
phone_number_update_from_dict = PhoneNumberUpdate.from_dict(phone_number_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


