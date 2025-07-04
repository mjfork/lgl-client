# CreateBody

Body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First Name | 
**last_name** | **str** | Last Name | 
**email** | **str** | Email | 
**role_id** | **int** | Role Id | 
**is_primary_contact** | **bool** | Is Primary Contact? | 
**is_billing_contact** | **bool** | Is Billing Contact? | 

## Example

```python
from lgl_openapi_3_0_client.models.create_body import CreateBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBody from a JSON string
create_body_instance = CreateBody.from_json(json)
# print the JSON string representation of the object
print(CreateBody.to_json())

# convert the object into a dict
create_body_dict = create_body_instance.to_dict()
# create an instance of CreateBody from a dict
create_body_from_dict = CreateBody.from_dict(create_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


