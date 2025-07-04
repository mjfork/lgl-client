# AppealRequestAggregatedResponse

A AppealRequest object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**constituent_id** | **int** | Constituent Id | 
**appeal_id** | **int** | Appeal Id | 
**ask_amount** | **float** |  | [optional] 
**status** | **str** | Status | [optional] 
**assigned_to** | **int** | Assigned to team member id | [optional] 
**custom_fields** | [**List[CustomFieldAggregatedUpdate]**](CustomFieldAggregatedUpdate.md) | Appeal request custom fields (Categories) | [optional] 
**custom_attrs** | [**List[CustomAttrCreate]**](CustomAttrCreate.md) | Appeal request custom attributes | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.appeal_request_aggregated_response import AppealRequestAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppealRequestAggregatedResponse from a JSON string
appeal_request_aggregated_response_instance = AppealRequestAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(AppealRequestAggregatedResponse.to_json())

# convert the object into a dict
appeal_request_aggregated_response_dict = appeal_request_aggregated_response_instance.to_dict()
# create an instance of AppealRequestAggregatedResponse from a dict
appeal_request_aggregated_response_from_dict = AppealRequestAggregatedResponse.from_dict(appeal_request_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


