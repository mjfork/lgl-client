# GiftTypesShow

gift_type object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | ID | 

## Example

```python
from lgl_openapi_3_0_client.models.gift_types_show import GiftTypesShow

# TODO update the JSON string below
json = "{}"
# create an instance of GiftTypesShow from a JSON string
gift_types_show_instance = GiftTypesShow.from_json(json)
# print the JSON string representation of the object
print(GiftTypesShow.to_json())

# convert the object into a dict
gift_types_show_dict = gift_types_show_instance.to_dict()
# create an instance of GiftTypesShow from a dict
gift_types_show_from_dict = GiftTypesShow.from_dict(gift_types_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


