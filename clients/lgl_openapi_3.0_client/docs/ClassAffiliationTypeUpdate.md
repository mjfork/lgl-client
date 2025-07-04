# ClassAffiliationTypeUpdate

A ClassAffiliationType object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.class_affiliation_type_update import ClassAffiliationTypeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAffiliationTypeUpdate from a JSON string
class_affiliation_type_update_instance = ClassAffiliationTypeUpdate.from_json(json)
# print the JSON string representation of the object
print(ClassAffiliationTypeUpdate.to_json())

# convert the object into a dict
class_affiliation_type_update_dict = class_affiliation_type_update_instance.to_dict()
# create an instance of ClassAffiliationTypeUpdate from a dict
class_affiliation_type_update_from_dict = ClassAffiliationTypeUpdate.from_dict(class_affiliation_type_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


