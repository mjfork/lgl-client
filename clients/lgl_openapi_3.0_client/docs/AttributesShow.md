# AttributesShow

attribute object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
**id** | **int** | ID | 
**item_type** | **int** | Item Type | 
**name** | **str** | Name | 
**description** | **str** | Description | 
**key** | **str** | Key | [optional] 
**min_val** | **int** | Minimum Value | [optional] 
**max_val** | **int** | Maximum Value | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.attributes_show import AttributesShow

# TODO update the JSON string below
json = "{}"
# create an instance of AttributesShow from a JSON string
attributes_show_instance = AttributesShow.from_json(json)
# print the JSON string representation of the object
print(AttributesShow.to_json())

# convert the object into a dict
attributes_show_dict = attributes_show_instance.to_dict()
# create an instance of AttributesShow from a dict
attributes_show_from_dict = AttributesShow.from_dict(attributes_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


