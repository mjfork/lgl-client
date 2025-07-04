# GroupAggregatedResponse

A Group object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**name** | **str** | Name | 
**key** | **str** | Key | [optional] 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.group_aggregated_response import GroupAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAggregatedResponse from a JSON string
group_aggregated_response_instance = GroupAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(GroupAggregatedResponse.to_json())

# convert the object into a dict
group_aggregated_response_dict = group_aggregated_response_instance.to_dict()
# create an instance of GroupAggregatedResponse from a dict
group_aggregated_response_from_dict = GroupAggregatedResponse.from_dict(group_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


