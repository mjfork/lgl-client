Category Management
-------------------

GET /api/v1/categories - Fetch Categories for Account
-----------------------------------------------------

Lists all the categories for an account.



* Parameter Name: item_type
  * Description: Categories for type (default: Constituent). Available: Constituent, Gift, VolunteerTime
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
  * Response:                 urltomarkdowncodeblockplaceholder170.30781727201906484              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/categories

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 4,
  "total_items": 4,
  "limit": 5,
  "offset": 0,
  "item_type": "category",
  "items": [
    {
      "id": 1041,
      "item_type": "Constituent",
      "name": "Acknowledgment Preference",
      "key": "ack_preferences",
      "facet_type": "single",
      "ordinal": 100,
      "removable": false,
      "editable": true,
      "display_format": "compact",
      "keywords": [
        {
          "id": 12220,
          "category_id": 1041,
          "name": "Prefers mail",
          "description": null,
          "short_code": "ack_pref_mailing",
          "ordinal": 0,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        },
        {
          "id": 12221,
          "category_id": 1041,
          "name": "Prefers email",
          "description": null,
          "short_code": "ack_pref_email",
          "ordinal": 1,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        },
        {
          "id": 12222,
          "category_id": 1041,
          "name": "Prefers none",
          "description": null,
          "short_code": "ack_pref_none",
          "ordinal": 2,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        }
      ]
    },
    {
      "id": 1039,
      "item_type": "Constituent",
      "name": "Communication Tags",
      "key": "tags",
      "facet_type": "list",
      "ordinal": 100,
      "removable": true,
      "editable": true,
      "display_format": "compact",
      "keywords": [
        {
          "id": 12211,
          "category_id": 1039,
          "name": "Do not call",
          "description": null,
          "short_code": "do_not_call",
          "ordinal": 100,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        },
        {
          "id": 12210,
          "category_id": 1039,
          "name": "Do not email",
          "description": null,
          "short_code": "do_not_email",
          "ordinal": 100,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        },
        {
          "id": 12209,
          "category_id": 1039,
          "name": "Do not mail",
          "description": null,
          "short_code": "do_not_mail",
          "ordinal": 100,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        },
        {
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
      ]
    },
    {
      "id": 1040,
      "item_type": "Constituent",
      "name": "Giving Status",
      "key": "giving_status",
      "facet_type": "list",
      "ordinal": 100,
      "removable": false,
      "editable": false,
      "display_format": "compact",
      "keywords": [
        {
          "id": 12215,
          "category_id": 1040,
          "name": "Top 100 Donor",
          "description": null,
          "short_code": "top_100_donor",
          "ordinal": 0,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        },
        {
          "id": 12217,
          "category_id": 1040,
          "name": "New Donor",
          "description": null,
          "short_code": "new_donor",
          "ordinal": 1,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        },
        {
          "id": 12216,
          "category_id": 1040,
          "name": "Active Donor",
          "description": null,
          "short_code": "active_donor",
          "ordinal": 2,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        },
        {
          "id": 12218,
          "category_id": 1040,
          "name": "Lapsed Donor",
          "description": null,
          "short_code": "lapsed_donor",
          "ordinal": 3,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        },
        {
          "id": 12219,
          "category_id": 1040,
          "name": "Non Donor",
          "description": null,
          "short_code": "non_donor",
          "ordinal": 4,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        }
      ]
    },
    {
      "id": 1042,
      "item_type": "Constituent",
      "name": "New Custom Category",
      "key": "3fc5a2c0_ba66_43bc_9fc9_17959941bae4",
      "facet_type": "list",
      "ordinal": 100,
      "removable": true,
      "editable": true,
      "display_format": "compact",
      "keywords": [
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
  ]
}
                
```


### Example:

URI: https://api.littlegreenlight.com/api/v1/categories

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 25,
  "offset": 0,
  "item_type": "category",
  "items": [
    {
      "id": 1056,
      "item_type": "Gift",
      "name": "Test Gift Field #2",
      "key": "e0c9cb38_48e9_4515_abde_72a6d93722e6",
      "facet_type": "list",
      "ordinal": 100,
      "removable": true,
      "editable": true,
      "display_format": "compact",
      "keywords": [
        {
          "id": 12252,
          "category_id": 1056,
          "name": "v1",
          "description": null,
          "short_code": null,
          "ordinal": 100,
          "removable": true,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-19T17:00:48Z",
          "updated_at": "2023-09-19T17:00:48Z"
        },
        {
          "id": 12253,
          "category_id": 1056,
          "name": "v2",
          "description": null,
          "short_code": null,
          "ordinal": 100,
          "removable": true,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-19T17:00:48Z",
          "updated_at": "2023-09-19T17:00:48Z"
        },
        {
          "id": 12254,
          "category_id": 1056,
          "name": "v3",
          "description": null,
          "short_code": null,
          "ordinal": 100,
          "removable": true,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-19T17:00:48Z",
          "updated_at": "2023-09-19T17:00:48Z"
        }
      ]
    }
  ]
}
                
```


* * *

POST /api/v1/categories - Create new Category
---------------------------------------------

Add a category to an account.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

item\_type ( string , required ): Item Type,

name ( string , required ): Name,

key ( string , optional ): Key,

facet\_type ( string , optional ): Facet Type,

ordinal ( integer , optional ): Ordinal,

removable ( boolean , optional ): Removable?,

editable ( boolean , optional ): Editable?,

display\_format ( string , optional ): Display Format

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder200.0034454370333085738              
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

URI: https://api.littlegreenlight.com/api/v1/categories

Body:

```
                  
{
  "item_type": "Constituent",
  "name": "My Cat",
  "key": "my_cat"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 1123,
  "item_type": "Constituent",
  "name": "My Cat",
  "key": "my_cat",
  "facet_type": "list",
  "ordinal": 100,
  "removable": true,
  "editable": true,
  "display_format": "compact",
  "keywords": [

  ]
}
                
```


* * *

GET /api/v1/categories/{id} - Show Category details
---------------------------------------------------

Show details for the category.


|Parameter Name|Description|Type   |Required?|Parameter Type|
|--------------|-----------|-------|---------|--------------|
|id            |Category Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder230.0799899099774759              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/categories/1042

Response:

```
                  
{
  "api_version": "1.0",
  "id": 1042,
  "item_type": "Constituent",
  "name": "New Custom Category",
  "key": "3fc5a2c0_ba66_43bc_9fc9_17959941bae4",
  "facet_type": "list",
  "ordinal": 100,
  "removable": true,
  "editable": true,
  "display_format": "compact",
  "keywords": [
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

PATCH /api/v1/categories/{id} - Update Category
-----------------------------------------------

Update the category.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|id            |Category Id   |integer   |true     |path          |
|body          |Update Objects|UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

item\_type ( string , required ): Item Type,

name ( string , required ): Name,

key ( string , optional ): Key,

facet\_type ( string , optional ): Facet Type,

ordinal ( integer , optional ): Ordinal,

removable ( boolean , optional ): Removable?,

editable ( boolean , optional ): Editable?,

display\_format ( string , optional ): Display Format

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder250.8134009863710179              
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

URI: https://api.littlegreenlight.com/api/v1/categories/1123

Body:

```
                  
{
  "facet_type": "single"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 1123,
  "item_type": "Constituent",
  "name": "My Cat",
  "key": "my_cat",
  "facet_type": "single",
  "ordinal": 100,
  "removable": true,
  "editable": true,
  "display_format": "compact",
  "keywords": [

  ]
}
                
```


* * *

DELETE /api/v1/categories/{id} - Delete Category
------------------------------------------------

Delete the category.


|Parameter Name|Description|Type   |Required?|Parameter Type|
|--------------|-----------|-------|---------|--------------|
|id            |Category Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/categories/1123

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

GET /api/v1/constituents/{constituent\_id}/categories - Fetch Categories for Constituent
----------------------------------------------------------------------------------------

Lists all the categories for a constituent.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder290.6534333017508462              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/categories

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 3,
  "total_items": 3,
  "limit": 25,
  "offset": 0,
  "item_type": "category",
  "items": [
    {
      "id": 1041,
      "item_type": "Constituent",
      "name": "Acknowledgment Preference",
      "key": "ack_preferences",
      "facet_type": "single",
      "ordinal": 100,
      "removable": false,
      "editable": true,
      "display_format": "compact",
      "keywords": [
        {
          "id": 12221,
          "category_id": 1041,
          "name": "Prefers email",
          "description": null,
          "short_code": "ack_pref_email",
          "ordinal": 1,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        }
      ]
    },
    {
      "id": 1040,
      "item_type": "Constituent",
      "name": "Giving Status",
      "key": "giving_status",
      "facet_type": "list",
      "ordinal": 100,
      "removable": false,
      "editable": false,
      "display_format": "compact",
      "keywords": [
        {
          "id": 12218,
          "category_id": 1040,
          "name": "Lapsed Donor",
          "description": null,
          "short_code": "lapsed_donor",
          "ordinal": 3,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        }
      ]
    },
    {
      "id": 1039,
      "item_type": "Constituent",
      "name": "Communication Tags",
      "key": "tags",
      "facet_type": "list",
      "ordinal": 100,
      "removable": true,
      "editable": true,
      "display_format": "compact",
      "keywords": [
        {
          "id": 12211,
          "category_id": 1039,
          "name": "Do not call",
          "description": null,
          "short_code": "do_not_call",
          "ordinal": 100,
          "removable": false,
          "can_change": true,
          "can_select": true,
          "created_at": "2023-09-18T18:06:47Z",
          "updated_at": "2023-09-18T18:06:47Z"
        }
      ]
    }
  ]
}
                
```


* * *

