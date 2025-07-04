# CampaignUpdate

A Campaign object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**financial_goal** | **float** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**code** | **str** | Code | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.campaign_update import CampaignUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignUpdate from a JSON string
campaign_update_instance = CampaignUpdate.from_json(json)
# print the JSON string representation of the object
print(CampaignUpdate.to_json())

# convert the object into a dict
campaign_update_dict = campaign_update_instance.to_dict()
# create an instance of CampaignUpdate from a dict
campaign_update_from_dict = CampaignUpdate.from_dict(campaign_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


