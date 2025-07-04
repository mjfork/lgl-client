# Membership

A Membership object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**membership_level_id** | **int** | Membership Level ID | [optional] 
**membership_level_name** | **str** | Membership Level Name | [optional] 
**date_start** | **date** |  | [optional] 
**finish_date** | **date** |  | [optional] 
**note** | **str** | Note | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.membership import Membership

# TODO update the JSON string below
json = "{}"
# create an instance of Membership from a JSON string
membership_instance = Membership.from_json(json)
# print the JSON string representation of the object
print(Membership.to_json())

# convert the object into a dict
membership_dict = membership_instance.to_dict()
# create an instance of Membership from a dict
membership_from_dict = Membership.from_dict(membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


