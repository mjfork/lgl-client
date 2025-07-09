Membership Management
---------------------

GET /api/v1/constituents/{constituent\_id}/memberships - Fetch Memberships
--------------------------------------------------------------------------

Lists all the memberships.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2080.526333083448399              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/memberships

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 25,
  "offset": 0,
  "item_type": "membership",
  "items": [
    {
      "id": 424,
      "constituent_id": 959480,
      "membership_level_id": 388,
      "membership_level_name": "Gold",
      "date_start": "2022-09-18",
      "finish_date": "2023-09-18",
      "note": null,
      "created_at": "2023-09-18T18:25:01Z",
      "updated_at": "2025-04-07T17:08:29Z"
    }
  ]
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/memberships - Create new Membership
-------------------------------------------------------------------------------

Add membership.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|constituent_id|Constituent Id|integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

membership\_level\_id ( integer , optional ): Membership Level ID,

membership\_level\_name ( string , optional ): Membership Level Name,

date\_start ( date , optional ): Date start,

finish\_date ( date , optional ): Date end,

note ( string , optional ): Note

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2100.28549196630962914              
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

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/memberships

Body:

```
                  
{
  "membership_level_name": "Gold",
  "date_start": "2012-01-01",
  "finish_date": "2024-01-01"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 506,
  "constituent_id": 959480,
  "membership_level_id": 388,
  "membership_level_name": "Gold",
  "date_start": "2012-01-01",
  "finish_date": "2024-01-01",
  "note": null,
  "created_at": "2025-06-03T17:08:51Z",
  "updated_at": "2025-06-03T17:08:51Z"
}
                
```


* * *

GET /api/v1/memberships/{id} - Show Membership details
------------------------------------------------------

Show details for the membership.


|Parameter Name|Description  |Type   |Required?|Parameter Type|
|--------------|-------------|-------|---------|--------------|
|id            |Membership Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2130.2762622275450455              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/memberships/506

Response:

```
                  
{
  "api_version": "1.0",
  "id": 506,
  "constituent_id": 959480,
  "membership_level_id": 388,
  "membership_level_name": "Gold",
  "date_start": "2012-01-01",
  "finish_date": "2024-01-01",
  "note": null,
  "created_at": "2025-06-03T17:08:51Z",
  "updated_at": "2025-06-03T17:08:51Z"
}
                
```


* * *

PATCH /api/v1/memberships/{id} - Update Membership
--------------------------------------------------

Update the membership.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|id            |Membership Id |integer   |true     |path          |
|body          |Update Objects|UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

membership\_level\_id ( integer , optional ): Membership Level ID,

membership\_level\_name ( string , optional ): Membership Level Name,

date\_start ( date , optional ): Date start,

finish\_date ( date , optional ): Date end,

note ( string , optional ): Note

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2150.4101025327405545              
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

URI: https://api.littlegreenlight.com/api/v1/memberships/506

Body:

```
                  
{
  "membership_level_name": "Silver"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 506,
  "constituent_id": 959480,
  "membership_level_id": 389,
  "membership_level_name": "Silver",
  "date_start": "2012-01-01",
  "finish_date": "2024-01-01",
  "note": null,
  "created_at": "2025-06-03T17:08:51Z",
  "updated_at": "2025-06-03T17:08:51Z"
}
                
```


* * *

DELETE /api/v1/memberships/{id} - Delete Membership
---------------------------------------------------

Delete the membership.


|Parameter Name|Description  |Type   |Required?|Parameter Type|
|--------------|-------------|-------|---------|--------------|
|id            |Membership Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/memberships/506

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

