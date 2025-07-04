# RelationshipTypesIndex

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
**items** | [**List[RelationshipTypeResponse]**](RelationshipTypeResponse.md) | RelationshipTypes Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.relationship_types_index import RelationshipTypesIndex

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipTypesIndex from a JSON string
relationship_types_index_instance = RelationshipTypesIndex.from_json(json)
# print the JSON string representation of the object
print(RelationshipTypesIndex.to_json())

# convert the object into a dict
relationship_types_index_dict = relationship_types_index_instance.to_dict()
# create an instance of RelationshipTypesIndex from a dict
relationship_types_index_from_dict = RelationshipTypesIndex.from_dict(relationship_types_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


