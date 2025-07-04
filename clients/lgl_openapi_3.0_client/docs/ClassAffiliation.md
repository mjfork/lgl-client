# ClassAffiliation

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
from lgl_openapi_3_0_client.models.class_affiliation import ClassAffiliation

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAffiliation from a JSON string
class_affiliation_instance = ClassAffiliation.from_json(json)
# print the JSON string representation of the object
print(ClassAffiliation.to_json())

# convert the object into a dict
class_affiliation_dict = class_affiliation_instance.to_dict()
# create an instance of ClassAffiliation from a dict
class_affiliation_from_dict = ClassAffiliation.from_dict(class_affiliation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


