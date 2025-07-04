# lgl_openapi_3_0_client.ConstituentRelationshipsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lgl_api_v1_constituent_relationships_create**](ConstituentRelationshipsApi.md#lgl_api_v1_constituent_relationships_create) | **POST** /v1/constituents/{constituent_id}/constituent_relationships.json | Create new Constituent Relationship
[**lgl_api_v1_constituent_relationships_destroy**](ConstituentRelationshipsApi.md#lgl_api_v1_constituent_relationships_destroy) | **DELETE** /v1/constituent_relationships/{id}.json | Delete Constituent Relationship
[**lgl_api_v1_constituent_relationships_update**](ConstituentRelationshipsApi.md#lgl_api_v1_constituent_relationships_update) | **PATCH** /v1/constituent_relationships/{id}.json | Update Constituent Relationship
[**v1_constituent_constituent_relationships**](ConstituentRelationshipsApi.md#v1_constituent_constituent_relationships) | **GET** /v1/constituents/{constituent_id}/constituent_relationships.json | Fetch Constituent Relationships for a Constituent
[**v1_constituent_relationship**](ConstituentRelationshipsApi.md#v1_constituent_relationship) | **GET** /v1/constituent_relationships/{id}.json | Show Constituent Relationship details


# **lgl_api_v1_constituent_relationships_create**
> ConstituentRelationshipsShow lgl_api_v1_constituent_relationships_create(constituent_id, body)

Create new Constituent Relationship

Add constituent relationship.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.constituent_relationships_show import ConstituentRelationshipsShow
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
    api_instance = lgl_openapi_3_0_client.ConstituentRelationshipsApi(api_client)
    constituent_id = 56 # int | Constituent Id
    body = lgl_openapi_3_0_client.CreateBody() # CreateBody | Create Objects

    try:
        # Create new Constituent Relationship
        api_response = api_instance.lgl_api_v1_constituent_relationships_create(constituent_id, body)
        print("The response of ConstituentRelationshipsApi->lgl_api_v1_constituent_relationships_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstituentRelationshipsApi->lgl_api_v1_constituent_relationships_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **constituent_id** | **int**| Constituent Id | 
 **body** | [**CreateBody**](CreateBody.md)| Create Objects | 

### Return type

[**ConstituentRelationshipsShow**](ConstituentRelationshipsShow.md)

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

# **lgl_api_v1_constituent_relationships_destroy**
> lgl_api_v1_constituent_relationships_destroy(id)

Delete Constituent Relationship

Delete the constituent relationship.

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
    api_instance = lgl_openapi_3_0_client.ConstituentRelationshipsApi(api_client)
    id = 56 # int | Constituent Relationship Id

    try:
        # Delete Constituent Relationship
        api_instance.lgl_api_v1_constituent_relationships_destroy(id)
    except Exception as e:
        print("Exception when calling ConstituentRelationshipsApi->lgl_api_v1_constituent_relationships_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Constituent Relationship Id | 

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

# **lgl_api_v1_constituent_relationships_update**
> ConstituentRelationshipsShow lgl_api_v1_constituent_relationships_update(id, body)

Update Constituent Relationship

Update the constituent relationship.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.constituent_relationships_show import ConstituentRelationshipsShow
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
    api_instance = lgl_openapi_3_0_client.ConstituentRelationshipsApi(api_client)
    id = 56 # int | Constituent Relationship Id
    body = lgl_openapi_3_0_client.UpdateBody() # UpdateBody | Update Objects

    try:
        # Update Constituent Relationship
        api_response = api_instance.lgl_api_v1_constituent_relationships_update(id, body)
        print("The response of ConstituentRelationshipsApi->lgl_api_v1_constituent_relationships_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstituentRelationshipsApi->lgl_api_v1_constituent_relationships_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Constituent Relationship Id | 
 **body** | [**UpdateBody**](UpdateBody.md)| Update Objects | 

### Return type

[**ConstituentRelationshipsShow**](ConstituentRelationshipsShow.md)

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

# **v1_constituent_constituent_relationships**
> ConstituentRelationshipsIndex v1_constituent_constituent_relationships(constituent_id)

Fetch Constituent Relationships for a Constituent

Lists all the constituent relationships for a constituent.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.constituent_relationships_index import ConstituentRelationshipsIndex
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
    api_instance = lgl_openapi_3_0_client.ConstituentRelationshipsApi(api_client)
    constituent_id = 56 # int | Constituent Id

    try:
        # Fetch Constituent Relationships for a Constituent
        api_response = api_instance.v1_constituent_constituent_relationships(constituent_id)
        print("The response of ConstituentRelationshipsApi->v1_constituent_constituent_relationships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstituentRelationshipsApi->v1_constituent_constituent_relationships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **constituent_id** | **int**| Constituent Id | 

### Return type

[**ConstituentRelationshipsIndex**](ConstituentRelationshipsIndex.md)

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

# **v1_constituent_relationship**
> ConstituentRelationshipsShow v1_constituent_relationship(id)

Show Constituent Relationship details

Show details for the constituent relationship.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.constituent_relationships_show import ConstituentRelationshipsShow
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
    api_instance = lgl_openapi_3_0_client.ConstituentRelationshipsApi(api_client)
    id = 56 # int | Constituent Relationship Id

    try:
        # Show Constituent Relationship details
        api_response = api_instance.v1_constituent_relationship(id)
        print("The response of ConstituentRelationshipsApi->v1_constituent_relationship:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConstituentRelationshipsApi->v1_constituent_relationship: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Constituent Relationship Id | 

### Return type

[**ConstituentRelationshipsShow**](ConstituentRelationshipsShow.md)

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

