# GiftCategoryResponse

A GiftCategory object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Gift category ID | 
**display_name** | **str** | Display mame | 
**gift_type_id** | **int** | Gift type ID | 
**gift_type_name** | **str** | Gift type name | 

## Example

```python
from lgl_openapi_3_0_client.models.gift_category_response import GiftCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCategoryResponse from a JSON string
gift_category_response_instance = GiftCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(GiftCategoryResponse.to_json())

# convert the object into a dict
gift_category_response_dict = gift_category_response_instance.to_dict()
# create an instance of GiftCategoryResponse from a dict
gift_category_response_from_dict = GiftCategoryResponse.from_dict(gift_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


