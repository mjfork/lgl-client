# MailingTemplatesIndex

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
**items** | [**List[MailingTemplateResponse]**](MailingTemplateResponse.md) | MailingTemplates Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.mailing_templates_index import MailingTemplatesIndex

# TODO update the JSON string below
json = "{}"
# create an instance of MailingTemplatesIndex from a JSON string
mailing_templates_index_instance = MailingTemplatesIndex.from_json(json)
# print the JSON string representation of the object
print(MailingTemplatesIndex.to_json())

# convert the object into a dict
mailing_templates_index_dict = mailing_templates_index_instance.to_dict()
# create an instance of MailingTemplatesIndex from a dict
mailing_templates_index_from_dict = MailingTemplatesIndex.from_dict(mailing_templates_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


