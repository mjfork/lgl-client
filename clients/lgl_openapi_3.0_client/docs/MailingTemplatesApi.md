# lgl_openapi_3_0_client.MailingTemplatesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_mailing_templates**](MailingTemplatesApi.md#v1_mailing_templates) | **GET** /v1/mailing_templates.json | Fetch Mailing Templates


# **v1_mailing_templates**
> MailingTemplatesIndex v1_mailing_templates(mailing_type_id=mailing_type_id, limit=limit, offset=offset)

Fetch Mailing Templates

Lists all the mailing templates.

### Example

* Basic Authentication (BasicAuth):
* Api Key Authentication (ApiKeyQuery):
* Bearer Authentication (BearerAuth):

```python
import lgl_openapi_3_0_client
from lgl_openapi_3_0_client.models.mailing_templates_index import MailingTemplatesIndex
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
    api_instance = lgl_openapi_3_0_client.MailingTemplatesApi(api_client)
    mailing_type_id = 'mailing_type_id_example' # str | Mailing type ID (optional)
    limit = 25 # int | Number of entries to return. Default: 25 (optional) (default to 25)
    offset = 0 # int | Start at given entry. Default: 0 (optional) (default to 0)

    try:
        # Fetch Mailing Templates
        api_response = api_instance.v1_mailing_templates(mailing_type_id=mailing_type_id, limit=limit, offset=offset)
        print("The response of MailingTemplatesApi->v1_mailing_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailingTemplatesApi->v1_mailing_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailing_type_id** | **str**| Mailing type ID | [optional] 
 **limit** | **int**| Number of entries to return. Default: 25 | [optional] [default to 25]
 **offset** | **int**| Start at given entry. Default: 0 | [optional] [default to 0]

### Return type

[**MailingTemplatesIndex**](MailingTemplatesIndex.md)

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

