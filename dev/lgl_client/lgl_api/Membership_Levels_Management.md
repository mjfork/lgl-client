Membership Levels Management
----------------------------

GET /api/v1/membership\_levels - Fetch Membership Levels
--------------------------------------------------------

Lists all the membership levels.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1970.7893891181890547              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/membership\_levels

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 6,
  "total_items": 6,
  "limit": 25,
  "offset": 0,
  "item_type": "membership_level",
  "items": [
    {
      "id": 386,
      "name": "General",
      "ordinal": 0
    },
    {
      "id": 387,
      "name": "Friend",
      "ordinal": 1
    },
    {
      "id": 388,
      "name": "Gold",
      "ordinal": 100
    },
    {
      "id": 389,
      "name": "Silver",
      "ordinal": 100
    },
    {
      "id": 390,
      "name": "Diamond",
      "ordinal": 100
    },
    {
      "id": 391,
      "name": "Bronze",
      "ordinal": 100
    }
  ]
}
                
```


* * *

POST /api/v1/membership\_levels - Create new Membership Level
-------------------------------------------------------------

Add membership level.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

name ( string , required ): Name,

ordinal ( integer , optional ): Ordinal

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1990.28427460575487973              
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

URI: https://api.littlegreenlight.com/api/v1/membership\_levels

Body:

```
                  
{
  "name": "Super Star",
  "ordinal": "1000"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 470,
  "name": "Super Star",
  "ordinal": 1000
}
                
```


* * *

GET /api/v1/membership\_levels/{id} - Show Membership Level details
-------------------------------------------------------------------

Show details for the membership level.


|Parameter Name|Description        |Type   |Required?|Parameter Type|
|--------------|-------------------|-------|---------|--------------|
|id            |Membership Level Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2020.7927989647428073              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/membership\_levels/470

Response:

```
                  
{
  "api_version": "1.0",
  "id": 470,
  "name": "Super Star",
  "ordinal": 1000
}
                
```


* * *

PATCH /api/v1/membership\_levels/{id} - Update Membership Level
---------------------------------------------------------------

Update the membership level.


|Parameter Name|Description        |Type      |Required?|Parameter Type|
|--------------|-------------------|----------|---------|--------------|
|id            |Membership Level Id|integer   |true     |path          |
|body          |Update Objects     |UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

name ( string , required ): Name,

ordinal ( integer , optional ): Ordinal

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2040.5227152824002674              
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

URI: https://api.littlegreenlight.com/api/v1/membership\_levels/470

Body:

```
                  
{
  "name": "Super Luminal"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 470,
  "name": "Super Luminal",
  "ordinal": 1000
}
                
```


* * *

DELETE /api/v1/membership\_levels/{id} - Delete Membership Level
----------------------------------------------------------------

Delete the membership level.


|Parameter Name|Description        |Type   |Required?|Parameter Type|
|--------------|-------------------|-------|---------|--------------|
|id            |Membership Level Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/membership\_levels/470

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

