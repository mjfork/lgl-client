# ConstituentsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1ConstituentsCreate**](ConstituentsApi.md#lglApiV1ConstituentsCreate) | **POST** /v1/constituents.json | Create new Constituent |
| [**lglApiV1ConstituentsDestroy**](ConstituentsApi.md#lglApiV1ConstituentsDestroy) | **DELETE** /v1/constituents/{id}.json | Delete constituent |
| [**lglApiV1ConstituentsUpdate**](ConstituentsApi.md#lglApiV1ConstituentsUpdate) | **PATCH** /v1/constituents/{id}.json | Update constituent |
| [**searchV1Constituents**](ConstituentsApi.md#searchV1Constituents) | **GET** /v1/constituents/search.json | Search for Constituents |
| [**v1Constituent**](ConstituentsApi.md#v1Constituent) | **GET** /v1/constituents/{id}.json | Show Constituent details |
| [**v1Constituents**](ConstituentsApi.md#v1Constituents) | **GET** /v1/constituents.json | Fetch all Constituents for an account |


<a name="lglApiV1ConstituentsCreate"></a>
# **lglApiV1ConstituentsCreate**
> Constituents_show lglApiV1ConstituentsCreate(body)

Create new Constituent

    Add a Constituent to an account along with related objects.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**Constituents_show**](../Models/Constituents_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1ConstituentsDestroy"></a>
# **lglApiV1ConstituentsDestroy**
> lglApiV1ConstituentsDestroy(id)

Delete constituent

    Delete the Constituent along with related objects.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Constituent Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1ConstituentsUpdate"></a>
# **lglApiV1ConstituentsUpdate**
> Constituents_show lglApiV1ConstituentsUpdate(id, body)

Update constituent

    Update the Constituent along with related objects

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**Constituents_show**](../Models/Constituents_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="searchV1Constituents"></a>
# **searchV1Constituents**
> Constituents_index searchV1Constituents(q\[\], expand, sort, limit, offset)

Search for Constituents

    Search for active constituents.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **q\[\]** | **String**| Query string. (EX: name&#x3D;brady). Parameter value must be URL encoded. | [default to null] |
| **expand** | **String**| Expand requested, comma separated, data structures: &#39;class_affiliations, relationships, street_addresses, phone_numbers, email_addresses, web_addresses, categories, groups, memberships, custom_attrs&#39; | [optional] [default to null] |
| **sort** | **String**| Sort by one of the following fields: &#39;name, external_id, lgl_id, date_created, date_updated, membership_level, membership_end_date_from&#39;. Add an exclamation point to reverse the order. (EX: sort&#x3D;name!) | [optional] [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Constituents_index**](../Models/Constituents_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1Constituent"></a>
# **v1Constituent**
> Constituents_show v1Constituent(id)

Show Constituent details

    Show details for the constituent.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Constituent Id | [default to null] |

### Return type

[**Constituents_show**](../Models/Constituents_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1Constituents"></a>
# **v1Constituents**
> Constituents_index v1Constituents(limit, offset)

Fetch all Constituents for an account

    This lists all the active constituents for an account.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Constituents_index**](../Models/Constituents_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

