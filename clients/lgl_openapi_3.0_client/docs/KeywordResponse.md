# KeywordResponse

A Keyword object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from lgl_openapi_3_0_client.models.keyword_response import KeywordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordResponse from a JSON string
keyword_response_instance = KeywordResponse.from_json(json)
# print the JSON string representation of the object
print(KeywordResponse.to_json())

# convert the object into a dict
keyword_response_dict = keyword_response_instance.to_dict()
# create an instance of KeywordResponse from a dict
keyword_response_from_dict = KeywordResponse.from_dict(keyword_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


