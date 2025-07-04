# AppealRequestResponse

A AppealRequest object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Appeal Request Id | 
**constituent_id** | **int** | Constituent Id | 
**constituent_name** | **str** | Constituent Name | [optional] 
**appeal_id** | **int** | Appeal Id | 
**name** | **str** | Appeal Name | [optional] 
**raised** | **float** |  | [optional] 
**status** | **str** | Status | [optional] 
**ask_amount** | **float** |  | [optional] 
**assigned_to** | **int** | Assigned to team member id | [optional] 
**custom_fields** | [**List[CustomField]**](CustomField.md) | Appeal request custom fields (Categories) | [optional] 
**custom_attrs** | [**List[CustomAttr]**](CustomAttr.md) | Appeal request custom attributes | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.appeal_request_response import AppealRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppealRequestResponse from a JSON string
appeal_request_response_instance = AppealRequestResponse.from_json(json)
# print the JSON string representation of the object
print(AppealRequestResponse.to_json())

# convert the object into a dict
appeal_request_response_dict = appeal_request_response_instance.to_dict()
# create an instance of AppealRequestResponse from a dict
appeal_request_response_from_dict = AppealRequestResponse.from_dict(appeal_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


