Type Management
---------------

GET /api/v1/types - Fetch Types for Account
-------------------------------------------

Lists all the types for an account.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder2600.004515512994218707              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/types

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 10,
  "total_items": 10,
  "limit": 25,
  "offset": 0,
  "item_type": "type",
  "items": [
    {
      "name": "Contact Report Types",
      "key": "contact_report_types",
      "values": [
        {
          "id": 2183,
          "name": "Call",
          "display_name": "Call",
          "code": "call",
          "ordinal": 0
        },
        {
          "id": 2184,
          "name": "Email",
          "display_name": "Email",
          "code": "email",
          "ordinal": 1
        },
        {
          "id": 2185,
          "name": "Meeting",
          "display_name": "Meeting",
          "code": "meeting",
          "ordinal": 2
        },
        {
          "id": 2186,
          "name": "Mailing",
          "display_name": "Mailing",
          "code": "letter",
          "ordinal": 3
        },
        {
          "id": 2187,
          "name": "Proposal",
          "display_name": "Proposal",
          "code": "proposal",
          "ordinal": 4
        },
        {
          "id": 2188,
          "name": "Other",
          "display_name": "Other",
          "code": "other",
          "ordinal": 5
        }
      ]
    },
    {
      "name": "Email Address Types",
      "key": "email_address_types",
      "values": [
        {
          "id": 1,
          "name": "Home",
          "display_name": "Home",
          "code": "home",
          "ordinal": 100
        },
        {
          "id": 2,
          "name": "Work",
          "display_name": "Work",
          "code": "work",
          "ordinal": 100
        },
        {
          "id": 3,
          "name": "Other",
          "display_name": "Other",
          "code": "other",
          "ordinal": 100
        },
        {
          "id": 4,
          "name": "Assistant",
          "display_name": "Assistant",
          "code": "assistant",
          "ordinal": 101
        }
      ]
    },
    {
      "name": "Mailing Types",
      "key": "mailing_types",
      "values": [
        {
          "id": 1907,
          "name": "Acknowledgment",
          "display_name": "Acknowledgment",
          "code": "acknowledgment",
          "ordinal": 0
        },
        {
          "id": 1908,
          "name": "Reminder",
          "display_name": "Reminder",
          "code": "reminder",
          "ordinal": 1
        },
        {
          "id": 1909,
          "name": "Appeal",
          "display_name": "Appeal",
          "code": "appeal",
          "ordinal": 2
        },
        {
          "id": 1910,
          "name": "Newsletter",
          "display_name": "Newsletter",
          "code": "newsletter",
          "ordinal": 3
        },
        {
          "id": 1911,
          "name": "Other",
          "display_name": "Other",
          "code": "other",
          "ordinal": 4
        },
        {
          "id": 1912,
          "name": "Invitation",
          "display_name": "Invitation",
          "code": "invitation",
          "ordinal": 5
        },
        {
          "id": 1913,
          "name": "Honorary",
          "display_name": "Honorary",
          "code": "honorary",
          "ordinal": 6
        },
        {
          "id": 1914,
          "name": "Memorial",
          "display_name": "Memorial",
          "code": "memorial",
          "ordinal": 7
        },
        {
          "id": 1915,
          "name": "Annual Statement",
          "display_name": "Annual Statement",
          "code": "annual_statement",
          "ordinal": 8
        }
      ]
    },
    {
      "name": "Street Address Types",
      "key": "street_address_types",
      "values": [
        {
          "id": 1,
          "name": "Home",
          "display_name": "Home",
          "code": "home",
          "ordinal": 100
        },
        {
          "id": 2,
          "name": "Work",
          "display_name": "Work",
          "code": "work",
          "ordinal": 100
        },
        {
          "id": 3,
          "name": "Other",
          "display_name": "Other",
          "code": "other",
          "ordinal": 100
        },
        {
          "id": 4,
          "name": "School",
          "display_name": "School",
          "code": "school",
          "ordinal": 100
        }
      ]
    },
    {
      "name": "Phone Number Types",
      "key": "phone_number_types",
      "values": [
        {
          "id": 1,
          "name": "Home",
          "display_name": "Home",
          "code": "home",
          "ordinal": 100
        },
        {
          "id": 2,
          "name": "Work",
          "display_name": "Work",
          "code": "work",
          "ordinal": 100
        },
        {
          "id": 3,
          "name": "Mobile",
          "display_name": "Mobile",
          "code": "mobile",
          "ordinal": 100
        },
        {
          "id": 4,
          "name": "Other",
          "display_name": "Other",
          "code": "other",
          "ordinal": 100
        },
        {
          "id": 6,
          "name": "Skype",
          "display_name": "Skype",
          "code": "skype",
          "ordinal": 100
        },
        {
          "id": 5,
          "name": "Fax",
          "display_name": "Fax",
          "code": "fax",
          "ordinal": 101
        },
        {
          "id": 7,
          "name": "Assistant",
          "display_name": "Assistant",
          "code": "assistant",
          "ordinal": 101
        },
        {
          "id": 8,
          "name": "Pager",
          "display_name": "Pager",
          "code": "pager",
          "ordinal": 102
        }
      ]
    },
    {
      "name": "Web Address Types",
      "key": "web_address_types",
      "values": [
        {
          "id": 5,
          "name": "Website",
          "display_name": "Website",
          "code": "website",
          "ordinal": 0
        },
        {
          "id": 6,
          "name": "Facebook",
          "display_name": "Facebook",
          "code": "facebook",
          "ordinal": 1
        },
        {
          "id": 7,
          "name": "Twitter",
          "display_name": "Twitter",
          "code": "twitter",
          "ordinal": 2
        },
        {
          "id": 8,
          "name": "LinkedIn",
          "display_name": "LinkedIn",
          "code": "linkedin",
          "ordinal": 3
        }
      ]
    },
    {
      "name": "Volunteering Categories",
      "key": "volunteering_categories",
      "values": [
        {
          "id": 446,
          "name": "General",
          "display_name": "General",
          "code": "general",
          "ordinal": 0
        },
        {
          "id": 447,
          "name": "Donor Management",
          "display_name": "Donor Management",
          "code": "donor_management",
          "ordinal": 100
        }
      ]
    },
    {
      "name": "Appeal Types",
      "key": "appeal_types",
      "values": [
        {
          "id": 15,
          "name": "appeal type alpha",
          "display_name": "appeal type alpha",
          "code": null,
          "ordinal": 100
        },
        {
          "id": 16,
          "name": "appeal type zulu",
          "display_name": "appeal type zulu",
          "code": null,
          "ordinal": 100
        }
      ]
    },
    {
      "name": "Event Types",
      "key": "event_types",
      "values": [

      ]
    },
    {
      "name": "Note Types",
      "key": "note_types",
      "values": [
        {
          "id": 373,
          "name": "General",
          "display_name": null,
          "code": "general",
          "ordinal": 0
        },
        {
          "id": 374,
          "name": "Update",
          "display_name": null,
          "code": "update",
          "ordinal": 100
        }
      ]
    }
  ]
}
                
```


* * *

GET /api/v1/types/{type} - Fetch Values for Type
------------------------------------------------

Lists all the values for a type.



* Parameter Name: type
  * Description: Type: [ contact_report_types | email_address_types | mailing_types | street_address_types | phone_number_types | web_address_types | volunteering_categories | appeal_types | event_types | note_types ]
  * Type: string
  * Required?: true
  * Parameter Type: path
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
  * Response:                 urltomarkdowncodeblockplaceholder2620.9212068329443639              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/types/email\_address\_types

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 4,
  "total_items": 4,
  "limit": 25,
  "offset": 0,
  "item_type": "email_address_type",
  "items": [
    {
      "id": 1,
      "name": "Home",
      "display_name": "Home",
      "code": "home",
      "ordinal": 100
    },
    {
      "id": 2,
      "name": "Work",
      "display_name": "Work",
      "code": "work",
      "ordinal": 100
    },
    {
      "id": 3,
      "name": "Other",
      "display_name": "Other",
      "code": "other",
      "ordinal": 100
    },
    {
      "id": 4,
      "name": "Assistant",
      "display_name": "Assistant",
      "code": "assistant",
      "ordinal": 101
    }
  ]
}
                
```


* * *

