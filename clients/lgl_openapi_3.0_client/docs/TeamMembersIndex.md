# TeamMembersIndex

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
**items** | [**List[TeamMemberResponse]**](TeamMemberResponse.md) | TeamMembers Objects | 

## Example

```python
from lgl_openapi_3_0_client.models.team_members_index import TeamMembersIndex

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMembersIndex from a JSON string
team_members_index_instance = TeamMembersIndex.from_json(json)
# print the JSON string representation of the object
print(TeamMembersIndex.to_json())

# convert the object into a dict
team_members_index_dict = team_members_index_instance.to_dict()
# create an instance of TeamMembersIndex from a dict
team_members_index_from_dict = TeamMembersIndex.from_dict(team_members_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


