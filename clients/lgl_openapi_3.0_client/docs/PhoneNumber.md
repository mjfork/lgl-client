# PhoneNumber

A PhoneNumber object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Phone Number | [optional] 
**phone_number_type_id** | **int** | Phone Number Type Id | [optional] 
**phone_type_name** | **str** | Phone Number Type Name | [optional] 
**is_preferred** | **bool** | Make this the preferred phone number | [optional] 
**not_current** | **bool** | No longer a current phone number | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.phone_number import PhoneNumber

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumber from a JSON string
phone_number_instance = PhoneNumber.from_json(json)
# print the JSON string representation of the object
print(PhoneNumber.to_json())

# convert the object into a dict
phone_number_dict = phone_number_instance.to_dict()
# create an instance of PhoneNumber from a dict
phone_number_from_dict = PhoneNumber.from_dict(phone_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


