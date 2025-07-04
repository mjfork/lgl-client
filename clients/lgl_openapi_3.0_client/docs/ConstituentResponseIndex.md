# ConstituentResponseIndex

Constituent object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Constituent ID | 
**external_constituent_id** | **int** | External constituent ID | [optional] 
**is_org** | **bool** | This constituent is an organization or company | [optional] 
**constituent_contact_type_id** | **int** | Constituent contact type ID | [optional] 
**constituent_contact_type_name** | **str** | Constituent contact type | [optional] 
**prefix** | **str** | Prefix | [optional] 
**first_name** | **str** | First name | 
**middle_name** | **str** | Middle name | [optional] 
**last_name** | **str** | Last name | 
**suffix** | **str** | Suffix | [optional] 
**spouse_name** | **str** | Spouse/Partner | [optional] 
**org_name** | **str** | Organization name | [optional] 
**job_title** | **str** | Job title | [optional] 
**addressee** | **str** | Addressee/Label name | [optional] 
**salutation** | **str** | Salutation | [optional] 
**sort_name** | **str** | Sort name | [optional] 
**constituent_interest_level_id** | **int** | Interest Level ID | [optional] 
**constituent_interest_level_name** | **str** | Interest Level | [optional] 
**constituent_rating_id** | **int** | Capacity ID | [optional] 
**constituent_rating_name** | **str** | Capacity | [optional] 
**is_deceased** | **bool** | Deceased? | [optional] 
**deceased_date** | **str** | Deceased date | [optional] 
**annual_report_name** | **str** | Annual report name | [optional] 
**birthday** | **date** |  | [optional] 
**gender** | **str** | Gender | [optional] 
**maiden_name** | **str** | Maiden name | [optional] 
**nick_name** | **str** | Nickname | [optional] 
**spouse_nick_name** | **str** | Spouse nickname | [optional] 
**date_added** | **date** |  | [optional] 
**alt_salutation** | **str** | Alt salutation | [optional] 
**alt_addressee** | **str** | Alt addressee | [optional] 
**honorary_name** | **str** | Honorary name | [optional] 
**assistant_name** | **str** | Assistant name | [optional] 
**marital_status_id** | **int** | Marital status ID | [optional] 
**marital_status_name** | **str** | Marital status | [optional] 
**is_anon** | **bool** | Gives anonymously? | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.constituent_response_index import ConstituentResponseIndex

# TODO update the JSON string below
json = "{}"
# create an instance of ConstituentResponseIndex from a JSON string
constituent_response_index_instance = ConstituentResponseIndex.from_json(json)
# print the JSON string representation of the object
print(ConstituentResponseIndex.to_json())

# convert the object into a dict
constituent_response_index_dict = constituent_response_index_instance.to_dict()
# create an instance of ConstituentResponseIndex from a dict
constituent_response_index_from_dict = ConstituentResponseIndex.from_dict(constituent_response_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


