# InvitationsShow

An Invitation object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | Invitation Id | [optional] 
**constituent_id** | **int** | Constituent Id | 
**guest_name** | **str** | Guest Name | [optional] 
**is_a_guest** | **bool** | Creating an additional guest record | [optional] 
**parent_invitation_id** | **int** | Parent Invitation Id (for additional guests) | [optional] 
**parent_invitation_guest_name** | **str** | Parent Invitation Guest Name (for additional guests) | [optional] 
**event_id** | **int** | Event Id | 
**name** | **str** | Event Name | [optional] 
**notes** | **str** | Notes | [optional] 
**rsvp** | **int** | RSVP (1-Yes, 2-No, 3-Maybe, 4-Unknown) | [optional] 
**attended** | **int** | Attended | [optional] 
**raised** | **float** |  | [optional] 
**status** | **str** | Status | [optional] 
**donated** | **bool** | Donated | [optional] 
**assigned_to** | **int** | Assigned to | [optional] 
**additional_guests** | **int** | Number of additional guests | [optional] 
**attendees** | **int** | Attendees | [optional] 
**attendee_names** | **str** | Attendees Names | [optional] 
**attend_count** | **int** | Attend Count | [optional] 
**attendances** | [**List[Attendance]**](Attendance.md) | Multiple attendances | [optional] 
**custom_fields** | [**List[CustomField]**](CustomField.md) | Invitation custom fields (Categories) | [optional] 
**custom_attrs** | [**List[CustomAttr]**](CustomAttr.md) | Invitation custom attributes | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.invitations_show import InvitationsShow

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationsShow from a JSON string
invitations_show_instance = InvitationsShow.from_json(json)
# print the JSON string representation of the object
print(InvitationsShow.to_json())

# convert the object into a dict
invitations_show_dict = invitations_show_instance.to_dict()
# create an instance of InvitationsShow from a dict
invitations_show_from_dict = InvitationsShow.from_dict(invitations_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


