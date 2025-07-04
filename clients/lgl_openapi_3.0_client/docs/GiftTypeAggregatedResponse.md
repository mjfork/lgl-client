# GiftTypeAggregatedResponse

A GiftType object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.gift_type_aggregated_response import GiftTypeAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GiftTypeAggregatedResponse from a JSON string
gift_type_aggregated_response_instance = GiftTypeAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(GiftTypeAggregatedResponse.to_json())

# convert the object into a dict
gift_type_aggregated_response_dict = gift_type_aggregated_response_instance.to_dict()
# create an instance of GiftTypeAggregatedResponse from a dict
gift_type_aggregated_response_from_dict = GiftTypeAggregatedResponse.from_dict(gift_type_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


