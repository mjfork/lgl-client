# PhoneNumbersShow

phone_number object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
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
from lgl_openapi_3_0_client.models.phone_numbers_show import PhoneNumbersShow

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumbersShow from a JSON string
phone_numbers_show_instance = PhoneNumbersShow.from_json(json)
# print the JSON string representation of the object
print(PhoneNumbersShow.to_json())

# convert the object into a dict
phone_numbers_show_dict = phone_numbers_show_instance.to_dict()
# create an instance of PhoneNumbersShow from a dict
phone_numbers_show_from_dict = PhoneNumbersShow.from_dict(phone_numbers_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


