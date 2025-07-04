# Fund

A Fund object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**code** | **int** | Code | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**financial_goal** | **float** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.fund import Fund

# TODO update the JSON string below
json = "{}"
# create an instance of Fund from a JSON string
fund_instance = Fund.from_json(json)
# print the JSON string representation of the object
print(Fund.to_json())

# convert the object into a dict
fund_dict = fund_instance.to_dict()
# create an instance of Fund from a dict
fund_from_dict = Fund.from_dict(fund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


