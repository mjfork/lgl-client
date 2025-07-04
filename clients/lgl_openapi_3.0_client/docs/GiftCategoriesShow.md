# GiftCategoriesShow

gift_category object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | Gift category ID | 
**display_name** | **str** | Display mame | 
**gift_type_id** | **int** | Gift type ID | 
**gift_type_name** | **str** | Gift type name | 

## Example

```python
from lgl_openapi_3_0_client.models.gift_categories_show import GiftCategoriesShow

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCategoriesShow from a JSON string
gift_categories_show_instance = GiftCategoriesShow.from_json(json)
# print the JSON string representation of the object
print(GiftCategoriesShow.to_json())

# convert the object into a dict
gift_categories_show_dict = gift_categories_show_instance.to_dict()
# create an instance of GiftCategoriesShow from a dict
gift_categories_show_from_dict = GiftCategoriesShow.from_dict(gift_categories_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


