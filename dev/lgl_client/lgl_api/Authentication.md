Authentication
--------------

Generate an API key
-------------------

Administrators can generate API keys in their Little Green Light account by going to Settings > Integration settings, and then clicking on the LGL API link. If that link is not visible, please request access by writing to support@littlegreenlight.com, with details about how you plan to use the API and which LGL account you will use for development.

Using your API key
------------------

There are three ways you can pass your API key to the LGL API server. You will need to check with your HTTP or Client library for how to use each method. Examples use the 'curl' command line application.

### HTTP Basic Authentication

HTTP Basic Authentication allows you to pass a username and password. In this case, set the username to the API key and leave the password blank.

Example:

curl -u \[api\_key\]: "https://api.littlegreenlight.com/api/v1/constituents"

### Use the "access\_token" parameter

You can provide the API key in each call by using the "access\_token" parameter.

Example:

curl "https://api.littlegreenlight.com/api/v1/constituents?access\_token=\[api\_key\]"

### Use the "Bearer" HTTP authorization header

Example:

curl -H "Authorization: Bearer \[api\_key\]" "https://api.littlegreenlight.com/api/v1/constituents"

