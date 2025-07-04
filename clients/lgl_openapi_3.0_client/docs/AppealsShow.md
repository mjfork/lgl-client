# AppealsShow

appeal object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | ID | 
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**var_date** | **date** |  | [optional] 
**financial_goal** | **float** |  | [optional] 
**projected_amount** | **float** |  | [optional] 
**code** | **str** | Code | [optional] 
**is_active** | **bool** | Is active appeal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.appeals_show import AppealsShow

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsShow from a JSON string
appeals_show_instance = AppealsShow.from_json(json)
# print the JSON string representation of the object
print(AppealsShow.to_json())

# convert the object into a dict
appeals_show_dict = appeals_show_instance.to_dict()
# create an instance of AppealsShow from a dict
appeals_show_from_dict = AppealsShow.from_dict(appeals_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


