# MembershipResponse

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
from lgl_openapi_3_0_client.models.membership_response import MembershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipResponse from a JSON string
membership_response_instance = MembershipResponse.from_json(json)
# print the JSON string representation of the object
print(MembershipResponse.to_json())

# convert the object into a dict
membership_response_dict = membership_response_instance.to_dict()
# create an instance of MembershipResponse from a dict
membership_response_from_dict = MembershipResponse.from_dict(membership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


