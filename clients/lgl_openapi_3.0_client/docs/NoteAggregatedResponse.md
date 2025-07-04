# NoteAggregatedResponse

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

## Example

```python
from lgl_openapi_3_0_client.models.note_aggregated_response import NoteAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NoteAggregatedResponse from a JSON string
note_aggregated_response_instance = NoteAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(NoteAggregatedResponse.to_json())

# convert the object into a dict
note_aggregated_response_dict = note_aggregated_response_instance.to_dict()
# create an instance of NoteAggregatedResponse from a dict
note_aggregated_response_from_dict = NoteAggregatedResponse.from_dict(note_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


