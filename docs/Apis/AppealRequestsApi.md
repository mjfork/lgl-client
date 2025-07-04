# AppealRequestsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1AppealRequestsCreate**](AppealRequestsApi.md#lglApiV1AppealRequestsCreate) | **POST** /v1/appeals/{appeal_id}/appeal_requests.json | Create new Appeal Request |
| [**lglApiV1AppealRequestsDestroy**](AppealRequestsApi.md#lglApiV1AppealRequestsDestroy) | **DELETE** /v1/appeal_requests/{id}.json | Delete Appeal Request |
| [**lglApiV1AppealRequestsUpdate**](AppealRequestsApi.md#lglApiV1AppealRequestsUpdate) | **PATCH** /v1/appeal_requests/{id}.json | Update Appeal Request |
| [**v1AppealAppealRequests**](AppealRequestsApi.md#v1AppealAppealRequests) | **GET** /v1/appeals/{appeal_id}/appeal_requests.json | Fetch Appeal Requests for Appeal |
| [**v1AppealRequest**](AppealRequestsApi.md#v1AppealRequest) | **GET** /v1/appeal_requests/{id}.json | Show Appeal Request details |
| [**v1ConstituentAppealRequests**](AppealRequestsApi.md#v1ConstituentAppealRequests) | **GET** /v1/constituents/{constituent_id}/appeal_requests.json | Fetch Appeal Requests for Constituent |
| [**v1CreateAppealRequestV1ConstituentAppealRequests**](AppealRequestsApi.md#v1CreateAppealRequestV1ConstituentAppealRequests) | **POST** /v1/constituents/{constituent_id}/appeal_requests.json | Create new Appeal Request for Constituent |


<a name="lglApiV1AppealRequestsCreate"></a>
# **lglApiV1AppealRequestsCreate**
> AppealRequests_show lglApiV1AppealRequestsCreate(appeal\_id, body)

Create new Appeal Request

    Add appeal request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appeal\_id** | **Integer**| Appeal Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**AppealRequests_show**](../Models/AppealRequests_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1AppealRequestsDestroy"></a>
# **lglApiV1AppealRequestsDestroy**
> lglApiV1AppealRequestsDestroy(id)

Delete Appeal Request

    Delete the appeal request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Appeal Request Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1AppealRequestsUpdate"></a>
# **lglApiV1AppealRequestsUpdate**
> AppealRequests_show lglApiV1AppealRequestsUpdate(id, body)

Update Appeal Request

    Update the appeal request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Appeal Request Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**AppealRequests_show**](../Models/AppealRequests_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1AppealAppealRequests"></a>
# **v1AppealAppealRequests**
> AppealRequests_index v1AppealAppealRequests(appeal\_id, limit, offset)

Fetch Appeal Requests for Appeal

    Lists all the appeal requests for an appeal.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appeal\_id** | **Integer**| Appeal Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**AppealRequests_index**](../Models/AppealRequests_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1AppealRequest"></a>
# **v1AppealRequest**
> AppealRequests_show v1AppealRequest(id)

Show Appeal Request details

    Show details for the appeal request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Appeal Request Id | [default to null] |

### Return type

[**AppealRequests_show**](../Models/AppealRequests_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1ConstituentAppealRequests"></a>
# **v1ConstituentAppealRequests**
> AppealRequests_index v1ConstituentAppealRequests(constituent\_id, limit, offset)

Fetch Appeal Requests for Constituent

    Lists all the appeal requests for a constituent.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**AppealRequests_index**](../Models/AppealRequests_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1CreateAppealRequestV1ConstituentAppealRequests"></a>
# **v1CreateAppealRequestV1ConstituentAppealRequests**
> AppealRequests_show v1CreateAppealRequestV1ConstituentAppealRequests(constituent\_id, body)

Create new Appeal Request for Constituent

    Add appeal request to constituent.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody_Const**](../Models/CreateBody_Const.md)| Create Objects | |

### Return type

[**AppealRequests_show**](../Models/AppealRequests_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

