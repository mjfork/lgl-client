# ContactReportsShow

contact_report object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
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
from lgl_openapi_3_0_client.models.contact_reports_show import ContactReportsShow

# TODO update the JSON string below
json = "{}"
# create an instance of ContactReportsShow from a JSON string
contact_reports_show_instance = ContactReportsShow.from_json(json)
# print the JSON string representation of the object
print(ContactReportsShow.to_json())

# convert the object into a dict
contact_reports_show_dict = contact_reports_show_instance.to_dict()
# create an instance of ContactReportsShow from a dict
contact_reports_show_from_dict = ContactReportsShow.from_dict(contact_reports_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


