# StreetAddressUpdate

A StreetAddress object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**street** | **str** | Street | [optional] 
**street_address_type_id** | **int** | Street Address Type ID | [optional] 
**street_type_name** | **str** | Street Address Type Name | [optional] 
**city** | **str** | City | [optional] 
**state** | **str** | State/Province | [optional] 
**postal_code** | **str** | Zip/Postal Code | [optional] 
**county** | **str** | County | [optional] 
**country** | **str** | Country | [optional] 
**seasonal_from** | **str** | Seasonal from (mm-dd) | [optional] 
**seasonal_to** | **str** | Seasonal to (mm-dd) | [optional] 
**seasonal** | **bool** | Is seasonal? | [optional] 
**is_preferred** | **bool** | Is preferred address | [optional] 
**not_current** | **bool** | Not current? | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.street_address_update import StreetAddressUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of StreetAddressUpdate from a JSON string
street_address_update_instance = StreetAddressUpdate.from_json(json)
# print the JSON string representation of the object
print(StreetAddressUpdate.to_json())

# convert the object into a dict
street_address_update_dict = street_address_update_instance.to_dict()
# create an instance of StreetAddressUpdate from a dict
street_address_update_from_dict = StreetAddressUpdate.from_dict(street_address_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


