# PaymentTypesIndex

Index

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**items_count** | **int** | Items returned | 
**total_items** | **int** | Total items available | 
**limit** | **int** | Item return limit | 
**offset** | **int** | Start item | 
**next_item** | **int** | Next item in list | 
**next_link** | **str** | Link to next page of items | 
**item_type** | **str** | Type of items | 
**items** | [**List[PaymentTypeResponse]**](PaymentTypeResponse.md) | PaymentTypes Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.payment_types_index import PaymentTypesIndex

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypesIndex from a JSON string
payment_types_index_instance = PaymentTypesIndex.from_json(json)
# print the JSON string representation of the object
print(PaymentTypesIndex.to_json())

# convert the object into a dict
payment_types_index_dict = payment_types_index_instance.to_dict()
# create an instance of PaymentTypesIndex from a dict
payment_types_index_from_dict = PaymentTypesIndex.from_dict(payment_types_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


