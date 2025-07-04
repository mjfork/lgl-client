# RelationshipType

A RelationshipType object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**short_code** | **str** | Short Code | [optional] 
**type_code** | **str** | Type Code | [optional] 
**ordinal** | **int** | Ordinal | [optional] 
**reciprocal_id** | **int** | Reciprocal Id | [optional] 
**auto_soft_credit** | **int** | Automatically soft credit? | [optional] 
**is_spouse_partner** | **bool** | Is Spouse Partner? | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.relationship_type import RelationshipType

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipType from a JSON string
relationship_type_instance = RelationshipType.from_json(json)
# print the JSON string representation of the object
print(RelationshipType.to_json())

# convert the object into a dict
relationship_type_dict = relationship_type_instance.to_dict()
# create an instance of RelationshipType from a dict
relationship_type_from_dict = RelationshipType.from_dict(relationship_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


