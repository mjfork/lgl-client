# KeywordAggregatedUpdate

A Keyword object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Keyword Id | 
**name** | **str** | Name | 
**short_code** | **str** | Short Code | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.keyword_aggregated_update import KeywordAggregatedUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordAggregatedUpdate from a JSON string
keyword_aggregated_update_instance = KeywordAggregatedUpdate.from_json(json)
# print the JSON string representation of the object
print(KeywordAggregatedUpdate.to_json())

# convert the object into a dict
keyword_aggregated_update_dict = keyword_aggregated_update_instance.to_dict()
# create an instance of KeywordAggregatedUpdate from a dict
keyword_aggregated_update_from_dict = KeywordAggregatedUpdate.from_dict(keyword_aggregated_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


