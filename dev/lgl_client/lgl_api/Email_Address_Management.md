Email Address Management
------------------------

GET /api/v1/constituents/{constituent\_id}/email\_addresses - Fetch Email Addresses
-----------------------------------------------------------------------------------

Lists all the email addresses.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder990.9141077874117942              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/email\_addresses

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 25,
  "offset": 0,
  "item_type": "email_address",
  "items": [
    {
      "id": 276464,
      "item_id": 959480,
      "item_type": "Constituent",
      "address": "appleton@perfectstrangers.com",
      "email_address_type_id": 1,
      "email_type_name": "Home",
      "is_preferred": true,
      "not_current": false,
      "parent_id": null,
      "created_at": "2023-09-18T18:25:01Z",
      "updated_at": "2023-09-19T22:34:56Z"
    }
  ]
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/email\_addresses - Create new Email Address
---------------------------------------------------------------------------------------

Add email address.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|constituent_id|Constituent Id|integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

address ( string , optional ): Email Address,

email\_address\_type\_id ( integer , optional ): Email Address Type ID,

email\_type\_name ( string , optional ): Email Address Type Name,

is\_preferred ( boolean , optional ): Make this the preferred email address,

not\_current ( boolean , optional ): No longer a current email address

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1010.4074418888265141              
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

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/email\_addresses

Body:

```
                  
{
  "address": "test@example.com"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 276662,
  "item_id": 959480,
  "item_type": "Constituent",
  "address": "test@example.com",
  "email_address_type_id": 1,
  "email_type_name": "Home",
  "is_preferred": false,
  "not_current": false,
  "parent_id": null,
  "created_at": "2025-06-03T17:08:37Z",
  "updated_at": "2025-06-03T17:08:37Z"
}
                
```


* * *

GET /api/v1/email\_addresses/{id} - Show Email Address details
--------------------------------------------------------------

Show details for the email address.


|Parameter Name|Description     |Type   |Required?|Parameter Type|
|--------------|----------------|-------|---------|--------------|
|id            |Email Address Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1040.842055165418772              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/email\_addresses/276464

Response:

```
                  
{
  "api_version": "1.0",
  "id": 276464,
  "item_id": 959480,
  "item_type": "Constituent",
  "address": "appleton@perfectstrangers.com",
  "email_address_type_id": 1,
  "email_type_name": "Home",
  "is_preferred": true,
  "not_current": false,
  "parent_id": null,
  "created_at": "2023-09-18T18:25:01Z",
  "updated_at": "2023-09-19T22:34:56Z"
}
                
```


* * *

PATCH /api/v1/email\_addresses/{id} - Update Email Address
----------------------------------------------------------

Update the email address.


|Parameter Name|Description     |Type      |Required?|Parameter Type|
|--------------|----------------|----------|---------|--------------|
|id            |Email Address Id|integer   |true     |path          |
|body          |Update Objects  |UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

address ( string , optional ): Email Address,

email\_address\_type\_id ( integer , optional ): Email Address Type ID,

email\_type\_name ( string , optional ): Email Address Type Name,

is\_preferred ( boolean , optional ): Make this the preferred email address,

not\_current ( boolean , optional ): No longer a current email address

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1060.005788972921774604              
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

URI: https://api.littlegreenlight.com/api/v1/email\_addresses/276662

Body:

```
                  
{
  "email_address_type_id": 2
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 276662,
  "item_id": 959480,
  "item_type": "Constituent",
  "address": "test@example.com",
  "email_address_type_id": 2,
  "email_type_name": "Work",
  "is_preferred": false,
  "not_current": false,
  "parent_id": null,
  "created_at": "2025-06-03T17:08:37Z",
  "updated_at": "2025-06-03T17:08:38Z"
}
                
```


* * *

DELETE /api/v1/email\_addresses/{id} - Delete Email Address
-----------------------------------------------------------

Delete the email address.


|Parameter Name|Description     |Type   |Required?|Parameter Type|
|--------------|----------------|-------|---------|--------------|
|id            |Email Address Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/email\_addresses/276662

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

