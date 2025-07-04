# CustomFieldAggregatedUpdate

A CustomField object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Custom Field Id | [optional] 
**name** | **str** | Name | 
**key** | **str** | Key | [optional] 
**remove_previous_values** | **bool** | Remove previous field values | [optional] 
**values** | [**List[CustomValueAggregatedUpdate]**](CustomValueAggregatedUpdate.md) | Values | 

## Example

```python
from lgl_openapi_3_0_client.models.custom_field_aggregated_update import CustomFieldAggregatedUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldAggregatedUpdate from a JSON string
custom_field_aggregated_update_instance = CustomFieldAggregatedUpdate.from_json(json)
# print the JSON string representation of the object
print(CustomFieldAggregatedUpdate.to_json())

# convert the object into a dict
custom_field_aggregated_update_dict = custom_field_aggregated_update_instance.to_dict()
# create an instance of CustomFieldAggregatedUpdate from a dict
custom_field_aggregated_update_from_dict = CustomFieldAggregatedUpdate.from_dict(custom_field_aggregated_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


