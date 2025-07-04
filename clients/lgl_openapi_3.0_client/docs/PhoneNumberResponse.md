# PhoneNumberResponse

A PhoneNumber object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Phone Number Id | 
**item_id** | **int** | Owner Id | 
**item_type** | **str** | Owner Type | 
**number** | **str** | Phone Number | [optional] 
**phone_number_type_id** | **int** | Phone Number Type Id | [optional] 
**phone_type_name** | **str** | Phone Number Type Name | [optional] 
**is_preferred** | **bool** | Make this the preferred phone number | [optional] 
**not_current** | **bool** | No longer a current phone number | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.phone_number_response import PhoneNumberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumberResponse from a JSON string
phone_number_response_instance = PhoneNumberResponse.from_json(json)
# print the JSON string representation of the object
print(PhoneNumberResponse.to_json())

# convert the object into a dict
phone_number_response_dict = phone_number_response_instance.to_dict()
# create an instance of PhoneNumberResponse from a dict
phone_number_response_from_dict = PhoneNumberResponse.from_dict(phone_number_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


