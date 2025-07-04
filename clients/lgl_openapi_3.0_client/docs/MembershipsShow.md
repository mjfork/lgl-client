# MembershipsShow

membership object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
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
from lgl_openapi_3_0_client.models.memberships_show import MembershipsShow

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipsShow from a JSON string
memberships_show_instance = MembershipsShow.from_json(json)
# print the JSON string representation of the object
print(MembershipsShow.to_json())

# convert the object into a dict
memberships_show_dict = memberships_show_instance.to_dict()
# create an instance of MembershipsShow from a dict
memberships_show_from_dict = MembershipsShow.from_dict(memberships_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


