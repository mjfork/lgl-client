# GiftsIndex

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
**items** | [**List[GiftResponse]**](GiftResponse.md) | Gifts Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.gifts_index import GiftsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of GiftsIndex from a JSON string
gifts_index_instance = GiftsIndex.from_json(json)
# print the JSON string representation of the object
print(GiftsIndex.to_json())

# convert the object into a dict
gifts_index_dict = gifts_index_instance.to_dict()
# create an instance of GiftsIndex from a dict
gifts_index_from_dict = GiftsIndex.from_dict(gifts_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


