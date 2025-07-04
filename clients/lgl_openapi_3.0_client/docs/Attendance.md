# Attendance

An Attendance object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Attendance Id | [optional] 
**var_date** | **date** |  | 
**notes** | **str** | Attendance notes | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.attendance import Attendance

# TODO update the JSON string below
json = "{}"
# create an instance of Attendance from a JSON string
attendance_instance = Attendance.from_json(json)
# print the JSON string representation of the object
print(Attendance.to_json())

# convert the object into a dict
attendance_dict = attendance_instance.to_dict()
# create an instance of Attendance from a dict
attendance_from_dict = Attendance.from_dict(attendance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


