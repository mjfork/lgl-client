# ContactReportsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1ContactReportsCreate**](ContactReportsApi.md#lglApiV1ContactReportsCreate) | **POST** /v1/constituents/{constituent_id}/contact_reports.json | Create new Contact Report |
| [**lglApiV1ContactReportsDestroy**](ContactReportsApi.md#lglApiV1ContactReportsDestroy) | **DELETE** /v1/contact_reports/{id}.json | Delete Contact Report |
| [**lglApiV1ContactReportsUpdate**](ContactReportsApi.md#lglApiV1ContactReportsUpdate) | **PATCH** /v1/contact_reports/{id}.json | Update Contact Report |
| [**searchV1ContactReports**](ContactReportsApi.md#searchV1ContactReports) | **GET** /v1/contact_reports/search.json | Search for Contact Reports |
| [**v1ConstituentContactReports**](ContactReportsApi.md#v1ConstituentContactReports) | **GET** /v1/constituents/{constituent_id}/contact_reports.json | Fetch Contact Reports for Constituent |
| [**v1ContactReport**](ContactReportsApi.md#v1ContactReport) | **GET** /v1/contact_reports/{id}.json | Show Contact Report details |
| [**v1ContactReports**](ContactReportsApi.md#v1ContactReports) | **GET** /v1/contact_reports.json | Fetch Contact Reports for Account |


<a name="lglApiV1ContactReportsCreate"></a>
# **lglApiV1ContactReportsCreate**
> ContactReports_show lglApiV1ContactReportsCreate(constituent\_id, body)

Create new Contact Report

    Add contact report.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**ContactReports_show**](../Models/ContactReports_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1ContactReportsDestroy"></a>
# **lglApiV1ContactReportsDestroy**
> lglApiV1ContactReportsDestroy(id)

Delete Contact Report

    Delete the contact report.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Contact Report Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1ContactReportsUpdate"></a>
# **lglApiV1ContactReportsUpdate**
> ContactReports_show lglApiV1ContactReportsUpdate(id, body)

Update Contact Report

    Update the contact report.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Contact Report Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**ContactReports_show**](../Models/ContactReports_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="searchV1ContactReports"></a>
# **searchV1ContactReports**
> ContactReports_index searchV1ContactReports(q\[\], sort, limit, offset)

Search for Contact Reports

    Search for active contact reports

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **q\[\]** | **String**| Query string. (EX: updated_from&#x3D;2016-01-01). Parameter value must be URL encoded. | [default to null] |
| **sort** | **String**| Sort by one of the following fields: &#39;name, date, constituent_id&#39;. Add an exclamation point to reverse the order. (EX: sort&#x3D;name!) | [optional] [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**ContactReports_index**](../Models/ContactReports_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1ConstituentContactReports"></a>
# **v1ConstituentContactReports**
> ContactReports_index v1ConstituentContactReports(constituent\_id, limit, offset)

Fetch Contact Reports for Constituent

    Lists all the contact reports for a constituent.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**ContactReports_index**](../Models/ContactReports_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1ContactReport"></a>
# **v1ContactReport**
> ContactReports_show v1ContactReport(id)

Show Contact Report details

    Show details for the contact report.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Contact Report Id | [default to null] |

### Return type

[**ContactReports_show**](../Models/ContactReports_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1ContactReports"></a>
# **v1ContactReports**
> ContactReports_index v1ContactReports(limit, offset)

Fetch Contact Reports for Account

    Lists all the contact reports for an account.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**ContactReports_index**](../Models/ContactReports_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

