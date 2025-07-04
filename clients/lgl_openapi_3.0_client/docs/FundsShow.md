# FundsShow

fund object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | ID | 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**code** | **int** | Code | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**financial_goal** | **float** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.funds_show import FundsShow

# TODO update the JSON string below
json = "{}"
# create an instance of FundsShow from a JSON string
funds_show_instance = FundsShow.from_json(json)
# print the JSON string representation of the object
print(FundsShow.to_json())

# convert the object into a dict
funds_show_dict = funds_show_instance.to_dict()
# create an instance of FundsShow from a dict
funds_show_from_dict = FundsShow.from_dict(funds_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


