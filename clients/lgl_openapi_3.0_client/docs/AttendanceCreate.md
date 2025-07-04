# AttendanceCreate

An Attendance object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**notes** | **str** | Attendance notes | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.attendance_create import AttendanceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceCreate from a JSON string
attendance_create_instance = AttendanceCreate.from_json(json)
# print the JSON string representation of the object
print(AttendanceCreate.to_json())

# convert the object into a dict
attendance_create_dict = attendance_create_instance.to_dict()
# create an instance of AttendanceCreate from a dict
attendance_create_from_dict = AttendanceCreate.from_dict(attendance_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


