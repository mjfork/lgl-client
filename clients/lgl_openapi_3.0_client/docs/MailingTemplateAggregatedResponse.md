# MailingTemplateAggregatedResponse

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
from lgl_openapi_3_0_client.models.mailing_template_aggregated_response import MailingTemplateAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MailingTemplateAggregatedResponse from a JSON string
mailing_template_aggregated_response_instance = MailingTemplateAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(MailingTemplateAggregatedResponse.to_json())

# convert the object into a dict
mailing_template_aggregated_response_dict = mailing_template_aggregated_response_instance.to_dict()
# create an instance of MailingTemplateAggregatedResponse from a dict
mailing_template_aggregated_response_from_dict = MailingTemplateAggregatedResponse.from_dict(mailing_template_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


