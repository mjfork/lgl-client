Street Address Management
-------------------------

GET /api/v1/constituents/{constituent\_id}/street\_addresses - Fetch Street Addresses
-------------------------------------------------------------------------------------

Lists all the street addresses.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2470.5086945309491757              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/street\_addresses

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 25,
  "offset": 0,
  "item_type": "street_address",
  "items": [
    {
      "id": 838379,
      "item_id": 959480,
      "item_type": "Constituent",
      "street": "711 Calhoun Street",
      "city": "Chicago",
      "state": "IL",
      "country": "US",
      "postal_code": "60603",
      "county": "",
      "street_address_type_id": 1,
      "street_type_name": "Home",
      "is_preferred": true,
      "not_current": false,
      "parent_id": null,
      "seasonal_from": "01-01",
      "seasonal_to": "12-31",
      "seasonal": null,
      "lat": null,
      "lng": null,
      "zip5": "60603",
      "verified": false,
      "verified_on": null,
      "created_at": "2023-09-18T18:25:01Z",
      "updated_at": "2023-09-19T22:34:56Z"
    }
  ]
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/street\_addresses - Create new Street Address
-----------------------------------------------------------------------------------------

Add street address.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|constituent_id|Constituent Id|integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

street ( string , optional ): Street,

street\_address\_type\_id ( integer , optional ): Street Address Type ID,

street\_type\_name ( string , optional ): Street Address Type Name,

city ( string , optional ): City,

state ( string , optional ): State/Province,

postal\_code ( string , optional ): Zip/Postal Code,

county ( string , optional ): County,

country ( string , optional ): Country,

seasonal\_from ( string , optional ): Seasonal from (mm-dd),

seasonal\_to ( string , optional ): Seasonal to (mm-dd),

seasonal ( boolean , optional ): Is seasonal?,

is\_preferred ( boolean , optional ): Is preferred address,

not\_current ( boolean , optional ): Not current?

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2490.5845806824935553              
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

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/street\_addresses

Body:

```
                  
{
  "street": "123 SE Tree",
  "city": "Seattle",
  "state": "WA",
  "postal_code": "98101"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 838577,
  "item_id": 959480,
  "item_type": "Constituent",
  "street": "123 SE Tree",
  "city": "Seattle",
  "state": "WA",
  "country": null,
  "postal_code": "98101",
  "county": null,
  "street_address_type_id": 1,
  "street_type_name": "Home",
  "is_preferred": false,
  "not_current": false,
  "parent_id": null,
  "seasonal_from": "01-01",
  "seasonal_to": "12-31",
  "seasonal": null,
  "lat": null,
  "lng": null,
  "zip5": "98101",
  "verified": false,
  "verified_on": null,
  "created_at": "2025-06-03T17:08:55Z",
  "updated_at": "2025-06-03T17:08:55Z"
}
                
```


* * *

GET /api/v1/street\_addresses/{id} - Show Street Address details
----------------------------------------------------------------

Show details for the street address.


|Parameter Name|Description      |Type   |Required?|Parameter Type|
|--------------|-----------------|-------|---------|--------------|
|id            |Street Address Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2520.2361454117724091              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/street\_addresses/838577

Response:

```
                  
{
  "api_version": "1.0",
  "id": 838577,
  "item_id": 959480,
  "item_type": "Constituent",
  "street": "123 SE Tree",
  "city": "Seattle",
  "state": "WA",
  "country": null,
  "postal_code": "98101",
  "county": null,
  "street_address_type_id": 1,
  "street_type_name": "Home",
  "is_preferred": false,
  "not_current": false,
  "parent_id": null,
  "seasonal_from": "01-01",
  "seasonal_to": "12-31",
  "seasonal": null,
  "lat": null,
  "lng": null,
  "zip5": "98101",
  "verified": false,
  "verified_on": null,
  "created_at": "2025-06-03T17:08:55Z",
  "updated_at": "2025-06-03T17:08:55Z"
}
                
```


* * *

PATCH /api/v1/street\_addresses/{id} - Update Street Address
------------------------------------------------------------

Update the street address.


|Parameter Name|Description      |Type      |Required?|Parameter Type|
|--------------|-----------------|----------|---------|--------------|
|id            |Street Address Id|integer   |true     |path          |
|body          |Update Objects   |UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

street ( string , optional ): Street,

street\_address\_type\_id ( integer , optional ): Street Address Type ID,

street\_type\_name ( string , optional ): Street Address Type Name,

city ( string , optional ): City,

state ( string , optional ): State/Province,

postal\_code ( string , optional ): Zip/Postal Code,

county ( string , optional ): County,

country ( string , optional ): Country,

seasonal\_from ( string , optional ): Seasonal from (mm-dd),

seasonal\_to ( string , optional ): Seasonal to (mm-dd),

seasonal ( boolean , optional ): Is seasonal?,

is\_preferred ( boolean , optional ): Is preferred address,

not\_current ( boolean , optional ): Not current?

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2540.0741098785333889              
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

URI: https://api.littlegreenlight.com/api/v1/street\_addresses/838577

Body:

```
                  
{
  "street_address_type_id": 2
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 838577,
  "item_id": 959480,
  "item_type": "Constituent",
  "street": "123 SE Tree",
  "city": "Seattle",
  "state": "WA",
  "country": null,
  "postal_code": "98101",
  "county": null,
  "street_address_type_id": 2,
  "street_type_name": "Work",
  "is_preferred": false,
  "not_current": false,
  "parent_id": null,
  "seasonal_from": "01-01",
  "seasonal_to": "12-31",
  "seasonal": null,
  "lat": null,
  "lng": null,
  "zip5": "98101",
  "verified": false,
  "verified_on": null,
  "created_at": "2025-06-03T17:08:55Z",
  "updated_at": "2025-06-03T17:08:55Z"
}
                
```


* * *

DELETE /api/v1/street\_addresses/{id} - Delete Street Address
-------------------------------------------------------------

Delete the street address.


|Parameter Name|Description      |Type   |Required?|Parameter Type|
|--------------|-----------------|-------|---------|--------------|
|id            |Street Address Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/street\_addresses/838577

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

