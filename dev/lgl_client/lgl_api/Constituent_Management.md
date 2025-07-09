Constituent Management
----------------------

GET /api/v1/constituents/search - Search for Constituents
---------------------------------------------------------

Search for active constituents.



* Parameter Name: q[]
  * Description: Query string. (EX: name=brady). Parameter value must be URL encoded.
  * Type: string
  * Required?: true
  * Parameter Type: query
* Parameter Name: expand
  * Description: Expand requested, comma separated, data structures: 'class_affiliations, relationships, street_addresses, phone_numbers, email_addresses, web_addresses, categories, groups, memberships, custom_attrs'
  * Type: string
  * Required?: 
  * Parameter Type: query
* Parameter Name: sort
  * Description: Sort by one of the following fields: 'name, external_id, lgl_id, date_created, date_updated, membership_level, membership_end_date_from'. Add an exclamation point to reverse the order. (EX: sort=name!)
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
  * Response:                 urltomarkdowncodeblockplaceholder430.997806642679359              
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



* Name: Email
  * name: eaddr
  * Any name field contains term: Email contains term
* Name: Phone Number
  * name: phone_number
  * Any name field contains term: Phone number contains term
* Name: Street Address
  * name: street
  * Any name field contains term: Street contains term
* Name: 
  * name: city
  * Any name field contains term: City equals term
* Name: 
  * name: state
  * Any name field contains term: State equals term (2 letter)
* Name: 
  * name: postal_code
  * Any name field contains term: Postal code equals term (matches left most characters)
* Name: 
  * name: country
  * Any name field contains term: Country contains term
* Name: Keyword
  * name: keyword
  * Any name field contains term: Has keyword ID
* Name: Updated At
  * name: updated_from
  * Any name field contains term: Date updated from (YYYY-MM-DDTHH:MM:SSZ)
* Name: 
  * name: updated_to
  * Any name field contains term: Date updated to (YYYY-MM-DDTHH:MM:SSZ)
* Name: Membership
  * name: membership_status
  * Any name field contains term: 0 = Lapsed, 1 = Active
* Name: 
  * name: membership_level
  * Any name field contains term: Comma separated membership_level_ids
* Name: 
  * name: membership_end_date_from
  * Any name field contains term: Latest membership end date from (YYYY-MM-DD)
* Name: 
  * name: membership_end_date_to
  * Any name field contains term: Latest membership end date to (YYYY-MM-DD)
* Name: External ID
  * name: external_id
  * Any name field contains term: The external_id equals term
* Name: Constituent Type
  * name: constituent_type
  * Any name field contains term: 0 = Individual, 1 = Organization
* Name: Groups
  * name: groups
  * Any name field contains term: Comma separated group_ids
* Name: Class Affiliations
  * name: class
  * Any name field contains term: "type[,type]|YYYY-MM-DD[ to YYYY-MM-DD]" (Dates)
* Name: Custom Attributes
  * name: custom_attr
  * Any name field contains term: "key|op|value"
* Name: 
  * name: key:
  * Any name field contains term: Custom attribute key
* Name: 
  * name: op:
  * Any name field contains term: Operator:
* Name: 
  * name: 
  * Any name field contains term: "ft" - contains
* Name: 
  * name: 
  * Any name field contains term: "nft" - doesn't contains
* Name: 
  * name: 
  * Any name field contains term: "eq" - equals
* Name: 
  * name: 
  * Any name field contains term: "ne" - doesn't equal
* Name: 
  * name: 
  * Any name field contains term: "sw" - starts with
* Name: 
  * name: 
  * Any name field contains term: "bl" - is blank
* Name: 
  * name: 
  * Any name field contains term: "nb" - not blank
* Name: 
  * name: custom_attr_from
  * Any name field contains term: "key|YYYY-MM-DD" (Dates)
* Name: 
  * name: custom_attr_to
  * Any name field contains term: "key|YYYY-MM-DD" (Dates)
* Name: 
  * name: custom_attr_int
  * Any name field contains term: "key|op|number[|number2]" (Number, Currency)
* Name: 
  * name: key:
  * Any name field contains term: Custom attribute key
* Name: 
  * name: op:
  * Any name field contains term: Operator:
* Name: 
  * name: 
  * Any name field contains term: "gte" - is greater/equal
* Name: 
  * name: 
  * Any name field contains term: "lte" - is less/equal
* Name: 
  * name: 
  * Any name field contains term: "btw" - is between number and number2
* Name: 
  * name: 
  * Any name field contains term: "gt" - is greater than
* Name: 
  * name: 
  * Any name field contains term: "lt" - is less than
* Name: 
  * name: 
  * Any name field contains term: "eq" - equals
* Name: 
  * name: 
  * Any name field contains term: "ne" - doesn't equal


Note: Multiple terms may be combined using a semi-colon: "membership\_end\_date\_from=2018-05-04;membership\_end\_date\_to=2018-05-04"

### Example - Search by Name and sort:

URI: https://api.littlegreenlight.com/api/v1/constituents/search

Query:

```
q[]=name=brady&sort=name&limit=5
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 5,
  "offset": 0,
  "item_type": "constituent",
  "items": [
    {
      "id": 959508,
      "external_constituent_id": "t00072",
      "is_org": false,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": null,
      "first_name": "Mike",
      "middle_name": null,
      "last_name": "Brady",
      "suffix": null,
      "spouse_name": null,
      "org_name": null,
      "job_title": null,
      "addressee": "Mr. and Mrs. Mike Brady",
      "salutation": "Mike and Carol",
      "sort_name": "Brady, Mike",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": "Mr. and Mrs. Mike Brady",
      "birthday": null,
      "gender": null,
      "maiden_name": null,
      "nick_name": null,
      "spouse_nick_name": null,
      "date_added": "2023-09-18",
      "alt_salutation": "Mike and Carol",
      "alt_addressee": "Mr. and Mrs. Mike Brady",
      "honorary_name": "Mr. and Mrs. Mike Brady",
      "assistant_name": null,
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:25:25Z",
      "updated_at": "2023-10-31T18:01:04Z"
    }
  ]
}
                
```


### Example - Search by Name and Expand Class Affiliation, Relationship, Address, Phone, and Email Records:

URI: https://api.littlegreenlight.com/api/v1/constituents/search

Query:

```
q[]=name=brady&expand=class_affiliations,relationships,street_addresses,phone_numbers,email_addresses&limit=3
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 3,
  "offset": 0,
  "item_type": "constituent",
  "items": [
    {
      "id": 959508,
      "external_constituent_id": "t00072",
      "is_org": false,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": null,
      "first_name": "Mike",
      "middle_name": null,
      "last_name": "Brady",
      "suffix": null,
      "spouse_name": null,
      "org_name": null,
      "job_title": null,
      "addressee": "Mr. and Mrs. Mike Brady",
      "salutation": "Mike and Carol",
      "sort_name": "Brady, Mike",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": "Mr. and Mrs. Mike Brady",
      "birthday": null,
      "gender": null,
      "maiden_name": null,
      "nick_name": null,
      "spouse_nick_name": null,
      "date_added": "2023-09-18",
      "alt_salutation": "Mike and Carol",
      "alt_addressee": "Mr. and Mrs. Mike Brady",
      "honorary_name": "Mr. and Mrs. Mike Brady",
      "assistant_name": null,
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:25:25Z",
      "updated_at": "2023-10-31T18:01:04Z",
      "class_affiliations": [
        {
          "id": 154,
          "constituent_id": 959508,
          "class_affiliation_type_id": 515,
          "year": 1978,
          "note": "graduated cum laude"
        },
        {
          "id": 155,
          "constituent_id": 959508,
          "class_affiliation_type_id": 516,
          "year": 2001,
          "note": "Mikey (son)"
        }
      ],
      "relationships": [

      ],
      "street_addresses": [
        {
          "id": 838407,
          "street": "4222 Clinton Way",
          "city": "Los Angeles",
          "state": "CA",
          "country": "US",
          "postal_code": "90002",
          "county": null,
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
          "zip5": "90002",
          "verified": false,
          "verified_on": null,
          "created_at": "2023-09-18T18:25:25Z",
          "updated_at": "2023-09-18T18:25:25Z"
        }
      ],
      "phone_numbers": [
        {
          "id": 479655,
          "number": "(888) 555-0072",
          "phone_number_type_id": 1,
          "phone_type_name": "Home",
          "is_preferred": true,
          "not_current": false,
          "parent_id": null,
          "normalized_number": "8885550072",
          "created_at": "2023-09-18T18:25:25Z",
          "updated_at": "2023-09-18T18:25:25Z"
        }
      ],
      "email_addresses": [
        {
          "id": 276492,
          "address": "brady@thebradybunch.com",
          "email_address_type_id": 1,
          "email_type_name": "Home",
          "is_preferred": true,
          "not_current": false,
          "parent_id": null,
          "created_at": "2023-09-18T18:25:25Z",
          "updated_at": "2023-09-18T18:25:25Z"
        }
      ]
    }
  ]
}
                
```


### Example - Search by Custom Keyword ID and Updated Since:

URI: https://api.littlegreenlight.com/api/v1/constituents/search

Query:

```
q[]=keyword=12221;updated_from=2016-01-01&limit=5
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 2,
  "total_items": 2,
  "limit": 5,
  "offset": 0,
  "item_type": "constituent",
  "items": [
    {
      "id": 959480,
      "external_constituent_id": "t00044",
      "is_org": false,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": "",
      "first_name": "Larry",
      "middle_name": "",
      "last_name": "Appleton",
      "suffix": "",
      "spouse_name": "",
      "org_name": "Perfect Strangers",
      "job_title": "",
      "addressee": "Larry Appleton and his cousin Balki Bartokomous",
      "salutation": "Larry",
      "sort_name": "Appleton, Larry",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": "Larry Appleton and his cousin Balki Bartokomous",
      "birthday": null,
      "gender": null,
      "maiden_name": "",
      "nick_name": "",
      "spouse_nick_name": "",
      "date_added": "2023-09-18",
      "alt_salutation": "Larry",
      "alt_addressee": "Larry Appleton and his cousin Balki Bartokomous",
      "honorary_name": "Larry Appleton and his cousin Balki Bartokomous",
      "assistant_name": "",
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:25:01Z",
      "updated_at": "2025-04-07T17:08:22Z"
    },
    {
      "id": 959453,
      "external_constituent_id": "t00017",
      "is_org": false,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": "",
      "first_name": "Ray",
      "middle_name": "",
      "last_name": "Barone",
      "suffix": "",
      "spouse_name": "",
      "org_name": "Everybody Loves Raymond",
      "job_title": "",
      "addressee": "Barone family",
      "salutation": "Ray",
      "sort_name": "Barone, Ray",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": "Barone family",
      "birthday": null,
      "gender": null,
      "maiden_name": "",
      "nick_name": "",
      "spouse_nick_name": "",
      "date_added": "2023-09-18",
      "alt_salutation": "Ray",
      "alt_addressee": "Barone family",
      "honorary_name": "Barone family",
      "assistant_name": "",
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:24:43Z",
      "updated_at": "2023-10-31T18:01:04Z"
    }
  ]
}
                
```


### Example - Search For Organizations, Sort by Date Updated:

URI: https://api.littlegreenlight.com/api/v1/constituents/search

Query:

```
q[]=constituent_type=1&sort=date_updated!&limit=5
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 5,
  "total_items": 8,
  "limit": 5,
  "offset": 0,
  "next_item": 5,
  "next_link": "https://api.littlegreenlight.com/api/v1/constituents/search?limit=5&offset=5&q%5B%5D=constituent_type%3D1&sort=date_updated%21",
  "item_type": "constituent",
  "items": [
    {
      "id": 959506,
      "external_constituent_id": "t00070",
      "is_org": true,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": null,
      "first_name": null,
      "middle_name": null,
      "last_name": "Bower",
      "suffix": null,
      "spouse_name": null,
      "org_name": "Who's the Boss?",
      "job_title": null,
      "addressee": "The Bower Agency",
      "salutation": null,
      "sort_name": "Who's the Boss?",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": null,
      "birthday": null,
      "gender": null,
      "maiden_name": null,
      "nick_name": null,
      "spouse_nick_name": null,
      "date_added": "2023-09-18",
      "alt_salutation": null,
      "alt_addressee": "The Bower Agency",
      "honorary_name": null,
      "assistant_name": null,
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:25:24Z",
      "updated_at": "2023-10-31T18:01:08Z"
    },
    {
      "id": 959507,
      "external_constituent_id": "t00071",
      "is_org": true,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": null,
      "first_name": null,
      "middle_name": null,
      "last_name": "Xavier Institute for Higher Learning",
      "suffix": null,
      "spouse_name": null,
      "org_name": "X Men",
      "job_title": null,
      "addressee": "Xavier Institute for Higher Learning",
      "salutation": null,
      "sort_name": "X Men",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": null,
      "birthday": null,
      "gender": null,
      "maiden_name": null,
      "nick_name": null,
      "spouse_nick_name": null,
      "date_added": "2023-09-18",
      "alt_salutation": null,
      "alt_addressee": "Xavier Institute for Higher Learning",
      "honorary_name": null,
      "assistant_name": null,
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:25:25Z",
      "updated_at": "2023-10-31T18:01:08Z"
    },
    {
      "id": 959491,
      "external_constituent_id": "t00055",
      "is_org": true,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": null,
      "first_name": null,
      "middle_name": null,
      "last_name": "The Fantastic Four",
      "suffix": null,
      "spouse_name": null,
      "org_name": "The Fantastic Four",
      "job_title": null,
      "addressee": "The Fantastic Four",
      "salutation": null,
      "sort_name": "The Fantastic Four",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": null,
      "birthday": null,
      "gender": null,
      "maiden_name": null,
      "nick_name": null,
      "spouse_nick_name": null,
      "date_added": "2023-09-18",
      "alt_salutation": null,
      "alt_addressee": "The Fantastic Four",
      "honorary_name": null,
      "assistant_name": null,
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:25:14Z",
      "updated_at": "2023-10-31T18:01:07Z"
    },
    {
      "id": 959471,
      "external_constituent_id": "t00035",
      "is_org": true,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": null,
      "first_name": null,
      "middle_name": null,
      "last_name": "Laverne & Shirley",
      "suffix": null,
      "spouse_name": null,
      "org_name": "Laverne & Shirley",
      "job_title": null,
      "addressee": "Laverne & Shirley",
      "salutation": null,
      "sort_name": "Laverne & Shirley",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": null,
      "birthday": null,
      "gender": null,
      "maiden_name": null,
      "nick_name": null,
      "spouse_nick_name": null,
      "date_added": "2023-09-18",
      "alt_salutation": null,
      "alt_addressee": "Laverne & Shirley",
      "honorary_name": null,
      "assistant_name": null,
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:24:54Z",
      "updated_at": "2023-10-31T18:01:06Z"
    },
    {
      "id": 959478,
      "external_constituent_id": "t00042",
      "is_org": true,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": null,
      "first_name": null,
      "middle_name": null,
      "last_name": "Phil's",
      "suffix": null,
      "spouse_name": null,
      "org_name": "Murphy Brown",
      "job_title": null,
      "addressee": "Phil's Bar & Grill",
      "salutation": null,
      "sort_name": "Murphy Brown",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": null,
      "birthday": null,
      "gender": null,
      "maiden_name": null,
      "nick_name": null,
      "spouse_nick_name": null,
      "date_added": "2023-09-18",
      "alt_salutation": null,
      "alt_addressee": "Phil's Bar & Grill",
      "honorary_name": null,
      "assistant_name": null,
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:25:00Z",
      "updated_at": "2023-10-31T18:01:06Z"
    }
  ]
}
                
```


### Example - Search Full Text of Custom Attribute:

URI: https://api.littlegreenlight.com/api/v1/constituents/search

Query:

```
q[]=custom_attr=background_info|ft|Ck returned&limit=5
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 5,
  "offset": 0,
  "item_type": "constituent",
  "items": [
    {
      "id": 959448,
      "external_constituent_id": "t00012",
      "is_org": false,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": "",
      "first_name": "Susan",
      "middle_name": "",
      "last_name": "Alexander",
      "suffix": "",
      "spouse_name": "",
      "org_name": "Citizen Kane",
      "job_title": "",
      "addressee": "Mrs. Susan Alexander",
      "salutation": "Susan",
      "sort_name": "Alexander, Susan",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": "Mrs. Susan Alexander",
      "birthday": null,
      "gender": null,
      "maiden_name": "",
      "nick_name": "",
      "spouse_nick_name": "",
      "date_added": "2023-09-18",
      "alt_salutation": "Susan",
      "alt_addressee": "Mrs. Susan Alexander",
      "honorary_name": "Mrs. Susan Alexander",
      "assistant_name": "",
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:24:41Z",
      "updated_at": "2023-10-31T17:53:29Z"
    }
  ]
}
                
```


### Example - Search Between Numbers for Custom Attribute:

URI: https://api.littlegreenlight.com/api/v1/constituents/search

Query:

```
q[]=custom_attr_int=test_number|btw|5|50&limit=5
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 5,
  "offset": 0,
  "item_type": "constituent",
  "items": [
    {
      "id": 959456,
      "external_constituent_id": "t00020",
      "is_org": false,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": "",
      "first_name": "Ferris",
      "middle_name": "",
      "last_name": "Bueller",
      "suffix": "",
      "spouse_name": "",
      "org_name": "Ferris Bueller's Day Off",
      "job_title": "",
      "addressee": "Bueller family",
      "salutation": "Ferris",
      "sort_name": "Bueller, Ferris",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": "Bueller family",
      "birthday": null,
      "gender": null,
      "maiden_name": "",
      "nick_name": "",
      "spouse_nick_name": "",
      "date_added": "2023-09-18",
      "alt_salutation": "Ferris",
      "alt_addressee": "Bueller family",
      "honorary_name": "Bueller family",
      "assistant_name": "",
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:24:45Z",
      "updated_at": "2023-10-31T18:01:04Z"
    }
  ]
}
                
```


### Example - Search for Parent and Grandparent Class Affiliations between 2000 and 2009:

URI: https://api.littlegreenlight.com/api/v1/constituents/search

Query:

```
q[]=class=516,517|2000 to 2009&expand=class_affiliations&limit=5
```


Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 5,
  "offset": 0,
  "item_type": "constituent",
  "items": [
    {
      "id": 959508,
      "external_constituent_id": "t00072",
      "is_org": false,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": null,
      "first_name": "Mike",
      "middle_name": null,
      "last_name": "Brady",
      "suffix": null,
      "spouse_name": null,
      "org_name": null,
      "job_title": null,
      "addressee": "Mr. and Mrs. Mike Brady",
      "salutation": "Mike and Carol",
      "sort_name": "Brady, Mike",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": "Mr. and Mrs. Mike Brady",
      "birthday": null,
      "gender": null,
      "maiden_name": null,
      "nick_name": null,
      "spouse_nick_name": null,
      "date_added": "2023-09-18",
      "alt_salutation": "Mike and Carol",
      "alt_addressee": "Mr. and Mrs. Mike Brady",
      "honorary_name": "Mr. and Mrs. Mike Brady",
      "assistant_name": null,
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:25:25Z",
      "updated_at": "2023-10-31T18:01:04Z",
      "class_affiliations": [
        {
          "id": 154,
          "constituent_id": 959508,
          "class_affiliation_type_id": 515,
          "year": 1978,
          "note": "graduated cum laude"
        },
        {
          "id": 155,
          "constituent_id": 959508,
          "class_affiliation_type_id": 516,
          "year": 2001,
          "note": "Mikey (son)"
        }
      ]
    }
  ]
}
                
```


### Example - Unknown Parameter Error:

URI: https://api.littlegreenlight.com/api/v1/constituents/search

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "error": "Parameter Error",
  "description": "Unknown query parameter: badterm"
}
                
```


* * *

GET /api/v1/constituents - Fetch all Constituents for an account
----------------------------------------------------------------

This lists all the active constituents for an account.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder590.4510768708255195              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 5,
  "total_items": 84,
  "limit": 5,
  "offset": 0,
  "next_item": 5,
  "next_link": "https://api.littlegreenlight.com/api/v1/constituents?limit=5&offset=5",
  "item_type": "constituent",
  "items": [
    {
      "id": 959448,
      "external_constituent_id": "t00012",
      "is_org": false,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": "",
      "first_name": "Susan",
      "middle_name": "",
      "last_name": "Alexander",
      "suffix": "",
      "spouse_name": "",
      "org_name": "Citizen Kane",
      "job_title": "",
      "addressee": "Mrs. Susan Alexander",
      "salutation": "Susan",
      "sort_name": "Alexander, Susan",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": "Mrs. Susan Alexander",
      "birthday": null,
      "gender": null,
      "maiden_name": "",
      "nick_name": "",
      "spouse_nick_name": "",
      "date_added": "2023-09-18",
      "alt_salutation": "Susan",
      "alt_addressee": "Mrs. Susan Alexander",
      "honorary_name": "Mrs. Susan Alexander",
      "assistant_name": "",
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:24:41Z",
      "updated_at": "2023-10-31T17:53:29Z"
    },
    {
      "id": 959480,
      "external_constituent_id": "t00044",
      "is_org": false,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": "",
      "first_name": "Larry",
      "middle_name": "",
      "last_name": "Appleton",
      "suffix": "",
      "spouse_name": "",
      "org_name": "Perfect Strangers",
      "job_title": "",
      "addressee": "Larry Appleton and his cousin Balki Bartokomous",
      "salutation": "Larry",
      "sort_name": "Appleton, Larry",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": "Larry Appleton and his cousin Balki Bartokomous",
      "birthday": null,
      "gender": null,
      "maiden_name": "",
      "nick_name": "",
      "spouse_nick_name": "",
      "date_added": "2023-09-18",
      "alt_salutation": "Larry",
      "alt_addressee": "Larry Appleton and his cousin Balki Bartokomous",
      "honorary_name": "Larry Appleton and his cousin Balki Bartokomous",
      "assistant_name": "",
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:25:01Z",
      "updated_at": "2025-04-07T17:08:22Z"
    },
    {
      "id": 959486,
      "external_constituent_id": "t00050",
      "is_org": false,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": null,
      "first_name": null,
      "middle_name": null,
      "last_name": "Archer's",
      "suffix": null,
      "spouse_name": null,
      "org_name": "series of novels",
      "job_title": null,
      "addressee": "Lew Archer's office",
      "salutation": "Archer's",
      "sort_name": "Archer's",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": "Lew Archer's office",
      "birthday": null,
      "gender": null,
      "maiden_name": null,
      "nick_name": null,
      "spouse_nick_name": null,
      "date_added": "2023-09-18",
      "alt_salutation": "Archer's",
      "alt_addressee": "Lew Archer's office",
      "honorary_name": "Lew Archer's office",
      "assistant_name": null,
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:25:11Z",
      "updated_at": "2023-10-31T18:01:04Z"
    },
    {
      "id": 959440,
      "external_constituent_id": "t00004",
      "is_org": true,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": null,
      "first_name": null,
      "middle_name": null,
      "last_name": "Mansion",
      "suffix": null,
      "spouse_name": null,
      "org_name": "Avengers Mansion Headquarters of the Avengers",
      "job_title": null,
      "addressee": "Headquarters of the Avengers",
      "salutation": null,
      "sort_name": "Avengers Mansion Headquarters of the Avengers",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": null,
      "birthday": null,
      "gender": null,
      "maiden_name": null,
      "nick_name": null,
      "spouse_nick_name": null,
      "date_added": "2023-09-18",
      "alt_salutation": null,
      "alt_addressee": "Headquarters of the Avengers",
      "honorary_name": null,
      "assistant_name": null,
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:24:35Z",
      "updated_at": "2023-10-31T18:01:04Z"
    },
    {
      "id": 959453,
      "external_constituent_id": "t00017",
      "is_org": false,
      "constituent_contact_type_id": 1243,
      "constituent_contact_type_name": "Primary",
      "prefix": "",
      "first_name": "Ray",
      "middle_name": "",
      "last_name": "Barone",
      "suffix": "",
      "spouse_name": "",
      "org_name": "Everybody Loves Raymond",
      "job_title": "",
      "addressee": "Barone family",
      "salutation": "Ray",
      "sort_name": "Barone, Ray",
      "constituent_interest_level_id": null,
      "constituent_interest_level_name": null,
      "constituent_rating_id": null,
      "constituent_rating_name": null,
      "is_deceased": false,
      "deceased_date": null,
      "annual_report_name": "Barone family",
      "birthday": null,
      "gender": null,
      "maiden_name": "",
      "nick_name": "",
      "spouse_nick_name": "",
      "date_added": "2023-09-18",
      "alt_salutation": "Ray",
      "alt_addressee": "Barone family",
      "honorary_name": "Barone family",
      "assistant_name": "",
      "marital_status_id": null,
      "marital_status_name": null,
      "is_anon": false,
      "created_at": "2023-09-18T18:24:43Z",
      "updated_at": "2023-10-31T18:01:04Z"
    }
  ]
}
                
```


* * *

POST /api/v1/constituents - Create new Constituent
--------------------------------------------------

Add a Constituent to an account along with related objects.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

external\_constituent\_id ( integer , optional ): External constituent ID,

is\_org ( boolean , optional ): This constituent is an organization or company,

constituent\_contact\_type\_id ( integer , optional ): Constituent contact type ID,

constituent\_contact\_type\_name ( string , optional ): Constituent contact type,

prefix ( string , optional ): Prefix,

first\_name ( string , required ): First name,

middle\_name ( string , optional ): Middle name,

last\_name ( string , required ): Last name,

suffix ( string , optional ): Suffix,

spouse\_name ( string , optional ): Spouse/Partner,

org\_name ( string , optional ): Organization name,

job\_title ( string , optional ): Job title,

addressee ( string , optional ): Addressee/Label name,

salutation ( string , optional ): Salutation,

is\_deceased ( boolean , optional ): Deceased?,

deceased\_date ( string , optional ): Deceased date,

annual\_report\_name ( string , optional ): Annual report name,

birthday ( date , optional ): Birthday,

gender ( string , optional ): Gender,

maiden\_name ( string , optional ): Maiden name,

nick\_name ( string , optional ): Nickname,

spouse\_nick\_name ( string , optional ): Spouse nickname,

date\_added ( date , optional ): Date added,

alt\_salutation ( string , optional ): Alt salutation,

alt\_addressee ( string , optional ): Alt addressee,

honorary\_name ( string , optional ): Honorary name,

assistant\_name ( string , optional ): Assistant name,

marital\_status\_id ( integer , optional ): Marital status ID,

marital\_status\_name ( string , optional ): Marital status,

is\_anon ( boolean , optional ): Gives anonymously?,

class\_affiliations ( array , optional , ClassAffiliation ): Class Affiliation Objects,

relationships ( array , optional , ConstituentRelationship ): Relationship Objects,

email\_addresses ( array , required , EmailAddress ): Email Address Objects,

phone\_numbers ( array , optional , PhoneNumber ): Phone Number Objects,

street\_addresses ( array , optional , StreetAddress ): Street Address Objects,

web\_addresses ( array , optional , WebAddress ): Web Address Objects,

categories ( array , optional , CategoryAggregatedCreate ): Constituent Categories,

groups ( array , optional , GroupMembership ): Group Objects,

custom\_attrs ( array , optional , CustomAttr\_create ): Custom Attribute Objects

}

ClassAffiliation {

id ( integer , optional ): Class Affiliation ID,

class\_affiliation\_type\_id ( integer , optional ): Class Affiliation Type ID,

year ( integer , optional ): Year,

note ( string , optional ): Note

}

ConstituentRelationship {

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

EmailAddress {

address ( string , optional ): Email Address,

email\_address\_type\_id ( integer , optional ): Email Address Type ID,

email\_type\_name ( string , optional ): Email Address Type Name,

is\_preferred ( boolean , optional ): Make this the preferred email address,

not\_current ( boolean , optional ): No longer a current email address

}

PhoneNumber {

number ( string , optional ): Phone Number,

phone\_number\_type\_id ( integer , optional ): Phone Number Type Id,

phone\_type\_name ( string , optional ): Phone Number Type Name,

is\_preferred ( boolean , optional ): Make this the preferred phone number,

not\_current ( boolean , optional ): No longer a current phone number

}

StreetAddress {

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

WebAddress {

url ( string , optional ): Web Address,

web\_address\_type\_id ( integer , optional ): Web Address Type ID,

web\_address\_type\_name ( string , optional ): Web Address Type Name,

is\_preferred ( boolean , optional ): Make this the preferred email address

}

CategoryAggregatedCreate {

id ( integer , optional ): Category Id,

name ( string , required ): Name,

key ( string , optional ): Key,

keywords ( array , required , KeywordAggregatedUpdate ): Keyword Values

}

KeywordAggregatedUpdate {

id ( integer , required ): Keyword Id,

name ( string , required ): Name,

short\_code ( string , optional ): Short Code

}

GroupMembership {

group\_id ( integer , required ): Group Id,

group\_name ( string , optional ): Group Name,

date\_start ( date , optional ): Start Date,

date\_end ( date , optional ): End Date,

is\_current ( boolean , optional ): Current?

}

CustomAttr\_create {

id ( integer , optional ): Custom Field Id,

key ( string , optional ): Key,

value ( string , required ): Value

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder610.5493967666359834              
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

URI: https://api.littlegreenlight.com/api/v1/constituents

Body:

```
                  
{
  "is_org": false,
  "external_constituent_id": "999",
  "first_name": "Joe",
  "last_name": "Doe",
  "class_affiliations": [
    {
      "class_affiliation_type_id": "515",
      "year": "2021"
    }
  ],
  "relationships": [
    {
      "related_constituent_id": "959463",
      "name": "Friend"
    }
  ],
  "email_addresses": [
    {
      "address": "joed@example.com"
    }
  ],
  "categories": [
    {
      "key": "tags",
      "keywords": [
        {
          "name": "New Tag"
        }
      ]
    }
  ],
  "groups": [
    {
      "group_name": "Board Member"
    }
  ],
  "custom_attrs": [
    {
      "key": "background_info",
      "value": "Founding member"
    }
  ]
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 959599,
  "external_constituent_id": "999",
  "is_org": false,
  "constituent_contact_type_id": 1243,
  "constituent_contact_type_name": "Primary",
  "prefix": null,
  "first_name": "Joe",
  "middle_name": null,
  "last_name": "Doe",
  "suffix": null,
  "spouse_name": null,
  "org_name": null,
  "job_title": null,
  "addressee": "Joe Doe",
  "salutation": "Joe",
  "sort_name": "Doe, Joe",
  "constituent_interest_level_id": null,
  "constituent_interest_level_name": null,
  "constituent_rating_id": null,
  "constituent_rating_name": null,
  "is_deceased": false,
  "deceased_date": null,
  "annual_report_name": "Joe Doe",
  "birthday": null,
  "gender": null,
  "maiden_name": null,
  "nick_name": null,
  "spouse_nick_name": null,
  "date_added": "2025-06-03",
  "alt_salutation": "Joe",
  "alt_addressee": "Joe Doe",
  "honorary_name": "Joe Doe",
  "assistant_name": null,
  "marital_status_id": null,
  "marital_status_name": null,
  "is_anon": false,
  "created_at": "2025-06-03T17:08:33Z",
  "updated_at": "2025-06-03T17:08:33Z",
  "class_affiliations": [
    {
      "id": 236,
      "constituent_id": 959599,
      "class_affiliation_type_id": 515,
      "year": 2021,
      "note": null
    }
  ],
  "relationships": [
    {
      "id": 214580,
      "relationship_type_id": 50,
      "constituent_id": 959599,
      "related_constituent_id": 959463,
      "name": "Friend",
      "description": null,
      "auto_soft_credit": false,
      "also_acknowledge": false,
      "share_address": null,
      "share_phone": null
    }
  ],
  "street_addresses": [

  ],
  "phone_numbers": [

  ],
  "email_addresses": [
    {
      "id": 276661,
      "address": "joed@example.com",
      "email_address_type_id": 1,
      "email_type_name": "Home",
      "is_preferred": true,
      "not_current": false,
      "parent_id": null,
      "created_at": "2025-06-03T17:08:33Z",
      "updated_at": "2025-06-03T17:08:33Z"
    }
  ],
  "web_addresses": [

  ],
  "categories": [
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
    }
  ],
  "groups": [
    {
      "id": 595533,
      "constituent_id": 959599,
      "group_id": 3241,
      "group_name": "Board Member",
      "date_start": null,
      "date_end": null,
      "is_current": true,
      "created_at": "2025-06-03T17:08:33Z",
      "updated_at": "2025-06-03T17:08:33Z"
    }
  ],
  "memberships": [

  ],
  "custom_attrs": [
    {
      "id": 514928,
      "classification": "text",
      "name": "Background Info",
      "key": "background_info",
      "ordinal": 100,
      "value": "Founding member"
    }
  ]
}
                
```


* * *

GET /api/v1/constituents/{id} - Show Constituent details
--------------------------------------------------------

Show details for the constituent.


|Parameter Name|Description   |Type   |Required?|Parameter Type|
|--------------|--------------|-------|---------|--------------|
|id            |Constituent Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder640.2349461790306051              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480

Response:

```
                  
{
  "api_version": "1.0",
  "id": 959480,
  "external_constituent_id": "t00044",
  "is_org": false,
  "constituent_contact_type_id": 1243,
  "constituent_contact_type_name": "Primary",
  "prefix": "",
  "first_name": "Larry",
  "middle_name": "",
  "last_name": "Appleton",
  "suffix": "",
  "spouse_name": "",
  "org_name": "Perfect Strangers",
  "job_title": "",
  "addressee": "Larry Appleton and his cousin Balki Bartokomous",
  "salutation": "Larry",
  "sort_name": "Appleton, Larry",
  "constituent_interest_level_id": null,
  "constituent_interest_level_name": null,
  "constituent_rating_id": null,
  "constituent_rating_name": null,
  "is_deceased": false,
  "deceased_date": null,
  "annual_report_name": "Larry Appleton and his cousin Balki Bartokomous",
  "birthday": null,
  "gender": null,
  "maiden_name": "",
  "nick_name": "",
  "spouse_nick_name": "",
  "date_added": "2023-09-18",
  "alt_salutation": "Larry",
  "alt_addressee": "Larry Appleton and his cousin Balki Bartokomous",
  "honorary_name": "Larry Appleton and his cousin Balki Bartokomous",
  "assistant_name": "",
  "marital_status_id": null,
  "marital_status_name": null,
  "is_anon": false,
  "created_at": "2023-09-18T18:25:01Z",
  "updated_at": "2025-04-07T17:08:22Z",
  "class_affiliations": [
    {
      "id": 159,
      "constituent_id": 959480,
      "class_affiliation_type_id": 515,
      "year": 2002,
      "note": "U Chicago Alum"
    }
  ],
  "relationships": [
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
  ],
  "street_addresses": [
    {
      "id": 838379,
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
  ],
  "phone_numbers": [
    {
      "id": 479627,
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
  ],
  "email_addresses": [
    {
      "id": 276464,
      "address": "appleton@perfectstrangers.com",
      "email_address_type_id": 1,
      "email_type_name": "Home",
      "is_preferred": true,
      "not_current": false,
      "parent_id": null,
      "created_at": "2023-09-18T18:25:01Z",
      "updated_at": "2023-09-19T22:34:56Z"
    }
  ],
  "web_addresses": [
    {
      "id": 46,
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
      "url": "facebook.com/something",
      "web_address_type_id": 6,
      "web_address_type_name": "Facebook",
      "is_preferred": false,
      "parent_id": null,
      "created_at": "2023-09-19T22:34:56Z",
      "updated_at": "2023-09-19T22:34:56Z"
    }
  ],
  "categories": [
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
    }
  ],
  "groups": [
    {
      "id": 595476,
      "constituent_id": 959480,
      "group_id": 3241,
      "group_name": "Board Member",
      "date_start": null,
      "date_end": null,
      "is_current": true,
      "created_at": "2023-09-19T22:24:37Z",
      "updated_at": "2023-09-19T22:24:37Z"
    }
  ],
  "memberships": [
    {
      "id": 424,
      "constituent_id": 959480,
      "membership_level_id": 388,
      "membership_level_name": "Gold",
      "date_start": "2022-09-18",
      "finish_date": "2023-09-18",
      "note": null,
      "created_at": "2023-09-18T18:25:01Z",
      "updated_at": "2025-04-07T17:08:29Z"
    }
  ],
  "custom_attrs": [
    {
      "id": 514928,
      "classification": "text",
      "name": "Background Info",
      "key": "background_info",
      "ordinal": 100,
      "value": ""
    },
    {
      "id": 514936,
      "classification": "integer",
      "name": "Test Number",
      "key": "test_number",
      "ordinal": 100,
      "value": ""
    }
  ]
}
                
```


* * *

PATCH /api/v1/constituents/{id} - Update constituent
----------------------------------------------------

Update the Constituent along with related objects


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|id            |Constituent Id|integer   |true     |path          |
|body          |Update Objects|UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

external\_constituent\_id ( integer , optional ): External constituent ID,

is\_org ( boolean , optional ): This constituent is an organization or company,

constituent\_contact\_type\_id ( integer , optional ): Constituent contact type ID,

constituent\_contact\_type\_name ( string , optional ): Constituent contact type,

prefix ( string , optional ): Prefix,

first\_name ( string , required ): First name,

middle\_name ( string , optional ): Middle name,

last\_name ( string , required ): Last name,

suffix ( string , optional ): Suffix,

spouse\_name ( string , optional ): Spouse/Partner,

org\_name ( string , optional ): Organization name,

job\_title ( string , optional ): Job title,

addressee ( string , optional ): Addressee/Label name,

salutation ( string , optional ): Salutation,

is\_deceased ( boolean , optional ): Deceased?,

deceased\_date ( string , optional ): Deceased date,

annual\_report\_name ( string , optional ): Annual report name,

birthday ( date , optional ): Birthday,

gender ( string , optional ): Gender,

maiden\_name ( string , optional ): Maiden name,

nick\_name ( string , optional ): Nickname,

spouse\_nick\_name ( string , optional ): Spouse nickname,

date\_added ( date , optional ): Date added,

alt\_salutation ( string , optional ): Alt salutation,

alt\_addressee ( string , optional ): Alt addressee,

honorary\_name ( string , optional ): Honorary name,

assistant\_name ( string , optional ): Assistant name,

marital\_status\_id ( integer , optional ): Marital status ID,

marital\_status\_name ( string , optional ): Marital status,

is\_anon ( boolean , optional ): Gives anonymously?,

remove\_previous\_class\_affiliations ( boolean , optional ): Remove previous class affiliations,

class\_affiliations ( array , optional , ClassAffiliationUpdate ): Class Affiliation Objects,

remove\_previous\_relationships ( boolean , optional ): Remove previous relationships,

relationships ( array , optional , ConstituentRelationshipUpdate ): Relationship Objects,

remove\_previous\_email\_addresses ( boolean , optional ): Remove previous email addresses,

email\_addresses ( array , required , EmailAddress ): Email Address Objects,

remove\_previous\_phone\_numbers ( boolean , optional ): Remove previous phone numbers,

phone\_numbers ( array , optional , PhoneNumber ): Phone Number Objects,

remove\_previous\_street\_addresses ( boolean , optional ): Remove previous street addresses,

street\_addresses ( array , optional , StreetAddress ): Street Address Objects,

remove\_previous\_web\_addresses ( boolean , optional ): Remove previous web addresses,

web\_addresses ( array , optional , WebAddress ): Web Address Objects,

categories ( array , optional , CategoryAggregatedUpdate ): Constituent Categories,

remove\_previous\_groups ( boolean , optional ): Remove previous groups,

groups ( array , optional , GroupMembershipUpdate ): Group Objects,

custom\_attrs ( array , optional , CustomAttr\_create ): Custom Attribute Objects

}

ClassAffiliationUpdate {

id ( integer , optional ): Class Affiliation ID,

class\_affiliation\_type\_id ( integer , optional ): Class Affiliation Type ID,

year ( integer , optional ): Year,

note ( string , optional ): Note

}

ConstituentRelationshipUpdate {

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

EmailAddress {

address ( string , optional ): Email Address,

email\_address\_type\_id ( integer , optional ): Email Address Type ID,

email\_type\_name ( string , optional ): Email Address Type Name,

is\_preferred ( boolean , optional ): Make this the preferred email address,

not\_current ( boolean , optional ): No longer a current email address

}

PhoneNumber {

number ( string , optional ): Phone Number,

phone\_number\_type\_id ( integer , optional ): Phone Number Type Id,

phone\_type\_name ( string , optional ): Phone Number Type Name,

is\_preferred ( boolean , optional ): Make this the preferred phone number,

not\_current ( boolean , optional ): No longer a current phone number

}

StreetAddress {

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

WebAddress {

url ( string , optional ): Web Address,

web\_address\_type\_id ( integer , optional ): Web Address Type ID,

web\_address\_type\_name ( string , optional ): Web Address Type Name,

is\_preferred ( boolean , optional ): Make this the preferred email address

}

CategoryAggregatedUpdate {

id ( integer , optional ): Category Id,

name ( string , required ): Name,

key ( string , optional ): Key,

remove\_previous\_keywords ( boolean , optional ): Remove previous category keywords,

keywords ( array , required , KeywordAggregatedUpdate ): Keyword Values

}

KeywordAggregatedUpdate {

id ( integer , required ): Keyword Id,

name ( string , required ): Name,

short\_code ( string , optional ): Short Code

}

GroupMembershipUpdate {

id ( integer , optional ): ID,

group\_id ( integer , required ): Group Id,

group\_name ( string , optional ): Group Name,

date\_start ( date , optional ): Start Date,

date\_end ( date , optional ): End Date,

is\_current ( boolean , optional ): Current?

}

CustomAttr\_create {

id ( integer , optional ): Custom Field Id,

key ( string , optional ): Key,

value ( string , required ): Value

}



* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder660.36595989811231733              
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

URI: https://api.littlegreenlight.com/api/v1/constituents/959599

Body:

```
                  
{
  "is_org": false,
  "first_name": "Joe",
  "last_name": "Doe",
  "middle_name": "Moe",
  "class_affiliations": [
    {
      "class_affiliation_type_id": "515",
      "year": "2022"
    }
  ],
  "relationships": [
    {
      "related_constituent_id": "959463",
      "name": "Family"
    }
  ],
  "street_addresses": [
    {
      "street": "123 SE Tree",
      "city": "Seattle",
      "state": "WA",
      "postal_code": "98101"
    }
  ]
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 959599,
  "external_constituent_id": "999",
  "is_org": false,
  "constituent_contact_type_id": 1243,
  "constituent_contact_type_name": "Primary",
  "prefix": null,
  "first_name": "Joe",
  "middle_name": "Moe",
  "last_name": "Doe",
  "suffix": null,
  "spouse_name": null,
  "org_name": null,
  "job_title": null,
  "addressee": "Joe Doe",
  "salutation": "Joe",
  "sort_name": "Doe, Joe",
  "constituent_interest_level_id": null,
  "constituent_interest_level_name": null,
  "constituent_rating_id": null,
  "constituent_rating_name": null,
  "is_deceased": false,
  "deceased_date": null,
  "annual_report_name": "Joe Doe",
  "birthday": null,
  "gender": null,
  "maiden_name": null,
  "nick_name": null,
  "spouse_nick_name": null,
  "date_added": "2025-06-03",
  "alt_salutation": "Joe",
  "alt_addressee": "Joe Doe",
  "honorary_name": "Joe Doe",
  "assistant_name": null,
  "marital_status_id": null,
  "marital_status_name": null,
  "is_anon": false,
  "created_at": "2025-06-03T17:08:33Z",
  "updated_at": "2025-06-03T17:08:34Z",
  "class_affiliations": [
    {
      "id": 236,
      "constituent_id": 959599,
      "class_affiliation_type_id": 515,
      "year": 2021,
      "note": null
    },
    {
      "id": 237,
      "constituent_id": 959599,
      "class_affiliation_type_id": 515,
      "year": 2022,
      "note": null
    }
  ],
  "relationships": [
    {
      "id": 214580,
      "relationship_type_id": 50,
      "constituent_id": 959599,
      "related_constituent_id": 959463,
      "name": "Friend",
      "description": null,
      "auto_soft_credit": false,
      "also_acknowledge": false,
      "share_address": null,
      "share_phone": null
    },
    {
      "id": 214581,
      "relationship_type_id": 51,
      "constituent_id": 959599,
      "related_constituent_id": 959463,
      "name": "Family",
      "description": null,
      "auto_soft_credit": false,
      "also_acknowledge": false,
      "share_address": null,
      "share_phone": null
    }
  ],
  "street_addresses": [
    {
      "id": 838576,
      "street": "123 SE Tree",
      "city": "Seattle",
      "state": "WA",
      "country": null,
      "postal_code": "98101",
      "county": null,
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
      "zip5": "98101",
      "verified": false,
      "verified_on": null,
      "created_at": "2025-06-03T17:08:34Z",
      "updated_at": "2025-06-03T17:08:34Z"
    }
  ],
  "phone_numbers": [

  ],
  "email_addresses": [
    {
      "id": 276661,
      "address": "joed@example.com",
      "email_address_type_id": 1,
      "email_type_name": "Home",
      "is_preferred": true,
      "not_current": false,
      "parent_id": null,
      "created_at": "2025-06-03T17:08:33Z",
      "updated_at": "2025-06-03T17:08:33Z"
    }
  ],
  "web_addresses": [

  ],
  "categories": [
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
    }
  ],
  "groups": [
    {
      "id": 595533,
      "constituent_id": 959599,
      "group_id": 3241,
      "group_name": "Board Member",
      "date_start": null,
      "date_end": null,
      "is_current": true,
      "created_at": "2025-06-03T17:08:33Z",
      "updated_at": "2025-06-03T17:08:33Z"
    }
  ],
  "memberships": [

  ],
  "custom_attrs": [
    {
      "id": 514928,
      "classification": "text",
      "name": "Background Info",
      "key": "background_info",
      "ordinal": 100,
      "value": "Founding member"
    }
  ]
}
                
```


* * *

DELETE /api/v1/constituents/{id} - Delete constituent
-----------------------------------------------------

Delete the Constituent along with related objects.


|Parameter Name|Description   |Type   |Required?|Parameter Type|
|--------------|--------------|-------|---------|--------------|
|id            |Constituent Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959599

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

