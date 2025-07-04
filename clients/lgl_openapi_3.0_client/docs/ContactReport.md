# ContactReport

A ContactReport object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**contact_report_type_id** | **int** | Contact Report Type Id | [optional] 
**contact_report_type_name** | **str** | Contact Report Type Name | [optional] 
**original_date** | **date** |  | [optional] 
**text** | **str** | Text | 
**team_member** | **str** | Team Member (&#39;id&#39;, &#39;email&#39;, or &#39;first_name last_name&#39;) | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.contact_report import ContactReport

# TODO update the JSON string below
json = "{}"
# create an instance of ContactReport from a JSON string
contact_report_instance = ContactReport.from_json(json)
# print the JSON string representation of the object
print(ContactReport.to_json())

# convert the object into a dict
contact_report_dict = contact_report_instance.to_dict()
# create an instance of ContactReport from a dict
contact_report_from_dict = ContactReport.from_dict(contact_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


