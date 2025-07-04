# CampaignAggregatedResponse

A Campaign object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**financial_goal** | **float** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**code** | **str** | Code | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.campaign_aggregated_response import CampaignAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAggregatedResponse from a JSON string
campaign_aggregated_response_instance = CampaignAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(CampaignAggregatedResponse.to_json())

# convert the object into a dict
campaign_aggregated_response_dict = campaign_aggregated_response_instance.to_dict()
# create an instance of CampaignAggregatedResponse from a dict
campaign_aggregated_response_from_dict = CampaignAggregatedResponse.from_dict(campaign_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


