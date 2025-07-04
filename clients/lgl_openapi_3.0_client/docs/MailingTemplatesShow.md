# MailingTemplatesShow

mailing_template object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | ID | 
**name** | **str** | Name | 
**code** | **bool** | Code | [optional] 
**mailing_type_id** | **int** | Mailing Type ID | [optional] 
**mailing_type_name** | **str** | Mailing Type Name | [optional] 
**template_type** | **str** | Template Type | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.mailing_templates_show import MailingTemplatesShow

# TODO update the JSON string below
json = "{}"
# create an instance of MailingTemplatesShow from a JSON string
mailing_templates_show_instance = MailingTemplatesShow.from_json(json)
# print the JSON string representation of the object
print(MailingTemplatesShow.to_json())

# convert the object into a dict
mailing_templates_show_dict = mailing_templates_show_instance.to_dict()
# create an instance of MailingTemplatesShow from a dict
mailing_templates_show_from_dict = MailingTemplatesShow.from_dict(mailing_templates_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


