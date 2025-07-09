Gifts Management
----------------

GET /api/v1/constituents/{constituent\_id}/gifts - Fetch Gifts
--------------------------------------------------------------

Lists all the gifts.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1180.23281787276158727              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example - Fetch Gifts for a Constituent:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/gifts

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 4,
  "total_items": 4,
  "limit": 25,
  "offset": 0,
  "item_type": "gift",
  "items": [
    {
      "id": 894485,
      "constituent_id": 959480,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "amount": 250.0,
      "date": "2023-03-18",
      "created_at": "2023-09-18T18:25:01Z",
      "updated_at": "2023-09-18T18:25:01Z"
    },
    {
      "id": 894486,
      "constituent_id": 959480,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "amount": 100.0,
      "date": "2021-02-18",
      "created_at": "2023-09-18T18:25:01Z",
      "updated_at": "2023-09-18T18:25:01Z"
    },
    {
      "id": 894487,
      "constituent_id": 959480,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "amount": 200.0,
      "date": "2020-03-18",
      "created_at": "2023-09-18T18:25:02Z",
      "updated_at": "2023-09-18T18:25:02Z"
    },
    {
      "id": 894488,
      "constituent_id": 959480,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "amount": 50.0,
      "date": "2019-08-18",
      "created_at": "2023-09-18T18:25:02Z",
      "updated_at": "2023-09-18T18:25:02Z"
    }
  ]
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/gifts - Create new Gift
-------------------------------------------------------------------

Add gift.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|constituent_id|Constituent Id|integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

external\_id ( integer , optional ): External Gift ID,

is\_anon ( boolean , optional ): Gift is Anonymous?,

gift\_type\_id ( integer , required ): Gift type ID,

gift\_type\_name ( string , required ): Gift type name,

gift\_category\_id ( integer , optional ): Gift category ID,

gift\_category\_name ( string , optional ): Gift category name,

campaign\_id ( integer , optional ): Campaign ID,

campaign\_name ( string , optional ): Campaign name,

fund\_id ( integer , optional ): Fund ID,

fund\_name ( string , optional ): Fund name,

appeal\_id ( integer , optional ): Appeal ID,

appeal\_name ( string , optional ): Appeal name,

event\_id ( integer , optional ): Event ID,

event\_name ( string , optional ): Event name,

received\_amount ( double , optional ): Gift amount,

received\_date ( date , optional ): Gift date,

payment\_type\_id ( integer , optional ): Payment type ID,

payment\_type\_name ( string , optional ): Payment type name,

check\_number ( string , optional ): Check/Reference No.,

deductible\_amount ( double , optional ): Tax deductible amount,

note ( string , optional ): Gift note,

ack\_template\_name ( string , optional ): Ack. mailing template name. (use 'do\_not\_ack' to indicate no acknowledgment),

deposit\_date ( date , optional ): Deposit Date,

deposited\_amount ( double , optional ): Deposit Amount,

parent\_gift\_id ( integer , optional ): LGL parent gift ID,

parent\_external\_id ( integer , optional ): External parent gift ID,

auto\_sync\_to\_qbo ( boolean , optional ): Auto Sync to QBO (only for active QuickBooks integrations),

tribute\_name ( string , optional ): The name of tribute. Values: "Honorary - General", "Memorial - General", or a pre-defined named tribute,

tributee\_name ( string , optional ): The name of the honoree/deceased,

tribute\_dedication ( string , optional ): The tribute dedication note/text for a gift,

tribute\_recipient\_name ( string , optional ): The name of person who should be notified about this tribute gift.,

tribute\_recipient\_salutation ( string , optional ): The name of person who should be notified about this tribute gift.,

tribute\_recipient\_email ( string , optional ): The email of the person who should be notified about this tribute gift.,

tribute\_recipient\_address ( string , optional ): The address of the person who should be notified about this tribute gift.,

tribute\_recipient\_notification\_template ( string , optional ): The notification template to be used for the person who should be notified about this tribute gift.,

team\_member ( string , optional ): Team Member ('id', 'email', or 'first\_name last\_name'),

custom\_fields ( array , optional , CustomFieldAggregatedUpdate ): Gift custom fields (Categories)

}

CustomFieldAggregatedUpdate {

id ( integer , optional ): Custom Field Id,

name ( string , required ): Name,

key ( string , optional ): Key,

remove\_previous\_values ( boolean , optional ): Remove previous field values,

values ( array , required , CustomValueAggregatedUpdate ): Values

}

CustomValueAggregatedUpdate {

id ( integer , required ): Value Id,

name ( string , required ): Name

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1200.4874009666903991              
* Code: 400
  * Message: Bad Request
  * Response: 
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 
* Code: 422
  * Message: Unprocessable Entity
  * Response: 


### Example - Create Gift with Custom Field:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/gifts

Body:

```
                  
{
  "gift_type_name": "Gift",
  "gift_category_name": "Donation",
  "campaign_name": "Annual Giving",
  "fund_name": "General",
  "appeal_name": "Annual Appeal 2020",
  "received_amount": 100,
  "received_date": "2021-07-01",
  "payment_type_name": "Credit Card",
  "deductible_amount": 100,
  "note": "See other note",
  "ack_template_name": "Donation Acknowledgment",
  "deposit_date": "2021-07-01",
  "deposited_amount": 100,
  "team_member": "1047042",
  "custom_fields": [
    {
      "name": "Test Gift Field #2",
      "values": [
        {
          "name": "v1"
        }
      ]
    }
  ]
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 894819,
  "constituent_id": 959480,
  "external_id": null,
  "is_anon": false,
  "gift_type_id": 1,
  "gift_type_name": "Gift",
  "gift_category_id": 5937,
  "gift_category_name": "Donation",
  "campaign_id": 822,
  "campaign_name": "Annual Giving",
  "fund_id": 2398,
  "fund_name": "General",
  "appeal_id": 2663,
  "appeal_name": "Annual Appeal 2020",
  "event_id": 0,
  "event_name": null,
  "received_amount": 100.0,
  "received_date": "2021-07-01",
  "payment_type_id": 1509,
  "payment_type_name": "Credit Card",
  "check_number": null,
  "deductible_amount": 100.0,
  "note": "See other note",
  "ack_template_name": "Donation Acknowledgment",
  "deposit_date": "2021-07-01",
  "deposited_amount": 100.0,
  "parent_gift_id": null,
  "parent_external_id": null,
  "tribute_name": null,
  "tributee_name": null,
  "tribute_dedication": null,
  "tribute_recipient_name": null,
  "tribute_recipient_salutation": null,
  "tribute_recipient_email": null,
  "tribute_recipient_address": null,
  "tribute_recipient_notification_template": null,
  "team_member": "Nick Bicknell",
  "team_member_email": "team_member@example.com",
  "custom_fields": [
    {
      "id": 1056,
      "item_type": "Gift",
      "name": "Test Gift Field #2",
      "key": "e0c9cb38_48e9_4515_abde_72a6d93722e6",
      "facet_type": "list",
      "ordinal": 100,
      "removable": true,
      "editable": true,
      "values": [
        {
          "id": 12252,
          "category_id": 1056,
          "name": "v1",
          "description": null,
          "short_code": null,
          "ordinal": 100,
          "removable": true,
          "can_change": true,
          "can_select": true
        }
      ]
    }
  ],
  "created_at": "2025-06-03T17:08:40Z",
  "updated_at": "2025-06-03T17:08:40Z"
}
                
```


### Example - Create Gift with Tribute:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/gifts

Body:

```
                  
{
  "gift_type_name": "Gift",
  "gift_category_name": "Donation",
  "received_amount": 101,
  "received_date": "2021-07-02",
  "ack_template_name": "Donation Acknowledgment",
  "team_member": "1047042",
  "tribute_name": "Honorary - General",
  "tributee_name": "Mr. Rogers",
  "tribute_dedication": "Yes. I'll be your neighbor.",
  "tribute_recipient_name": "Ron Howard",
  "tribute_recipient_salutation": "Ron",
  "tribute_recipient_email": "rh@example.com",
  "tribute_recipient_notification_template": "Honorary Notification"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 894820,
  "constituent_id": 959480,
  "external_id": null,
  "is_anon": false,
  "gift_type_id": 1,
  "gift_type_name": "Gift",
  "gift_category_id": 5937,
  "gift_category_name": "Donation",
  "campaign_id": 0,
  "campaign_name": null,
  "fund_id": 0,
  "fund_name": null,
  "appeal_id": 0,
  "appeal_name": null,
  "event_id": 0,
  "event_name": null,
  "received_amount": 101.0,
  "received_date": "2021-07-02",
  "payment_type_id": null,
  "payment_type_name": null,
  "check_number": null,
  "deductible_amount": 101.0,
  "note": null,
  "ack_template_name": "Donation Acknowledgment",
  "deposit_date": "2021-07-02",
  "deposited_amount": 101.0,
  "parent_gift_id": null,
  "parent_external_id": null,
  "tribute_name": "Honorary - General",
  "tributee_name": "Mr. Rogers",
  "tribute_dedication": "Yes. I'll be your neighbor.",
  "tribute_recipient_name": "Ron Howard",
  "tribute_recipient_salutation": "Ron",
  "tribute_recipient_email": "rh@example.com",
  "tribute_recipient_address": null,
  "tribute_recipient_notification_template": "Honorary Notification",
  "team_member": "Nick Bicknell",
  "team_member_email": "team_member@example.com",
  "custom_fields": [

  ],
  "created_at": "2025-06-03T17:08:41Z",
  "updated_at": "2025-06-03T17:08:41Z"
}
                
```


* * *

GET /api/v1/gifts/search - Search for Gifts
-------------------------------------------

Search for active gifts



* Parameter Name: q[]
  * Description: Query string. (EX: updated_from=2016-01-01). Parameter value must be URL encoded.
  * Type: string
  * Required?: true
  * Parameter Type: query
* Parameter Name: expand
  * Description: Expand requested, comma separated, data structures: 'external_constituent_id, first_name, last_name, org_name, phone_numbers, email_addresses, street_addresses'
  * Type: string
  * Required?: 
  * Parameter Type: query
* Parameter Name: sort
  * Description: Sort by one of the following fields: 'name, gift_amount, date, date_created, date_updated, fund, appeal, campaign, gift_type'. Add an exclamation point to reverse the order. (EX: sort=name!)
  * Type: string
  * Required?: 
  * Parameter Type: query
* Parameter Name: limit
  * Description: Number of entries to return. Default: 25
  * Type: integer
  * Required?: 
  * Parameter Type: query
* Parameter Name: offset
  * Description: Start at given entry. Default: 0
  * Type: integer
  * Required?: 
  * Parameter Type: query




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1250.7853561954957942              
* Code: 400
  * Message: Bad Request
  * Response: 
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Available Search Terms:


|Gift Date        |date_from        |"YYYY-MM-DD"                            |
|-----------------|-----------------|----------------------------------------|
|                 |date_to          |"YYYY-MM-DD"                            |
|Gift Types       |gift_types       |"op|comma sep type IDs"                 |
|                 |                 |operators: in,ni                        |
|Amount           |gift_amount      |"op|number[|number2]"                   |
|                 |                 |operators: gte,lte,btw,gt,lt,eq,ne      |
|Payment Types    |payment_types    |"op|comma sep type IDs"                 |
|                 |                 |operators: in,ni,bl                     |
|Campaigns        |campaigns        |"op|comma sep campaign IDs"             |
|                 |                 |operators: in,ni,bl                     |
|Funds            |funds            |"op|comma sep fund IDs"                 |
|                 |                 |operators: in,ni,bl                     |
|Appeals          |appeals          |"op|comma sep appeal IDs"               |
|                 |                 |operators: in,ni,bl                     |
|Appeal Type      |appeal_types     |"op|comma sep type IDs"                 |
|                 |                 |operators: in,ni                        |
|Events           |events           |"op|comma sep event IDs"                |
|                 |                 |operators: in,ni,bl                     |
|Event Type       |event_types      |"op|comma sep type IDs"                 |
|                 |                 |operators: in,ni                        |
|Gift Categories  |categories       |"op|comma sep cat IDs"                  |
|                 |                 |operators: in,ni,bl                     |
|Gift IDs         |gift_ids         |"comma sep gift IDs"                    |
|External Gift IDs|external_gift_ids|"comma sep ext gift IDs"                |
|Creation Date    |created_from     |Date created from (YYYY-MM-DDTHH:MM:SSZ)|
|                 |created_to       |Date created to (YYYY-MM-DDTHH:MM:SSZ)  |
|Updated Date     |updated_from     |Date updated from (YYYY-MM-DDTHH:MM:SSZ)|
|                 |updated_to       |Date updated to (YYYY-MM-DDTHH:MM:SSZ)  |


Note: Multiple terms may be combined using a semi-colon: "updated\_from=2018-05-04;updated\_to=2018-05-04"

### Example - Search by Between Amounts:

URI: https://api.littlegreenlight.com/api/v1/gifts/search

Query:

```
q[]=gift_amount=btw|100|1000&limit=5
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 5,
  "total_items": 232,
  "limit": 5,
  "offset": 0,
  "next_item": 5,
  "next_link": "https://api.littlegreenlight.com/api/v1/gifts/search?limit=5&offset=5&q%5B%5D=gift_amount%3Dbtw%7C100%7C1000",
  "item_type": "gift",
  "items": [
    {
      "id": 894311,
      "constituent_id": 959438,
      "external_id": "lgl_sample_data-12",
      "is_anon": false,
      "gift_type_id": 13,
      "gift_type_name": "Installment",
      "gift_category_id": 0,
      "gift_category_name": null,
      "campaign_id": 0,
      "campaign_name": null,
      "fund_id": 0,
      "fund_name": null,
      "appeal_id": 0,
      "appeal_name": null,
      "event_id": 0,
      "event_name": null,
      "received_amount": 200.0,
      "received_date": null,
      "payment_type_id": null,
      "payment_type_name": null,
      "check_number": null,
      "deductible_amount": 0.0,
      "note": null,
      "ack_template_name": null,
      "deposit_date": null,
      "deposited_amount": 200.0,
      "parent_gift_id": 894305,
      "parent_external_id": "pledge001",
      "tribute_name": null,
      "tributee_name": null,
      "tribute_dedication": null,
      "tribute_recipient_name": null,
      "tribute_recipient_salutation": null,
      "tribute_recipient_email": null,
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": null,
      "team_member": null,
      "team_member_email": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-18T18:24:34Z",
      "updated_at": "2023-09-18T18:24:34Z"
    },
    {
      "id": 894422,
      "constituent_id": 959466,
      "external_id": "lgl_sample_data-123",
      "is_anon": false,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "gift_category_id": 5937,
      "gift_category_name": "Donation",
      "campaign_id": 819,
      "campaign_name": "Annual Giving (sample)",
      "fund_id": 2395,
      "fund_name": "Unrestricted (sample)",
      "appeal_id": 2660,
      "appeal_name": "Board Mailing (sample)",
      "event_id": 0,
      "event_name": null,
      "received_amount": 600.0,
      "received_date": "2023-09-17",
      "payment_type_id": 1508,
      "payment_type_name": "Check",
      "check_number": "6450",
      "deductible_amount": 600.0,
      "note": null,
      "ack_template_name": null,
      "deposit_date": "2023-09-17",
      "deposited_amount": 600.0,
      "parent_gift_id": null,
      "parent_external_id": null,
      "tribute_name": null,
      "tributee_name": null,
      "tribute_dedication": null,
      "tribute_recipient_name": null,
      "tribute_recipient_salutation": null,
      "tribute_recipient_email": null,
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": null,
      "team_member": null,
      "team_member_email": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-18T18:24:51Z",
      "updated_at": "2023-09-18T18:24:51Z"
    },
    {
      "id": 894400,
      "constituent_id": 959460,
      "external_id": "lgl_sample_data-101",
      "is_anon": false,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "gift_category_id": 5937,
      "gift_category_name": "Donation",
      "campaign_id": 819,
      "campaign_name": "Annual Giving (sample)",
      "fund_id": 2395,
      "fund_name": "Unrestricted (sample)",
      "appeal_id": 2660,
      "appeal_name": "Board Mailing (sample)",
      "event_id": 0,
      "event_name": null,
      "received_amount": 500.0,
      "received_date": "2023-09-17",
      "payment_type_id": 1508,
      "payment_type_name": "Check",
      "check_number": "8070",
      "deductible_amount": 500.0,
      "note": "Example of a gift note",
      "ack_template_name": null,
      "deposit_date": "2023-09-17",
      "deposited_amount": 500.0,
      "parent_gift_id": null,
      "parent_external_id": null,
      "tribute_name": null,
      "tributee_name": null,
      "tribute_dedication": null,
      "tribute_recipient_name": null,
      "tribute_recipient_salutation": null,
      "tribute_recipient_email": null,
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": null,
      "team_member": null,
      "team_member_email": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-18T18:24:48Z",
      "updated_at": "2023-09-18T18:24:48Z"
    },
    {
      "id": 894310,
      "constituent_id": 959438,
      "external_id": "lgl_sample_data-11",
      "is_anon": false,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "gift_category_id": 5937,
      "gift_category_name": "Donation",
      "campaign_id": 819,
      "campaign_name": "Annual Giving (sample)",
      "fund_id": 2395,
      "fund_name": "Unrestricted (sample)",
      "appeal_id": 2660,
      "appeal_name": "Board Mailing (sample)",
      "event_id": 0,
      "event_name": null,
      "received_amount": 200.0,
      "received_date": "2023-09-17",
      "payment_type_id": 1508,
      "payment_type_name": "Check",
      "check_number": "8416",
      "deductible_amount": 200.0,
      "note": "Example of a gift note",
      "ack_template_name": null,
      "deposit_date": "2023-09-17",
      "deposited_amount": 200.0,
      "parent_gift_id": 894305,
      "parent_external_id": "pledge001",
      "tribute_name": null,
      "tributee_name": null,
      "tribute_dedication": null,
      "tribute_recipient_name": null,
      "tribute_recipient_salutation": null,
      "tribute_recipient_email": null,
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": null,
      "team_member": null,
      "team_member_email": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-18T18:24:34Z",
      "updated_at": "2023-09-18T18:24:34Z"
    },
    {
      "id": 894415,
      "constituent_id": 959464,
      "external_id": "lgl_sample_data-116",
      "is_anon": false,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "gift_category_id": 5937,
      "gift_category_name": "Donation",
      "campaign_id": 819,
      "campaign_name": "Annual Giving (sample)",
      "fund_id": 2395,
      "fund_name": "Unrestricted (sample)",
      "appeal_id": 2660,
      "appeal_name": "Board Mailing (sample)",
      "event_id": 0,
      "event_name": null,
      "received_amount": 130.0,
      "received_date": "2023-09-17",
      "payment_type_id": 1508,
      "payment_type_name": "Check",
      "check_number": "9720",
      "deductible_amount": 130.0,
      "note": null,
      "ack_template_name": null,
      "deposit_date": "2023-09-17",
      "deposited_amount": 130.0,
      "parent_gift_id": null,
      "parent_external_id": null,
      "tribute_name": null,
      "tributee_name": null,
      "tribute_dedication": null,
      "tribute_recipient_name": null,
      "tribute_recipient_salutation": null,
      "tribute_recipient_email": null,
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": null,
      "team_member": null,
      "team_member_email": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-18T18:24:50Z",
      "updated_at": "2023-09-18T18:24:50Z"
    }
  ]
}
                
```


### Example - Search by Gift Types and Updated Since, Sort by Date Updated:

URI: https://api.littlegreenlight.com/api/v1/gifts/search

Query:

```
q[]=gift_types=in|1,7;updated_from=2023-01-01&sort=date_updated!&limit=5
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 5,
  "total_items": 363,
  "limit": 5,
  "offset": 0,
  "next_item": 5,
  "next_link": "https://api.littlegreenlight.com/api/v1/gifts/search?limit=5&offset=5&q%5B%5D=gift_types%3Din%7C1%2C7%3Bupdated_from%3D2023-01-01&sort=date_updated%21",
  "item_type": "gift",
  "items": [
    {
      "id": 894820,
      "constituent_id": 959480,
      "external_id": null,
      "is_anon": false,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "gift_category_id": 5937,
      "gift_category_name": "Donation",
      "campaign_id": 0,
      "campaign_name": null,
      "fund_id": 0,
      "fund_name": null,
      "appeal_id": 0,
      "appeal_name": null,
      "event_id": 0,
      "event_name": null,
      "received_amount": 101.0,
      "received_date": "2021-07-02",
      "payment_type_id": null,
      "payment_type_name": null,
      "check_number": null,
      "deductible_amount": 101.0,
      "note": null,
      "ack_template_name": "Donation Acknowledgment",
      "deposit_date": "2021-07-02",
      "deposited_amount": 101.0,
      "parent_gift_id": null,
      "parent_external_id": null,
      "tribute_name": "Honorary - General",
      "tributee_name": "Mr. Rogers",
      "tribute_dedication": "Yes. I'll be your neighbor.",
      "tribute_recipient_name": "Ron Howard",
      "tribute_recipient_salutation": "Ron",
      "tribute_recipient_email": "rh@example.com",
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": "Honorary Notification",
      "team_member": "Nick Bicknell",
      "team_member_email": "team_member@example.com",
      "custom_fields": [

      ],
      "created_at": "2025-06-03T17:08:41Z",
      "updated_at": "2025-06-03T17:08:41Z"
    },
    {
      "id": 894819,
      "constituent_id": 959480,
      "external_id": null,
      "is_anon": false,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "gift_category_id": 5937,
      "gift_category_name": "Donation",
      "campaign_id": 822,
      "campaign_name": "Annual Giving",
      "fund_id": 2398,
      "fund_name": "General",
      "appeal_id": 2663,
      "appeal_name": "Annual Appeal 2020",
      "event_id": 0,
      "event_name": null,
      "received_amount": 100.0,
      "received_date": "2021-07-01",
      "payment_type_id": 1509,
      "payment_type_name": "Credit Card",
      "check_number": null,
      "deductible_amount": 100.0,
      "note": "See other note",
      "ack_template_name": "Donation Acknowledgment",
      "deposit_date": "2021-07-01",
      "deposited_amount": 100.0,
      "parent_gift_id": null,
      "parent_external_id": null,
      "tribute_name": null,
      "tributee_name": null,
      "tribute_dedication": null,
      "tribute_recipient_name": null,
      "tribute_recipient_salutation": null,
      "tribute_recipient_email": null,
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": null,
      "team_member": "Nick Bicknell",
      "team_member_email": "team_member@example.com",
      "custom_fields": [
        {
          "id": 1056,
          "item_type": "Gift",
          "name": "Test Gift Field #2",
          "key": "e0c9cb38_48e9_4515_abde_72a6d93722e6",
          "facet_type": "list",
          "ordinal": 100,
          "removable": true,
          "editable": true,
          "values": [
            {
              "id": 12252,
              "category_id": 1056,
              "name": "v1",
              "description": null,
              "short_code": null,
              "ordinal": 100,
              "removable": true,
              "can_change": true,
              "can_select": true
            }
          ]
        }
      ],
      "created_at": "2025-06-03T17:08:40Z",
      "updated_at": "2025-06-03T17:08:40Z"
    },
    {
      "id": 894660,
      "constituent_id": 959520,
      "external_id": "lgl_sample_data-362",
      "is_anon": false,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "gift_category_id": 5937,
      "gift_category_name": "Donation",
      "campaign_id": 819,
      "campaign_name": "Annual Giving (sample)",
      "fund_id": 2395,
      "fund_name": "Unrestricted (sample)",
      "appeal_id": 2660,
      "appeal_name": "Board Mailing (sample)",
      "event_id": 0,
      "event_name": null,
      "received_amount": 80.0,
      "received_date": "2022-04-18",
      "payment_type_id": 1508,
      "payment_type_name": "Check",
      "check_number": "6080",
      "deductible_amount": 80.0,
      "note": null,
      "ack_template_name": null,
      "deposit_date": "2022-04-18",
      "deposited_amount": 80.0,
      "parent_gift_id": null,
      "parent_external_id": null,
      "tribute_name": null,
      "tributee_name": null,
      "tribute_dedication": null,
      "tribute_recipient_name": null,
      "tribute_recipient_salutation": null,
      "tribute_recipient_email": null,
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": null,
      "team_member": null,
      "team_member_email": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-18T18:25:34Z",
      "updated_at": "2023-09-18T18:25:34Z"
    },
    {
      "id": 894661,
      "constituent_id": 959520,
      "external_id": "lgl_sample_data-363",
      "is_anon": false,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "gift_category_id": 5937,
      "gift_category_name": "Donation",
      "campaign_id": 819,
      "campaign_name": "Annual Giving (sample)",
      "fund_id": 2395,
      "fund_name": "Unrestricted (sample)",
      "appeal_id": 2660,
      "appeal_name": "Board Mailing (sample)",
      "event_id": 0,
      "event_name": null,
      "received_amount": 50.0,
      "received_date": "2021-06-18",
      "payment_type_id": 1508,
      "payment_type_name": "Check",
      "check_number": "6200",
      "deductible_amount": 50.0,
      "note": null,
      "ack_template_name": null,
      "deposit_date": "2021-06-18",
      "deposited_amount": 50.0,
      "parent_gift_id": null,
      "parent_external_id": null,
      "tribute_name": null,
      "tributee_name": null,
      "tribute_dedication": null,
      "tribute_recipient_name": null,
      "tribute_recipient_salutation": null,
      "tribute_recipient_email": null,
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": null,
      "team_member": null,
      "team_member_email": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-18T18:25:34Z",
      "updated_at": "2023-09-18T18:25:34Z"
    },
    {
      "id": 894659,
      "constituent_id": 959520,
      "external_id": "lgl_sample_data-361",
      "is_anon": false,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "gift_category_id": 5937,
      "gift_category_name": "Donation",
      "campaign_id": 820,
      "campaign_name": "Capital Campaign (sample)",
      "fund_id": 2396,
      "fund_name": "New Building (sample)",
      "appeal_id": 2662,
      "appeal_name": "Major Donor Email (sample)",
      "event_id": 0,
      "event_name": null,
      "received_amount": 45.0,
      "received_date": "2023-02-18",
      "payment_type_id": 1508,
      "payment_type_name": "Check",
      "check_number": "9850",
      "deductible_amount": 45.0,
      "note": null,
      "ack_template_name": null,
      "deposit_date": "2023-02-18",
      "deposited_amount": 45.0,
      "parent_gift_id": null,
      "parent_external_id": null,
      "tribute_name": null,
      "tributee_name": null,
      "tribute_dedication": null,
      "tribute_recipient_name": null,
      "tribute_recipient_salutation": null,
      "tribute_recipient_email": null,
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": null,
      "team_member": null,
      "team_member_email": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-18T18:25:34Z",
      "updated_at": "2023-09-18T18:25:34Z"
    }
  ]
}
                
```


### Example - Search by Gift Types and Updated Since, Expand First Name, Last Name, Org Name, Address, Phone, and Email Records:

URI: https://api.littlegreenlight.com/api/v1/gifts/search

Query:

```
q[]=gift_types=in|1,7;updated_from=2023-01-01&expand=first_name, last_name, org_name, street_addresses, phone_numbers, email_addresses&limit=3
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 3,
  "total_items": 363,
  "limit": 3,
  "offset": 0,
  "next_item": 3,
  "next_link": "https://api.littlegreenlight.com/api/v1/gifts/search?limit=3&offset=3&q%5B%5D=gift_types%3Din%7C1%2C7%3Bupdated_from%3D2023-01-01",
  "item_type": "gift",
  "items": [
    {
      "id": 894422,
      "constituent_id": 959466,
      "external_id": "lgl_sample_data-123",
      "is_anon": false,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "gift_category_id": 5937,
      "gift_category_name": "Donation",
      "campaign_id": 819,
      "campaign_name": "Annual Giving (sample)",
      "fund_id": 2395,
      "fund_name": "Unrestricted (sample)",
      "appeal_id": 2660,
      "appeal_name": "Board Mailing (sample)",
      "event_id": 0,
      "event_name": null,
      "received_amount": 600.0,
      "received_date": "2023-09-17",
      "payment_type_id": 1508,
      "payment_type_name": "Check",
      "check_number": "6450",
      "deductible_amount": 600.0,
      "note": null,
      "ack_template_name": null,
      "deposit_date": "2023-09-17",
      "deposited_amount": 600.0,
      "parent_gift_id": null,
      "parent_external_id": null,
      "tribute_name": null,
      "tributee_name": null,
      "tribute_dedication": null,
      "tribute_recipient_name": null,
      "tribute_recipient_salutation": null,
      "tribute_recipient_email": null,
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": null,
      "team_member": null,
      "team_member_email": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-18T18:24:51Z",
      "updated_at": "2023-09-18T18:24:51Z",
      "first_name": null,
      "last_name": "Taylor",
      "org_name": "Home Improvement",
      "street_addresses": [
        {
          "id": 838365,
          "street": "510 Glenview",
          "city": "Detroit",
          "state": "MI",
          "country": "US",
          "postal_code": "48239",
          "county": null,
          "street_address_type_id": 1,
          "street_type_name": "Home",
          "is_preferred": true,
          "not_current": false,
          "parent_id": null,
          "seasonal_from": "01-01",
          "seasonal_to": "12-31",
          "seasonal": null,
          "lat": null,
          "lng": null,
          "zip5": "48239",
          "verified": false,
          "verified_on": null,
          "created_at": "2023-09-18T18:24:51Z",
          "updated_at": "2023-09-18T18:24:51Z"
        }
      ],
      "phone_numbers": [
        {
          "id": 479613,
          "number": "(888) 555-0030",
          "phone_number_type_id": 1,
          "phone_type_name": "Home",
          "is_preferred": true,
          "not_current": false,
          "parent_id": null,
          "normalized_number": "8885550030",
          "created_at": "2023-09-18T18:24:51Z",
          "updated_at": "2023-09-18T18:24:51Z"
        }
      ],
      "email_addresses": [
        {
          "id": 276450,
          "address": "taylor@homeimprovement.com",
          "email_address_type_id": 1,
          "email_type_name": "Home",
          "is_preferred": true,
          "not_current": false,
          "parent_id": null,
          "created_at": "2023-09-18T18:24:51Z",
          "updated_at": "2023-09-18T18:24:51Z"
        }
      ]
    },
    {
      "id": 894400,
      "constituent_id": 959460,
      "external_id": "lgl_sample_data-101",
      "is_anon": false,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "gift_category_id": 5937,
      "gift_category_name": "Donation",
      "campaign_id": 819,
      "campaign_name": "Annual Giving (sample)",
      "fund_id": 2395,
      "fund_name": "Unrestricted (sample)",
      "appeal_id": 2660,
      "appeal_name": "Board Mailing (sample)",
      "event_id": 0,
      "event_name": null,
      "received_amount": 500.0,
      "received_date": "2023-09-17",
      "payment_type_id": 1508,
      "payment_type_name": "Check",
      "check_number": "8070",
      "deductible_amount": 500.0,
      "note": "Example of a gift note",
      "ack_template_name": null,
      "deposit_date": "2023-09-17",
      "deposited_amount": 500.0,
      "parent_gift_id": null,
      "parent_external_id": null,
      "tribute_name": null,
      "tributee_name": null,
      "tribute_dedication": null,
      "tribute_recipient_name": null,
      "tribute_recipient_salutation": null,
      "tribute_recipient_email": null,
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": null,
      "team_member": null,
      "team_member_email": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-18T18:24:48Z",
      "updated_at": "2023-09-18T18:24:48Z",
      "first_name": null,
      "last_name": "Tanner",
      "org_name": "Full House",
      "street_addresses": [
        {
          "id": 838359,
          "street": "1882 Gerard Street",
          "city": "San Francisco",
          "state": "CA",
          "country": "US",
          "postal_code": "94102",
          "county": null,
          "street_address_type_id": 1,
          "street_type_name": "Home",
          "is_preferred": true,
          "not_current": false,
          "parent_id": null,
          "seasonal_from": "01-01",
          "seasonal_to": "12-31",
          "seasonal": null,
          "lat": null,
          "lng": null,
          "zip5": "94102",
          "verified": false,
          "verified_on": null,
          "created_at": "2023-09-18T18:24:47Z",
          "updated_at": "2023-09-18T18:24:47Z"
        }
      ],
      "phone_numbers": [
        {
          "id": 479607,
          "number": "(888) 555-0024",
          "phone_number_type_id": 1,
          "phone_type_name": "Home",
          "is_preferred": true,
          "not_current": false,
          "parent_id": null,
          "normalized_number": "8885550024",
          "created_at": "2023-09-18T18:24:47Z",
          "updated_at": "2023-09-18T18:24:47Z"
        }
      ],
      "email_addresses": [
        {
          "id": 276444,
          "address": "tanner@fullhouse.com",
          "email_address_type_id": 1,
          "email_type_name": "Home",
          "is_preferred": true,
          "not_current": false,
          "parent_id": null,
          "created_at": "2023-09-18T18:24:47Z",
          "updated_at": "2023-09-18T18:24:47Z"
        }
      ]
    },
    {
      "id": 894310,
      "constituent_id": 959438,
      "external_id": "lgl_sample_data-11",
      "is_anon": false,
      "gift_type_id": 1,
      "gift_type_name": "Gift",
      "gift_category_id": 5937,
      "gift_category_name": "Donation",
      "campaign_id": 819,
      "campaign_name": "Annual Giving (sample)",
      "fund_id": 2395,
      "fund_name": "Unrestricted (sample)",
      "appeal_id": 2660,
      "appeal_name": "Board Mailing (sample)",
      "event_id": 0,
      "event_name": null,
      "received_amount": 200.0,
      "received_date": "2023-09-17",
      "payment_type_id": 1508,
      "payment_type_name": "Check",
      "check_number": "8416",
      "deductible_amount": 200.0,
      "note": "Example of a gift note",
      "ack_template_name": null,
      "deposit_date": "2023-09-17",
      "deposited_amount": 200.0,
      "parent_gift_id": 894305,
      "parent_external_id": "pledge001",
      "tribute_name": null,
      "tributee_name": null,
      "tribute_dedication": null,
      "tribute_recipient_name": null,
      "tribute_recipient_salutation": null,
      "tribute_recipient_email": null,
      "tribute_recipient_address": null,
      "tribute_recipient_notification_template": null,
      "team_member": null,
      "team_member_email": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-18T18:24:34Z",
      "updated_at": "2023-09-18T18:24:34Z",
      "first_name": "Alf",
      "last_name": "Tanner",
      "org_name": "ALF",
      "street_addresses": [
        {
          "id": 838337,
          "street": "167 Hemdale Street",
          "city": "Los Angeles",
          "state": "CA",
          "country": "US",
          "postal_code": "90001",
          "county": null,
          "street_address_type_id": 1,
          "street_type_name": "Home",
          "is_preferred": true,
          "not_current": false,
          "parent_id": null,
          "seasonal_from": "01-01",
          "seasonal_to": "12-31",
          "seasonal": null,
          "lat": null,
          "lng": null,
          "zip5": "90001",
          "verified": false,
          "verified_on": null,
          "created_at": "2023-09-18T18:24:33Z",
          "updated_at": "2023-09-18T18:24:33Z"
        }
      ],
      "phone_numbers": [
        {
          "id": 479585,
          "number": "(888) 555-0002",
          "phone_number_type_id": 3,
          "phone_type_name": "Mobile",
          "is_preferred": true,
          "not_current": false,
          "parent_id": null,
          "normalized_number": "8885550002",
          "created_at": "2023-09-18T18:24:33Z",
          "updated_at": "2023-09-18T18:24:33Z"
        }
      ],
      "email_addresses": [
        {
          "id": 276422,
          "address": "tanner@alf.com",
          "email_address_type_id": 1,
          "email_type_name": "Home",
          "is_preferred": true,
          "not_current": false,
          "parent_id": null,
          "created_at": "2023-09-18T18:24:33Z",
          "updated_at": "2023-09-18T18:24:33Z"
        }
      ]
    }
  ]
}
                
```


* * *

GET /api/v1/gifts/{id} - Show Gift details
------------------------------------------

Show details for the gift.


|Parameter Name|Description|Type   |Required?|Parameter Type|
|--------------|-----------|-------|---------|--------------|
|id            |Gift Id    |integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1320.2840392475554385              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/gifts/894819

Response:

```
                  
{
  "api_version": "1.0",
  "id": 894819,
  "constituent_id": 959480,
  "external_id": null,
  "is_anon": false,
  "gift_type_id": 1,
  "gift_type_name": "Gift",
  "gift_category_id": 5937,
  "gift_category_name": "Donation",
  "campaign_id": 822,
  "campaign_name": "Annual Giving",
  "fund_id": 2398,
  "fund_name": "General",
  "appeal_id": 2663,
  "appeal_name": "Annual Appeal 2020",
  "event_id": 0,
  "event_name": null,
  "received_amount": 100.0,
  "received_date": "2021-07-01",
  "payment_type_id": 1509,
  "payment_type_name": "Credit Card",
  "check_number": null,
  "deductible_amount": 100.0,
  "note": "See other note",
  "ack_template_name": "Donation Acknowledgment",
  "deposit_date": "2021-07-01",
  "deposited_amount": 100.0,
  "parent_gift_id": null,
  "parent_external_id": null,
  "tribute_name": null,
  "tributee_name": null,
  "tribute_dedication": null,
  "tribute_recipient_name": null,
  "tribute_recipient_salutation": null,
  "tribute_recipient_email": null,
  "tribute_recipient_address": null,
  "tribute_recipient_notification_template": null,
  "team_member": "Nick Bicknell",
  "team_member_email": "team_member@example.com",
  "custom_fields": [
    {
      "id": 1056,
      "item_type": "Gift",
      "name": "Test Gift Field #2",
      "key": "e0c9cb38_48e9_4515_abde_72a6d93722e6",
      "facet_type": "list",
      "ordinal": 100,
      "removable": true,
      "editable": true,
      "values": [
        {
          "id": 12252,
          "category_id": 1056,
          "name": "v1",
          "description": null,
          "short_code": null,
          "ordinal": 100,
          "removable": true,
          "can_change": true,
          "can_select": true
        }
      ]
    }
  ],
  "created_at": "2025-06-03T17:08:40Z",
  "updated_at": "2025-06-03T17:08:40Z"
}
                
```


* * *

PATCH /api/v1/gifts/{id} - Update Gift
--------------------------------------

Update the gift.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|id            |Gift Id       |integer   |true     |path          |
|body          |Update Objects|UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

external\_id ( integer , optional ): External Gift ID,

is\_anon ( boolean , optional ): Gift is Anonymous?,

gift\_type\_id ( integer , required ): Gift type ID,

gift\_type\_name ( string , required ): Gift type name,

gift\_category\_id ( integer , optional ): Gift category ID,

gift\_category\_name ( string , optional ): Gift category name,

campaign\_id ( integer , optional ): Campaign ID,

campaign\_name ( string , optional ): Campaign name,

fund\_id ( integer , optional ): Fund ID,

fund\_name ( string , optional ): Fund name,

appeal\_id ( integer , optional ): Appeal ID,

appeal\_name ( string , optional ): Appeal name,

event\_id ( integer , optional ): Event ID,

event\_name ( string , optional ): Event name,

received\_amount ( double , optional ): Gift amount,

received\_date ( date , optional ): Gift date,

payment\_type\_id ( integer , optional ): Payment type ID,

payment\_type\_name ( string , optional ): Payment type name,

check\_number ( string , optional ): Check/Reference No.,

deductible\_amount ( double , optional ): Tax deductible amount,

note ( string , optional ): Gift note,

ack\_template\_name ( string , optional ): Ack. mailing template name. (use 'do\_not\_ack' to indicate no acknowledgment),

deposit\_date ( date , optional ): Deposit Date,

deposited\_amount ( double , optional ): Deposit Amount,

parent\_gift\_id ( integer , optional ): LGL parent gift ID,

parent\_external\_id ( integer , optional ): External parent gift ID,

auto\_sync\_to\_qbo ( boolean , optional ): Auto Sync to QBO (only for active QuickBooks integrations),

tribute\_name ( string , optional ): The name of tribute. Values: "Honorary - General", "Memorial - General", or a pre-defined named tribute,

tributee\_name ( string , optional ): The name of the honoree/deceased,

tribute\_dedication ( string , optional ): The tribute dedication note/text for a gift,

tribute\_recipient\_name ( string , optional ): The name of person who should be notified about this tribute gift.,

tribute\_recipient\_salutation ( string , optional ): The name of person who should be notified about this tribute gift.,

tribute\_recipient\_email ( string , optional ): The email of the person who should be notified about this tribute gift.,

tribute\_recipient\_address ( string , optional ): The address of the person who should be notified about this tribute gift.,

tribute\_recipient\_notification\_template ( string , optional ): The notification template to be used for the person who should be notified about this tribute gift.,

team\_member ( string , optional ): Team Member ('id', 'email', or 'first\_name last\_name'),

custom\_fields ( array , optional , CustomFieldAggregatedUpdate ): Gift custom fields (Categories)

}

CustomFieldAggregatedUpdate {

id ( integer , optional ): Custom Field Id,

name ( string , required ): Name,

key ( string , optional ): Key,

remove\_previous\_values ( boolean , optional ): Remove previous field values,

values ( array , required , CustomValueAggregatedUpdate ): Values

}

CustomValueAggregatedUpdate {

id ( integer , required ): Value Id,

name ( string , required ): Name

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1340.24564322439559816              
* Code: 400
  * Message: Bad Request
  * Response: 
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 
* Code: 422
  * Message: Unprocessable Entity
  * Response: 


### Example - Add Event and Custom Field Value:

URI: https://api.littlegreenlight.com/api/v1/gifts/894819

Body:

```
                  
{
  "event_name": "Winter 2020 Fundraising Gala",
  "custom_fields": [
    {
      "name": "Test Gift Field #2",
      "values": [
        {
          "name": "v2"
        }
      ]
    }
  ]
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 894819,
  "constituent_id": 959480,
  "external_id": null,
  "is_anon": false,
  "gift_type_id": 1,
  "gift_type_name": "Gift",
  "gift_category_id": 5937,
  "gift_category_name": "Donation",
  "campaign_id": 822,
  "campaign_name": "Annual Giving",
  "fund_id": 2398,
  "fund_name": "General",
  "appeal_id": 2663,
  "appeal_name": "Annual Appeal 2020",
  "event_id": 1069,
  "event_name": "Winter 2020 Fundraising Gala",
  "received_amount": 100.0,
  "received_date": "2021-07-01",
  "payment_type_id": 1509,
  "payment_type_name": "Credit Card",
  "check_number": null,
  "deductible_amount": 100.0,
  "note": "See other note",
  "ack_template_name": "Donation Acknowledgment",
  "deposit_date": "2021-07-01",
  "deposited_amount": 100.0,
  "parent_gift_id": null,
  "parent_external_id": null,
  "tribute_name": null,
  "tributee_name": null,
  "tribute_dedication": null,
  "tribute_recipient_name": null,
  "tribute_recipient_salutation": null,
  "tribute_recipient_email": null,
  "tribute_recipient_address": null,
  "tribute_recipient_notification_template": null,
  "team_member": "Nick Bicknell",
  "team_member_email": "team_member@example.com",
  "custom_fields": [
    {
      "id": 1056,
      "item_type": "Gift",
      "name": "Test Gift Field #2",
      "key": "e0c9cb38_48e9_4515_abde_72a6d93722e6",
      "facet_type": "list",
      "ordinal": 100,
      "removable": true,
      "editable": true,
      "values": [
        {
          "id": 12252,
          "category_id": 1056,
          "name": "v1",
          "description": null,
          "short_code": null,
          "ordinal": 100,
          "removable": true,
          "can_change": true,
          "can_select": true
        },
        {
          "id": 12253,
          "category_id": 1056,
          "name": "v2",
          "description": null,
          "short_code": null,
          "ordinal": 100,
          "removable": true,
          "can_change": true,
          "can_select": true
        }
      ]
    }
  ],
  "created_at": "2025-06-03T17:08:40Z",
  "updated_at": "2025-06-03T17:08:42Z"
}
                
```


### Example - Replace Previous Custom Field Values with New Value:

URI: https://api.littlegreenlight.com/api/v1/gifts/894819

Body:

```
                  
{
  "custom_fields": [
    {
      "name": "Test Gift Field #2",
      "remove_previous_values": true,
      "values": [
        {
          "name": "v3"
        }
      ]
    }
  ]
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 894819,
  "constituent_id": 959480,
  "external_id": null,
  "is_anon": false,
  "gift_type_id": 1,
  "gift_type_name": "Gift",
  "gift_category_id": 5937,
  "gift_category_name": "Donation",
  "campaign_id": 822,
  "campaign_name": "Annual Giving",
  "fund_id": 2398,
  "fund_name": "General",
  "appeal_id": 2663,
  "appeal_name": "Annual Appeal 2020",
  "event_id": 1069,
  "event_name": "Winter 2020 Fundraising Gala",
  "received_amount": 100.0,
  "received_date": "2021-07-01",
  "payment_type_id": 1509,
  "payment_type_name": "Credit Card",
  "check_number": null,
  "deductible_amount": 100.0,
  "note": "See other note",
  "ack_template_name": "Donation Acknowledgment",
  "deposit_date": "2021-07-01",
  "deposited_amount": 100.0,
  "parent_gift_id": null,
  "parent_external_id": null,
  "tribute_name": null,
  "tributee_name": null,
  "tribute_dedication": null,
  "tribute_recipient_name": null,
  "tribute_recipient_salutation": null,
  "tribute_recipient_email": null,
  "tribute_recipient_address": null,
  "tribute_recipient_notification_template": null,
  "team_member": "Nick Bicknell",
  "team_member_email": "team_member@example.com",
  "custom_fields": [
    {
      "id": 1056,
      "item_type": "Gift",
      "name": "Test Gift Field #2",
      "key": "e0c9cb38_48e9_4515_abde_72a6d93722e6",
      "facet_type": "list",
      "ordinal": 100,
      "removable": true,
      "editable": true,
      "values": [
        {
          "id": 12254,
          "category_id": 1056,
          "name": "v3",
          "description": null,
          "short_code": null,
          "ordinal": 100,
          "removable": true,
          "can_change": true,
          "can_select": true
        }
      ]
    }
  ],
  "created_at": "2025-06-03T17:08:40Z",
  "updated_at": "2025-06-03T17:08:42Z"
}
                
```


* * *

DELETE /api/v1/gifts/{id} - Delete Gift
---------------------------------------

Delete the gift.


|Parameter Name|Description|Type   |Required?|Parameter Type|
|--------------|-----------|-------|---------|--------------|
|id            |Gift Id    |integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/gifts/894819

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


### Example:

URI: https://api.littlegreenlight.com/api/v1/gifts/894820

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

