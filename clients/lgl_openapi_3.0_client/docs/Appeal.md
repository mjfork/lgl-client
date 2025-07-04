# Appeal

A Appeal object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**description** | **str** | Description | [optional] 
**var_date** | **date** |  | [optional] 
**financial_goal** | **float** |  | [optional] 
**projected_amount** | **float** |  | [optional] 
**code** | **str** | Code | [optional] 
**is_active** | **bool** | Is active appeal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.appeal import Appeal

# TODO update the JSON string below
json = "{}"
# create an instance of Appeal from a JSON string
appeal_instance = Appeal.from_json(json)
# print the JSON string representation of the object
print(Appeal.to_json())

# convert the object into a dict
appeal_dict = appeal_instance.to_dict()
# create an instance of Appeal from a dict
appeal_from_dict = Appeal.from_dict(appeal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


