Class Affiliations Management
-----------------------------

GET /api/v1/constituents/{constituent\_id}/class\_affiliations - Fetch Class Affiliations
-----------------------------------------------------------------------------------------

Lists all the class affiliations.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder330.9671014002371774              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/class\_affiliations

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 25,
  "offset": 0,
  "item_type": "class_affiliation",
  "items": [
    {
      "id": 159,
      "constituent_id": 959480,
      "class_affiliation_type_id": 515,
      "year": 2002,
      "note": "U Chicago Alum"
    }
  ]
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/class\_affiliations - Create new Class Affiliation
----------------------------------------------------------------------------------------------

Add class affiliation.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|constituent_id|Constituent Id|integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

id ( integer , optional ): Class Affiliation ID,

class\_affiliation\_type\_id ( integer , optional ): Class Affiliation Type ID,

year ( integer , optional ): Year,

note ( string , optional ): Note

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder350.7466373824761441              
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

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/class\_affiliations

Body:

```
                  
{
  "year": "2023",
  "class_affiliation_type_id": "515"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 235,
  "constituent_id": 959480,
  "class_affiliation_type_id": 515,
  "year": 2023,
  "note": null
}
                
```


* * *

GET /api/v1/class\_affiliations/{id} - Show Class Affiliation details
---------------------------------------------------------------------

Show details for the class affiliation.


|Parameter Name|Description         |Type   |Required?|Parameter Type|
|--------------|--------------------|-------|---------|--------------|
|id            |Class Affiliation Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder380.7387591478959863              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/class\_affiliations/159

Response:

```
                  
{
  "api_version": "1.0",
  "id": 159,
  "constituent_id": 959480,
  "class_affiliation_type_id": 515,
  "year": 2002,
  "note": "U Chicago Alum"
}
                
```


* * *

PATCH /api/v1/class\_affiliations/{id} - Update Class Affiliation
-----------------------------------------------------------------

Update the class affiliation.


|Parameter Name|Description         |Type      |Required?|Parameter Type|
|--------------|--------------------|----------|---------|--------------|
|id            |Class Affiliation Id|integer   |true     |path          |
|body          |Update Objects      |UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

id ( integer , optional ): Class Affiliation ID,

class\_affiliation\_type\_id ( integer , optional ): Class Affiliation Type ID,

year ( integer , optional ): Year,

note ( string , optional ): Note

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder400.5368067064385438              
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

URI: https://api.littlegreenlight.com/api/v1/class\_affiliations/235

Body:

Response:

```
                  
{
  "api_version": "1.0",
  "id": 235,
  "constituent_id": 959480,
  "class_affiliation_type_id": 515,
  "year": 2024,
  "note": null
}
                
```


* * *

DELETE /api/v1/class\_affiliations/{id} - Delete Class Affiliation
------------------------------------------------------------------

Delete the class affiliation.


|Parameter Name|Description         |Type   |Required?|Parameter Type|
|--------------|--------------------|-------|---------|--------------|
|id            |Class Affiliation Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/class\_affiliations/235

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

