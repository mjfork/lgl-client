# GiftTypesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1GiftTypes**](GiftTypesApi.md#v1GiftTypes) | **GET** /v1/gift_types.json | Fetch Gift Types |


<a name="v1GiftTypes"></a>
# **v1GiftTypes**
> GiftTypes_index v1GiftTypes(limit, offset)

Fetch Gift Types

    Lists all the gift types.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**GiftTypes_index**](../Models/GiftTypes_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

