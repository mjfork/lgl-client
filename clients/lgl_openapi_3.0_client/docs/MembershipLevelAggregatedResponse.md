# MembershipLevelAggregatedResponse

A MembershipLevel object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Membership ID | 
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.membership_level_aggregated_response import MembershipLevelAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipLevelAggregatedResponse from a JSON string
membership_level_aggregated_response_instance = MembershipLevelAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(MembershipLevelAggregatedResponse.to_json())

# convert the object into a dict
membership_level_aggregated_response_dict = membership_level_aggregated_response_instance.to_dict()
# create an instance of MembershipLevelAggregatedResponse from a dict
membership_level_aggregated_response_from_dict = MembershipLevelAggregatedResponse.from_dict(membership_level_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


