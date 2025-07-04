# Event

A Event object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**var_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**financial_goal** | **float** |  | [optional] 
**projected_amount** | **float** |  | [optional] 
**code** | **str** | Code | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


