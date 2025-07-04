# PaymentTypeUpdate

A PaymentType object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | 
**key** | **float** |  | [optional] 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.payment_type_update import PaymentTypeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypeUpdate from a JSON string
payment_type_update_instance = PaymentTypeUpdate.from_json(json)
# print the JSON string representation of the object
print(PaymentTypeUpdate.to_json())

# convert the object into a dict
payment_type_update_dict = payment_type_update_instance.to_dict()
# create an instance of PaymentTypeUpdate from a dict
payment_type_update_from_dict = PaymentTypeUpdate.from_dict(payment_type_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


