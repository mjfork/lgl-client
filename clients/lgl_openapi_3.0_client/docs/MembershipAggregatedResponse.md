# MembershipAggregatedResponse

A Membership object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Membership ID | 
**constituent_id** | **int** | Constituent ID | 
**membership_level_id** | **int** | Membership Level ID | [optional] 
**membership_level_name** | **str** | Membership Level Name | [optional] 
**date_start** | **date** |  | [optional] 
**finish_date** | **date** |  | [optional] 
**note** | **str** | Note | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.membership_aggregated_response import MembershipAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipAggregatedResponse from a JSON string
membership_aggregated_response_instance = MembershipAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(MembershipAggregatedResponse.to_json())

# convert the object into a dict
membership_aggregated_response_dict = membership_aggregated_response_instance.to_dict()
# create an instance of MembershipAggregatedResponse from a dict
membership_aggregated_response_from_dict = MembershipAggregatedResponse.from_dict(membership_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


