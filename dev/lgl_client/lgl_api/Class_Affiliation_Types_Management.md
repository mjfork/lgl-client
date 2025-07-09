Class Affiliation Types Management
----------------------------------

GET /api/v1/class\_affiliation\_types - Fetch Class Affiliation Types
---------------------------------------------------------------------

Lists all the class affiliation types.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder310.5125391094023615              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/class\_affiliation\_types

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 3,
  "total_items": 3,
  "limit": 5,
  "offset": 0,
  "item_type": "class_affiliation_type",
  "items": [
    {
      "id": 515,
      "name": "Student",
      "ordinal": 0
    },
    {
      "id": 516,
      "name": "Parent",
      "ordinal": 1
    },
    {
      "id": 517,
      "name": "Grandparent",
      "ordinal": 2
    }
  ]
}
                
```


* * *

