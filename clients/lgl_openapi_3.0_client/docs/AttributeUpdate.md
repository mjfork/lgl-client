# AttributeUpdate

A Attribute object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**item_type** | **int** | Item Type | 
**name** | **str** | Name | 
**description** | **str** | Description | 
**key** | **str** | Key | [optional] 
**min_val** | **int** | Minimum Value | [optional] 
**max_val** | **int** | Maximum Value | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.attribute_update import AttributeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeUpdate from a JSON string
attribute_update_instance = AttributeUpdate.from_json(json)
# print the JSON string representation of the object
print(AttributeUpdate.to_json())

# convert the object into a dict
attribute_update_dict = attribute_update_instance.to_dict()
# create an instance of AttributeUpdate from a dict
attribute_update_from_dict = AttributeUpdate.from_dict(attribute_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


