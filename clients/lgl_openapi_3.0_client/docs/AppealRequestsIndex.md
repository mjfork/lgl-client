# AppealRequestsIndex

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
**items** | [**List[AppealRequestResponse]**](AppealRequestResponse.md) | AppealRequests Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.appeal_requests_index import AppealRequestsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of AppealRequestsIndex from a JSON string
appeal_requests_index_instance = AppealRequestsIndex.from_json(json)
# print the JSON string representation of the object
print(AppealRequestsIndex.to_json())

# convert the object into a dict
appeal_requests_index_dict = appeal_requests_index_instance.to_dict()
# create an instance of AppealRequestsIndex from a dict
appeal_requests_index_from_dict = AppealRequestsIndex.from_dict(appeal_requests_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


