# GiftCategory

A GiftCategory object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display mame | 
**gift_type_id** | **int** | Gift type ID | 
**gift_type_name** | **str** | Gift type name | 

## Example

```python
from lgl_openapi_3_0_client.models.gift_category import GiftCategory

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCategory from a JSON string
gift_category_instance = GiftCategory.from_json(json)
# print the JSON string representation of the object
print(GiftCategory.to_json())

# convert the object into a dict
gift_category_dict = gift_category_instance.to_dict()
# create an instance of GiftCategory from a dict
gift_category_from_dict = GiftCategory.from_dict(gift_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


