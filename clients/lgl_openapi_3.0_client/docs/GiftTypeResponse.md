# GiftTypeResponse

A GiftType object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.gift_type_response import GiftTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GiftTypeResponse from a JSON string
gift_type_response_instance = GiftTypeResponse.from_json(json)
# print the JSON string representation of the object
print(GiftTypeResponse.to_json())

# convert the object into a dict
gift_type_response_dict = gift_type_response_instance.to_dict()
# create an instance of GiftTypeResponse from a dict
gift_type_response_from_dict = GiftTypeResponse.from_dict(gift_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


