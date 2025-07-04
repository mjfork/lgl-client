# NotesShow

note object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | Note ID | 
**constituent_id** | **int** | Constituent Id | 
**note_type_id** | **int** | Note Type Id | [optional] 
**note_type_name** | **str** | Note Type Name | [optional] 
**text** | **str** | Text | 
**external_id** | **str** | External Id | [optional] 
**original_date** | **date** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.notes_show import NotesShow

# TODO update the JSON string below
json = "{}"
# create an instance of NotesShow from a JSON string
notes_show_instance = NotesShow.from_json(json)
# print the JSON string representation of the object
print(NotesShow.to_json())

# convert the object into a dict
notes_show_dict = notes_show_instance.to_dict()
# create an instance of NotesShow from a dict
notes_show_from_dict = NotesShow.from_dict(notes_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


