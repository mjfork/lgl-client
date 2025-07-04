# GiftsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1GiftsCreate**](GiftsApi.md#lglApiV1GiftsCreate) | **POST** /v1/constituents/{constituent_id}/gifts.json | Create new Gift |
| [**lglApiV1GiftsDestroy**](GiftsApi.md#lglApiV1GiftsDestroy) | **DELETE** /v1/gifts/{id}.json | Delete Gift |
| [**lglApiV1GiftsUpdate**](GiftsApi.md#lglApiV1GiftsUpdate) | **PATCH** /v1/gifts/{id}.json | Update Gift |
| [**searchV1Gifts**](GiftsApi.md#searchV1Gifts) | **GET** /v1/gifts/search.json | Search for Gifts |
| [**v1ConstituentGifts**](GiftsApi.md#v1ConstituentGifts) | **GET** /v1/constituents/{constituent_id}/gifts.json | Fetch Gifts |
| [**v1Gift**](GiftsApi.md#v1Gift) | **GET** /v1/gifts/{id}.json | Show Gift details |


<a name="lglApiV1GiftsCreate"></a>
# **lglApiV1GiftsCreate**
> Gifts_show lglApiV1GiftsCreate(constituent\_id, body)

Create new Gift

    Add gift.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**Gifts_show**](../Models/Gifts_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1GiftsDestroy"></a>
# **lglApiV1GiftsDestroy**
> lglApiV1GiftsDestroy(id)

Delete Gift

    Delete the gift.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Gift Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1GiftsUpdate"></a>
# **lglApiV1GiftsUpdate**
> Gifts_show lglApiV1GiftsUpdate(id, body)

Update Gift

    Update the gift.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Gift Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**Gifts_show**](../Models/Gifts_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="searchV1Gifts"></a>
# **searchV1Gifts**
> Gifts_index searchV1Gifts(q\[\], expand, sort, limit, offset)

Search for Gifts

    Search for active gifts

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **q\[\]** | **String**| Query string. (EX: updated_from&#x3D;2016-01-01). Parameter value must be URL encoded. | [default to null] |
| **expand** | **String**| Expand requested, comma separated, data structures: &#39;external_constituent_id, first_name, last_name, org_name, phone_numbers, email_addresses, street_addresses&#39; | [optional] [default to null] |
| **sort** | **String**| Sort by one of the following fields: &#39;name, gift_amount, date, date_created, date_updated, fund, appeal, campaign, gift_type&#39;. Add an exclamation point to reverse the order. (EX: sort&#x3D;name!) | [optional] [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Gifts_index**](../Models/Gifts_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1ConstituentGifts"></a>
# **v1ConstituentGifts**
> Gifts_index v1ConstituentGifts(constituent\_id, limit, offset)

Fetch Gifts

    Lists all the gifts.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Gifts_index**](../Models/Gifts_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1Gift"></a>
# **v1Gift**
> Gifts_show v1Gift(id)

Show Gift details

    Show details for the gift.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Gift Id | [default to null] |

### Return type

[**Gifts_show**](../Models/Gifts_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

