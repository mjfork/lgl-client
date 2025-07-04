# PhoneNumbersIndex

Index

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**items_count** | **int** | Items returned | 
**total_items** | **int** | Total items available | 
**limit** | **int** | Item return limit | 
**offset** | **int** | Start item | 
**next_item** | **int** | Next item in list | 
**next_link** | **str** | Link to next page of items | 
**item_type** | **str** | Type of items | 
**items** | [**List[PhoneNumberResponse]**](PhoneNumberResponse.md) | PhoneNumbers Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.phone_numbers_index import PhoneNumbersIndex

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumbersIndex from a JSON string
phone_numbers_index_instance = PhoneNumbersIndex.from_json(json)
# print the JSON string representation of the object
print(PhoneNumbersIndex.to_json())

# convert the object into a dict
phone_numbers_index_dict = phone_numbers_index_instance.to_dict()
# create an instance of PhoneNumbersIndex from a dict
phone_numbers_index_from_dict = PhoneNumbersIndex.from_dict(phone_numbers_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


