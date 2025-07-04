# PaymentTypeAggregatedResponse

A PaymentType object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**name** | **str** | Name | 
**key** | **float** |  | [optional] 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.payment_type_aggregated_response import PaymentTypeAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypeAggregatedResponse from a JSON string
payment_type_aggregated_response_instance = PaymentTypeAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentTypeAggregatedResponse.to_json())

# convert the object into a dict
payment_type_aggregated_response_dict = payment_type_aggregated_response_instance.to_dict()
# create an instance of PaymentTypeAggregatedResponse from a dict
payment_type_aggregated_response_from_dict = PaymentTypeAggregatedResponse.from_dict(payment_type_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


