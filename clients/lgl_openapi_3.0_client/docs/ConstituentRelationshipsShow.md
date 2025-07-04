# ConstituentRelationshipsShow

constituent_relationship object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | ConstituentRelationship ID | 
**relationship_type_id** | **int** | Relationship Type ID | [optional] 
**constituent_id** | **int** | Constituent ID | [optional] 
**related_constituent_id** | **int** | Related Constituent ID | [optional] 
**name** | **str** | Relationship name | [optional] 
**description** | **str** | Relationship description | [optional] 
**auto_soft_credit** | **bool** | Automatically soft credit? | [optional] 
**also_acknowledge** | **bool** | Send memorial acknowledgements? | [optional] 
**share_address** | **int** | Share address? | [optional] 
**share_phone** | **int** | Share phone? | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.constituent_relationships_show import ConstituentRelationshipsShow

# TODO update the JSON string below
json = "{}"
# create an instance of ConstituentRelationshipsShow from a JSON string
constituent_relationships_show_instance = ConstituentRelationshipsShow.from_json(json)
# print the JSON string representation of the object
print(ConstituentRelationshipsShow.to_json())

# convert the object into a dict
constituent_relationships_show_dict = constituent_relationships_show_instance.to_dict()
# create an instance of ConstituentRelationshipsShow from a dict
constituent_relationships_show_from_dict = ConstituentRelationshipsShow.from_dict(constituent_relationships_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


