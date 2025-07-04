# lgl_openapi_3_0_client.InvitationsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lgl_api_v1_invitations_create**](InvitationsApi.md#lgl_api_v1_invitations_create) | **POST** /v1/events/{event_id}/invitations.json | Create new Invitation
[**lgl_api_v1_invitations_destroy**](InvitationsApi.md#lgl_api_v1_invitations_destroy) | **DELETE** /v1/invitations/{id}.json | Delete Invitation
[**lgl_api_v1_invitations_update**](InvitationsApi.md#lgl_api_v1_invitations_update) | **PATCH** /v1/invitations/{id}.json | Update Invitation
[**v1_constituent_invitations**](InvitationsApi.md#v1_constituent_invitations) | **GET** /v1/constituents/{constituent_id}/invitations.json | Fetch Invitations for Constituent
[**v1_create_invitation_v1_constituent_invitations**](InvitationsApi.md#v1_create_invitation_v1_constituent_invitations) | **POST** /v1/constituents/{constituent_id}/invitations.json | Create new Invitation for Constituent
[**v1_event_invitations**](InvitationsApi.md#v1_event_invitations) | **GET** /v1/events/{event_id}/invitations.json | Fetch Invitations for Event
[**v1_invitation**](InvitationsApi.md#v1_invitation) | **GET** /v1/invitations/{id}.json | Show Invitation details


# **lgl_api_v1_invitations_create**
> InvitationsShow lgl_api_v1_invitations_create(event_id, body)

Create new Invitation

Add invitation.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.create_body import CreateBody
from lgl_openapi_3_0_client.models.invitations_show import InvitationsShow
from lgl_openapi_3_0_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = lgl_openapi_3_0_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lgl_openapi_3_0_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyQuery
configuration.api_key['ApiKeyQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyQuery'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = lgl_openapi_3_0_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lgl_openapi_3_0_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lgl_openapi_3_0_client.InvitationsApi(api_client)
    event_id = 56 # int | Event Id
    body = lgl_openapi_3_0_client.CreateBody() # CreateBody | Create Objects

    try:
        # Create new Invitation
        api_response = api_instance.lgl_api_v1_invitations_create(event_id, body)
        print("The response of InvitationsApi->lgl_api_v1_invitations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->lgl_api_v1_invitations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Event Id | 
 **body** | [**CreateBody**](CreateBody.md)| Create Objects | 

### Return type

[**InvitationsShow**](InvitationsShow.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lgl_api_v1_invitations_destroy**
> lgl_api_v1_invitations_destroy(id)

Delete Invitation

Delete the invitation.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = lgl_openapi_3_0_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lgl_openapi_3_0_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyQuery
configuration.api_key['ApiKeyQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyQuery'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = lgl_openapi_3_0_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lgl_openapi_3_0_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lgl_openapi_3_0_client.InvitationsApi(api_client)
    id = 56 # int | Invitation Id

    try:
        # Delete Invitation
        api_instance.lgl_api_v1_invitations_destroy(id)
    except Exception as e:
        print("Exception when calling InvitationsApi->lgl_api_v1_invitations_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Invitation Id | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lgl_api_v1_invitations_update**
> InvitationsShow lgl_api_v1_invitations_update(id, body)

Update Invitation

Update the invitation.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.invitations_show import InvitationsShow
from lgl_openapi_3_0_client.models.update_body import UpdateBody
from lgl_openapi_3_0_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = lgl_openapi_3_0_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lgl_openapi_3_0_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyQuery
configuration.api_key['ApiKeyQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyQuery'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = lgl_openapi_3_0_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lgl_openapi_3_0_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lgl_openapi_3_0_client.InvitationsApi(api_client)
    id = 56 # int | Invitation Id
    body = lgl_openapi_3_0_client.UpdateBody() # UpdateBody | Update Objects

    try:
        # Update Invitation
        api_response = api_instance.lgl_api_v1_invitations_update(id, body)
        print("The response of InvitationsApi->lgl_api_v1_invitations_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->lgl_api_v1_invitations_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Invitation Id | 
 **body** | [**UpdateBody**](UpdateBody.md)| Update Objects | 

### Return type

[**InvitationsShow**](InvitationsShow.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_constituent_invitations**
> InvitationsIndex v1_constituent_invitations(constituent_id, limit=limit, offset=offset)

Fetch Invitations for Constituent

Lists all the invitations for a constituent.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.invitations_index import InvitationsIndex
from lgl_openapi_3_0_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = lgl_openapi_3_0_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lgl_openapi_3_0_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyQuery
configuration.api_key['ApiKeyQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyQuery'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = lgl_openapi_3_0_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lgl_openapi_3_0_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lgl_openapi_3_0_client.InvitationsApi(api_client)
    constituent_id = 56 # int | Constituent Id
    limit = 25 # int | Number of entries to return. Default: 25 (optional) (default to 25)
    offset = 0 # int | Start at given entry. Default: 0 (optional) (default to 0)

    try:
        # Fetch Invitations for Constituent
        api_response = api_instance.v1_constituent_invitations(constituent_id, limit=limit, offset=offset)
        print("The response of InvitationsApi->v1_constituent_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->v1_constituent_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **constituent_id** | **int**| Constituent Id | 
 **limit** | **int**| Number of entries to return. Default: 25 | [optional] [default to 25]
 **offset** | **int**| Start at given entry. Default: 0 | [optional] [default to 0]

### Return type

[**InvitationsIndex**](InvitationsIndex.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_invitation_v1_constituent_invitations**
> InvitationsShow v1_create_invitation_v1_constituent_invitations(constituent_id, body)

Create new Invitation for Constituent

Add invitation to constituent.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.create_body_const import CreateBodyConst
from lgl_openapi_3_0_client.models.invitations_show import InvitationsShow
from lgl_openapi_3_0_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = lgl_openapi_3_0_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lgl_openapi_3_0_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyQuery
configuration.api_key['ApiKeyQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyQuery'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = lgl_openapi_3_0_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lgl_openapi_3_0_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lgl_openapi_3_0_client.InvitationsApi(api_client)
    constituent_id = 56 # int | Constituent Id
    body = lgl_openapi_3_0_client.CreateBodyConst() # CreateBodyConst | Create Objects

    try:
        # Create new Invitation for Constituent
        api_response = api_instance.v1_create_invitation_v1_constituent_invitations(constituent_id, body)
        print("The response of InvitationsApi->v1_create_invitation_v1_constituent_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->v1_create_invitation_v1_constituent_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **constituent_id** | **int**| Constituent Id | 
 **body** | [**CreateBodyConst**](CreateBodyConst.md)| Create Objects | 

### Return type

[**InvitationsShow**](InvitationsShow.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_event_invitations**
> InvitationsIndex v1_event_invitations(event_id, limit=limit, offset=offset)

Fetch Invitations for Event

Lists all the invitations for an event.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.invitations_index import InvitationsIndex
from lgl_openapi_3_0_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = lgl_openapi_3_0_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lgl_openapi_3_0_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyQuery
configuration.api_key['ApiKeyQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyQuery'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = lgl_openapi_3_0_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lgl_openapi_3_0_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lgl_openapi_3_0_client.InvitationsApi(api_client)
    event_id = 56 # int | Event Id
    limit = 25 # int | Number of entries to return. Default: 25 (optional) (default to 25)
    offset = 0 # int | Start at given entry. Default: 0 (optional) (default to 0)

    try:
        # Fetch Invitations for Event
        api_response = api_instance.v1_event_invitations(event_id, limit=limit, offset=offset)
        print("The response of InvitationsApi->v1_event_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->v1_event_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Event Id | 
 **limit** | **int**| Number of entries to return. Default: 25 | [optional] [default to 25]
 **offset** | **int**| Start at given entry. Default: 0 | [optional] [default to 0]

### Return type

[**InvitationsIndex**](InvitationsIndex.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_invitation**
> InvitationsShow v1_invitation(id)

Show Invitation details

Show details for the invitation.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.invitations_show import InvitationsShow
from lgl_openapi_3_0_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = lgl_openapi_3_0_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = lgl_openapi_3_0_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: ApiKeyQuery
configuration.api_key['ApiKeyQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyQuery'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = lgl_openapi_3_0_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with lgl_openapi_3_0_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lgl_openapi_3_0_client.InvitationsApi(api_client)
    id = 56 # int | Invitation Id

    try:
        # Show Invitation details
        api_response = api_instance.v1_invitation(id)
        print("The response of InvitationsApi->v1_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->v1_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Invitation Id | 

### Return type

[**InvitationsShow**](InvitationsShow.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

