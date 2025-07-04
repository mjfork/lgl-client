# RelationshipTypesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1RelationshipTypes**](RelationshipTypesApi.md#v1RelationshipTypes) | **GET** /v1/relationship_types.json | Fetch Relationship Types |


<a name="v1RelationshipTypes"></a>
# **v1RelationshipTypes**
> RelationshipTypes_index v1RelationshipTypes(limit, offset)

Fetch Relationship Types

    Lists all the relationship types.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**RelationshipTypes_index**](../Models/RelationshipTypes_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

