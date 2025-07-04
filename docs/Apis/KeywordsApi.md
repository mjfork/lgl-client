# KeywordsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1KeywordsCreate**](KeywordsApi.md#lglApiV1KeywordsCreate) | **POST** /v1/categories/{category_id}/keywords.json | Create new Keyword |
| [**lglApiV1KeywordsDestroy**](KeywordsApi.md#lglApiV1KeywordsDestroy) | **DELETE** /v1/keywords/{id}.json | Delete Keyword |
| [**lglApiV1KeywordsUpdate**](KeywordsApi.md#lglApiV1KeywordsUpdate) | **PATCH** /v1/keywords/{id}.json | Update Keyword |
| [**v1CategoryKeywords**](KeywordsApi.md#v1CategoryKeywords) | **GET** /v1/categories/{category_id}/keywords.json | Fetch Keywords |
| [**v1ConstituentKeyword**](KeywordsApi.md#v1ConstituentKeyword) | **DELETE** /v1/constituents/{constituent_id}/keywords/{id}.json | Remove Keyword |
| [**v1ConstituentKeywords**](KeywordsApi.md#v1ConstituentKeywords) | **POST** /v1/constituents/{constituent_id}/keywords.json | Add Keyword |
| [**v1Keyword**](KeywordsApi.md#v1Keyword) | **GET** /v1/keywords/{id}.json | Show Keyword details |


<a name="lglApiV1KeywordsCreate"></a>
# **lglApiV1KeywordsCreate**
> Keywords_show lglApiV1KeywordsCreate(category\_id, body)

Create new Keyword

    Add keyword.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **category\_id** | **Integer**| Category Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**Keywords_show**](../Models/Keywords_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1KeywordsDestroy"></a>
# **lglApiV1KeywordsDestroy**
> lglApiV1KeywordsDestroy(id, permanent)

Delete Keyword

    Delete the keyword.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Keyword Id | [default to null] |
| **permanent** | **Integer**| Delete permantently. Default: 0 | [optional] [default to 0] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1KeywordsUpdate"></a>
# **lglApiV1KeywordsUpdate**
> Keywords_show lglApiV1KeywordsUpdate(id, body)

Update Keyword

    Update the keyword.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Keyword Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**Keywords_show**](../Models/Keywords_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1CategoryKeywords"></a>
# **v1CategoryKeywords**
> Keywords_index v1CategoryKeywords(category\_id, limit, offset)

Fetch Keywords

    Lists all the keywords.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **category\_id** | **Integer**| Category Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Keywords_index**](../Models/Keywords_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1ConstituentKeyword"></a>
# **v1ConstituentKeyword**
> v1ConstituentKeyword(id, constituent\_id)

Remove Keyword

    Remove a keyword from a constituent

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Keyword Id | [default to null] |
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="v1ConstituentKeywords"></a>
# **v1ConstituentKeywords**
> v1ConstituentKeywords(constituent\_id, body)

Add Keyword

    Add a keyword to a constituent.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**AddBody**](../Models/AddBody.md)| Add Keyword | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: Not defined

<a name="v1Keyword"></a>
# **v1Keyword**
> Keywords_show v1Keyword(id)

Show Keyword details

    Show details for the keyword.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Keyword Id | [default to null] |

### Return type

[**Keywords_show**](../Models/Keywords_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

