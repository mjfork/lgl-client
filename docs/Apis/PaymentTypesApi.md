# PaymentTypesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1PaymentTypes**](PaymentTypesApi.md#v1PaymentTypes) | **GET** /v1/payment_types.json | Fetch Payment Types |


<a name="v1PaymentTypes"></a>
# **v1PaymentTypes**
> PaymentTypes_index v1PaymentTypes(limit, offset)

Fetch Payment Types

    Lists all the payment types.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**PaymentTypes_index**](../Models/PaymentTypes_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

