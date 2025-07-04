# CategoriesShow

A Cagetory object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
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
from lgl_openapi_3_0_client.models.categories_show import CategoriesShow

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesShow from a JSON string
categories_show_instance = CategoriesShow.from_json(json)
# print the JSON string representation of the object
print(CategoriesShow.to_json())

# convert the object into a dict
categories_show_dict = categories_show_instance.to_dict()
# create an instance of CategoriesShow from a dict
categories_show_from_dict = CategoriesShow.from_dict(categories_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


