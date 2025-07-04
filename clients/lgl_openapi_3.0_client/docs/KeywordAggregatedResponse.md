# KeywordAggregatedResponse

A Keyword object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**category_id** | **int** | Category Id | 
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**short_code** | **str** | Short Code | [optional] 
**ordinal** | **int** | Ordinal | [optional] 
**removable** | **bool** | Removable? | [optional] 
**can_change** | **bool** | Can Change? | [optional] 
**can_select** | **bool** | Can Select? | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.keyword_aggregated_response import KeywordAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordAggregatedResponse from a JSON string
keyword_aggregated_response_instance = KeywordAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(KeywordAggregatedResponse.to_json())

# convert the object into a dict
keyword_aggregated_response_dict = keyword_aggregated_response_instance.to_dict()
# create an instance of KeywordAggregatedResponse from a dict
keyword_aggregated_response_from_dict = KeywordAggregatedResponse.from_dict(keyword_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


