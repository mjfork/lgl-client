# GiftUpdate
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **Integer** | ID | [optional] [default to null] |
| **external\_id** | **Integer** | External Gift ID | [optional] [default to null] |
| **is\_anon** | **Boolean** | Gift is Anonymous? | [optional] [default to null] |
| **gift\_type\_id** | **Integer** | Gift type ID | [default to null] |
| **gift\_type\_name** | **String** | Gift type name | [default to null] |
| **gift\_category\_id** | **Integer** | Gift category ID | [optional] [default to null] |
| **gift\_category\_name** | **String** | Gift category name | [optional] [default to null] |
| **campaign\_id** | **Integer** | Campaign ID | [optional] [default to null] |
| **campaign\_name** | **String** | Campaign name | [optional] [default to null] |
| **fund\_id** | **Integer** | Fund ID | [optional] [default to null] |
| **fund\_name** | **String** | Fund name | [optional] [default to null] |
| **appeal\_id** | **Integer** | Appeal ID | [optional] [default to null] |
| **appeal\_name** | **String** | Appeal name | [optional] [default to null] |
| **event\_id** | **Integer** | Event ID | [optional] [default to null] |
| **event\_name** | **String** | Event name | [optional] [default to null] |
| **received\_amount** | **Double** |  | [optional] [default to null] |
| **received\_date** | **date** |  | [optional] [default to null] |
| **payment\_type\_id** | **Integer** | Payment type ID | [optional] [default to null] |
| **payment\_type\_name** | **String** | Payment type name | [optional] [default to null] |
| **check\_number** | **String** | Check/Reference No. | [optional] [default to null] |
| **deductible\_amount** | **Double** |  | [optional] [default to null] |
| **note** | **String** | Gift note | [optional] [default to null] |
| **ack\_template\_name** | **String** | Ack. mailing template name. (use &#39;do_not_ack&#39; to indicate no acknowledgment) | [optional] [default to null] |
| **deposit\_date** | **date** |  | [optional] [default to null] |
| **deposited\_amount** | **Double** |  | [optional] [default to null] |
| **parent\_gift\_id** | **Integer** | LGL parent gift ID | [optional] [default to null] |
| **parent\_external\_id** | **Integer** | External parent gift ID | [optional] [default to null] |
| **auto\_sync\_to\_qbo** | **Boolean** | Auto Sync to QBO (only for active QuickBooks integrations) | [optional] [default to null] |
| **tribute\_name** | **String** | The name of tribute. Values: \&quot;Honorary - General\&quot;, \&quot;Memorial - General\&quot;, or a pre-defined named tribute | [optional] [default to null] |
| **tributee\_name** | **String** | The name of the honoree/deceased | [optional] [default to null] |
| **tribute\_dedication** | **String** | The tribute dedication note/text for a gift | [optional] [default to null] |
| **tribute\_recipient\_name** | **String** | The name of person who should be notified about this tribute gift. | [optional] [default to null] |
| **tribute\_recipient\_salutation** | **String** | The name of person who should be notified about this tribute gift. | [optional] [default to null] |
| **tribute\_recipient\_email** | **String** | The email of the person who should be notified about this tribute gift. | [optional] [default to null] |
| **tribute\_recipient\_address** | **String** | The address of the person who should be notified about this tribute gift. | [optional] [default to null] |
| **tribute\_recipient\_notification\_template** | **String** | The notification template to be used for the person who should be notified about this tribute gift. | [optional] [default to null] |
| **team\_member** | **String** | Team Member (&#39;id&#39;, &#39;email&#39;, or &#39;first_name last_name&#39;) | [optional] [default to null] |
| **custom\_fields** | [**List**](CustomFieldAggregatedUpdate.md) | Gift custom fields (Categories) | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

