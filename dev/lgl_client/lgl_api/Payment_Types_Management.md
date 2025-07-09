Payment Types Management
------------------------

GET /api/v1/payment\_types - Fetch Payment Types
------------------------------------------------

Lists all the payment types.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2320.7879988111881724              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/payment\_types

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 4,
  "total_items": 4,
  "limit": 5,
  "offset": 0,
  "item_type": "payment_type",
  "items": [
    {
      "id": 1507,
      "name": "Cash",
      "key": "cash",
      "ordinal": 0
    },
    {
      "id": 1508,
      "name": "Check",
      "key": "check",
      "ordinal": 1
    },
    {
      "id": 1509,
      "name": "Credit Card",
      "key": "credit",
      "ordinal": 2
    },
    {
      "id": 1510,
      "name": "Stock",
      "key": "stock",
      "ordinal": 3
    }
  ]
}
                
```


* * *

