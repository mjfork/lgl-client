# AppealResponse

A Appeal object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**var_date** | **date** |  | [optional] 
**financial_goal** | **float** |  | [optional] 
**projected_amount** | **float** |  | [optional] 
**code** | **str** | Code | [optional] 
**is_active** | **bool** | Is active appeal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.appeal_response import AppealResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppealResponse from a JSON string
appeal_response_instance = AppealResponse.from_json(json)
# print the JSON string representation of the object
print(AppealResponse.to_json())

# convert the object into a dict
appeal_response_dict = appeal_response_instance.to_dict()
# create an instance of AppealResponse from a dict
appeal_response_from_dict = AppealResponse.from_dict(appeal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


