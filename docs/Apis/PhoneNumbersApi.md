# PhoneNumbersApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1PhoneNumbersCreate**](PhoneNumbersApi.md#lglApiV1PhoneNumbersCreate) | **POST** /v1/constituents/{constituent_id}/phone_numbers.json | Create new Phone Number |
| [**lglApiV1PhoneNumbersDestroy**](PhoneNumbersApi.md#lglApiV1PhoneNumbersDestroy) | **DELETE** /v1/phone_numbers/{id}.json | Delete Phone Number |
| [**lglApiV1PhoneNumbersUpdate**](PhoneNumbersApi.md#lglApiV1PhoneNumbersUpdate) | **PATCH** /v1/phone_numbers/{id}.json | Update Phone Number |
| [**v1ConstituentPhoneNumbers**](PhoneNumbersApi.md#v1ConstituentPhoneNumbers) | **GET** /v1/constituents/{constituent_id}/phone_numbers.json | Fetch Phone Numbers |
| [**v1PhoneNumber**](PhoneNumbersApi.md#v1PhoneNumber) | **GET** /v1/phone_numbers/{id}.json | Show Phone Number details |


<a name="lglApiV1PhoneNumbersCreate"></a>
# **lglApiV1PhoneNumbersCreate**
> PhoneNumbers_show lglApiV1PhoneNumbersCreate(constituent\_id, body)

Create new Phone Number

    Add phone number.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**PhoneNumbers_show**](../Models/PhoneNumbers_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1PhoneNumbersDestroy"></a>
# **lglApiV1PhoneNumbersDestroy**
> lglApiV1PhoneNumbersDestroy(id)

Delete Phone Number

    Delete the phone number.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Phone Number Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1PhoneNumbersUpdate"></a>
# **lglApiV1PhoneNumbersUpdate**
> PhoneNumbers_show lglApiV1PhoneNumbersUpdate(id, body)

Update Phone Number

    Update the phone number.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Phone Number Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**PhoneNumbers_show**](../Models/PhoneNumbers_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1ConstituentPhoneNumbers"></a>
# **v1ConstituentPhoneNumbers**
> PhoneNumbers_index v1ConstituentPhoneNumbers(constituent\_id, limit, offset)

Fetch Phone Numbers

    Lists all the phone numbers.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**PhoneNumbers_index**](../Models/PhoneNumbers_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1PhoneNumber"></a>
# **v1PhoneNumber**
> PhoneNumbers_show v1PhoneNumber(id)

Show Phone Number details

    Show details for the phone number.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Phone Number Id | [default to null] |

### Return type

[**PhoneNumbers_show**](../Models/PhoneNumbers_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

