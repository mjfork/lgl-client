# EventUpdate

A Event object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**var_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**financial_goal** | **float** |  | [optional] 
**projected_amount** | **float** |  | [optional] 
**code** | **str** | Code | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.event_update import EventUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EventUpdate from a JSON string
event_update_instance = EventUpdate.from_json(json)
# print the JSON string representation of the object
print(EventUpdate.to_json())

# convert the object into a dict
event_update_dict = event_update_instance.to_dict()
# create an instance of EventUpdate from a dict
event_update_from_dict = EventUpdate.from_dict(event_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


