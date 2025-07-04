# MailingTemplateResponse

A MailingTemplate object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**name** | **str** | Name | 
**code** | **bool** | Code | [optional] 
**mailing_type_id** | **int** | Mailing Type ID | [optional] 
**mailing_type_name** | **str** | Mailing Type Name | [optional] 
**template_type** | **str** | Template Type | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.mailing_template_response import MailingTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MailingTemplateResponse from a JSON string
mailing_template_response_instance = MailingTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(MailingTemplateResponse.to_json())

# convert the object into a dict
mailing_template_response_dict = mailing_template_response_instance.to_dict()
# create an instance of MailingTemplateResponse from a dict
mailing_template_response_from_dict = MailingTemplateResponse.from_dict(mailing_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


