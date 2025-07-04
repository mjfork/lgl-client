# CreateBodyConst

Body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** | Event Id | 
**parent_invitation_id** | **int** | Parent Invitation Id (for additional guests) | [optional] 
**notes** | **str** | Notes | [optional] 
**rsvp** | **int** | RSVP (1-Yes, 2-No, 3-Maybe, 4-Unknown) | [optional] 
**attended** | **int** | Attended | [optional] 
**assigned_to** | **int** | Assigned to | [optional] 
**attendee_names** | **str** | Attendees Names | [optional] 
**guest_first_name** | **str** | Additional Guest First Name | [optional] 
**guest_last_name** | **str** | Additional Guest Last Name | [optional] 
**is_a_guest** | **bool** | Creating an additional guest record | [optional] 
**attendances** | [**List[AttendanceCreate]**](AttendanceCreate.md) | Multiple attendances | [optional] 
**custom_fields** | [**List[CustomFieldAggregatedUpdate]**](CustomFieldAggregatedUpdate.md) | Invitation custom fields (Categories) | [optional] 
**custom_attrs** | [**List[CustomAttrCreate]**](CustomAttrCreate.md) | Invitation custom attributes | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.create_body_const import CreateBodyConst

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBodyConst from a JSON string
create_body_const_instance = CreateBodyConst.from_json(json)
# print the JSON string representation of the object
print(CreateBodyConst.to_json())

# convert the object into a dict
create_body_const_dict = create_body_const_instance.to_dict()
# create an instance of CreateBodyConst from a dict
create_body_const_from_dict = CreateBodyConst.from_dict(create_body_const_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


