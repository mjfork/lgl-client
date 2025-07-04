# Note

A Note object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note_type_id** | **int** | Note Type Id | [optional] 
**note_type_name** | **str** | Note Type Name | [optional] 
**text** | **str** | Text | 
**external_id** | **str** | External Id | [optional] 
**original_date** | **date** |  | 

## Example

```python
from lgl_openapi_3_0_client.models.note import Note

# TODO update the JSON string below
json = "{}"
# create an instance of Note from a JSON string
note_instance = Note.from_json(json)
# print the JSON string representation of the object
print(Note.to_json())

# convert the object into a dict
note_dict = note_instance.to_dict()
# create an instance of Note from a dict
note_from_dict = Note.from_dict(note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


