# ConstituentRelationshipAggregatedResponse

A ConstituentRelationship object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from lgl_openapi_3_0_client.models.constituent_relationship_aggregated_response import ConstituentRelationshipAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConstituentRelationshipAggregatedResponse from a JSON string
constituent_relationship_aggregated_response_instance = ConstituentRelationshipAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(ConstituentRelationshipAggregatedResponse.to_json())

# convert the object into a dict
constituent_relationship_aggregated_response_dict = constituent_relationship_aggregated_response_instance.to_dict()
# create an instance of ConstituentRelationshipAggregatedResponse from a dict
constituent_relationship_aggregated_response_from_dict = ConstituentRelationshipAggregatedResponse.from_dict(constituent_relationship_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


