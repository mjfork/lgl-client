Team Members Management
-----------------------

GET /api/v1/team\_members - Fetch Team Members
----------------------------------------------

Lists all the team members.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2580.5468530290413476              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/team\_members

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 2,
  "total_items": 2,
  "limit": 5,
  "offset": 0,
  "item_type": "team_member",
  "items": [
    {
      "id": 1047033,
      "first_name": "Tom",
      "last_name": "Talbott",
      "email": "team_member@example.com",
      "role_id": 406638,
      "is_admin": true,
      "is_primary_contact": true,
      "is_billing_contact": true
    },
    {
      "id": 1047042,
      "first_name": "Nick",
      "last_name": "Bicknell",
      "email": "team_member@example.com",
      "role_id": 406638,
      "is_admin": true,
      "is_primary_contact": false,
      "is_billing_contact": false
    }
  ]
}
                
```


* * *

