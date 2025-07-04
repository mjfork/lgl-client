# GiftTypeUpdate

A GiftType object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.gift_type_update import GiftTypeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GiftTypeUpdate from a JSON string
gift_type_update_instance = GiftTypeUpdate.from_json(json)
# print the JSON string representation of the object
print(GiftTypeUpdate.to_json())

# convert the object into a dict
gift_type_update_dict = gift_type_update_instance.to_dict()
# create an instance of GiftTypeUpdate from a dict
gift_type_update_from_dict = GiftTypeUpdate.from_dict(gift_type_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


