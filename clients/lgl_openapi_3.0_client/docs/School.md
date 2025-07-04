# School

A School object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_name** | **str** | School | [optional] 
**school_type_id** | **int** | School Type ID | [optional] 
**year** | **str** | Year | [optional] 
**degree** | **str** | Degree | [optional] 
**specialization** | **str** | Focus/Major | [optional] 
**add_class_year** | **bool** | Add class year affiliation? | [optional] 
**school_tie_type_id** | **int** | School Tie Type ID | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.school import School

# TODO update the JSON string below
json = "{}"
# create an instance of School from a JSON string
school_instance = School.from_json(json)
# print the JSON string representation of the object
print(School.to_json())

# convert the object into a dict
school_dict = school_instance.to_dict()
# create an instance of School from a dict
school_from_dict = School.from_dict(school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


