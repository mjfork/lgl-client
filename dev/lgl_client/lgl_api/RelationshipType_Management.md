RelationshipType Management
---------------------------

GET /api/v1/relationship\_types - Fetch Relationship Types
----------------------------------------------------------

Lists all the relationship types.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2450.39732368926181505              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/relationship\_types

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 5,
  "total_items": 11,
  "limit": 5,
  "offset": 0,
  "next_item": 5,
  "next_link": "https://api.littlegreenlight.com/api/v1/relationship_types?limit=5&offset=5",
  "item_type": "relationship_type",
  "items": [
    {
      "id": 41,
      "name": "Parent",
      "short_code": "Parent",
      "type_code": "family",
      "ordinal": 0,
      "removable": true,
      "reciprocal_id": null,
      "auto_soft_credit": null,
      "share_class_year": null,
      "share_membership": false,
      "is_spouse_partner": false,
      "share_class_year_to": null
    },
    {
      "id": 42,
      "name": "Mother",
      "short_code": "Mother",
      "type_code": "family",
      "ordinal": 1,
      "removable": true,
      "reciprocal_id": null,
      "auto_soft_credit": null,
      "share_class_year": null,
      "share_membership": false,
      "is_spouse_partner": false,
      "share_class_year_to": null
    },
    {
      "id": 43,
      "name": "Father",
      "short_code": "Father",
      "type_code": "family",
      "ordinal": 2,
      "removable": true,
      "reciprocal_id": null,
      "auto_soft_credit": null,
      "share_class_year": null,
      "share_membership": false,
      "is_spouse_partner": false,
      "share_class_year_to": null
    },
    {
      "id": 44,
      "name": "Child",
      "short_code": "Child",
      "type_code": "family",
      "ordinal": 3,
      "removable": true,
      "reciprocal_id": null,
      "auto_soft_credit": null,
      "share_class_year": null,
      "share_membership": false,
      "is_spouse_partner": false,
      "share_class_year_to": null
    },
    {
      "id": 45,
      "name": "Daughter",
      "short_code": "Daughter",
      "type_code": "family",
      "ordinal": 4,
      "removable": true,
      "reciprocal_id": null,
      "auto_soft_credit": null,
      "share_class_year": null,
      "share_membership": false,
      "is_spouse_partner": false,
      "share_class_year_to": null
    }
  ]
}
                
```


* * *

