# InvitationsIndex

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
**items** | [**List[Invitation]**](Invitation.md) | Invitations | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.invitations_index import InvitationsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationsIndex from a JSON string
invitations_index_instance = InvitationsIndex.from_json(json)
# print the JSON string representation of the object
print(InvitationsIndex.to_json())

# convert the object into a dict
invitations_index_dict = invitations_index_instance.to_dict()
# create an instance of InvitationsIndex from a dict
invitations_index_from_dict = InvitationsIndex.from_dict(invitations_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


