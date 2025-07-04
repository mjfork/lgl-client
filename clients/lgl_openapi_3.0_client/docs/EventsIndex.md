# EventsIndex

Index

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**items_count** | **int** | Items returned | 
**total_items** | **int** | Total items available | 
**limit** | **int** | Item return limit | 
**offset** | **int** | Start item | 
**next_item** | **int** | Next item in list | 
**next_link** | **str** | Link to next page of items | 
**item_type** | **str** | Type of items | 
**items** | [**List[EventResponse]**](EventResponse.md) | Events Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.events_index import EventsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of EventsIndex from a JSON string
events_index_instance = EventsIndex.from_json(json)
# print the JSON string representation of the object
print(EventsIndex.to_json())

# convert the object into a dict
events_index_dict = events_index_instance.to_dict()
# create an instance of EventsIndex from a dict
events_index_from_dict = EventsIndex.from_dict(events_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


