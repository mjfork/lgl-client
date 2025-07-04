# EmailAddressesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1EmailAddressesCreate**](EmailAddressesApi.md#lglApiV1EmailAddressesCreate) | **POST** /v1/constituents/{constituent_id}/email_addresses.json | Create new Email Address |
| [**lglApiV1EmailAddressesDestroy**](EmailAddressesApi.md#lglApiV1EmailAddressesDestroy) | **DELETE** /v1/email_addresses/{id}.json | Delete Email Address |
| [**lglApiV1EmailAddressesUpdate**](EmailAddressesApi.md#lglApiV1EmailAddressesUpdate) | **PATCH** /v1/email_addresses/{id}.json | Update Email Address |
| [**v1ConstituentEmailAddresses**](EmailAddressesApi.md#v1ConstituentEmailAddresses) | **GET** /v1/constituents/{constituent_id}/email_addresses.json | Fetch Email Addresses |
| [**v1EmailAddress**](EmailAddressesApi.md#v1EmailAddress) | **GET** /v1/email_addresses/{id}.json | Show Email Address details |


<a name="lglApiV1EmailAddressesCreate"></a>
# **lglApiV1EmailAddressesCreate**
> EmailAddresses_show lglApiV1EmailAddressesCreate(constituent\_id, body)

Create new Email Address

    Add email address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**EmailAddresses_show**](../Models/EmailAddresses_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1EmailAddressesDestroy"></a>
# **lglApiV1EmailAddressesDestroy**
> lglApiV1EmailAddressesDestroy(id)

Delete Email Address

    Delete the email address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Email Address Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1EmailAddressesUpdate"></a>
# **lglApiV1EmailAddressesUpdate**
> EmailAddresses_show lglApiV1EmailAddressesUpdate(id, body)

Update Email Address

    Update the email address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Email Address Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**EmailAddresses_show**](../Models/EmailAddresses_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1ConstituentEmailAddresses"></a>
# **v1ConstituentEmailAddresses**
> EmailAddresses_index v1ConstituentEmailAddresses(constituent\_id, limit, offset)

Fetch Email Addresses

    Lists all the email addresses.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**EmailAddresses_index**](../Models/EmailAddresses_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1EmailAddress"></a>
# **v1EmailAddress**
> EmailAddresses_show v1EmailAddress(id)

Show Email Address details

    Show details for the email address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Email Address Id | [default to null] |

### Return type

[**EmailAddresses_show**](../Models/EmailAddresses_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

