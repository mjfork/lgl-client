# KeywordsShow

keyword object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | Keyword Id | 
**category_id** | **int** | Category Id | 
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**short_code** | **str** | Short Code | [optional] 
**ordinal** | **int** | Ordinal | [optional] 
**removable** | **bool** | Removable? | [optional] 
**can_change** | **bool** | Can Change? | [optional] 
**can_select** | **bool** | Can Select? | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.keywords_show import KeywordsShow

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsShow from a JSON string
keywords_show_instance = KeywordsShow.from_json(json)
# print the JSON string representation of the object
print(KeywordsShow.to_json())

# convert the object into a dict
keywords_show_dict = keywords_show_instance.to_dict()
# create an instance of KeywordsShow from a dict
keywords_show_from_dict = KeywordsShow.from_dict(keywords_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


