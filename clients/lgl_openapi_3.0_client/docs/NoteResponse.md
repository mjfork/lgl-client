# NoteResponse

A Note object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from lgl_openapi_3_0_client.models.note_response import NoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NoteResponse from a JSON string
note_response_instance = NoteResponse.from_json(json)
# print the JSON string representation of the object
print(NoteResponse.to_json())

# convert the object into a dict
note_response_dict = note_response_instance.to_dict()
# create an instance of NoteResponse from a dict
note_response_from_dict = NoteResponse.from_dict(note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


