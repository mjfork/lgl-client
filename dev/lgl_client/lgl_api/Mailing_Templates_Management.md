Mailing Templates Management
----------------------------

GET /api/v1/mailing\_templates - Fetch Mailing Templates
--------------------------------------------------------

Lists all the mailing templates.


|Parameter Name |Description                             |Type   |Required?|Parameter Type|
|---------------|----------------------------------------|-------|---------|--------------|
|mailing_type_id|Mailing type ID                         |string |         |query         |
|limit          |Number of entries to return. Default: 25|integer|         |query         |
|offset         |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1940.9510888756499949              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/mailing\_templates

Query:

```
mailing_type_id=1907&limit=5
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 2,
  "total_items": 2,
  "limit": 5,
  "offset": 0,
  "item_type": "mailing_template",
  "items": [
    {
      "id": 174,
      "name": "Donation Acknowledgment",
      "code": "donation_ack",
      "mailing_type_id": 1907,
      "mailing_type_name": "Acknowledgment",
      "template_type": "letter"
    },
    {
      "id": 175,
      "name": "Pledge Acknowledgment",
      "code": "pledge_ack",
      "mailing_type_id": 1907,
      "mailing_type_name": "Acknowledgment",
      "template_type": "letter"
    }
  ]
}
                
```


* * *

