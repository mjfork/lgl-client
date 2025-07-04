# ClassAffiliationUpdate

A ClassAffiliation object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Class Affiliation ID | [optional] 
**class_affiliation_type_id** | **int** | Class Affiliation Type ID | [optional] 
**year** | **int** | Year | [optional] 
**note** | **str** | Note | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.class_affiliation_update import ClassAffiliationUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAffiliationUpdate from a JSON string
class_affiliation_update_instance = ClassAffiliationUpdate.from_json(json)
# print the JSON string representation of the object
print(ClassAffiliationUpdate.to_json())

# convert the object into a dict
class_affiliation_update_dict = class_affiliation_update_instance.to_dict()
# create an instance of ClassAffiliationUpdate from a dict
class_affiliation_update_from_dict = ClassAffiliationUpdate.from_dict(class_affiliation_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


