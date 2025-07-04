# VolunteerTimeResponse

A VolunteerTime object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Volunteer Time ID | 
**constituent_id** | **int** | Constituent ID | 
**external_id** | **int** | External Volunteering ID | [optional] 
**volunteering_category_id** | **int** | Volunteer Category Id | 
**volunteering_category_name** | **str** | Volunteer Category Name | [optional] 
**description** | **str** | Description | [optional] 
**hours** | **float** |  | [optional] 
**var_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**completed_hours** | **float** |  | [optional] 
**custom_fields** | [**List[CustomField]**](CustomField.md) | VolunteerTime custom fields (Categories) | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.volunteer_time_response import VolunteerTimeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VolunteerTimeResponse from a JSON string
volunteer_time_response_instance = VolunteerTimeResponse.from_json(json)
# print the JSON string representation of the object
print(VolunteerTimeResponse.to_json())

# convert the object into a dict
volunteer_time_response_dict = volunteer_time_response_instance.to_dict()
# create an instance of VolunteerTimeResponse from a dict
volunteer_time_response_from_dict = VolunteerTimeResponse.from_dict(volunteer_time_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


