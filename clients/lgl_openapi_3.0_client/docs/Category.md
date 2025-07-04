# Category

A Category object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Category Id | [optional] 
**item_type** | **str** | Item Type | 
**name** | **str** | Name | 
**key** | **str** | Key | [optional] 
**facet_type** | **str** | Facet Type | [optional] 
**ordinal** | **int** | Ordinal | [optional] 
**removable** | **bool** | Removable? | [optional] 
**editable** | **bool** | Editable? | [optional] 
**display_format** | **str** | Display Format | [optional] 
**keywords** | [**List[KeywordResponse]**](KeywordResponse.md) | Keyword Values | 

## Example

```python
from lgl_openapi_3_0_client.models.category import Category

# TODO update the JSON string below
json = "{}"
# create an instance of Category from a JSON string
category_instance = Category.from_json(json)
# print the JSON string representation of the object
print(Category.to_json())

# convert the object into a dict
category_dict = category_instance.to_dict()
# create an instance of Category from a dict
category_from_dict = Category.from_dict(category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


