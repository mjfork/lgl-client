# ConstituentsShow

A Constituent object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | 
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
**class_affiliations** | [**List[ClassAffiliationAggregatedResponse]**](ClassAffiliationAggregatedResponse.md) | Class Affiliation Objects | [optional] 
**relationships** | [**List[ConstituentRelationshipAggregatedResponse]**](ConstituentRelationshipAggregatedResponse.md) | Relationship Objects | [optional] 
**email_addresses** | [**List[EmailAddressAggregatedResponse]**](EmailAddressAggregatedResponse.md) | Email Address Objects | 
**phone_numbers** | [**List[PhoneNumberAggregatedResponse]**](PhoneNumberAggregatedResponse.md) | Phone Number Objects | [optional] 
**street_addresses** | [**List[StreetAddressAggregatedResponse]**](StreetAddressAggregatedResponse.md) | Street Address Objects | [optional] 
**web_addresses** | [**List[WebAddressAggregatedResponse]**](WebAddressAggregatedResponse.md) | Web Address Objects | [optional] 
**categories** | [**List[Category]**](Category.md) | Constituent Categories | [optional] 
**groups** | [**List[GroupMembershipAggregatedResponse]**](GroupMembershipAggregatedResponse.md) | Group Objects | [optional] 
**memberships** | [**List[MembershipAggregatedResponse]**](MembershipAggregatedResponse.md) | Memberships | [optional] 
**custom_attrs** | [**List[CustomAttr]**](CustomAttr.md) | Custom Attributes | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.constituents_show import ConstituentsShow

# TODO update the JSON string below
json = "{}"
# create an instance of ConstituentsShow from a JSON string
constituents_show_instance = ConstituentsShow.from_json(json)
# print the JSON string representation of the object
print(ConstituentsShow.to_json())

# convert the object into a dict
constituents_show_dict = constituents_show_instance.to_dict()
# create an instance of ConstituentsShow from a dict
constituents_show_from_dict = ConstituentsShow.from_dict(constituents_show_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


