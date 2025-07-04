# GiftCategoriesIndex

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
**items** | [**List[GiftCategoryResponse]**](GiftCategoryResponse.md) | GiftCategories Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.gift_categories_index import GiftCategoriesIndex

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCategoriesIndex from a JSON string
gift_categories_index_instance = GiftCategoriesIndex.from_json(json)
# print the JSON string representation of the object
print(GiftCategoriesIndex.to_json())

# convert the object into a dict
gift_categories_index_dict = gift_categories_index_instance.to_dict()
# create an instance of GiftCategoriesIndex from a dict
gift_categories_index_from_dict = GiftCategoriesIndex.from_dict(gift_categories_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


