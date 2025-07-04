# GiftCategoriesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1GiftCategories**](GiftCategoriesApi.md#v1GiftCategories) | **GET** /v1/gift_categories.json | Fetch Gift Categories |


<a name="v1GiftCategories"></a>
# **v1GiftCategories**
> GiftCategories_index v1GiftCategories(gift\_type\_id, limit, offset)

Fetch Gift Categories

    Lists all the gift categories.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **gift\_type\_id** | **String**| Gift type ID | [optional] [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**GiftCategories_index**](../Models/GiftCategories_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

