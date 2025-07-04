# PaymentTypesShow

payment_type object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | ID | 
**name** | **str** | Name | 
**key** | **float** |  | [optional] 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.payment_types_show import PaymentTypesShow

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypesShow from a JSON string
payment_types_show_instance = PaymentTypesShow.from_json(json)
# print the JSON string representation of the object
print(PaymentTypesShow.to_json())

# convert the object into a dict
payment_types_show_dict = payment_types_show_instance.to_dict()
# create an instance of PaymentTypesShow from a dict
payment_types_show_from_dict = PaymentTypesShow.from_dict(payment_types_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


