# ClassAffiliationAggregatedResponse

A ClassAffiliation object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Class Affiliation ID | 
**constituent_id** | **int** | Constituent ID | 
**class_affiliation_type_id** | **int** | Class Affiliation Type ID | [optional] 
**year** | **int** | Year | [optional] 
**note** | **str** | Note | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.class_affiliation_aggregated_response import ClassAffiliationAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAffiliationAggregatedResponse from a JSON string
class_affiliation_aggregated_response_instance = ClassAffiliationAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(ClassAffiliationAggregatedResponse.to_json())

# convert the object into a dict
class_affiliation_aggregated_response_dict = class_affiliation_aggregated_response_instance.to_dict()
# create an instance of ClassAffiliationAggregatedResponse from a dict
class_affiliation_aggregated_response_from_dict = ClassAffiliationAggregatedResponse.from_dict(class_affiliation_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


