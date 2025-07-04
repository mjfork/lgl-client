# EventAggregatedResponse

A Event object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**var_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**financial_goal** | **float** |  | [optional] 
**projected_amount** | **float** |  | [optional] 
**code** | **str** | Code | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.event_aggregated_response import EventAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventAggregatedResponse from a JSON string
event_aggregated_response_instance = EventAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(EventAggregatedResponse.to_json())

# convert the object into a dict
event_aggregated_response_dict = event_aggregated_response_instance.to_dict()
# create an instance of EventAggregatedResponse from a dict
event_aggregated_response_from_dict = EventAggregatedResponse.from_dict(event_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


