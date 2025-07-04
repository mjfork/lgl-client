# ContactReportResponse

A ContactReport object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Contact Report ID | 
**constituent_id** | **int** | Constituent Id | 
**name** | **str** | Name | [optional] 
**contact_report_type_id** | **int** | Contact Report Type Id | [optional] 
**contact_report_type_name** | **str** | Contact Report Type Name | [optional] 
**original_date** | **date** |  | [optional] 
**text** | **str** | Text | 
**team_member** | **str** | Team Member | [optional] 
**team_member_email** | **str** | Team Member Email | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.contact_report_response import ContactReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContactReportResponse from a JSON string
contact_report_response_instance = ContactReportResponse.from_json(json)
# print the JSON string representation of the object
print(ContactReportResponse.to_json())

# convert the object into a dict
contact_report_response_dict = contact_report_response_instance.to_dict()
# create an instance of ContactReportResponse from a dict
contact_report_response_from_dict = ContactReportResponse.from_dict(contact_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


