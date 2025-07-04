# AppealsIndex

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
**items** | [**List[AppealResponse]**](AppealResponse.md) | Appeals Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.appeals_index import AppealsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of AppealsIndex from a JSON string
appeals_index_instance = AppealsIndex.from_json(json)
# print the JSON string representation of the object
print(AppealsIndex.to_json())

# convert the object into a dict
appeals_index_dict = appeals_index_instance.to_dict()
# create an instance of AppealsIndex from a dict
appeals_index_from_dict = AppealsIndex.from_dict(appeals_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


