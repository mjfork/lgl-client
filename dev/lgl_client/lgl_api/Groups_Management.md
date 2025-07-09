Groups Management
-----------------

GET /api/v1/groups - Fetch Groups
---------------------------------

Lists all the groups.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1500.9568732274075658              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/groups

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 4,
  "total_items": 4,
  "limit": 25,
  "offset": 0,
  "item_type": "group",
  "items": [
    {
      "id": 3240,
      "name": "Team Member",
      "key": "team_member",
      "ordinal": 0
    },
    {
      "id": 3241,
      "name": "Board Member",
      "key": "board_member",
      "ordinal": 0
    },
    {
      "id": 3242,
      "name": "Staff",
      "key": "staff",
      "ordinal": 0
    },
    {
      "id": 3243,
      "name": "Volunteer",
      "key": "volunteer",
      "ordinal": 0
    }
  ]
}
                
```


* * *

POST /api/v1/groups - Create new Group
--------------------------------------

Add group.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

name ( string , required ): Name,

key ( string , optional ): Key,

ordinal ( integer , optional ): Ordinal

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1520.03300461935484922              
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

URI: https://api.littlegreenlight.com/api/v1/groups

Body:

Response:

```
                  
{
  "api_version": "1.0",
  "id": 3322,
  "name": "New Group",
  "key": "new_group",
  "ordinal": 0
}
                
```


* * *

GET /api/v1/groups/{id} - Show Group details
--------------------------------------------

Show details for the group.


|Parameter Name|Description|Type   |Required?|Parameter Type|
|--------------|-----------|-------|---------|--------------|
|id            |Group Id   |integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1540.26467477496208813              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/groups/3322

Response:

```
                  
{
  "api_version": "1.0",
  "id": 3322,
  "name": "New Group",
  "key": "new_group",
  "ordinal": 0
}
                
```


* * *

PATCH /api/v1/groups/{id} - Update Group
----------------------------------------

Update the group.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|id            |Group Id      |integer   |true     |path          |
|body          |Update Objects|UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

name ( string , required ): Name,

key ( string , optional ): Key,

ordinal ( integer , optional ): Ordinal

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1560.006887969218564383              
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

URI: https://api.littlegreenlight.com/api/v1/groups/3322

Body:

Response:

```
                  
{
  "api_version": "1.0",
  "id": 3322,
  "name": "New Group",
  "key": "new_group",
  "ordinal": 10
}
                
```


* * *

DELETE /api/v1/groups/{id} - Delete Group
-----------------------------------------

Delete the group.


|Parameter Name|Description|Type   |Required?|Parameter Type|
|--------------|-----------|-------|---------|--------------|
|id            |Group Id   |integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/groups/3322

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

