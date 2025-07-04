# ClassAffiliationType

A ClassAffiliationType object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.class_affiliation_type import ClassAffiliationType

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAffiliationType from a JSON string
class_affiliation_type_instance = ClassAffiliationType.from_json(json)
# print the JSON string representation of the object
print(ClassAffiliationType.to_json())

# convert the object into a dict
class_affiliation_type_dict = class_affiliation_type_instance.to_dict()
# create an instance of ClassAffiliationType from a dict
class_affiliation_type_from_dict = ClassAffiliationType.from_dict(class_affiliation_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


