# WebAddressesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1WebAddressesCreate**](WebAddressesApi.md#lglApiV1WebAddressesCreate) | **POST** /v1/constituents/{constituent_id}/web_addresses.json | Create new Web Address |
| [**lglApiV1WebAddressesDestroy**](WebAddressesApi.md#lglApiV1WebAddressesDestroy) | **DELETE** /v1/web_addresses/{id}.json | Delete Web Address |
| [**lglApiV1WebAddressesUpdate**](WebAddressesApi.md#lglApiV1WebAddressesUpdate) | **PATCH** /v1/web_addresses/{id}.json | Update Web Address |
| [**v1ConstituentWebAddresses**](WebAddressesApi.md#v1ConstituentWebAddresses) | **GET** /v1/constituents/{constituent_id}/web_addresses.json | Fetch Web Addresses |
| [**v1WebAddress**](WebAddressesApi.md#v1WebAddress) | **GET** /v1/web_addresses/{id}.json | Show Web Address details |


<a name="lglApiV1WebAddressesCreate"></a>
# **lglApiV1WebAddressesCreate**
> WebAddresses_show lglApiV1WebAddressesCreate(constituent\_id, body)

Create new Web Address

    Add web address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**WebAddresses_show**](../Models/WebAddresses_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1WebAddressesDestroy"></a>
# **lglApiV1WebAddressesDestroy**
> lglApiV1WebAddressesDestroy(id)

Delete Web Address

    Delete the web address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Web Address Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1WebAddressesUpdate"></a>
# **lglApiV1WebAddressesUpdate**
> WebAddresses_show lglApiV1WebAddressesUpdate(id, body)

Update Web Address

    Update the web address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Web Address Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**WebAddresses_show**](../Models/WebAddresses_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1ConstituentWebAddresses"></a>
# **v1ConstituentWebAddresses**
> WebAddresses_index v1ConstituentWebAddresses(constituent\_id, limit, offset)

Fetch Web Addresses

    Lists all the web addresses.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**WebAddresses_index**](../Models/WebAddresses_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1WebAddress"></a>
# **v1WebAddress**
> WebAddresses_show v1WebAddress(id)

Show Web Address details

    Show details for the web address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Web Address Id | [default to null] |

### Return type

[**WebAddresses_show**](../Models/WebAddresses_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

