# VolunteerTimesIndex

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
**items** | [**List[VolunteerTimeResponse]**](VolunteerTimeResponse.md) | VolunteerTimes Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.volunteer_times_index import VolunteerTimesIndex

# TODO update the JSON string below
json = "{}"
# create an instance of VolunteerTimesIndex from a JSON string
volunteer_times_index_instance = VolunteerTimesIndex.from_json(json)
# print the JSON string representation of the object
print(VolunteerTimesIndex.to_json())

# convert the object into a dict
volunteer_times_index_dict = volunteer_times_index_instance.to_dict()
# create an instance of VolunteerTimesIndex from a dict
volunteer_times_index_from_dict = VolunteerTimesIndex.from_dict(volunteer_times_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


