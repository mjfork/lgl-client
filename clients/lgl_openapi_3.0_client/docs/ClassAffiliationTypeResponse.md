# ClassAffiliationTypeResponse

A ClassAffiliationType object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.class_affiliation_type_response import ClassAffiliationTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAffiliationTypeResponse from a JSON string
class_affiliation_type_response_instance = ClassAffiliationTypeResponse.from_json(json)
# print the JSON string representation of the object
print(ClassAffiliationTypeResponse.to_json())

# convert the object into a dict
class_affiliation_type_response_dict = class_affiliation_type_response_instance.to_dict()
# create an instance of ClassAffiliationTypeResponse from a dict
class_affiliation_type_response_from_dict = ClassAffiliationTypeResponse.from_dict(class_affiliation_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


