Invitations Management
----------------------

POST /api/v1/constituents/{constituent\_id}/invitations - Create new Invitation for Constituent
-----------------------------------------------------------------------------------------------

Add invitation to constituent.


|Parameter Name|Description   |Type            |Required?|Parameter Type|
|--------------|--------------|----------------|---------|--------------|
|constituent_id|Constituent Id|integer         |true     |path          |
|body          |Create Objects|CreateBody_Const|true     |body          |


### CreateBody\_Const

CreateBody\_Const {

event\_id ( integer , required ): Event Id,

parent\_invitation\_id ( integer , optional ): Parent Invitation Id (for additional guests),

notes ( string , optional ): Notes,

rsvp ( integer , optional ): RSVP (1-Yes, 2-No, 3-Maybe, 4-Unknown),

attended ( integer , optional ): Attended,

assigned\_to ( integer , optional ): Assigned to,

attendee\_names ( string , optional ): Attendees Names,

guest\_first\_name ( string , optional ): Additional Guest First Name,

guest\_last\_name ( string , optional ): Additional Guest Last Name,

is\_a\_guest ( boolean , optional ): Creating an additional guest record,

attendances ( array , optional , Attendance\_create ): Multiple attendances,

custom\_fields ( array , optional , CustomFieldAggregatedUpdate ): Invitation custom fields (Categories),

custom\_attrs ( array , optional , CustomAttr\_create ): Invitation custom attributes

}

Attendance\_create {

date ( date , required ): Attendance date,

notes ( string , optional ): Attendance notes

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
  * Response:                 urltomarkdowncodeblockplaceholder1590.04459600693736543              
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

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/invitations

Body:

Response:

```
                  
{
  "api_version": "1.0",
  "id": 168432,
  "constituent_id": 959480,
  "guest_name": "Larry Appleton",
  "is_a_guest": false,
  "parent_invitation_id": 0,
  "parent_invitation_guest_name": null,
  "event_id": 1069,
  "name": "Event: Winter 2020 Fundraising Gala",
  "notes": null,
  "rsvp": 0,
  "attended": 0,
  "raised": 0.0,
  "status": "unknown",
  "donated": false,
  "assigned_to": null,
  "additional_guests": 0,
  "attendees": 0,
  "attendee_names": null,
  "attend_count": 0,
  "attendances": [

  ],
  "custom_fields": [

  ],
  "custom_attrs": [

  ],
  "created_at": "2025-06-03T17:08:45Z",
  "updated_at": "2025-06-03T17:08:45Z"
}
                
```


* * *

GET /api/v1/constituents/{constituent\_id}/invitations - Fetch Invitations for Constituent
------------------------------------------------------------------------------------------

Lists all the invitations for a constituent.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|constituent_id|Constituent Id                          |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1610.4752456080418568              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/constituents/959480/invitations

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 1,
  "total_items": 1,
  "limit": 5,
  "offset": 0,
  "item_type": "invitation",
  "items": [
    {
      "id": 168432,
      "constituent_id": 959480,
      "guest_name": "Larry Appleton",
      "is_a_guest": false,
      "parent_invitation_id": 0,
      "parent_invitation_guest_name": null,
      "event_id": 1069,
      "name": "Event: Winter 2020 Fundraising Gala",
      "notes": null,
      "rsvp": 0,
      "attended": 0,
      "raised": 0.0,
      "status": "unknown",
      "donated": false,
      "assigned_to": null,
      "additional_guests": 0,
      "attendees": 0,
      "attendee_names": null,
      "attend_count": 0,
      "attendances": [

      ],
      "custom_fields": [

      ],
      "custom_attrs": [

      ],
      "created_at": "2025-06-03T17:08:45Z",
      "updated_at": "2025-06-03T17:08:45Z"
    }
  ]
}
                
```


* * *

GET /api/v1/events/{event\_id}/invitations - Fetch Invitations for Event
------------------------------------------------------------------------

Lists all the invitations for an event.


|Parameter Name|Description                             |Type   |Required?|Parameter Type|
|--------------|----------------------------------------|-------|---------|--------------|
|event_id      |Event Id                                |integer|true     |path          |
|limit         |Number of entries to return. Default: 25|integer|         |query         |
|offset        |Start at given entry. Default: 0        |integer|         |query         |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1630.9908691290368679              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/events/1069/invitations

Query:

Response:

```
                  
{
  "api_version": "1.0",
  "items_count": 5,
  "total_items": 83,
  "limit": 5,
  "offset": 0,
  "next_item": 5,
  "next_link": "https://api.littlegreenlight.com/api/v1/events/1069/invitations?limit=5&offset=5",
  "item_type": "invitation",
  "items": [
    {
      "id": 168229,
      "constituent_id": 959486,
      "guest_name": "Archer's",
      "is_a_guest": false,
      "parent_invitation_id": 0,
      "parent_invitation_guest_name": null,
      "event_id": 1069,
      "name": "Event: Winter 2020 Fundraising Gala",
      "notes": null,
      "rsvp": 0,
      "attended": 0,
      "raised": 0.0,
      "status": "unknown",
      "donated": false,
      "assigned_to": null,
      "additional_guests": 0,
      "attendees": 0,
      "attendee_names": null,
      "attend_count": 0,
      "attendances": [

      ],
      "custom_fields": [

      ],
      "custom_attrs": [

      ],
      "created_at": "2023-10-31T17:41:28Z",
      "updated_at": "2023-10-31T17:41:28Z"
    },
    {
      "id": 168230,
      "constituent_id": 959440,
      "guest_name": "Avengers Mansion Headquarters of the Avengers",
      "is_a_guest": false,
      "parent_invitation_id": 0,
      "parent_invitation_guest_name": null,
      "event_id": 1069,
      "name": "Event: Winter 2020 Fundraising Gala",
      "notes": null,
      "rsvp": 0,
      "attended": 0,
      "raised": 0.0,
      "status": "unknown",
      "donated": false,
      "assigned_to": null,
      "additional_guests": 0,
      "attendees": 0,
      "attendee_names": null,
      "attend_count": 0,
      "attendances": [

      ],
      "custom_fields": [

      ],
      "custom_attrs": [

      ],
      "created_at": "2023-10-31T17:41:28Z",
      "updated_at": "2023-10-31T17:41:28Z"
    },
    {
      "id": 168231,
      "constituent_id": 959453,
      "guest_name": "Ray Barone",
      "is_a_guest": false,
      "parent_invitation_id": 0,
      "parent_invitation_guest_name": null,
      "event_id": 1069,
      "name": "Event: Winter 2020 Fundraising Gala",
      "notes": null,
      "rsvp": 0,
      "attended": 0,
      "raised": 0.0,
      "status": "unknown",
      "donated": false,
      "assigned_to": null,
      "additional_guests": 0,
      "attendees": 0,
      "attendee_names": null,
      "attend_count": 0,
      "attendances": [

      ],
      "custom_fields": [

      ],
      "custom_attrs": [

      ],
      "created_at": "2023-10-31T17:41:28Z",
      "updated_at": "2023-10-31T17:41:28Z"
    },
    {
      "id": 168232,
      "constituent_id": 959465,
      "guest_name": "Joseph Baxter",
      "is_a_guest": false,
      "parent_invitation_id": 0,
      "parent_invitation_guest_name": null,
      "event_id": 1069,
      "name": "Event: Winter 2020 Fundraising Gala",
      "notes": null,
      "rsvp": 0,
      "attended": 0,
      "raised": 0.0,
      "status": "unknown",
      "donated": false,
      "assigned_to": null,
      "additional_guests": 0,
      "attendees": 0,
      "attendee_names": null,
      "attend_count": 0,
      "attendances": [

      ],
      "custom_fields": [

      ],
      "custom_attrs": [

      ],
      "created_at": "2023-10-31T17:41:28Z",
      "updated_at": "2023-10-31T17:41:28Z"
    },
    {
      "id": 168233,
      "constituent_id": 959474,
      "guest_name": "Frank Black",
      "is_a_guest": false,
      "parent_invitation_id": 0,
      "parent_invitation_guest_name": null,
      "event_id": 1069,
      "name": "Event: Winter 2020 Fundraising Gala",
      "notes": null,
      "rsvp": 0,
      "attended": 0,
      "raised": 0.0,
      "status": "unknown",
      "donated": false,
      "assigned_to": null,
      "additional_guests": 0,
      "attendees": 0,
      "attendee_names": null,
      "attend_count": 0,
      "attendances": [

      ],
      "custom_fields": [

      ],
      "custom_attrs": [

      ],
      "created_at": "2023-10-31T17:41:28Z",
      "updated_at": "2023-10-31T17:41:28Z"
    }
  ]
}
                
```


* * *

POST /api/v1/events/{event\_id}/invitations - Create new Invitation
-------------------------------------------------------------------

Add invitation.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|event_id      |Event Id      |integer   |true     |path          |
|body          |Create Objects|CreateBody|true     |body          |


### CreateBody

CreateBody {

constituent\_id ( integer , required ): Constituent Id,

parent\_invitation\_id ( integer , optional ): Parent Invitation Id (for additional guests),

notes ( string , optional ): Notes,

rsvp ( integer , optional ): RSVP (1-Yes, 2-No, 3-Maybe, 4-Unknown),

attended ( integer , optional ): Attended,

assigned\_to ( integer , optional ): Assigned to,

attendee\_names ( string , optional ): Attendees Names,

guest\_first\_name ( string , optional ): Additional Guest First Name,

guest\_last\_name ( string , optional ): Additional Guest Last Name,

is\_a\_guest ( boolean , optional ): Creating an additional guest record,

attendances ( array , optional , Attendance\_create ): Multiple attendances,

custom\_fields ( array , optional , CustomFieldAggregatedUpdate ): Invitation custom fields (Categories),

custom\_attrs ( array , optional , CustomAttr\_create ): Invitation custom attributes

}

Attendance\_create {

date ( date , required ): Attendance date,

notes ( string , optional ): Attendance notes

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
  * Response:                 urltomarkdowncodeblockplaceholder1650.5803560082575285              
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


### Example - Create invitation for an event:

URI: https://api.littlegreenlight.com/api/v1/events/1070/invitations

Body:

```
                  
{
  "constituent_id": "959480",
  "notes": "Event note"
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 168433,
  "constituent_id": 959480,
  "guest_name": "Larry Appleton",
  "is_a_guest": false,
  "parent_invitation_id": 0,
  "parent_invitation_guest_name": null,
  "event_id": 1070,
  "name": "Event: Board weekend",
  "notes": "Event note",
  "rsvp": 0,
  "attended": 0,
  "raised": 0.0,
  "status": "unknown",
  "donated": false,
  "assigned_to": null,
  "additional_guests": 0,
  "attendees": 0,
  "attendee_names": null,
  "attend_count": 0,
  "attendances": [

  ],
  "custom_fields": [

  ],
  "custom_attrs": [

  ],
  "created_at": "2025-06-03T17:08:46Z",
  "updated_at": "2025-06-03T17:08:46Z"
}
                
```


### Example - Create an additional guest for an invitation:

URI: https://api.littlegreenlight.com/api/v1/events/1069/invitations

Body:

```
                  
{
  "parent_invitation_id": "168432",
  "guest_first_name": "Max",
  "guest_last_name": "Million",
  "is_a_guest": true
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 168434,
  "constituent_id": null,
  "guest_name": "Max Million",
  "is_a_guest": true,
  "parent_invitation_id": 168432,
  "parent_invitation_guest_name": "Larry Appleton",
  "event_id": 1069,
  "name": "Event: Winter 2020 Fundraising Gala",
  "notes": null,
  "rsvp": 0,
  "attended": 0,
  "raised": 0.0,
  "status": "unknown",
  "donated": false,
  "assigned_to": null,
  "additional_guests": 0,
  "attendees": 0,
  "attendee_names": null,
  "attend_count": 0,
  "attendances": [

  ],
  "custom_fields": [

  ],
  "custom_attrs": [

  ],
  "created_at": "2025-06-03T17:08:46Z",
  "updated_at": "2025-06-03T17:08:46Z"
}
                
```


* * *

GET /api/v1/invitations/{id} - Show Invitation details
------------------------------------------------------

Show details for the invitation.


|Parameter Name|Description  |Type   |Required?|Parameter Type|
|--------------|-------------|-------|---------|--------------|
|id            |Invitation Id|integer|true     |path          |




* Code: 200
  * Message: Ok
  * Response:                 urltomarkdowncodeblockplaceholder1700.4226527154224009              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


### Example:

URI: https://api.littlegreenlight.com/api/v1/invitations/168432

Response:

```
                  
{
  "api_version": "1.0",
  "id": 168432,
  "constituent_id": 959480,
  "guest_name": "Larry Appleton",
  "is_a_guest": false,
  "parent_invitation_id": 0,
  "parent_invitation_guest_name": null,
  "event_id": 1069,
  "name": "Event: Winter 2020 Fundraising Gala",
  "notes": null,
  "rsvp": 0,
  "attended": 0,
  "raised": 0.0,
  "status": "unknown",
  "donated": false,
  "assigned_to": null,
  "additional_guests": 1,
  "attendees": 0,
  "attendee_names": null,
  "attend_count": 0,
  "attendances": [

  ],
  "custom_fields": [

  ],
  "custom_attrs": [

  ],
  "created_at": "2025-06-03T17:08:45Z",
  "updated_at": "2025-06-03T17:08:45Z"
}
                
```


* * *

PATCH /api/v1/invitations/{id} - Update Invitation
--------------------------------------------------

Update the invitation.


|Parameter Name|Description   |Type      |Required?|Parameter Type|
|--------------|--------------|----------|---------|--------------|
|id            |Invitation Id |integer   |true     |path          |
|body          |Update Objects|UpdateBody|true     |body          |


### UpdateBody

UpdateBody {

constituent\_id ( integer , required ): Constituent Id,

parent\_invitation\_id ( integer , optional ): Parent Invitation Id (for additional guests),

notes ( string , optional ): Notes,

rsvp ( integer , optional ): RSVP (1-Yes, 2-No, 3-Maybe, 4-Unknown),

attended ( integer , optional ): Attended,

assigned\_to ( integer , optional ): Assigned to,

attendee\_names ( string , optional ): Attendees Names,

guest\_first\_name ( string , optional ): Additional Guest First Name,

guest\_last\_name ( string , optional ): Additional Guest Last Name,

is\_a\_guest ( boolean , optional ): Creating an additional guest record,

attendances ( array , optional , Attendance\_create ): Multiple attendances,

custom\_fields ( array , optional , CustomFieldAggregatedUpdate ): Invitation custom fields (Categories),

custom\_attrs ( array , optional , CustomAttr\_create ): Invitation custom attributes

}

Attendance\_create {

date ( date , required ): Attendance date,

notes ( string , optional ): Attendance notes

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
  * Response:                 urltomarkdowncodeblockplaceholder1720.8488213430308922              
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

URI: https://api.littlegreenlight.com/api/v1/invitations/168433

Body:

```
                  
{
  "rsvp": "2",
  "attendances": [
    {
      "date": "2023-07-01",
      "notes": "attended"
    },
    {
      "date": "2023-08-01",
      "notes": "attended"
    }
  ]
}
                
```


Response:

```
                  
{
  "api_version": "1.0",
  "id": 168433,
  "constituent_id": 959480,
  "guest_name": "Larry Appleton",
  "is_a_guest": false,
  "parent_invitation_id": 0,
  "parent_invitation_guest_name": null,
  "event_id": 1070,
  "name": "Event: Board weekend",
  "notes": "Event note",
  "rsvp": 2,
  "attended": 1,
  "raised": 0.0,
  "status": "attended",
  "donated": false,
  "assigned_to": null,
  "additional_guests": 0,
  "attendees": 1,
  "attendee_names": null,
  "attend_count": 0,
  "attendances": [
    {
      "id": 129,
      "date": "2023-07-01",
      "notes": "attended"
    },
    {
      "id": 130,
      "date": "2023-08-01",
      "notes": "attended"
    }
  ],
  "custom_fields": [

  ],
  "custom_attrs": [

  ],
  "created_at": "2025-06-03T17:08:46Z",
  "updated_at": "2025-06-03T17:08:47Z"
}
                
```


* * *

DELETE /api/v1/invitations/{id} - Delete Invitation
---------------------------------------------------

Delete the invitation.


|Parameter Name|Description  |Type   |Required?|Parameter Type|
|--------------|-------------|-------|---------|--------------|
|id            |Invitation Id|integer|true     |path          |



|Code|Message     |Response|
|----|------------|--------|
|200 |Ok          |        |
|401 |Unauthorized|        |
|403 |Forbidden   |        |


### Example:

URI: https://api.littlegreenlight.com/api/v1/invitations/168432

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


### Example:

URI: https://api.littlegreenlight.com/api/v1/invitations/168433

Response:

```
                  
{
  "api_version": "1.0",
  "result": "success"
}
                
```


* * *

