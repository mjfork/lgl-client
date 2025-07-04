# EventsShow

event object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
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
from lgl_openapi_3_0_client.models.events_show import EventsShow

# TODO update the JSON string below
json = "{}"
# create an instance of EventsShow from a JSON string
events_show_instance = EventsShow.from_json(json)
# print the JSON string representation of the object
print(EventsShow.to_json())

# convert the object into a dict
events_show_dict = events_show_instance.to_dict()
# create an instance of EventsShow from a dict
events_show_from_dict = EventsShow.from_dict(events_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


