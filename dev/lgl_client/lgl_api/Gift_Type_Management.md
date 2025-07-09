Gift Type Management
--------------------

GET /api/v1/gift\_types - Fetch Gift Types
------------------------------------------

Lists all the gift types.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1160.7649608852326744              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/gift\_types

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 5,
  "total_items": 10,
  "limit": 5,
  "offset": 0,
  "next_item": 5,
  "next_link": "https://api.littlegreenlight.com/api/v1/gift_types?limit=5&offset=5",
  "item_type": "gift_type",
  "items": [
    {
      "id": 1,
      "name": "Gift",
      "ordinal": 1
    },
    {
      "id": 5,
      "name": "Other Income",
      "ordinal": 3
    },
    {
      "id": 7,
      "name": "Pledge",
      "ordinal": 4
    },
    {
      "id": 8,
      "name": "In Kind",
      "ordinal": 2
    },
    {
      "id": 9,
      "name": "Soft Credit",
      "ordinal": 6
    }
  ]
}
                
```


* * *

