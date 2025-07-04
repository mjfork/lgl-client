# GiftUpdate

A Gift object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**external_id** | **int** | External Gift ID | [optional] 
**is_anon** | **bool** | Gift is Anonymous? | [optional] 
**gift_type_id** | **int** | Gift type ID | 
**gift_type_name** | **str** | Gift type name | 
**gift_category_id** | **int** | Gift category ID | [optional] 
**gift_category_name** | **str** | Gift category name | [optional] 
**campaign_id** | **int** | Campaign ID | [optional] 
**campaign_name** | **str** | Campaign name | [optional] 
**fund_id** | **int** | Fund ID | [optional] 
**fund_name** | **str** | Fund name | [optional] 
**appeal_id** | **int** | Appeal ID | [optional] 
**appeal_name** | **str** | Appeal name | [optional] 
**event_id** | **int** | Event ID | [optional] 
**event_name** | **str** | Event name | [optional] 
**received_amount** | **float** |  | [optional] 
**received_date** | **date** |  | [optional] 
**payment_type_id** | **int** | Payment type ID | [optional] 
**payment_type_name** | **str** | Payment type name | [optional] 
**check_number** | **str** | Check/Reference No. | [optional] 
**deductible_amount** | **float** |  | [optional] 
**note** | **str** | Gift note | [optional] 
**ack_template_name** | **str** | Ack. mailing template name. (use &#39;do_not_ack&#39; to indicate no acknowledgment) | [optional] 
**deposit_date** | **date** |  | [optional] 
**deposited_amount** | **float** |  | [optional] 
**parent_gift_id** | **int** | LGL parent gift ID | [optional] 
**parent_external_id** | **int** | External parent gift ID | [optional] 
**auto_sync_to_qbo** | **bool** | Auto Sync to QBO (only for active QuickBooks integrations) | [optional] 
**tribute_name** | **str** | The name of tribute. Values: \&quot;Honorary - General\&quot;, \&quot;Memorial - General\&quot;, or a pre-defined named tribute | [optional] 
**tributee_name** | **str** | The name of the honoree/deceased | [optional] 
**tribute_dedication** | **str** | The tribute dedication note/text for a gift | [optional] 
**tribute_recipient_name** | **str** | The name of person who should be notified about this tribute gift. | [optional] 
**tribute_recipient_salutation** | **str** | The name of person who should be notified about this tribute gift. | [optional] 
**tribute_recipient_email** | **str** | The email of the person who should be notified about this tribute gift. | [optional] 
**tribute_recipient_address** | **str** | The address of the person who should be notified about this tribute gift. | [optional] 
**tribute_recipient_notification_template** | **str** | The notification template to be used for the person who should be notified about this tribute gift. | [optional] 
**team_member** | **str** | Team Member (&#39;id&#39;, &#39;email&#39;, or &#39;first_name last_name&#39;) | [optional] 
**custom_fields** | [**List[CustomFieldAggregatedUpdate]**](CustomFieldAggregatedUpdate.md) | Gift custom fields (Categories) | [optional] 

## Example

```python
from lgl_openapi_3_0_client.models.gift_update import GiftUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GiftUpdate from a JSON string
gift_update_instance = GiftUpdate.from_json(json)
# print the JSON string representation of the object
print(GiftUpdate.to_json())

# convert the object into a dict
gift_update_dict = gift_update_instance.to_dict()
# create an instance of GiftUpdate from a dict
gift_update_from_dict = GiftUpdate.from_dict(gift_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


