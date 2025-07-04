# MembershipLevelUpdate

A MembershipLevel object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.membership_level_update import MembershipLevelUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipLevelUpdate from a JSON string
membership_level_update_instance = MembershipLevelUpdate.from_json(json)
# print the JSON string representation of the object
print(MembershipLevelUpdate.to_json())

# convert the object into a dict
membership_level_update_dict = membership_level_update_instance.to_dict()
# create an instance of MembershipLevelUpdate from a dict
membership_level_update_from_dict = MembershipLevelUpdate.from_dict(membership_level_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


