# RelationshipTypesShow

relationship_type object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | ID | 
**name** | **str** | Name | 
**short_code** | **str** | Short Code | [optional] 
**type_code** | **str** | Type Code | [optional] 
**ordinal** | **int** | Ordinal | [optional] 
**reciprocal_id** | **int** | Reciprocal Id | [optional] 
**auto_soft_credit** | **int** | Automatically soft credit? | [optional] 
**is_spouse_partner** | **bool** | Is Spouse Partner? | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.relationship_types_show import RelationshipTypesShow

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipTypesShow from a JSON string
relationship_types_show_instance = RelationshipTypesShow.from_json(json)
# print the JSON string representation of the object
print(RelationshipTypesShow.to_json())

# convert the object into a dict
relationship_types_show_dict = relationship_types_show_instance.to_dict()
# create an instance of RelationshipTypesShow from a dict
relationship_types_show_from_dict = RelationshipTypesShow.from_dict(relationship_types_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


