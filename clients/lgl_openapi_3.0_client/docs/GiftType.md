# GiftType

A GiftType object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.gift_type import GiftType

# TODO update the JSON string below
json = "{}"
# create an instance of GiftType from a JSON string
gift_type_instance = GiftType.from_json(json)
# print the JSON string representation of the object
print(GiftType.to_json())

# convert the object into a dict
gift_type_dict = gift_type_instance.to_dict()
# create an instance of GiftType from a dict
gift_type_from_dict = GiftType.from_dict(gift_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


