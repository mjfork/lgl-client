# VolunteerTime

A VolunteerTime object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constituent_id** | **int** | Constituent ID | 
**external_id** | **int** | External Volunteering ID | [optional] 
**volunteering_category_id** | **int** | Volunteer Category Id | 
**volunteering_category_name** | **str** | Volunteer Category Name | [optional] 
**description** | **str** | Description | [optional] 
**hours** | **float** |  | [optional] 
**var_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**completed_hours** | **float** |  | [optional] 
**custom_fields** | [**List[CustomFieldAggregatedUpdate]**](CustomFieldAggregatedUpdate.md) | VolunteerTime custom fields (Categories) | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.volunteer_time import VolunteerTime

# TODO update the JSON string below
json = "{}"
# create an instance of VolunteerTime from a JSON string
volunteer_time_instance = VolunteerTime.from_json(json)
# print the JSON string representation of the object
print(VolunteerTime.to_json())

# convert the object into a dict
volunteer_time_dict = volunteer_time_instance.to_dict()
# create an instance of VolunteerTime from a dict
volunteer_time_from_dict = VolunteerTime.from_dict(volunteer_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


