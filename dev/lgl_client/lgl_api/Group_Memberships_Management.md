Group Memberships Management
----------------------------

GET /api/v1/group\_memberships/{id} - Show Group Membership details
-------------------------------------------------------------------

Show details for the group membership.


|Parameter Name|Description        |Type   |Required?|Parameter Type|
|--------------|-------------------|-------|---------|--------------|
|id            |Group Membership Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1410.9565273882263503              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/group\_memberships/595533

Response:

```
                  
{
  "api_version": "1.0",
  "id": 595533,
  "constituent_id": 959599,
  "group_id": 3241,
  "group_name": "Board Member",
  "date_start": null,
  "date_end": null,
  "is_current": true,
  "created_at": "2025-06-03T17:08:33Z",
  "updated_at": "2025-06-03T17:08:33Z"
}
                
```


* * *

PATCH /api/v1/group\_memberships/{id} - Update Group Membership
---------------------------------------------------------------

Update the group membership.


|Parameter Name|Description        |Type      |Required?|Parameter Type|
|--------------|-------------------|----------|---------|--------------|
|id            |Group Membership Id|integer   |true     |path          |
|body          |Update Objects     |UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

constituent\_id ( integer , optional ): Constituent Id,

group\_id ( integer , required ): Group Id,

group\_name ( string , optional ): Group Name,

date\_start ( date , optional ): Start Date,

date\_end ( date , optional ): End Date,

is\_current ( boolean , optional ): Current?

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1430.38621266102971163              
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


### Example:

URI: https://api.littlegreenlight.com/api/v1/group\_memberships/595533

Body:

```
                  
{
  "date_start": "2016-01-01"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 595533,
  "constituent_id": 959599,
  "group_id": 3241,
  "group_name": "Board Member",
  "date_start": "2016-01-01",
  "date_end": null,
  "is_current": true,
  "created_at": "2025-06-03T17:08:33Z",
  "updated_at": "2025-06-03T17:08:43Z"
}
                
```


* * *

DELETE /api/v1/group\_memberships/{id} - Delete Group Membership
----------------------------------------------------------------

Delete the group membership.


|Parameter Name|Description        |Type   |Required?|Parameter Type|
|--------------|-------------------|-------|---------|--------------|
|id            |Group Membership Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/group\_memberships/595533

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

GET /api/v1/constituents/{constituent\_id}/group\_memberships - Fetch Group Memberships
---------------------------------------------------------------------------------------

Lists all the group memberships.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1470.6336329341010987              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/group\_memberships

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 25,
  "offset": 0,
  "item_type": "group_membership",
  "items": [
    {
      "id": 595476,
      "constituent_id": 959480,
      "group_id": 3241,
      "group_name": "Board Member",
      "date_start": null,
      "date_end": null,
      "is_current": true,
      "created_at": "2023-09-19T22:24:37Z",
      "updated_at": "2023-09-19T22:24:37Z"
    }
  ]
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/group\_memberships - Create new Group Membership
--------------------------------------------------------------------------------------------

Add group membership.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|constituent_id|Constituent Id|integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

group\_id ( integer , required ): Group Id,

group\_name ( string , optional ): Group Name,

date\_start ( date , optional ): Start Date,

date\_end ( date , optional ): End Date,

is\_current ( boolean , optional ): Current?

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1490.9845986663446673              
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


* * *

