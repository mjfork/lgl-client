Custom Attributes Management
----------------------------

GET /api/v1/attributes - Fetch Custom Attributes
------------------------------------------------

Lists custom attributes..



* Parameter Name: item_type
  * Description: Attributes for type (default: Constituent). Available: Constituent, Invitation
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
  * Response:                 urltomarkdowncodeblockplaceholder980.7675883373687762              
* Code: 401
  * Message: Unauthorized
  * Response: 
* Code: 403
  * Message: Forbidden
  * Response: 


* * *

