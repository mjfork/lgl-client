AppealRequests Management
-------------------------

GET /api/v1/appeals/{appeal\_id}/appeal\_requests - Fetch Appeal Requests for Appeal
------------------------------------------------------------------------------------

Lists all the appeal requests for an appeal.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|appeal_id     |Appeal Id                               |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder00.6515686284501427              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/appeals/2663/appeal\_requests

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 5,
  "total_items": 82,
  "limit": 5,
  "offset": 0,
  "next_item": 5,
  "next_link": "https://api.littlegreenlight.com/api/v1/appeals/2663/appeal_requests?limit=5&offset=5",
  "item_type": "appeal_request",
  "items": [
    {
      "id": 316126,
      "constituent_id": 959486,
      "constituent_name": "Archer's",
      "appeal_id": 2663,
      "name": "Appeal: Annual Appeal 2020 (2021-07-01)",
      "raised": 0.0,
      "status": "open",
      "ask_amount": 100.0,
      "assigned_to": 1047042,
      "custom_fields": [

      ],
      "custom_attrs": [

      ],
      "created_at": "2023-10-31T18:01:04Z",
      "updated_at": "2023-10-31T18:01:04Z"
    },
    {
      "id": 316127,
      "constituent_id": 959440,
      "constituent_name": "Avengers Mansion Headquarters of the Avengers",
      "appeal_id": 2663,
      "name": "Appeal: Annual Appeal 2020 (2021-07-01)",
      "raised": 0.0,
      "status": "open",
      "ask_amount": 100.0,
      "assigned_to": 1047042,
      "custom_fields": [

      ],
      "custom_attrs": [

      ],
      "created_at": "2023-10-31T18:01:04Z",
      "updated_at": "2023-10-31T18:01:04Z"
    },
    {
      "id": 316128,
      "constituent_id": 959453,
      "constituent_name": "Barone, Ray",
      "appeal_id": 2663,
      "name": "Appeal: Annual Appeal 2020 (2021-07-01)",
      "raised": 0.0,
      "status": "open",
      "ask_amount": 100.0,
      "assigned_to": 1047042,
      "custom_fields": [

      ],
      "custom_attrs": [

      ],
      "created_at": "2023-10-31T18:01:04Z",
      "updated_at": "2023-10-31T18:01:04Z"
    },
    {
      "id": 316129,
      "constituent_id": 959465,
      "constituent_name": "Baxter, Joseph",
      "appeal_id": 2663,
      "name": "Appeal: Annual Appeal 2020 (2021-07-01)",
      "raised": 0.0,
      "status": "open",
      "ask_amount": 100.0,
      "assigned_to": 1047042,
      "custom_fields": [

      ],
      "custom_attrs": [

      ],
      "created_at": "2023-10-31T18:01:04Z",
      "updated_at": "2023-10-31T18:01:04Z"
    },
    {
      "id": 316130,
      "constituent_id": 959474,
      "constituent_name": "Black, Frank",
      "appeal_id": 2663,
      "name": "Appeal: Annual Appeal 2020 (2021-07-01)",
      "raised": 0.0,
      "status": "open",
      "ask_amount": 100.0,
      "assigned_to": 1047042,
      "custom_fields": [

      ],
      "custom_attrs": [

      ],
      "created_at": "2023-10-31T18:01:04Z",
      "updated_at": "2023-10-31T18:01:04Z"
    }
  ]
}
                
```


* * *

POST /api/v1/appeals/{appeal\_id}/appeal\_requests - Create new Appeal Request
------------------------------------------------------------------------------

Add appeal request.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|appeal_id     |Appeal Id     |integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

constituent\_id ( integer , required ): Constituent Id,

appeal\_id ( integer , required ): Appeal Id,

ask\_amount ( double , optional ): Donated,

status ( string , optional ): Status,

assigned\_to ( integer , optional ): Assigned to team member id,

custom\_fields ( array , optional , CustomFieldAggregatedUpdate ): Appeal request custom fields (Categories),

custom\_attrs ( array , optional , CustomAttr\_create ): Appeal request custom attributes

}

CustomFieldAggregatedUpdate {

id ( integer , optional ): Custom Field Id,

name ( string , required ): Name,

key ( string , optional ): Key,

remove\_previous\_values ( boolean , optional ): Remove previous field values,

values ( array , required , CustomValueAggregatedUpdate ): Values

}

CustomValueAggregatedUpdate {

id ( integer , required ): Value Id,

name ( string , required ): Name

}

CustomAttr\_create {

id ( integer , optional ): Custom Field Id,

key ( string , optional ): Key,

value ( string , required ): Value

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder20.6217246445117732              
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

URI: https://api.littlegreenlight.com/api/v1/appeals/2663/appeal\_requests

Body:

```
                  
{
  "constituent_id": "959480",
  "ask_amount": 100.0
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 316248,
  "constituent_id": 959480,
  "constituent_name": "Appleton, Larry",
  "appeal_id": 2663,
  "name": "Appeal: Annual Appeal 2020 (2021-07-01)",
  "raised": 0.0,
  "status": "open",
  "ask_amount": 100.0,
  "assigned_to": null,
  "custom_fields": [

  ],
  "custom_attrs": [

  ],
  "created_at": "2025-06-03T17:08:26Z",
  "updated_at": "2025-06-03T17:08:26Z"
}
                
```


* * *

GET /api/v1/appeal\_requests/{id} - Show Appeal Request details
---------------------------------------------------------------

Show details for the appeal request.


|Parameter Name|Description      |Type   |Required?|Parameter Type|
|--------------|-----------------|-------|---------|--------------|
|id            |Appeal Request Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder50.6111622848126264              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/appeal\_requests/316248

Response:

```
                  
{
  "api_version": "1.0",
  "id": 316248,
  "constituent_id": 959480,
  "constituent_name": "Appleton, Larry",
  "appeal_id": 2663,
  "name": "Appeal: Annual Appeal 2020 (2021-07-01)",
  "raised": 0.0,
  "status": "open",
  "ask_amount": 100.0,
  "assigned_to": null,
  "custom_fields": [

  ],
  "custom_attrs": [

  ],
  "created_at": "2025-06-03T17:08:26Z",
  "updated_at": "2025-06-03T17:08:26Z"
}
                
```


* * *

PATCH /api/v1/appeal\_requests/{id} - Update Appeal Request
-----------------------------------------------------------

Update the appeal request.


|Parameter Name|Description      |Type      |Required?|Parameter Type|
|--------------|-----------------|----------|---------|--------------|
|id            |Appeal Request Id|integer   |true     |path          |
|body          |Update Objects   |UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

constituent\_id ( integer , required ): Constituent Id,

appeal\_id ( integer , required ): Appeal Id,

ask\_amount ( double , optional ): Donated,

status ( string , optional ): Status,

assigned\_to ( integer , optional ): Assigned to team member id,

custom\_fields ( array , optional , CustomFieldAggregatedUpdate ): Appeal request custom fields (Categories),

custom\_attrs ( array , optional , CustomAttr\_create ): Appeal request custom attributes

}

CustomFieldAggregatedUpdate {

id ( integer , optional ): Custom Field Id,

name ( string , required ): Name,

key ( string , optional ): Key,

remove\_previous\_values ( boolean , optional ): Remove previous field values,

values ( array , required , CustomValueAggregatedUpdate ): Values

}

CustomValueAggregatedUpdate {

id ( integer , required ): Value Id,

name ( string , required ): Name

}

CustomAttr\_create {

id ( integer , optional ): Custom Field Id,

key ( string , optional ): Key,

value ( string , required ): Value

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder70.03280188787970584              
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

URI: https://api.littlegreenlight.com/api/v1/appeal\_requests/316248

Body:

Response:

```
                  
{
  "api_version": "1.0",
  "id": 316248,
  "constituent_id": 959480,
  "constituent_name": "Appleton, Larry",
  "appeal_id": 2663,
  "name": "Appeal: Annual Appeal 2020 (2021-07-01)",
  "raised": 0.0,
  "status": "open",
  "ask_amount": 200.0,
  "assigned_to": null,
  "custom_fields": [

  ],
  "custom_attrs": [

  ],
  "created_at": "2025-06-03T17:08:26Z",
  "updated_at": "2025-06-03T17:08:27Z"
}
                
```


* * *

DELETE /api/v1/appeal\_requests/{id} - Delete Appeal Request
------------------------------------------------------------

Delete the appeal request.


|Parameter Name|Description      |Type   |Required?|Parameter Type|
|--------------|-----------------|-------|---------|--------------|
|id            |Appeal Request Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/appeal\_requests/316248

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/appeal\_requests - Create new Appeal Request for Constituent
--------------------------------------------------------------------------------------------------------

Add appeal request to constituent.


|Parameter Name|Description   |Type            |Required?|Parameter Type|
|--------------|--------------|----------------|---------|--------------|
|constituent_id|Constituent Id|integer         |true     |path          |
|body          |Create Objects|CreateBody_Const|true     |body          |


### CreateBody\_Const

CreateBody\_Const {

appeal\_id ( integer , required ): Appeal Id,

ask\_amount ( double , optional ): Donated,

status ( string , optional ): Status,

assigned\_to ( integer , optional ): Assigned to team member id,

custom\_fields ( array , optional , CustomFieldAggregatedUpdate ): Appeal request custom fields (Categories),

custom\_attrs ( array , optional , CustomAttr\_create ): Appeal request custom attributes

}

CustomFieldAggregatedUpdate {

id ( integer , optional ): Custom Field Id,

name ( string , required ): Name,

key ( string , optional ): Key,

remove\_previous\_values ( boolean , optional ): Remove previous field values,

values ( array , required , CustomValueAggregatedUpdate ): Values

}

CustomValueAggregatedUpdate {

id ( integer , required ): Value Id,

name ( string , required ): Name

}

CustomAttr\_create {

id ( integer , optional ): Custom Field Id,

key ( string , optional ): Key,

value ( string , required ): Value

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder100.7961837999823742              
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


* * *

GET /api/v1/constituents/{constituent\_id}/appeal\_requests - Fetch Appeal Requests for Constituent
---------------------------------------------------------------------------------------------------

Lists all the appeal requests for a constituent.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder110.7214386705724076              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/appeal\_requests

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 0,
  "total_items": 0,
  "limit": 5,
  "offset": 0,
  "item_type": "appeal_request",
  "items": [

  ]
}
                
```


* * *

