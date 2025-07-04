# WebAddressesIndex

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
**items** | [**List[WebAddressResponse]**](WebAddressResponse.md) | WebAddresses Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.web_addresses_index import WebAddressesIndex

# TODO update the JSON string below
json = "{}"
# create an instance of WebAddressesIndex from a JSON string
web_addresses_index_instance = WebAddressesIndex.from_json(json)
# print the JSON string representation of the object
print(WebAddressesIndex.to_json())

# convert the object into a dict
web_addresses_index_dict = web_addresses_index_instance.to_dict()
# create an instance of WebAddressesIndex from a dict
web_addresses_index_from_dict = WebAddressesIndex.from_dict(web_addresses_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


