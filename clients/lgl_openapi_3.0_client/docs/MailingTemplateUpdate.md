# MailingTemplateUpdate

A MailingTemplate object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | 
**code** | **bool** | Code | [optional] 
**mailing_type_id** | **int** | Mailing Type ID | [optional] 
**mailing_type_name** | **str** | Mailing Type Name | [optional] 
**template_type** | **str** | Template Type | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.mailing_template_update import MailingTemplateUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MailingTemplateUpdate from a JSON string
mailing_template_update_instance = MailingTemplateUpdate.from_json(json)
# print the JSON string representation of the object
print(MailingTemplateUpdate.to_json())

# convert the object into a dict
mailing_template_update_dict = mailing_template_update_instance.to_dict()
# create an instance of MailingTemplateUpdate from a dict
mailing_template_update_from_dict = MailingTemplateUpdate.from_dict(mailing_template_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


