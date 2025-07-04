# ClassAffiliationsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1ClassAffiliationsCreate**](ClassAffiliationsApi.md#lglApiV1ClassAffiliationsCreate) | **POST** /v1/constituents/{constituent_id}/class_affiliations.json | Create new Class Affiliation |
| [**lglApiV1ClassAffiliationsDestroy**](ClassAffiliationsApi.md#lglApiV1ClassAffiliationsDestroy) | **DELETE** /v1/class_affiliations/{id}.json | Delete Class Affiliation |
| [**lglApiV1ClassAffiliationsUpdate**](ClassAffiliationsApi.md#lglApiV1ClassAffiliationsUpdate) | **PATCH** /v1/class_affiliations/{id}.json | Update Class Affiliation |
| [**v1ClassAffiliation**](ClassAffiliationsApi.md#v1ClassAffiliation) | **GET** /v1/class_affiliations/{id}.json | Show Class Affiliation details |
| [**v1ConstituentClassAffiliations**](ClassAffiliationsApi.md#v1ConstituentClassAffiliations) | **GET** /v1/constituents/{constituent_id}/class_affiliations.json | Fetch Class Affiliations |


<a name="lglApiV1ClassAffiliationsCreate"></a>
# **lglApiV1ClassAffiliationsCreate**
> ClassAffiliations_show lglApiV1ClassAffiliationsCreate(constituent\_id, body)

Create new Class Affiliation

    Add class affiliation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**ClassAffiliations_show**](../Models/ClassAffiliations_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1ClassAffiliationsDestroy"></a>
# **lglApiV1ClassAffiliationsDestroy**
> lglApiV1ClassAffiliationsDestroy(id)

Delete Class Affiliation

    Delete the class affiliation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Class Affiliation Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1ClassAffiliationsUpdate"></a>
# **lglApiV1ClassAffiliationsUpdate**
> ClassAffiliations_show lglApiV1ClassAffiliationsUpdate(id, body)

Update Class Affiliation

    Update the class affiliation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Class Affiliation Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**ClassAffiliations_show**](../Models/ClassAffiliations_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1ClassAffiliation"></a>
# **v1ClassAffiliation**
> ClassAffiliations_show v1ClassAffiliation(id)

Show Class Affiliation details

    Show details for the class affiliation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Class Affiliation Id | [default to null] |

### Return type

[**ClassAffiliations_show**](../Models/ClassAffiliations_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1ConstituentClassAffiliations"></a>
# **v1ConstituentClassAffiliations**
> ClassAffiliations_index v1ConstituentClassAffiliations(constituent\_id, limit, offset)

Fetch Class Affiliations

    Lists all the class affiliations.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**ClassAffiliations_index**](../Models/ClassAffiliations_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

