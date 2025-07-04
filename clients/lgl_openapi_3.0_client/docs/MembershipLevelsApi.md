# lgl_openapi_3_0_client.MembershipLevelsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lgl_api_v1_membership_levels_create**](MembershipLevelsApi.md#lgl_api_v1_membership_levels_create) | **POST** /v1/membership_levels.json | Create new Membership Level
[**lgl_api_v1_membership_levels_destroy**](MembershipLevelsApi.md#lgl_api_v1_membership_levels_destroy) | **DELETE** /v1/membership_levels/{id}.json | Delete Membership Level
[**lgl_api_v1_membership_levels_update**](MembershipLevelsApi.md#lgl_api_v1_membership_levels_update) | **PATCH** /v1/membership_levels/{id}.json | Update Membership Level
[**v1_membership_level**](MembershipLevelsApi.md#v1_membership_level) | **GET** /v1/membership_levels/{id}.json | Show Membership Level details
[**v1_membership_levels**](MembershipLevelsApi.md#v1_membership_levels) | **GET** /v1/membership_levels.json | Fetch Membership Levels


# **lgl_api_v1_membership_levels_create**
> MembershipLevelsShow lgl_api_v1_membership_levels_create(body)

Create new Membership Level

Add membership level.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.create_body import CreateBody
from lgl_openapi_3_0_client.models.membership_levels_show import MembershipLevelsShow
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
    api_instance = lgl_openapi_3_0_client.MembershipLevelsApi(api_client)
    body = lgl_openapi_3_0_client.CreateBody() # CreateBody | Create Objects

    try:
        # Create new Membership Level
        api_response = api_instance.lgl_api_v1_membership_levels_create(body)
        print("The response of MembershipLevelsApi->lgl_api_v1_membership_levels_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipLevelsApi->lgl_api_v1_membership_levels_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBody**](CreateBody.md)| Create Objects | 

### Return type

[**MembershipLevelsShow**](MembershipLevelsShow.md)

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

# **lgl_api_v1_membership_levels_destroy**
> lgl_api_v1_membership_levels_destroy(id)

Delete Membership Level

Delete the membership level.

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
    api_instance = lgl_openapi_3_0_client.MembershipLevelsApi(api_client)
    id = 56 # int | Membership Level Id

    try:
        # Delete Membership Level
        api_instance.lgl_api_v1_membership_levels_destroy(id)
    except Exception as e:
        print("Exception when calling MembershipLevelsApi->lgl_api_v1_membership_levels_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Membership Level Id | 

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

# **lgl_api_v1_membership_levels_update**
> MembershipLevelsShow lgl_api_v1_membership_levels_update(id, body)

Update Membership Level

Update the membership level.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.membership_levels_show import MembershipLevelsShow
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
    api_instance = lgl_openapi_3_0_client.MembershipLevelsApi(api_client)
    id = 56 # int | Membership Level Id
    body = lgl_openapi_3_0_client.UpdateBody() # UpdateBody | Update Objects

    try:
        # Update Membership Level
        api_response = api_instance.lgl_api_v1_membership_levels_update(id, body)
        print("The response of MembershipLevelsApi->lgl_api_v1_membership_levels_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipLevelsApi->lgl_api_v1_membership_levels_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Membership Level Id | 
 **body** | [**UpdateBody**](UpdateBody.md)| Update Objects | 

### Return type

[**MembershipLevelsShow**](MembershipLevelsShow.md)

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

# **v1_membership_level**
> MembershipLevelsShow v1_membership_level(id)

Show Membership Level details

Show details for the membership level.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.membership_levels_show import MembershipLevelsShow
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
    api_instance = lgl_openapi_3_0_client.MembershipLevelsApi(api_client)
    id = 56 # int | Membership Level Id

    try:
        # Show Membership Level details
        api_response = api_instance.v1_membership_level(id)
        print("The response of MembershipLevelsApi->v1_membership_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipLevelsApi->v1_membership_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Membership Level Id | 

### Return type

[**MembershipLevelsShow**](MembershipLevelsShow.md)

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

# **v1_membership_levels**
> MembershipLevelsIndex v1_membership_levels(limit=limit, offset=offset)

Fetch Membership Levels

Lists all the membership levels.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.membership_levels_index import MembershipLevelsIndex
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
    api_instance = lgl_openapi_3_0_client.MembershipLevelsApi(api_client)
    limit = 25 # int | Number of entries to return. Default: 25 (optional) (default to 25)
    offset = 0 # int | Start at given entry. Default: 0 (optional) (default to 0)

    try:
        # Fetch Membership Levels
        api_response = api_instance.v1_membership_levels(limit=limit, offset=offset)
        print("The response of MembershipLevelsApi->v1_membership_levels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MembershipLevelsApi->v1_membership_levels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of entries to return. Default: 25 | [optional] [default to 25]
 **offset** | **int**| Start at given entry. Default: 0 | [optional] [default to 0]

### Return type

[**MembershipLevelsIndex**](MembershipLevelsIndex.md)

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

