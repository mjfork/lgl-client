# ContactReportsIndex

Index

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**items_count** | **int** | Items returned | 
**total_items** | **int** | Total items available | 
**limit** | **int** | Item return limit | 
**offset** | **int** | Start item | 
**next_item** | **int** | Next item in list | 
**next_link** | **str** | Link to next page of items | 
**item_type** | **str** | Type of items | 
**items** | [**List[ContactReportResponse]**](ContactReportResponse.md) | ContactReports Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.contact_reports_index import ContactReportsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of ContactReportsIndex from a JSON string
contact_reports_index_instance = ContactReportsIndex.from_json(json)
# print the JSON string representation of the object
print(ContactReportsIndex.to_json())

# convert the object into a dict
contact_reports_index_dict = contact_reports_index_instance.to_dict()
# create an instance of ContactReportsIndex from a dict
contact_reports_index_from_dict = ContactReportsIndex.from_dict(contact_reports_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


