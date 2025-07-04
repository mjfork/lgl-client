# GroupMembershipAggregatedResponse

A GroupMembership object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Group ID | 
**constituent_id** | **int** | Constituent Id | 
**group_id** | **int** | Group Id | 
**group_name** | **str** | Group Name | [optional] 
**date_start** | **date** |  | [optional] 
**date_end** | **date** |  | [optional] 
**is_current** | **bool** | Current? | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.group_membership_aggregated_response import GroupMembershipAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMembershipAggregatedResponse from a JSON string
group_membership_aggregated_response_instance = GroupMembershipAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(GroupMembershipAggregatedResponse.to_json())

# convert the object into a dict
group_membership_aggregated_response_dict = group_membership_aggregated_response_instance.to_dict()
# create an instance of GroupMembershipAggregatedResponse from a dict
group_membership_aggregated_response_from_dict = GroupMembershipAggregatedResponse.from_dict(group_membership_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


