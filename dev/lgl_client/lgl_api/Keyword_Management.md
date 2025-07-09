Keyword Management
------------------

GET /api/v1/categories/{category\_id}/keywords - Fetch Keywords
---------------------------------------------------------------

Lists all the keywords.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|category_id   |Category Id                             |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1770.6058804477800535              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/categories/1042/keywords

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 2,
  "total_items": 2,
  "limit": 25,
  "offset": 0,
  "item_type": "keyword",
  "items": [
    {
      "id": 12223,
      "category_id": 1042,
      "name": "val1",
      "description": null,
      "short_code": null,
      "ordinal": 100,
      "removable": true,
      "can_change": true,
      "can_select": true,
      "created_at": "2023-09-18T20:20:40Z",
      "updated_at": "2023-09-18T20:20:40Z"
    },
    {
      "id": 12224,
      "category_id": 1042,
      "name": "val2",
      "description": null,
      "short_code": null,
      "ordinal": 100,
      "removable": true,
      "can_change": true,
      "can_select": true,
      "created_at": "2023-09-18T20:20:40Z",
      "updated_at": "2023-09-18T20:20:40Z"
    }
  ]
}
                
```


* * *

POST /api/v1/categories/{category\_id}/keywords - Create new Keyword
--------------------------------------------------------------------

Add keyword.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|category_id   |Category Id   |integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

category\_id ( integer , required ): Category Id,

name ( string , required ): Name,

description ( string , optional ): Description,

short\_code ( string , optional ): Short Code,

ordinal ( integer , optional ): Ordinal,

removable ( boolean , optional ): Removable?,

can\_change ( boolean , optional ): Can Change?,

can\_select ( boolean , optional ): Can Select?

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1790.10816813267503567              
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

URI: https://api.littlegreenlight.com/api/v1/categories/1042/keywords

Body:

```
                  
{
  "name": "New Keyword"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 12390,
  "category_id": 1042,
  "name": "New Keyword",
  "description": null,
  "short_code": null,
  "ordinal": 100,
  "removable": true,
  "can_change": true,
  "can_select": true,
  "created_at": "2025-06-03T17:08:48Z",
  "updated_at": "2025-06-03T17:08:48Z"
}
                
```


### Example:

URI: https://api.littlegreenlight.com/api/v1/categories/1042/keywords

Body:

```
                  
{
  "name": "New Keyword 2"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 12391,
  "category_id": 1042,
  "name": "New Keyword 2",
  "description": null,
  "short_code": null,
  "ordinal": 100,
  "removable": true,
  "can_change": true,
  "can_select": true,
  "created_at": "2025-06-03T17:08:48Z",
  "updated_at": "2025-06-03T17:08:48Z"
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/keywords - Add Keyword
------------------------------------------------------------------

Add a keyword to a constituent.


|Parameter Name|Description   |Type   |Required?|Parameter Type|
|--------------|--------------|-------|---------|--------------|
|constituent_id|Constituent Id|integer|true     |path          |
|body          |Add Keyword   |AddBody|true     |body          |


### AddBody

AddBody {

id ( integer , required ): Keyword Id

}


|Code|Message             |Response|
|----|--------------------|--------|
|200 |Ok                  |        |
|400 |Bad Request         |        |
|401 |Unauthorized        |        |
|403 |Forbidden           |        |
|422 |Unprocessable Entity|        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/keywords

Body:

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

DELETE /api/v1/constituents/{constituent\_id}/keywords/{id} - Remove Keyword
----------------------------------------------------------------------------

Remove a keyword from a constituent


|Parameter Name|Description   |Type   |Required?|Parameter Type|
|--------------|--------------|-------|---------|--------------|
|id            |Keyword Id    |integer|true     |path          |
|constituent_id|Constituent Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/keywords/12391

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

GET /api/v1/keywords/{id} - Show Keyword details
------------------------------------------------

Show details for the keyword.


|Parameter Name|Description|Type   |Required?|Parameter Type|
|--------------|-----------|-------|---------|--------------|
|id            |Keyword Id |integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1860.9622589213999686              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/keywords/12225

Response:

```
                  
{
  "api_version": "1.0",
  "id": 12225,
  "category_id": 1039,
  "name": "New Tag",
  "description": null,
  "short_code": null,
  "ordinal": 100,
  "removable": true,
  "can_change": true,
  "can_select": true,
  "created_at": "2023-09-18T20:48:13Z",
  "updated_at": "2023-09-18T20:48:13Z"
}
                
```


* * *

PATCH /api/v1/keywords/{id} - Update Keyword
--------------------------------------------

Update the keyword.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|id            |Keyword Id    |integer   |true     |path          |
|body          |Update Objects|UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

category\_id ( integer , required ): Category Id,

name ( string , required ): Name,

description ( string , optional ): Description,

short\_code ( string , optional ): Short Code,

ordinal ( integer , optional ): Ordinal,

removable ( boolean , optional ): Removable?,

can\_change ( boolean , optional ): Can Change?,

can\_select ( boolean , optional ): Can Select?

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1880.1099326037466708              
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

URI: https://api.littlegreenlight.com/api/v1/keywords/12390

Body:

```
                  
{
  "short_code": "new_keyword"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 12390,
  "category_id": 1042,
  "name": "New Keyword",
  "description": null,
  "short_code": "new_keyword",
  "ordinal": 100,
  "removable": true,
  "can_change": true,
  "can_select": true,
  "created_at": "2025-06-03T17:08:48Z",
  "updated_at": "2025-06-03T17:08:49Z"
}
                
```


* * *

DELETE /api/v1/keywords/{id} - Delete Keyword
---------------------------------------------

Delete the keyword.


|Parameter Name|Description                    |Type   |Required?|Parameter Type|
|--------------|-------------------------------|-------|---------|--------------|
|id            |Keyword Id                     |integer|true     |path          |
|permanent     |Delete permantently. Default: 0|integer|         |query         |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/keywords/12390

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


### Example:

URI: https://api.littlegreenlight.com/api/v1/keywords/12390

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


### Example:

URI: https://api.littlegreenlight.com/api/v1/keywords/12391

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

