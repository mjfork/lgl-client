# CustomValueAggregatedUpdate

A CustomField object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Value Id | 
**name** | **str** | Name | 

## Example

```python
from lgl_openapi_3_0_client.models.custom_value_aggregated_update import CustomValueAggregatedUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomValueAggregatedUpdate from a JSON string
custom_value_aggregated_update_instance = CustomValueAggregatedUpdate.from_json(json)
# print the JSON string representation of the object
print(CustomValueAggregatedUpdate.to_json())

# convert the object into a dict
custom_value_aggregated_update_dict = custom_value_aggregated_update_instance.to_dict()
# create an instance of CustomValueAggregatedUpdate from a dict
custom_value_aggregated_update_from_dict = CustomValueAggregatedUpdate.from_dict(custom_value_aggregated_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


