# StreetAddressesShow

street_address object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | Email Address ID | 
**item_id** | **int** | Owner ID | 
**item_type** | **str** | Owner Type | 
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
from lgl_openapi_3_0_client.models.street_addresses_show import StreetAddressesShow

# TODO update the JSON string below
json = "{}"
# create an instance of StreetAddressesShow from a JSON string
street_addresses_show_instance = StreetAddressesShow.from_json(json)
# print the JSON string representation of the object
print(StreetAddressesShow.to_json())

# convert the object into a dict
street_addresses_show_dict = street_addresses_show_instance.to_dict()
# create an instance of StreetAddressesShow from a dict
street_addresses_show_from_dict = StreetAddressesShow.from_dict(street_addresses_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


