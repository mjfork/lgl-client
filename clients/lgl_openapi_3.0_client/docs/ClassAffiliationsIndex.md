# ClassAffiliationsIndex

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
**items** | [**List[ClassAffiliationResponse]**](ClassAffiliationResponse.md) | ClassAffiliations Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.class_affiliations_index import ClassAffiliationsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAffiliationsIndex from a JSON string
class_affiliations_index_instance = ClassAffiliationsIndex.from_json(json)
# print the JSON string representation of the object
print(ClassAffiliationsIndex.to_json())

# convert the object into a dict
class_affiliations_index_dict = class_affiliations_index_instance.to_dict()
# create an instance of ClassAffiliationsIndex from a dict
class_affiliations_index_from_dict = ClassAffiliationsIndex.from_dict(class_affiliations_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


