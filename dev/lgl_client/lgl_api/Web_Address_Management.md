Web Address Management
----------------------

GET /api/v1/constituents/{constituent\_id}/web\_addresses - Fetch Web Addresses
-------------------------------------------------------------------------------

Lists all the web addresses.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2820.7856059910563074              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/web\_addresses

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 2,
  "total_items": 2,
  "limit": 25,
  "offset": 0,
  "item_type": "web_address",
  "items": [
    {
      "id": 46,
      "item_id": 959480,
      "item_type": "Constituent",
      "url": "www.website.com",
      "web_address_type_id": 5,
      "web_address_type_name": "Website",
      "is_preferred": false,
      "parent_id": null,
      "created_at": "2023-09-19T22:34:56Z",
      "updated_at": "2023-09-19T22:34:56Z"
    },
    {
      "id": 47,
      "item_id": 959480,
      "item_type": "Constituent",
      "url": "facebook.com/something",
      "web_address_type_id": 6,
      "web_address_type_name": "Facebook",
      "is_preferred": false,
      "parent_id": null,
      "created_at": "2023-09-19T22:34:56Z",
      "updated_at": "2023-09-19T22:34:56Z"
    }
  ]
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/web\_addresses - Create new Web Address
-----------------------------------------------------------------------------------

Add web address.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|constituent_id|Constituent Id|integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

url ( string , optional ): Web Address,

web\_address\_type\_id ( integer , optional ): Web Address Type ID,

web\_address\_type\_name ( string , optional ): Web Address Type Name,

is\_preferred ( boolean , optional ): Make this the preferred email address

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2840.7625100161735321              
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

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/web\_addresses

Body:

```
                  
{
  "url": "www.example.com"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 102,
  "item_id": 959480,
  "item_type": "Constituent",
  "url": "www.example.com",
  "web_address_type_id": 5,
  "web_address_type_name": "Website",
  "is_preferred": false,
  "parent_id": null,
  "created_at": "2025-06-03T17:08:59Z",
  "updated_at": "2025-06-03T17:08:59Z"
}
                
```


* * *

GET /api/v1/web\_addresses/{id} - Show Web Address details
----------------------------------------------------------

Show details for the web address.


|Parameter Name|Description   |Type   |Required?|Parameter Type|
|--------------|--------------|-------|---------|--------------|
|id            |Web Address Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2870.5945243381816665              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/web\_addresses/102

Response:

```
                  
{
  "api_version": "1.0",
  "id": 102,
  "item_id": 959480,
  "item_type": "Constituent",
  "url": "www.example.com",
  "web_address_type_id": 5,
  "web_address_type_name": "Website",
  "is_preferred": false,
  "parent_id": null,
  "created_at": "2025-06-03T17:08:59Z",
  "updated_at": "2025-06-03T17:08:59Z"
}
                
```


* * *

PATCH /api/v1/web\_addresses/{id} - Update Web Address
------------------------------------------------------

Update the web address.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|id            |Web Address Id|integer   |true     |path          |
|body          |Update Objects|UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

url ( string , optional ): Web Address,

web\_address\_type\_id ( integer , optional ): Web Address Type ID,

web\_address\_type\_name ( string , optional ): Web Address Type Name,

is\_preferred ( boolean , optional ): Make this the preferred email address

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2890.4890709818550889              
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

URI: https://api.littlegreenlight.com/api/v1/web\_addresses/102

Body:

```
                  
{
  "web_address_type_id": 2
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 102,
  "item_id": 959480,
  "item_type": "Constituent",
  "url": "www.example.com",
  "web_address_type_id": 2,
  "web_address_type_name": null,
  "is_preferred": false,
  "parent_id": null,
  "created_at": "2025-06-03T17:08:59Z",
  "updated_at": "2025-06-03T17:08:59Z"
}
                
```


* * *

DELETE /api/v1/web\_addresses/{id} - Delete Web Address
-------------------------------------------------------

Delete the web address.


|Parameter Name|Description   |Type   |Required?|Parameter Type|
|--------------|--------------|-------|---------|--------------|
|id            |Web Address Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/web\_addresses/102

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *