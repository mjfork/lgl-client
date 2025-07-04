# VolunteerTimesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1VolunteerTimesCreate**](VolunteerTimesApi.md#lglApiV1VolunteerTimesCreate) | **POST** /v1/constituents/{constituent_id}/volunteer_times.json | Create new Volunteer Time |
| [**lglApiV1VolunteerTimesDestroy**](VolunteerTimesApi.md#lglApiV1VolunteerTimesDestroy) | **DELETE** /v1/volunteer_times/{id}.json | Delete Volunteer Time |
| [**lglApiV1VolunteerTimesUpdate**](VolunteerTimesApi.md#lglApiV1VolunteerTimesUpdate) | **PATCH** /v1/volunteer_times/{id}.json | Update Volunteer Time |
| [**searchV1VolunteerTimes**](VolunteerTimesApi.md#searchV1VolunteerTimes) | **GET** /v1/volunteer_times/search.json | Search for Volunteer Times |
| [**v1ConstituentVolunteerTimes**](VolunteerTimesApi.md#v1ConstituentVolunteerTimes) | **GET** /v1/constituents/{constituent_id}/volunteer_times.json | Fetch Volunteer Times for Constituent |
| [**v1VolunteerTime**](VolunteerTimesApi.md#v1VolunteerTime) | **GET** /v1/volunteer_times/{id}.json | Show Volunteer Time details |
| [**v1VolunteerTimes**](VolunteerTimesApi.md#v1VolunteerTimes) | **GET** /v1/volunteer_times.json | Fetch Volunteer Times for Account |


<a name="lglApiV1VolunteerTimesCreate"></a>
# **lglApiV1VolunteerTimesCreate**
> VolunteerTimes_show lglApiV1VolunteerTimesCreate(constituent\_id, body)

Create new Volunteer Time

    Add volunteer time.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**VolunteerTimes_show**](../Models/VolunteerTimes_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1VolunteerTimesDestroy"></a>
# **lglApiV1VolunteerTimesDestroy**
> lglApiV1VolunteerTimesDestroy(id)

Delete Volunteer Time

    Delete the volunteer time.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Volunteer Time Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1VolunteerTimesUpdate"></a>
# **lglApiV1VolunteerTimesUpdate**
> VolunteerTimes_show lglApiV1VolunteerTimesUpdate(id, body)

Update Volunteer Time

    Update the volunteer time.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Volunteer Time Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**VolunteerTimes_show**](../Models/VolunteerTimes_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="searchV1VolunteerTimes"></a>
# **searchV1VolunteerTimes**
> VolunteerTimes_index searchV1VolunteerTimes(q\[\], sort, limit, offset)

Search for Volunteer Times

    Search for active volunteer times

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **q\[\]** | **String**| Query string. (EX: updated_from&#x3D;2016-01-01). Parameter value must be URL encoded. | [default to null] |
| **sort** | **String**| Sort by one of the following fields: &#39;date, constituent_id&#39;. Add an exclamation point to reverse the order. (EX: sort&#x3D;name!) | [optional] [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**VolunteerTimes_index**](../Models/VolunteerTimes_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1ConstituentVolunteerTimes"></a>
# **v1ConstituentVolunteerTimes**
> VolunteerTimes_index v1ConstituentVolunteerTimes(constituent\_id, limit, offset)

Fetch Volunteer Times for Constituent

    Lists all the volunteer times for a constituent.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**VolunteerTimes_index**](../Models/VolunteerTimes_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1VolunteerTime"></a>
# **v1VolunteerTime**
> VolunteerTimes_show v1VolunteerTime(id)

Show Volunteer Time details

    Show details for the volunteer time.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Volunteer Time Id | [default to null] |

### Return type

[**VolunteerTimes_show**](../Models/VolunteerTimes_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1VolunteerTimes"></a>
# **v1VolunteerTimes**
> VolunteerTimes_index v1VolunteerTimes(limit, offset)

Fetch Volunteer Times for Account

    Lists all the volunteer times for an account.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**VolunteerTimes_index**](../Models/VolunteerTimes_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

