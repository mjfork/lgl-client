# TypesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1Types**](TypesApi.md#v1Types) | **GET** /v1/types.json | Fetch Types for Account |
| [**v1V1TypesType**](TypesApi.md#v1V1TypesType) | **GET** /v1/types/{type}.json | Fetch Values for Type |


<a name="v1Types"></a>
# **v1Types**
> Types_index v1Types(limit, offset)

Fetch Types for Account

    Lists all the types for an account.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Types_index**](../Models/Types_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1V1TypesType"></a>
# **v1V1TypesType**
> TypeValues_index v1V1TypesType(type, limit, offset)

Fetch Values for Type

    Lists all the values for a type.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **String**| Type: [ contact_report_types | email_address_types | mailing_types | street_address_types | phone_number_types | web_address_types | volunteering_categories | appeal_types | event_types | note_types ] | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**TypeValues_index**](../Models/TypeValues_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

