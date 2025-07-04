# ClassAffiliationTypeAggregatedResponse

A ClassAffiliationType object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**name** | **str** | Name | 
**ordinal** | **int** | Ordinal | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.class_affiliation_type_aggregated_response import ClassAffiliationTypeAggregatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAffiliationTypeAggregatedResponse from a JSON string
class_affiliation_type_aggregated_response_instance = ClassAffiliationTypeAggregatedResponse.from_json(json)
# print the JSON string representation of the object
print(ClassAffiliationTypeAggregatedResponse.to_json())

# convert the object into a dict
class_affiliation_type_aggregated_response_dict = class_affiliation_type_aggregated_response_instance.to_dict()
# create an instance of ClassAffiliationTypeAggregatedResponse from a dict
class_affiliation_type_aggregated_response_from_dict = ClassAffiliationTypeAggregatedResponse.from_dict(class_affiliation_type_aggregated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


