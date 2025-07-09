Volunteer Time Management
-------------------------

GET /api/v1/constituents/{constituent\_id}/volunteer\_times - Fetch Volunteer Times for Constituent
---------------------------------------------------------------------------------------------------

Lists all the volunteer times for a constituent.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2640.9314658142185215              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/volunteer\_times

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 2,
  "total_items": 2,
  "limit": 25,
  "offset": 0,
  "item_type": "volunteer_time",
  "items": [
    {
      "id": 2981,
      "constituent_id": 959480,
      "external_id": null,
      "volunteering_category_id": 447,
      "volunteering_category_name": "Donor Management",
      "description": "",
      "hours": 4.0,
      "date": "2023-09-19",
      "end_date": "2023-09-19",
      "completed_hours": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-19T22:07:01Z",
      "updated_at": "2023-09-19T22:07:01Z"
    },
    {
      "id": 3001,
      "constituent_id": 959480,
      "external_id": null,
      "volunteering_category_id": 446,
      "volunteering_category_name": "General",
      "description": "Donor management",
      "hours": 4.0,
      "date": "2018-01-02",
      "end_date": "2018-01-12",
      "completed_hours": 4.0,
      "custom_fields": [

      ],
      "created_at": "2023-11-15T22:04:55Z",
      "updated_at": "2023-11-15T22:04:56Z"
    }
  ]
}
                
```


* * *

POST /api/v1/constituents/{constituent\_id}/volunteer\_times - Create new Volunteer Time
----------------------------------------------------------------------------------------

Add volunteer time.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|constituent_id|Constituent Id|integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

constituent\_id ( integer , required ): Constituent ID,

external\_id ( integer , optional ): External Volunteering ID,

volunteering\_category\_id ( integer , required ): Volunteer Category Id,

volunteering\_category\_name ( string , optional ): Volunteer Category Name,

description ( string , optional ): Description,

hours ( double , optional ): Hours,

date ( date , optional ): Date,

end\_date ( date , optional ): End Date,

completed\_hours ( double , optional ): Completed Hours,

custom\_fields ( array , optional , CustomFieldAggregatedUpdate ): VolunteerTime custom fields (Categories)

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



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2660.46835554469416163              
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

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/volunteer\_times

Body:

```
                  
{
  "volunteering_category_name": "General",
  "description": "Donor management",
  "hours": "4",
  "date": "2018-01-02",
  "external_id": "678890"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 3040,
  "constituent_id": 959480,
  "external_id": "678890",
  "volunteering_category_id": 446,
  "volunteering_category_name": "General",
  "description": "Donor management",
  "hours": 4.0,
  "date": "2018-01-02",
  "end_date": null,
  "completed_hours": null,
  "custom_fields": [

  ],
  "created_at": "2025-06-03T17:08:57Z",
  "updated_at": "2025-06-03T17:08:57Z"
}
                
```


* * *

GET /api/v1/volunteer\_times/search - Search for Volunteer Times
----------------------------------------------------------------

Search for active volunteer times



* Parameter Name: q[]
  * Description: Query string. (EX: updated_from=2016-01-01). Parameter value must be URL encoded.
  * Type: string
  * Required?: true
  * Parameter Type: query
* Parameter Name: sort
  * Description: Sort by one of the following fields: 'date, constituent_id'. Add an exclamation point to reverse the order. (EX: sort=name!)
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
  * Response:                 urltomarkdowncodeblockplaceholder2690.5510961101016905              
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


|Date                 |date_from               |Date updated from (YYYY-MM-DDTHH:MM:SSZ) |
|---------------------|------------------------|-----------------------------------------|
|                     |date_to                 |Date updated to (YYYY-MM-DDTHH:MM:SSZ)   |
|Description          |description             |Description contains string              |
|Volunteering Category|volunteering_category_id|Comma separated volunteering_category_ids|
|Constituent Id       |constituent_id          |Comma separated constituent_ids          |
|Constituent Keyword  |const_keyword           |Comma separated Constituent keyword_ids  |
|Updated At           |updated_from            |Date updated from (YYYY-MM-DDTHH:MM:SSZ) |
|                     |updated_to              |Date updated to (YYYY-MM-DDTHH:MM:SSZ)   |


Note: Multiple terms may be combined using a semi-colon: "updated\_from=2018-05-04;updated\_to=2018-05-04"

### Example - Search by Description, Sorted by Date:

URI: https://api.littlegreenlight.com/api/v1/volunteer\_times/search

Query:

```
q[]=description=Donor management&sort=date!&limit=5
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 2,
  "total_items": 2,
  "limit": 5,
  "offset": 0,
  "item_type": "volunteer_time",
  "items": [
    {
      "id": 3040,
      "constituent_id": 959480,
      "external_id": "678890",
      "volunteering_category_id": 446,
      "volunteering_category_name": "General",
      "description": "Donor management",
      "hours": 4.0,
      "date": "2018-01-02",
      "end_date": null,
      "completed_hours": null,
      "custom_fields": [

      ],
      "created_at": "2025-06-03T17:08:57Z",
      "updated_at": "2025-06-03T17:08:57Z"
    },
    {
      "id": 3001,
      "constituent_id": 959480,
      "external_id": null,
      "volunteering_category_id": 446,
      "volunteering_category_name": "General",
      "description": "Donor management",
      "hours": 4.0,
      "date": "2018-01-02",
      "end_date": "2018-01-12",
      "completed_hours": 4.0,
      "custom_fields": [

      ],
      "created_at": "2023-11-15T22:04:55Z",
      "updated_at": "2023-11-15T22:04:56Z"
    }
  ]
}
                
```


### Example - Search by Constituent Keyword ID and Updated Since:

URI: https://api.littlegreenlight.com/api/v1/volunteer\_times/search

Query:

```
q[]=const_keyword=12221;updated_from=2016-01-01&limit=5
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 3,
  "total_items": 3,
  "limit": 5,
  "offset": 0,
  "item_type": "volunteer_time",
  "items": [
    {
      "id": 2981,
      "constituent_id": 959480,
      "external_id": null,
      "volunteering_category_id": 447,
      "volunteering_category_name": "Donor Management",
      "description": "",
      "hours": 4.0,
      "date": "2023-09-19",
      "end_date": "2023-09-19",
      "completed_hours": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-19T22:07:01Z",
      "updated_at": "2023-09-19T22:07:01Z"
    },
    {
      "id": 3040,
      "constituent_id": 959480,
      "external_id": "678890",
      "volunteering_category_id": 446,
      "volunteering_category_name": "General",
      "description": "Donor management",
      "hours": 4.0,
      "date": "2018-01-02",
      "end_date": null,
      "completed_hours": null,
      "custom_fields": [

      ],
      "created_at": "2025-06-03T17:08:57Z",
      "updated_at": "2025-06-03T17:08:57Z"
    },
    {
      "id": 3001,
      "constituent_id": 959480,
      "external_id": null,
      "volunteering_category_id": 446,
      "volunteering_category_name": "General",
      "description": "Donor management",
      "hours": 4.0,
      "date": "2018-01-02",
      "end_date": "2018-01-12",
      "completed_hours": 4.0,
      "custom_fields": [

      ],
      "created_at": "2023-11-15T22:04:55Z",
      "updated_at": "2023-11-15T22:04:56Z"
    }
  ]
}
                
```


* * *

GET /api/v1/volunteer\_times - Fetch Volunteer Times for Account
----------------------------------------------------------------

Lists all the volunteer times for an account.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2740.7332900678564958              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/volunteer\_times

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 4,
  "total_items": 4,
  "limit": 5,
  "offset": 0,
  "item_type": "volunteer_time",
  "items": [
    {
      "id": 2981,
      "constituent_id": 959480,
      "external_id": null,
      "volunteering_category_id": 447,
      "volunteering_category_name": "Donor Management",
      "description": "",
      "hours": 4.0,
      "date": "2023-09-19",
      "end_date": "2023-09-19",
      "completed_hours": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-19T22:07:01Z",
      "updated_at": "2023-09-19T22:07:01Z"
    },
    {
      "id": 2982,
      "constituent_id": 959508,
      "external_id": null,
      "volunteering_category_id": 446,
      "volunteering_category_name": "General",
      "description": "",
      "hours": 5.0,
      "date": "2023-09-20",
      "end_date": "2023-09-20",
      "completed_hours": null,
      "custom_fields": [

      ],
      "created_at": "2023-09-19T22:08:07Z",
      "updated_at": "2023-09-19T22:08:07Z"
    },
    {
      "id": 3001,
      "constituent_id": 959480,
      "external_id": null,
      "volunteering_category_id": 446,
      "volunteering_category_name": "General",
      "description": "Donor management",
      "hours": 4.0,
      "date": "2018-01-02",
      "end_date": "2018-01-12",
      "completed_hours": 4.0,
      "custom_fields": [

      ],
      "created_at": "2023-11-15T22:04:55Z",
      "updated_at": "2023-11-15T22:04:56Z"
    },
    {
      "id": 3040,
      "constituent_id": 959480,
      "external_id": "678890",
      "volunteering_category_id": 446,
      "volunteering_category_name": "General",
      "description": "Donor management",
      "hours": 4.0,
      "date": "2018-01-02",
      "end_date": null,
      "completed_hours": null,
      "custom_fields": [

      ],
      "created_at": "2025-06-03T17:08:57Z",
      "updated_at": "2025-06-03T17:08:57Z"
    }
  ]
}
                
```


* * *

GET /api/v1/volunteer\_times/{id} - Show Volunteer Time details
---------------------------------------------------------------

Show details for the volunteer time.


|Parameter Name|Description      |Type   |Required?|Parameter Type|
|--------------|-----------------|-------|---------|--------------|
|id            |Volunteer Time Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2760.9605979800948417              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/volunteer\_times/3040

Response:

```
                  
{
  "api_version": "1.0",
  "id": 3040,
  "constituent_id": 959480,
  "external_id": "678890",
  "volunteering_category_id": 446,
  "volunteering_category_name": "General",
  "description": "Donor management",
  "hours": 4.0,
  "date": "2018-01-02",
  "end_date": null,
  "completed_hours": null,
  "custom_fields": [

  ],
  "created_at": "2025-06-03T17:08:57Z",
  "updated_at": "2025-06-03T17:08:57Z"
}
                
```


* * *

PATCH /api/v1/volunteer\_times/{id} - Update Volunteer Time
-----------------------------------------------------------

Update the volunteer time.


|Parameter Name|Description      |Type      |Required?|Parameter Type|
|--------------|-----------------|----------|---------|--------------|
|id            |Volunteer Time Id|integer   |true     |path          |
|body          |Update Objects   |UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

constituent\_id ( integer , required ): Constituent ID,

external\_id ( integer , optional ): External Volunteering ID,

volunteering\_category\_id ( integer , required ): Volunteer Category Id,

volunteering\_category\_name ( string , optional ): Volunteer Category Name,

description ( string , optional ): Description,

hours ( double , optional ): Hours,

date ( date , optional ): Date,

end\_date ( date , optional ): End Date,

completed\_hours ( double , optional ): Completed Hours,

custom\_fields ( array , optional , CustomFieldAggregatedUpdate ): VolunteerTime custom fields (Categories)

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



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2780.2054764399391753              
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

URI: https://api.littlegreenlight.com/api/v1/volunteer\_times/3040

Body:

```
                  
{
  "end_date": "2018-01-12",
  "completed_hours": "4",
  "custom_fields": [
    {
      "name": "Sponsor",
      "values": [
        {
          "name": "LGL"
        }
      ]
    }
  ]
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 3040,
  "constituent_id": 959480,
  "external_id": "678890",
  "volunteering_category_id": 446,
  "volunteering_category_name": "General",
  "description": "Donor management",
  "hours": 4.0,
  "date": "2018-01-02",
  "end_date": "2018-01-12",
  "completed_hours": 4.0,
  "custom_fields": [

  ],
  "created_at": "2025-06-03T17:08:57Z",
  "updated_at": "2025-06-03T17:08:58Z"
}
                
```


* * *

DELETE /api/v1/volunteer\_times/{id} - Delete Volunteer Time
------------------------------------------------------------

Delete the volunteer time.


|Parameter Name|Description      |Type   |Required?|Parameter Type|
|--------------|-----------------|-------|---------|--------------|
|id            |Volunteer Time Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/volunteer\_times/3040

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

