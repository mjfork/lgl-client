# ClassAffiliationsShow

class_affiliation object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | Class Affiliation ID | 
**constituent_id** | **int** | Constituent ID | 
**class_affiliation_type_id** | **int** | Class Affiliation Type ID | [optional] 
**year** | **int** | Year | [optional] 
**note** | **str** | Note | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.class_affiliations_show import ClassAffiliationsShow

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAffiliationsShow from a JSON string
class_affiliations_show_instance = ClassAffiliationsShow.from_json(json)
# print the JSON string representation of the object
print(ClassAffiliationsShow.to_json())

# convert the object into a dict
class_affiliations_show_dict = class_affiliations_show_instance.to_dict()
# create an instance of ClassAffiliationsShow from a dict
class_affiliations_show_from_dict = ClassAffiliationsShow.from_dict(class_affiliations_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


