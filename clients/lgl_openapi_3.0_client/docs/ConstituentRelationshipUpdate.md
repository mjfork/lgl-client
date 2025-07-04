# ConstituentRelationshipUpdate

A ConstituentRelationship object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ConstituentRelationship ID | [optional] 
**related_constituent_id** | **int** | Related Constituent ID | [optional] 
**relationship_type_id** | **int** | Relationship Type ID | [optional] 
**name** | **str** | Relationship name | [optional] 
**description** | **str** | Relationship description | [optional] 
**reciprocal_id** | **int** | Reciprocal Relationship Type ID | [optional] 
**rec_name** | **str** | Reciprocal relationship name | [optional] 
**reciprocal_description** | **str** | Reciprocal relationship description | [optional] 
**share_address** | **int** | Share address? | [optional] 
**share_phone** | **int** | Share phone? | [optional] 
**auto_soft_credit** | **bool** | Automatically soft credit? | [optional] 
**also_acknowledge** | **bool** | Send memorial acknowledgements? | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.constituent_relationship_update import ConstituentRelationshipUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ConstituentRelationshipUpdate from a JSON string
constituent_relationship_update_instance = ConstituentRelationshipUpdate.from_json(json)
# print the JSON string representation of the object
print(ConstituentRelationshipUpdate.to_json())

# convert the object into a dict
constituent_relationship_update_dict = constituent_relationship_update_instance.to_dict()
# create an instance of ConstituentRelationshipUpdate from a dict
constituent_relationship_update_from_dict = ConstituentRelationshipUpdate.from_dict(constituent_relationship_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


