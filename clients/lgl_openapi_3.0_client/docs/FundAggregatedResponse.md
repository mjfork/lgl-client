# FundAggregatedResponse

A Fund object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**code** | **int** | Code | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**financial_goal** | **float** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.fund_aggregated_response import FundAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FundAggregatedResponse from a JSON string
fund_aggregated_response_instance = FundAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(FundAggregatedResponse.to_json())

# convert the object into a dict
fund_aggregated_response_dict = fund_aggregated_response_instance.to_dict()
# create an instance of FundAggregatedResponse from a dict
fund_aggregated_response_from_dict = FundAggregatedResponse.from_dict(fund_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


