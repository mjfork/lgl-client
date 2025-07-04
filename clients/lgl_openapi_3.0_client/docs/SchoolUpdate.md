# SchoolUpdate

A School object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**school_name** | **str** | School | [optional] 
**school_type_id** | **int** | School Type ID | [optional] 
**year** | **str** | Year | [optional] 
**degree** | **str** | Degree | [optional] 
**specialization** | **str** | Focus/Major | [optional] 
**add_class_year** | **bool** | Add class year affiliation? | [optional] 
**school_tie_type_id** | **int** | School Tie Type ID | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.school_update import SchoolUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolUpdate from a JSON string
school_update_instance = SchoolUpdate.from_json(json)
# print the JSON string representation of the object
print(SchoolUpdate.to_json())

# convert the object into a dict
school_update_dict = school_update_instance.to_dict()
# create an instance of SchoolUpdate from a dict
school_update_from_dict = SchoolUpdate.from_dict(school_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


