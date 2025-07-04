# CategoryAggregatedUpdate

A CustomField object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Category Id | [optional] 
**name** | **str** | Name | 
**key** | **str** | Key | [optional] 
**remove_previous_keywords** | **bool** | Remove previous category keywords | [optional] 
**keywords** | [**List[KeywordAggregatedUpdate]**](KeywordAggregatedUpdate.md) | Keyword Values | 

## Example

```python
from lgl_openapi_3_0_client.models.category_aggregated_update import CategoryAggregatedUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAggregatedUpdate from a JSON string
category_aggregated_update_instance = CategoryAggregatedUpdate.from_json(json)
# print the JSON string representation of the object
print(CategoryAggregatedUpdate.to_json())

# convert the object into a dict
category_aggregated_update_dict = category_aggregated_update_instance.to_dict()
# create an instance of CategoryAggregatedUpdate from a dict
category_aggregated_update_from_dict = CategoryAggregatedUpdate.from_dict(category_aggregated_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


