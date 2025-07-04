# UpdateBody

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
from lgl_openapi_3_0_client.models.update_body import UpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBody from a JSON string
update_body_instance = UpdateBody.from_json(json)
# print the JSON string representation of the object
print(UpdateBody.to_json())

# convert the object into a dict
update_body_dict = update_body_instance.to_dict()
# create an instance of UpdateBody from a dict
update_body_from_dict = UpdateBody.from_dict(update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


