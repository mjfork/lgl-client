# NotesIndex

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
**items** | [**List[NoteResponse]**](NoteResponse.md) | Notes Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.notes_index import NotesIndex

# TODO update the JSON string below
json = "{}"
# create an instance of NotesIndex from a JSON string
notes_index_instance = NotesIndex.from_json(json)
# print the JSON string representation of the object
print(NotesIndex.to_json())

# convert the object into a dict
notes_index_dict = notes_index_instance.to_dict()
# create an instance of NotesIndex from a dict
notes_index_from_dict = NotesIndex.from_dict(notes_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


