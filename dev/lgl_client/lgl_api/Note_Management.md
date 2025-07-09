Note Management
---------------

GET /api/v1/constituents/{constituent\_id}/notes - Fetch Notes for Constituent
------------------------------------------------------------------------------

Lists all the notes for a constituent.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2190.13835895867853254              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/notes

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 25,
  "offset": 0,
  "item_type": "note",
  "items": [
    {
      "id": 13733,
      "constituent_id": 959480,
      "note_type_id": 373,
      "note_type_name": "General",
      "text": "A good contact for the future fundraising.",
      "external_id": null,
      "original_date": "2024-12-03",
      "created_at": "2025-02-26T22:04:16Z",
      "updated_at": "2025-02-26T22:04:16Z"
    }
  ]
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/notes - Create new Note
-------------------------------------------------------------------

Add note.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|constituent_id|Constituent Id|integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

note\_type\_id ( integer , optional ): Note Type Id,

note\_type\_name ( string , optional ): Note Type Name,

text ( string , required ): Text,

external\_id ( string , optional ): External Id,

original\_date ( date , required ): Original Date

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2210.7309951086296296              
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

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/notes

Body:

```
                  
{
  "text": "New Note",
  "note_type_name": "General",
  "original_date": "2025-02-01"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 13739,
  "constituent_id": 959480,
  "note_type_id": 373,
  "note_type_name": "General",
  "text": "New Note",
  "external_id": null,
  "original_date": "2025-02-01",
  "created_at": "2025-06-03T17:08:52Z",
  "updated_at": "2025-06-03T17:08:52Z"
}
                
```


* * *

GET /api/v1/notes - Fetch Notes for Account
-------------------------------------------

Lists all the notes for an account.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2240.02032955798982683              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/notes

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 2,
  "total_items": 2,
  "limit": 25,
  "offset": 0,
  "item_type": "note",
  "items": [
    {
      "id": 13733,
      "constituent_id": 959480,
      "note_type_id": 373,
      "note_type_name": "General",
      "text": "A good contact for the future fundraising.",
      "external_id": null,
      "original_date": "2024-12-03",
      "created_at": "2025-02-26T22:04:16Z",
      "updated_at": "2025-02-26T22:04:16Z"
    },
    {
      "id": 13739,
      "constituent_id": 959480,
      "note_type_id": 373,
      "note_type_name": "General",
      "text": "New Note",
      "external_id": null,
      "original_date": "2025-02-01",
      "created_at": "2025-06-03T17:08:52Z",
      "updated_at": "2025-06-03T17:08:52Z"
    }
  ]
}
                
```


* * *

GET /api/v1/notes/{id} - Show Note details
------------------------------------------

Show details for the note.


|Parameter Name|Description|Type   |Required?|Parameter Type|
|--------------|-----------|-------|---------|--------------|
|id            |Note Id    |integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2260.49945600327749506              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/notes/13739

Response:

```
                  
{
  "api_version": "1.0",
  "id": 13739,
  "constituent_id": 959480,
  "note_type_id": 373,
  "note_type_name": "General",
  "text": "New Note",
  "external_id": null,
  "original_date": "2025-02-01",
  "created_at": "2025-06-03T17:08:52Z",
  "updated_at": "2025-06-03T17:08:52Z"
}
                
```


* * *

PATCH /api/v1/notes/{id} - Update Note
--------------------------------------

Update the note.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|id            |Note Id       |integer   |true     |path          |
|body          |Update Objects|UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

constituent\_id ( integer , optional ): Constituent Id,

note\_type\_id ( integer , optional ): Note Type Id,

note\_type\_name ( string , optional ): Note Type Name,

text ( string , required ): Text,

external\_id ( string , optional ): External Id,

original\_date ( date , required ): Original Date

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2280.4846011329440807              
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

URI: https://api.littlegreenlight.com/api/v1/notes/13739

Body:

```
                  
{
  "note_type_name": "Update"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 13739,
  "constituent_id": 959480,
  "note_type_id": 374,
  "note_type_name": "Update",
  "text": "New Note",
  "external_id": null,
  "original_date": "2025-02-01",
  "created_at": "2025-06-03T17:08:52Z",
  "updated_at": "2025-06-03T17:08:53Z"
}
                
```


* * *

DELETE /api/v1/notes/{id} - Delete Note
---------------------------------------

Delete the note.


|Parameter Name|Description|Type   |Required?|Parameter Type|
|--------------|-----------|-------|---------|--------------|
|id            |Note Id    |integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/notes/13739

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

