ConstituentRelationship Management
----------------------------------

GET /api/v1/constituents/{constituent\_id}/constituent\_relationships - Fetch Constituent Relationships for a Constituent
-------------------------------------------------------------------------------------------------------------------------

Lists all the constituent relationships for a constituent.


|Parameter Name|Description   |Type   |Required?|Parameter Type|
|--------------|--------------|-------|---------|--------------|
|constituent_id|Constituent Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder700.46773152388533235              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/constituent\_relationships

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 2,
  "total_items": 2,
  "limit": 25,
  "offset": 0,
  "item_type": "constituent_relationship",
  "items": [
    {
      "id": 214491,
      "relationship_type_id": 47,
      "constituent_id": 959480,
      "related_constituent_id": 959455,
      "name": "Employer",
      "description": "",
      "auto_soft_credit": false,
      "also_acknowledge": false,
      "share_address": null,
      "share_phone": null
    },
    {
      "id": 214493,
      "relationship_type_id": 41,
      "constituent_id": 959480,
      "related_constituent_id": 959460,
      "name": "Parent",
      "description": "",
      "auto_soft_credit": false,
      "also_acknowledge": false,
      "share_address": null,
      "share_phone": null
    }
  ]
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/constituent\_relationships - Create new Constituent Relationship
------------------------------------------------------------------------------------------------------------

Add constituent relationship.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|constituent_id|Constituent Id|integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

id ( integer , optional ): ConstituentRelationship ID,

related\_constituent\_id ( integer , optional ): Related Constituent ID,

relationship\_type\_id ( integer , optional ): Relationship Type ID,

name ( string , optional ): Relationship name,

description ( string , optional ): Relationship description,

reciprocal\_id ( integer , optional ): Reciprocal Relationship Type ID,

rec\_name ( string , optional ): Reciprocal relationship name,

reciprocal\_description ( string , optional ): Reciprocal relationship description,

share\_address ( integer , optional ): Share address?,

share\_phone ( integer , optional ): Share phone?,

auto\_soft\_credit ( boolean , optional ): Automatically soft credit?,

also\_acknowledge ( boolean , optional ): Send memorial acknowledgements?,

created\_at ( datetime , optional ): Created At date and time,

updated\_at ( datetime , optional ): Updated At date and time

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder720.10845348175953773              
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

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/constituent\_relationships

Body:

```
                  
{
  "related_constituent_id": "959463",
  "name": "Friend"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 214582,
  "relationship_type_id": 50,
  "constituent_id": 959480,
  "related_constituent_id": 959463,
  "name": "Friend",
  "description": null,
  "auto_soft_credit": false,
  "also_acknowledge": false,
  "share_address": null,
  "share_phone": null
}
                
```


* * *

GET /api/v1/constituent\_relationships/{id} - Show Constituent Relationship details
-----------------------------------------------------------------------------------

Show details for the constituent relationship.


|Parameter Name|Description                |Type   |Required?|Parameter Type|
|--------------|---------------------------|-------|---------|--------------|
|id            |Constituent Relationship Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder750.5966728659150049              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituent\_relationships/214491

Response:

```
                  
{
  "api_version": "1.0",
  "id": 214491,
  "relationship_type_id": 47,
  "constituent_id": 959480,
  "related_constituent_id": 959455,
  "name": "Employer",
  "description": "",
  "auto_soft_credit": false,
  "also_acknowledge": false,
  "share_address": null,
  "share_phone": null
}
                
```


* * *

PATCH /api/v1/constituent\_relationships/{id} - Update Constituent Relationship
-------------------------------------------------------------------------------

Update the constituent relationship.


|Parameter Name|Description                |Type      |Required?|Parameter Type|
|--------------|---------------------------|----------|---------|--------------|
|id            |Constituent Relationship Id|integer   |true     |path          |
|body          |Update Objects             |UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

id ( integer , optional ): ConstituentRelationship ID,

related\_constituent\_id ( integer , optional ): Related Constituent ID,

relationship\_type\_id ( integer , optional ): Relationship Type ID,

name ( string , optional ): Relationship name,

description ( string , optional ): Relationship description,

reciprocal\_id ( integer , optional ): Reciprocal Relationship Type ID,

rec\_name ( string , optional ): Reciprocal relationship name,

reciprocal\_description ( string , optional ): Reciprocal relationship description,

share\_address ( integer , optional ): Share address?,

share\_phone ( integer , optional ): Share phone?,

auto\_soft\_credit ( boolean , optional ): Automatically soft credit?,

also\_acknowledge ( boolean , optional ): Send memorial acknowledgements?,

created\_at ( datetime , optional ): Created At date and time,

updated\_at ( datetime , optional ): Updated At date and time

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder770.8660314677337555              
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

URI: https://api.littlegreenlight.com/api/v1/constituent\_relationships/214582

Body:

```
                  
{
  "id": "214582",
  "name": "Family"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 214582,
  "relationship_type_id": 51,
  "constituent_id": 959480,
  "related_constituent_id": 959463,
  "name": "Family",
  "description": null,
  "auto_soft_credit": false,
  "also_acknowledge": false,
  "share_address": null,
  "share_phone": null
}
                
```


* * *

DELETE /api/v1/constituent\_relationships/{id} - Delete Constituent Relationship
--------------------------------------------------------------------------------

Delete the constituent relationship.


|Parameter Name|Description                |Type   |Required?|Parameter Type|
|--------------|---------------------------|-------|---------|--------------|
|id            |Constituent Relationship Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituent\_relationships/214582

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

Lists all the contact reports for a constituent.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder810.2340854603979361              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/contact\_reports

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 25,
  "offset": 0,
  "item_type": "contact_report",
  "items": [
    {
      "id": 9881,
      "constituent_id": 959480,
      "name": "Contact report for 'Appleton, Larry'",
      "contact_report_type_id": 2183,
      "contact_report_type_name": "Call",
      "original_date": "2023-09-18",
      "text": "Reached out to Larry regarding upcoming pledge drive.",
      "team_member": "Nick Bicknell",
      "team_member_email": "team_member@example.com",
      "created_at": "2023-09-18T21:49:19Z",
      "updated_at": "2023-09-18T22:05:56Z"
    }
  ]
}
                
```


* * *

Add contact report.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|constituent_id|Constituent Id|integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

name ( string , optional ): Name,

contact\_report\_type\_id ( integer , optional ): Contact Report Type Id,

contact\_report\_type\_name ( string , optional ): Contact Report Type Name,

original\_date ( date , optional ): Original Date,

text ( string , required ): Text,

team\_member ( string , optional ): Team Member ('id', 'email', or 'first\_name last\_name')

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder830.37714801652707997              
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

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/contact\_reports

Body:

```
                  
{
  "name": "New Contact Report",
  "contact_report_type_name": "Call",
  "original_date": "2018-06-05",
  "text": "Follow up contact.",
  "team_member": "nick@littlegreenlight.com"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 9953,
  "constituent_id": 959480,
  "name": "New Contact Report",
  "contact_report_type_id": 2183,
  "contact_report_type_name": "Call",
  "original_date": "2018-06-05",
  "text": "Follow up contact.",
  "team_member": "Nick Bicknell",
  "team_member_email": "team_member@example.com",
  "created_at": "2025-06-03T17:08:36Z",
  "updated_at": "2025-06-03T17:08:36Z"
}
                
```


* * *

Search for active contact reports



* Parameter Name: q[]
  * Description: Query string. (EX: updated_from=2016-01-01). Parameter value must be URL encoded.
  * Type: string
  * Required?: true
  * Parameter Type: query
* Parameter Name: sort
  * Description: Sort by one of the following fields: 'name, date, constituent_id'. Add an exclamation point to reverse the order. (EX: sort=name!)
  * Type: string
  * Required?: 
  * Parameter Type: query
* Parameter Name: limit
  * Description: Number of entries to return. Default: 25
  * Type: integer
  * Required?: 
  * Parameter Type: query
* Parameter Name: offset
  * Description: Start at given entry. Default: 0
  * Type: integer
  * Required?: 
  * Parameter Type: query




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder860.9893666532030196              
* Code: 400
  * Message: Bad Request
  * Response: 
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Available Search Terms:


|Original Date      |original_date_from    |Date updated from (YYYY-MM-DDTHH:MM:SSZ)|
|-------------------|----------------------|----------------------------------------|
|                   |original_date_to      |Date updated to (YYYY-MM-DDTHH:MM:SSZ)  |
|Name               |name                  |Name contains string                    |
|Text               |text                  |Text contains string                    |
|Contact Report Type|contact_report_type_id|Comma separated contact_report_type_ids |
|Constituent Id     |constituent_id        |Comma separated constituent_ids         |
|Constituent Keyword|const_keyword         |Comma separated Constituent keyword_ids |
|Updated At         |updated_from          |Date updated from (YYYY-MM-DDTHH:MM:SSZ)|
|                   |updated_to            |Date updated to (YYYY-MM-DDTHH:MM:SSZ)  |


Note: Multiple terms may be combined using a semi-colon: "updated\_from=2018-05-04;updated\_to=2018-05-04"

### Example - Search by Name:

URI: https://api.littlegreenlight.com/api/v1/contact\_reports/search

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 5,
  "offset": 0,
  "item_type": "contact_report",
  "items": [
    {
      "id": 9884,
      "constituent_id": 959519,
      "name": "Dinner with Jerry",
      "contact_report_type_id": 2185,
      "contact_report_type_name": "Meeting",
      "original_date": "2023-09-18",
      "text": "The details of the dinner in here.",
      "team_member": "Nick Bicknell",
      "team_member_email": "team_member@example.com",
      "created_at": "2023-09-18T22:01:22Z",
      "updated_at": "2023-09-18T22:05:03Z"
    }
  ]
}
                
```


### Example - Search by Constituent Keyword and Updated Since:

URI: https://api.littlegreenlight.com/api/v1/contact\_reports/search

Query:

```
q[]=const_keyword=12221;updated_from=2016-01-01&limit=5
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 2,
  "total_items": 2,
  "limit": 5,
  "offset": 0,
  "item_type": "contact_report",
  "items": [
    {
      "id": 9881,
      "constituent_id": 959480,
      "name": "Contact report for 'Appleton, Larry'",
      "contact_report_type_id": 2183,
      "contact_report_type_name": "Call",
      "original_date": "2023-09-18",
      "text": "Reached out to Larry regarding upcoming pledge drive.",
      "team_member": "Nick Bicknell",
      "team_member_email": "team_member@example.com",
      "created_at": "2023-09-18T21:49:19Z",
      "updated_at": "2023-09-18T22:05:56Z"
    },
    {
      "id": 9953,
      "constituent_id": 959480,
      "name": "New Contact Report",
      "contact_report_type_id": 2183,
      "contact_report_type_name": "Call",
      "original_date": "2018-06-05",
      "text": "Follow up contact.",
      "team_member": "Nick Bicknell",
      "team_member_email": "team_member@example.com",
      "created_at": "2025-06-03T17:08:36Z",
      "updated_at": "2025-06-03T17:08:36Z"
    }
  ]
}
                
```


* * *

Lists all the contact reports for an account.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder900.4697797629615663              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/contact\_reports

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 3,
  "total_items": 3,
  "limit": 25,
  "offset": 0,
  "item_type": "contact_report",
  "items": [
    {
      "id": 9881,
      "constituent_id": 959480,
      "name": "Contact report for 'Appleton, Larry'",
      "contact_report_type_id": 2183,
      "contact_report_type_name": "Call",
      "original_date": "2023-09-18",
      "text": "Reached out to Larry regarding upcoming pledge drive.",
      "team_member": "Nick Bicknell",
      "team_member_email": "team_member@example.com",
      "created_at": "2023-09-18T21:49:19Z",
      "updated_at": "2023-09-18T22:05:56Z"
    },
    {
      "id": 9884,
      "constituent_id": 959519,
      "name": "Dinner with Jerry",
      "contact_report_type_id": 2185,
      "contact_report_type_name": "Meeting",
      "original_date": "2023-09-18",
      "text": "The details of the dinner in here.",
      "team_member": "Nick Bicknell",
      "team_member_email": "team_member@example.com",
      "created_at": "2023-09-18T22:01:22Z",
      "updated_at": "2023-09-18T22:05:03Z"
    },
    {
      "id": 9953,
      "constituent_id": 959480,
      "name": "New Contact Report",
      "contact_report_type_id": 2183,
      "contact_report_type_name": "Call",
      "original_date": "2018-06-05",
      "text": "Follow up contact.",
      "team_member": "Nick Bicknell",
      "team_member_email": "team_member@example.com",
      "created_at": "2025-06-03T17:08:36Z",
      "updated_at": "2025-06-03T17:08:36Z"
    }
  ]
}
                
```


* * *

Show details for the contact report.


|Parameter Name|Description      |Type   |Required?|Parameter Type|
|--------------|-----------------|-------|---------|--------------|
|id            |Contact Report Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder920.06047237061466881              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/contact\_reports/9953

Response:

```
                  
{
  "api_version": "1.0",
  "id": 9953,
  "constituent_id": 959480,
  "name": "New Contact Report",
  "contact_report_type_id": 2183,
  "contact_report_type_name": "Call",
  "original_date": "2018-06-05",
  "text": "Follow up contact.",
  "team_member": "Nick Bicknell",
  "team_member_email": "team_member@example.com",
  "created_at": "2025-06-03T17:08:36Z",
  "updated_at": "2025-06-03T17:08:36Z"
}
                
```


* * *

Update the contact report.


|Parameter Name|Description      |Type      |Required?|Parameter Type|
|--------------|-----------------|----------|---------|--------------|
|id            |Contact Report Id|integer   |true     |path          |
|body          |Update Objects   |UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

constituent\_id ( integer , optional ): Constituent Id,

name ( string , optional ): Name,

contact\_report\_type\_id ( integer , optional ): Contact Report Type Id,

contact\_report\_type\_name ( string , optional ): Contact Report Type Name,

original\_date ( date , optional ): Original Date,

text ( string , required ): Text,

team\_member ( string , optional ): Team Member ('id', 'email', or 'first\_name last\_name')

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder940.24838539282735717              
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

URI: https://api.littlegreenlight.com/api/v1/contact\_reports/9953

Body:

```
                  
{
  "contact_report_type_name": "Email"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 9953,
  "constituent_id": 959480,
  "name": "New Contact Report",
  "contact_report_type_id": 2184,
  "contact_report_type_name": "Email",
  "original_date": "2018-06-05",
  "text": "Follow up contact.",
  "team_member": "Nick Bicknell",
  "team_member_email": "team_member@example.com",
  "created_at": "2025-06-03T17:08:36Z",
  "updated_at": "2025-06-03T17:08:37Z"
}
                
```


* * *

Delete the contact report.


|Parameter Name|Description      |Type   |Required?|Parameter Type|
|--------------|-----------------|-------|---------|--------------|
|id            |Contact Report Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/contact\_reports/9953

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

