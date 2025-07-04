# AttributesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1Attributes**](AttributesApi.md#v1Attributes) | **GET** /v1/attributes.json | Fetch Custom Attributes |


<a name="v1Attributes"></a>
# **v1Attributes**
> Attributes_index v1Attributes(item\_type, limit, offset)

Fetch Custom Attributes

    Lists custom attributes..

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **item\_type** | **String**| Attributes for type (default: Constituent). Available: Constituent, Invitation | [optional] [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Attributes_index**](../Models/Attributes_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

