# Invitations_show
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **api\_version** | **String** |  | [default to null] |
| **id** | **Integer** | Invitation Id | [optional] [default to null] |
| **constituent\_id** | **Integer** | Constituent Id | [default to null] |
| **guest\_name** | **String** | Guest Name | [optional] [default to null] |
| **is\_a\_guest** | **Boolean** | Creating an additional guest record | [optional] [default to null] |
| **parent\_invitation\_id** | **Integer** | Parent Invitation Id (for additional guests) | [optional] [default to null] |
| **parent\_invitation\_guest\_name** | **String** | Parent Invitation Guest Name (for additional guests) | [optional] [default to null] |
| **event\_id** | **Integer** | Event Id | [default to null] |
| **name** | **String** | Event Name | [optional] [default to null] |
| **notes** | **String** | Notes | [optional] [default to null] |
| **rsvp** | **Integer** | RSVP (1-Yes, 2-No, 3-Maybe, 4-Unknown) | [optional] [default to null] |
| **attended** | **Integer** | Attended | [optional] [default to null] |
| **raised** | **Double** |  | [optional] [default to null] |
| **status** | **String** | Status | [optional] [default to null] |
| **donated** | **Boolean** | Donated | [optional] [default to null] |
| **assigned\_to** | **Integer** | Assigned to | [optional] [default to null] |
| **additional\_guests** | **Integer** | Number of additional guests | [optional] [default to null] |
| **attendees** | **Integer** | Attendees | [optional] [default to null] |
| **attendee\_names** | **String** | Attendees Names | [optional] [default to null] |
| **attend\_count** | **Integer** | Attend Count | [optional] [default to null] |
| **attendances** | [**List**](Attendance.md) | Multiple attendances | [optional] [default to null] |
| **custom\_fields** | [**List**](CustomField.md) | Invitation custom fields (Categories) | [optional] [default to null] |
| **custom\_attrs** | [**List**](CustomAttr.md) | Invitation custom attributes | [optional] [default to null] |
| **created\_at** | **Date** |  | [optional] [default to null] |
| **updated\_at** | **Date** |  | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

