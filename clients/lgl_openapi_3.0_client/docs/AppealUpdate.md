# AppealUpdate

A Appeal object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**var_date** | **date** |  | [optional] 
**financial_goal** | **float** |  | [optional] 
**projected_amount** | **float** |  | [optional] 
**code** | **str** | Code | [optional] 
**is_active** | **bool** | Is active appeal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.appeal_update import AppealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AppealUpdate from a JSON string
appeal_update_instance = AppealUpdate.from_json(json)
# print the JSON string representation of the object
print(AppealUpdate.to_json())

# convert the object into a dict
appeal_update_dict = appeal_update_instance.to_dict()
# create an instance of AppealUpdate from a dict
appeal_update_from_dict = AppealUpdate.from_dict(appeal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


