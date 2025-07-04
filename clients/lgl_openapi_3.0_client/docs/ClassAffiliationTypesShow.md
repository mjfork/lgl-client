# ClassAffiliationTypesShow

class_affiliation_type object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | ID | 
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.class_affiliation_types_show import ClassAffiliationTypesShow

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAffiliationTypesShow from a JSON string
class_affiliation_types_show_instance = ClassAffiliationTypesShow.from_json(json)
# print the JSON string representation of the object
print(ClassAffiliationTypesShow.to_json())

# convert the object into a dict
class_affiliation_types_show_dict = class_affiliation_types_show_instance.to_dict()
# create an instance of ClassAffiliationTypesShow from a dict
class_affiliation_types_show_from_dict = ClassAffiliationTypesShow.from_dict(class_affiliation_types_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


