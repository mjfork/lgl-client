Phone Number Management
-----------------------

GET /api/v1/constituents/{constituent\_id}/phone\_numbers - Fetch Phone Numbers
-------------------------------------------------------------------------------

Lists all the phone numbers.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2340.6605718965605234              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/phone\_numbers

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 25,
  "offset": 0,
  "item_type": "phone_number",
  "items": [
    {
      "id": 479627,
      "item_id": 959480,
      "item_type": "Constituent",
      "number": "(888) 555-0044",
      "phone_number_type_id": 3,
      "phone_type_name": "Mobile",
      "is_preferred": true,
      "not_current": false,
      "parent_id": null,
      "normalized_number": "8885550044",
      "created_at": "2023-09-18T18:25:01Z",
      "updated_at": "2023-09-19T22:34:56Z"
    }
  ]
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/phone\_numbers - Create new Phone Number
------------------------------------------------------------------------------------

Add phone number.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|constituent_id|Constituent Id|integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

number ( string , optional ): Phone Number,

phone\_number\_type\_id ( integer , optional ): Phone Number Type Id,

phone\_type\_name ( string , optional ): Phone Number Type Name,

is\_preferred ( boolean , optional ): Make this the preferred phone number,

not\_current ( boolean , optional ): No longer a current phone number

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2360.474794547779148              
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

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/phone\_numbers

Body:

```
                  
{
  "number": "222-555-1212"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 479746,
  "item_id": 959480,
  "item_type": "Constituent",
  "number": "222-555-1212",
  "phone_number_type_id": 1,
  "phone_type_name": "Home",
  "is_preferred": false,
  "not_current": false,
  "parent_id": null,
  "normalized_number": "2225551212",
  "created_at": "2025-06-03T17:08:54Z",
  "updated_at": "2025-06-03T17:08:54Z"
}
                
```


* * *

GET /api/v1/phone\_numbers/{id} - Show Phone Number details
-----------------------------------------------------------

Show details for the phone number.


|Parameter Name|Description    |Type   |Required?|Parameter Type|
|--------------|---------------|-------|---------|--------------|
|id            |Phone Number Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2390.7646508645728904              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/phone\_numbers/479746

Response:

```
                  
{
  "api_version": "1.0",
  "id": 479746,
  "item_id": 959480,
  "item_type": "Constituent",
  "number": "222-555-1212",
  "phone_number_type_id": 1,
  "phone_type_name": "Home",
  "is_preferred": false,
  "not_current": false,
  "parent_id": null,
  "normalized_number": "2225551212",
  "created_at": "2025-06-03T17:08:54Z",
  "updated_at": "2025-06-03T17:08:54Z"
}
                
```


* * *

PATCH /api/v1/phone\_numbers/{id} - Update Phone Number
-------------------------------------------------------

Update the phone number.


|Parameter Name|Description    |Type      |Required?|Parameter Type|
|--------------|---------------|----------|---------|--------------|
|id            |Phone Number Id|integer   |true     |path          |
|body          |Update Objects |UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

number ( string , optional ): Phone Number,

phone\_number\_type\_id ( integer , optional ): Phone Number Type Id,

phone\_type\_name ( string , optional ): Phone Number Type Name,

is\_preferred ( boolean , optional ): Make this the preferred phone number,

not\_current ( boolean , optional ): No longer a current phone number

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2410.8128364711523302              
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

URI: https://api.littlegreenlight.com/api/v1/phone\_numbers/479746

Body:

```
                  
{
  "phone_number_type_id": 2
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 479746,
  "item_id": 959480,
  "item_type": "Constituent",
  "number": "222-555-1212",
  "phone_number_type_id": 2,
  "phone_type_name": "Work",
  "is_preferred": false,
  "not_current": false,
  "parent_id": null,
  "normalized_number": "2225551212",
  "created_at": "2025-06-03T17:08:54Z",
  "updated_at": "2025-06-03T17:08:54Z"
}
                
```


* * *

DELETE /api/v1/phone\_numbers/{id} - Delete Phone Number
--------------------------------------------------------

Delete the phone number.


|Parameter Name|Description    |Type   |Required?|Parameter Type|
|--------------|---------------|-------|---------|--------------|
|id            |Phone Number Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/phone\_numbers/479746

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

