# CampaignsShow

campaign object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | ID | 
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**financial_goal** | **float** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**code** | **str** | Code | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.campaigns_show import CampaignsShow

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignsShow from a JSON string
campaigns_show_instance = CampaignsShow.from_json(json)
# print the JSON string representation of the object
print(CampaignsShow.to_json())

# convert the object into a dict
campaigns_show_dict = campaigns_show_instance.to_dict()
# create an instance of CampaignsShow from a dict
campaigns_show_from_dict = CampaignsShow.from_dict(campaigns_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


