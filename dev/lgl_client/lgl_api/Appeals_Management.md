Appeals Management
------------------

GET /api/v1/appeals - Fetch Appeals
-----------------------------------

Lists all the appeals.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder130.5436477454432558              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/appeals

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 4,
  "total_items": 4,
  "limit": 5,
  "offset": 0,
  "item_type": "appeal",
  "items": [
    {
      "id": 2660,
      "name": "Board Mailing (sample)",
      "description": null,
      "date": "2019-12-18",
      "financial_goal": null,
      "projected_amount": null,
      "code": null
    },
    {
      "id": 2661,
      "name": "Alumni Mailing (sample)",
      "description": null,
      "date": "2020-10-18",
      "financial_goal": null,
      "projected_amount": null,
      "code": null
    },
    {
      "id": 2662,
      "name": "Major Donor Email (sample)",
      "description": null,
      "date": "2020-10-18",
      "financial_goal": null,
      "projected_amount": null,
      "code": null
    },
    {
      "id": 2663,
      "name": "Annual Appeal 2020",
      "description": null,
      "date": "2021-07-01",
      "financial_goal": null,
      "projected_amount": null,
      "code": null
    }
  ]
}
                
```


* * *

