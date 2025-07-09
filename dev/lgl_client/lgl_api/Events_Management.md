Events Management
-----------------

GET /api/v1/events - Fetch Events
---------------------------------

Lists all the events.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1100.17580176615637733              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/events

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 3,
  "total_items": 3,
  "limit": 5,
  "offset": 0,
  "item_type": "event",
  "items": [
    {
      "id": 1068,
      "name": "Fancy Lunch (sample)",
      "description": null,
      "date": "2023-09-11",
      "end_date": null,
      "financial_goal": null,
      "projected_amount": null,
      "code": null
    },
    {
      "id": 1069,
      "name": "Winter 2020 Fundraising Gala",
      "description": "",
      "date": "2021-07-01",
      "end_date": null,
      "financial_goal": null,
      "projected_amount": null,
      "code": ""
    },
    {
      "id": 1070,
      "name": "Board weekend",
      "description": "",
      "date": "2023-11-03",
      "end_date": "2023-11-05",
      "financial_goal": null,
      "projected_amount": null,
      "code": ""
    }
  ]
}
                
```


* * *

