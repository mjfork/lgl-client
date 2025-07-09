Campaigns Management
--------------------

GET /api/v1/campaigns - Fetch Campaigns
---------------------------------------

Lists all the campaigns.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder150.012923453152495545              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/campaigns

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 4,
  "total_items": 4,
  "limit": 5,
  "offset": 0,
  "item_type": "campaign",
  "items": [
    {
      "id": 819,
      "name": "Annual Giving (sample)",
      "description": null,
      "financial_goal": null,
      "start_date": null,
      "end_date": null,
      "code": null
    },
    {
      "id": 820,
      "name": "Capital Campaign (sample)",
      "description": null,
      "financial_goal": null,
      "start_date": null,
      "end_date": null,
      "code": null
    },
    {
      "id": 821,
      "name": "Scholarship (sample)",
      "description": null,
      "financial_goal": null,
      "start_date": null,
      "end_date": null,
      "code": null
    },
    {
      "id": 822,
      "name": "Annual Giving",
      "description": null,
      "financial_goal": null,
      "start_date": null,
      "end_date": null,
      "code": null
    }
  ]
}
                
```


* * *

