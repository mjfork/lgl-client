Gift Category Management
------------------------

GET /api/v1/gift\_categories - Fetch Gift Categories
----------------------------------------------------

Lists all the gift categories.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|gift_type_id  |Gift type ID                            |string |         |query         |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1140.6407226536631485              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/gift\_categories

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 5,
  "total_items": 14,
  "limit": 5,
  "offset": 0,
  "next_item": 5,
  "next_link": "https://api.littlegreenlight.com/api/v1/gift_categories?limit=5&offset=5",
  "item_type": "gift_category",
  "items": [
    {
      "id": 5937,
      "display_name": "Donation",
      "gift_type_id": 1,
      "gift_type_name": "Gift"
    },
    {
      "id": 5938,
      "display_name": "Matching Gift",
      "gift_type_id": 1,
      "gift_type_name": "Gift"
    },
    {
      "id": 5939,
      "display_name": "Pledge Payment",
      "gift_type_id": 1,
      "gift_type_name": "Gift"
    },
    {
      "id": 5940,
      "display_name": "Standard Pledge",
      "gift_type_id": 7,
      "gift_type_name": "Pledge"
    },
    {
      "id": 5941,
      "display_name": "Grant",
      "gift_type_id": 7,
      "gift_type_name": "Pledge"
    }
  ]
}
                
```


* * *

