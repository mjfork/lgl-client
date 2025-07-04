# MembershipLevelsShow

membership_level object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | Membership ID | 
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.membership_levels_show import MembershipLevelsShow

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipLevelsShow from a JSON string
membership_levels_show_instance = MembershipLevelsShow.from_json(json)
# print the JSON string representation of the object
print(MembershipLevelsShow.to_json())

# convert the object into a dict
membership_levels_show_dict = membership_levels_show_instance.to_dict()
# create an instance of MembershipLevelsShow from a dict
membership_levels_show_from_dict = MembershipLevelsShow.from_dict(membership_levels_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


