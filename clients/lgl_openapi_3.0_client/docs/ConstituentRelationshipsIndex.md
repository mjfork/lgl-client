# ConstituentRelationshipsIndex

Index

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**items_count** | **int** | Items returned | 
**item_type** | **str** | Type of items | 
**items** | [**List[ConstituentRelationshipResponse]**](ConstituentRelationshipResponse.md) | ConstituentRelationships Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.constituent_relationships_index import ConstituentRelationshipsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of ConstituentRelationshipsIndex from a JSON string
constituent_relationships_index_instance = ConstituentRelationshipsIndex.from_json(json)
# print the JSON string representation of the object
print(ConstituentRelationshipsIndex.to_json())

# convert the object into a dict
constituent_relationships_index_dict = constituent_relationships_index_instance.to_dict()
# create an instance of ConstituentRelationshipsIndex from a dict
constituent_relationships_index_from_dict = ConstituentRelationshipsIndex.from_dict(constituent_relationships_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


