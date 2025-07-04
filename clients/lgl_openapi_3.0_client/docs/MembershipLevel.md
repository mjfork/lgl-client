# MembershipLevel

A MembershipLevel object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.membership_level import MembershipLevel

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipLevel from a JSON string
membership_level_instance = MembershipLevel.from_json(json)
# print the JSON string representation of the object
print(MembershipLevel.to_json())

# convert the object into a dict
membership_level_dict = membership_level_instance.to_dict()
# create an instance of MembershipLevel from a dict
membership_level_from_dict = MembershipLevel.from_dict(membership_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


