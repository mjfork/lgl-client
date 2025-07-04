# ClassAffiliationTypesIndex

Index

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**items_count** | **int** | Items returned | 
**total_items** | **int** | Total items available | 
**limit** | **int** | Item return limit | 
**offset** | **int** | Start item | 
**next_item** | **int** | Next item in list | 
**next_link** | **str** | Link to next page of items | 
**item_type** | **str** | Type of items | 
**items** | [**List[ClassAffiliationTypeResponse]**](ClassAffiliationTypeResponse.md) | ClassAffiliationTypes Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.class_affiliation_types_index import ClassAffiliationTypesIndex

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAffiliationTypesIndex from a JSON string
class_affiliation_types_index_instance = ClassAffiliationTypesIndex.from_json(json)
# print the JSON string representation of the object
print(ClassAffiliationTypesIndex.to_json())

# convert the object into a dict
class_affiliation_types_index_dict = class_affiliation_types_index_instance.to_dict()
# create an instance of ClassAffiliationTypesIndex from a dict
class_affiliation_types_index_from_dict = ClassAffiliationTypesIndex.from_dict(class_affiliation_types_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


