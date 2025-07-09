Funds Management
----------------

GET /api/v1/funds - Fetch Funds
-------------------------------

Lists all the funds.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1120.9390841642915893              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/funds

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 4,
  "total_items": 4,
  "limit": 5,
  "offset": 0,
  "item_type": "fund",
  "items": [
    {
      "id": 2395,
      "name": "Unrestricted (sample)",
      "description": null,
      "code": null,
      "start_date": null,
      "end_date": null,
      "financial_goal": null
    },
    {
      "id": 2396,
      "name": "New Building (sample)",
      "description": null,
      "code": null,
      "start_date": null,
      "end_date": null,
      "financial_goal": null
    },
    {
      "id": 2397,
      "name": "Memorial Fund (sample)",
      "description": null,
      "code": null,
      "start_date": null,
      "end_date": null,
      "financial_goal": null
    },
    {
      "id": 2398,
      "name": "General",
      "description": null,
      "code": null,
      "start_date": null,
      "end_date": null,
      "financial_goal": null
    }
  ]
}
                
```


* * *

