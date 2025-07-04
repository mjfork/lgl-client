# GiftCategoryUpdate

A GiftCategory object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**display_name** | **str** | Display mame | 
**gift_type_id** | **int** | Gift type ID | 
**gift_type_name** | **str** | Gift type name | 

## Example

```python
from lgl_openapi_3_0_client.models.gift_category_update import GiftCategoryUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCategoryUpdate from a JSON string
gift_category_update_instance = GiftCategoryUpdate.from_json(json)
# print the JSON string representation of the object
print(GiftCategoryUpdate.to_json())

# convert the object into a dict
gift_category_update_dict = gift_category_update_instance.to_dict()
# create an instance of GiftCategoryUpdate from a dict
gift_category_update_from_dict = GiftCategoryUpdate.from_dict(gift_category_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


