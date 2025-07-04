# StreetAddressAggregatedResponse

A StreetAddress object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Email Address ID | 
**street** | **str** | Street | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State/Province | [optional] 
**country** | **str** | Country | [optional] 
**postal_code** | **str** | Zip/Postal Code | [optional] 
**county** | **str** | County | [optional] 
**street_address_type_id** | **int** | Street Address Type ID | [optional] 
**street_type_name** | **str** | Street Address Type Name | [optional] 
**is_preferred** | **bool** | Is preferred address | [optional] 
**not_current** | **bool** | Not current? | [optional] 
**seasonal_from** | **str** | Seasonal from (mm-dd) | [optional] 
**seasonal_to** | **str** | Seasonal to (mm-dd) | [optional] 
**seasonal** | **bool** | Is seasonal? | [optional] 
**lat** | **float** |  | [optional] 
**lng** | **float** |  | [optional] 
**zip5** | **str** | 5 digit zipcode | [optional] 
**verified** | **bool** | Is verified? | [optional] 
**verified_on** | **date** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.street_address_aggregated_response import StreetAddressAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreetAddressAggregatedResponse from a JSON string
street_address_aggregated_response_instance = StreetAddressAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(StreetAddressAggregatedResponse.to_json())

# convert the object into a dict
street_address_aggregated_response_dict = street_address_aggregated_response_instance.to_dict()
# create an instance of StreetAddressAggregatedResponse from a dict
street_address_aggregated_response_from_dict = StreetAddressAggregatedResponse.from_dict(street_address_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


