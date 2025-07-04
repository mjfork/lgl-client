# lgl_openapi_3_0_client.ConstituentsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lgl_api_v1_constituents_create**](ConstituentsApi.md#lgl_api_v1_constituents_create) | **POST** /v1/constituents.json | Create new Constituent
[**lgl_api_v1_constituents_destroy**](ConstituentsApi.md#lgl_api_v1_constituents_destroy) | **DELETE** /v1/constituents/{id}.json | Delete constituent
[**lgl_api_v1_constituents_update**](ConstituentsApi.md#lgl_api_v1_constituents_update) | **PATCH** /v1/constituents/{id}.json | Update constituent
[**search_v1_constituents**](ConstituentsApi.md#search_v1_constituents) | **GET** /v1/constituents/search.json | Search for Constituents
[**v1_constituent**](ConstituentsApi.md#v1_constituent) | **GET** /v1/constituents/{id}.json | Show Constituent details
[**v1_constituents**](ConstituentsApi.md#v1_constituents) | **GET** /v1/constituents.json | Fetch all Constituents for an account


# **lgl_api_v1_constituents_create**
> ConstituentsShow lgl_api_v1_constituents_create(body)

Create new Constituent

Add a Constituent to an account along with related objects.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.constituents_show import ConstituentsShow
from lgl_openapi_3_0_client.models.create_body import CreateBody
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
    api_instance = lgl_openapi_3_0_client.ConstituentsApi(api_client)
    body = lgl_openapi_3_0_client.CreateBody() # CreateBody | Create Objects

    try:
        # Create new Constituent
        api_response = api_instance.lgl_api_v1_constituents_create(body)
        print("The response of ConstituentsApi->lgl_api_v1_constituents_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstituentsApi->lgl_api_v1_constituents_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBody**](CreateBody.md)| Create Objects | 

### Return type

[**ConstituentsShow**](ConstituentsShow.md)

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

# **lgl_api_v1_constituents_destroy**
> lgl_api_v1_constituents_destroy(id)

Delete constituent

Delete the Constituent along with related objects.

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
    api_instance = lgl_openapi_3_0_client.ConstituentsApi(api_client)
    id = 56 # int | Constituent Id

    try:
        # Delete constituent
        api_instance.lgl_api_v1_constituents_destroy(id)
    except Exception as e:
        print("Exception when calling ConstituentsApi->lgl_api_v1_constituents_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Constituent Id | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lgl_api_v1_constituents_update**
> ConstituentsShow lgl_api_v1_constituents_update(id, body)

Update constituent

Update the Constituent along with related objects

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.constituents_show import ConstituentsShow
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
    api_instance = lgl_openapi_3_0_client.ConstituentsApi(api_client)
    id = 56 # int | Constituent Id
    body = lgl_openapi_3_0_client.UpdateBody() # UpdateBody | Update Objects

    try:
        # Update constituent
        api_response = api_instance.lgl_api_v1_constituents_update(id, body)
        print("The response of ConstituentsApi->lgl_api_v1_constituents_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstituentsApi->lgl_api_v1_constituents_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Constituent Id | 
 **body** | [**UpdateBody**](UpdateBody.md)| Update Objects | 

### Return type

[**ConstituentsShow**](ConstituentsShow.md)

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

# **search_v1_constituents**
> ConstituentsIndex search_v1_constituents(q, expand=expand, sort=sort, limit=limit, offset=offset)

Search for Constituents

Search for active constituents.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.constituents_index import ConstituentsIndex
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
    api_instance = lgl_openapi_3_0_client.ConstituentsApi(api_client)
    q = 'q_example' # str | Query string. (EX: name=brady). Parameter value must be URL encoded.
    expand = 'expand_example' # str | Expand requested, comma separated, data structures: 'class_affiliations, relationships, street_addresses, phone_numbers, email_addresses, web_addresses, categories, groups, memberships, custom_attrs' (optional)
    sort = 'sort_example' # str | Sort by one of the following fields: 'name, external_id, lgl_id, date_created, date_updated, membership_level, membership_end_date_from'. Add an exclamation point to reverse the order. (EX: sort=name!) (optional)
    limit = 25 # int | Number of entries to return. Default: 25 (optional) (default to 25)
    offset = 0 # int | Start at given entry. Default: 0 (optional) (default to 0)

    try:
        # Search for Constituents
        api_response = api_instance.search_v1_constituents(q, expand=expand, sort=sort, limit=limit, offset=offset)
        print("The response of ConstituentsApi->search_v1_constituents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstituentsApi->search_v1_constituents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Query string. (EX: name&#x3D;brady). Parameter value must be URL encoded. | 
 **expand** | **str**| Expand requested, comma separated, data structures: &#39;class_affiliations, relationships, street_addresses, phone_numbers, email_addresses, web_addresses, categories, groups, memberships, custom_attrs&#39; | [optional] 
 **sort** | **str**| Sort by one of the following fields: &#39;name, external_id, lgl_id, date_created, date_updated, membership_level, membership_end_date_from&#39;. Add an exclamation point to reverse the order. (EX: sort&#x3D;name!) | [optional] 
 **limit** | **int**| Number of entries to return. Default: 25 | [optional] [default to 25]
 **offset** | **int**| Start at given entry. Default: 0 | [optional] [default to 0]

### Return type

[**ConstituentsIndex**](ConstituentsIndex.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_constituent**
> ConstituentsShow v1_constituent(id)

Show Constituent details

Show details for the constituent.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.constituents_show import ConstituentsShow
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
    api_instance = lgl_openapi_3_0_client.ConstituentsApi(api_client)
    id = 56 # int | Constituent Id

    try:
        # Show Constituent details
        api_response = api_instance.v1_constituent(id)
        print("The response of ConstituentsApi->v1_constituent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstituentsApi->v1_constituent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Constituent Id | 

### Return type

[**ConstituentsShow**](ConstituentsShow.md)

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

# **v1_constituents**
> ConstituentsIndex v1_constituents(limit=limit, offset=offset)

Fetch all Constituents for an account

This lists all the active constituents for an account.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.constituents_index import ConstituentsIndex
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
    api_instance = lgl_openapi_3_0_client.ConstituentsApi(api_client)
    limit = 25 # int | Number of entries to return. Default: 25 (optional) (default to 25)
    offset = 0 # int | Start at given entry. Default: 0 (optional) (default to 0)

    try:
        # Fetch all Constituents for an account
        api_response = api_instance.v1_constituents(limit=limit, offset=offset)
        print("The response of ConstituentsApi->v1_constituents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstituentsApi->v1_constituents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of entries to return. Default: 25 | [optional] [default to 25]
 **offset** | **int**| Start at given entry. Default: 0 | [optional] [default to 0]

### Return type

[**ConstituentsIndex**](ConstituentsIndex.md)

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

