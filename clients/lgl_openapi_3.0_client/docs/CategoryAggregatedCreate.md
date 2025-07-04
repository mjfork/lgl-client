# CategoryAggregatedCreate

A CustomField object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Category Id | [optional] 
**name** | **str** | Name | 
**key** | **str** | Key | [optional] 
**keywords** | [**List[KeywordAggregatedUpdate]**](KeywordAggregatedUpdate.md) | Keyword Values | 

## Example

```python
from lgl_openapi_3_0_client.models.category_aggregated_create import CategoryAggregatedCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAggregatedCreate from a JSON string
category_aggregated_create_instance = CategoryAggregatedCreate.from_json(json)
# print the JSON string representation of the object
print(CategoryAggregatedCreate.to_json())

# convert the object into a dict
category_aggregated_create_dict = category_aggregated_create_instance.to_dict()
# create an instance of CategoryAggregatedCreate from a dict
category_aggregated_create_from_dict = CategoryAggregatedCreate.from_dict(category_aggregated_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


