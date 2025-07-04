# AppealsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1Appeals**](AppealsApi.md#v1Appeals) | **GET** /v1/appeals.json | Fetch Appeals |


<a name="v1Appeals"></a>
# **v1Appeals**
> Appeals_index v1Appeals(limit, offset)

Fetch Appeals

    Lists all the appeals.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Appeals_index**](../Models/Appeals_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

