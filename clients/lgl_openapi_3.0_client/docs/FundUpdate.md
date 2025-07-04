# FundUpdate

A Fund object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**code** | **int** | Code | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**financial_goal** | **float** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.fund_update import FundUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of FundUpdate from a JSON string
fund_update_instance = FundUpdate.from_json(json)
# print the JSON string representation of the object
print(FundUpdate.to_json())

# convert the object into a dict
fund_update_dict = fund_update_instance.to_dict()
# create an instance of FundUpdate from a dict
fund_update_from_dict = FundUpdate.from_dict(fund_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


