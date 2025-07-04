# ClassAffiliationTypesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1ClassAffiliationTypes**](ClassAffiliationTypesApi.md#v1ClassAffiliationTypes) | **GET** /v1/class_affiliation_types.json | Fetch Class Affiliation Types |


<a name="v1ClassAffiliationTypes"></a>
# **v1ClassAffiliationTypes**
> ClassAffiliationTypes_index v1ClassAffiliationTypes(limit, offset)

Fetch Class Affiliation Types

    Lists all the class affiliation types.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**ClassAffiliationTypes_index**](../Models/ClassAffiliationTypes_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

