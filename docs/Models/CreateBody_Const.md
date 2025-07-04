# CreateBody_Const
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **event\_id** | **Integer** | Event Id | [default to null] |
| **parent\_invitation\_id** | **Integer** | Parent Invitation Id (for additional guests) | [optional] [default to null] |
| **notes** | **String** | Notes | [optional] [default to null] |
| **rsvp** | **Integer** | RSVP (1-Yes, 2-No, 3-Maybe, 4-Unknown) | [optional] [default to null] |
| **attended** | **Integer** | Attended | [optional] [default to null] |
| **assigned\_to** | **Integer** | Assigned to | [optional] [default to null] |
| **attendee\_names** | **String** | Attendees Names | [optional] [default to null] |
| **guest\_first\_name** | **String** | Additional Guest First Name | [optional] [default to null] |
| **guest\_last\_name** | **String** | Additional Guest Last Name | [optional] [default to null] |
| **is\_a\_guest** | **Boolean** | Creating an additional guest record | [optional] [default to null] |
| **attendances** | [**List**](Attendance_create.md) | Multiple attendances | [optional] [default to null] |
| **custom\_fields** | [**List**](CustomFieldAggregatedUpdate.md) | Invitation custom fields (Categories) | [optional] [default to null] |
| **custom\_attrs** | [**List**](CustomAttr_create.md) | Invitation custom attributes | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

