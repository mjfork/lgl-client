# StreetAddressesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1StreetAddressesCreate**](StreetAddressesApi.md#lglApiV1StreetAddressesCreate) | **POST** /v1/constituents/{constituent_id}/street_addresses.json | Create new Street Address |
| [**lglApiV1StreetAddressesDestroy**](StreetAddressesApi.md#lglApiV1StreetAddressesDestroy) | **DELETE** /v1/street_addresses/{id}.json | Delete Street Address |
| [**lglApiV1StreetAddressesUpdate**](StreetAddressesApi.md#lglApiV1StreetAddressesUpdate) | **PATCH** /v1/street_addresses/{id}.json | Update Street Address |
| [**v1ConstituentStreetAddresses**](StreetAddressesApi.md#v1ConstituentStreetAddresses) | **GET** /v1/constituents/{constituent_id}/street_addresses.json | Fetch Street Addresses |
| [**v1StreetAddress**](StreetAddressesApi.md#v1StreetAddress) | **GET** /v1/street_addresses/{id}.json | Show Street Address details |


<a name="lglApiV1StreetAddressesCreate"></a>
# **lglApiV1StreetAddressesCreate**
> StreetAddresses_show lglApiV1StreetAddressesCreate(constituent\_id, body)

Create new Street Address

    Add street address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**StreetAddresses_show**](../Models/StreetAddresses_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1StreetAddressesDestroy"></a>
# **lglApiV1StreetAddressesDestroy**
> lglApiV1StreetAddressesDestroy(id)

Delete Street Address

    Delete the street address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Street Address Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1StreetAddressesUpdate"></a>
# **lglApiV1StreetAddressesUpdate**
> StreetAddresses_show lglApiV1StreetAddressesUpdate(id, body)

Update Street Address

    Update the street address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Street Address Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**StreetAddresses_show**](../Models/StreetAddresses_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1ConstituentStreetAddresses"></a>
# **v1ConstituentStreetAddresses**
> StreetAddresses_index v1ConstituentStreetAddresses(constituent\_id, limit, offset)

Fetch Street Addresses

    Lists all the street addresses.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**StreetAddresses_index**](../Models/StreetAddresses_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1StreetAddress"></a>
# **v1StreetAddress**
> StreetAddresses_show v1StreetAddress(id)

Show Street Address details

    Show details for the street address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Street Address Id | [default to null] |

### Return type

[**StreetAddresses_show**](../Models/StreetAddresses_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

