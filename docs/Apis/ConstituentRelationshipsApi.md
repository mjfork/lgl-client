# ConstituentRelationshipsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1ConstituentRelationshipsCreate**](ConstituentRelationshipsApi.md#lglApiV1ConstituentRelationshipsCreate) | **POST** /v1/constituents/{constituent_id}/constituent_relationships.json | Create new Constituent Relationship |
| [**lglApiV1ConstituentRelationshipsDestroy**](ConstituentRelationshipsApi.md#lglApiV1ConstituentRelationshipsDestroy) | **DELETE** /v1/constituent_relationships/{id}.json | Delete Constituent Relationship |
| [**lglApiV1ConstituentRelationshipsUpdate**](ConstituentRelationshipsApi.md#lglApiV1ConstituentRelationshipsUpdate) | **PATCH** /v1/constituent_relationships/{id}.json | Update Constituent Relationship |
| [**v1ConstituentConstituentRelationships**](ConstituentRelationshipsApi.md#v1ConstituentConstituentRelationships) | **GET** /v1/constituents/{constituent_id}/constituent_relationships.json | Fetch Constituent Relationships for a Constituent |
| [**v1ConstituentRelationship**](ConstituentRelationshipsApi.md#v1ConstituentRelationship) | **GET** /v1/constituent_relationships/{id}.json | Show Constituent Relationship details |


<a name="lglApiV1ConstituentRelationshipsCreate"></a>
# **lglApiV1ConstituentRelationshipsCreate**
> ConstituentRelationships_show lglApiV1ConstituentRelationshipsCreate(constituent\_id, body)

Create new Constituent Relationship

    Add constituent relationship.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**ConstituentRelationships_show**](../Models/ConstituentRelationships_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1ConstituentRelationshipsDestroy"></a>
# **lglApiV1ConstituentRelationshipsDestroy**
> lglApiV1ConstituentRelationshipsDestroy(id)

Delete Constituent Relationship

    Delete the constituent relationship.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Constituent Relationship Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1ConstituentRelationshipsUpdate"></a>
# **lglApiV1ConstituentRelationshipsUpdate**
> ConstituentRelationships_show lglApiV1ConstituentRelationshipsUpdate(id, body)

Update Constituent Relationship

    Update the constituent relationship.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Constituent Relationship Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**ConstituentRelationships_show**](../Models/ConstituentRelationships_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1ConstituentConstituentRelationships"></a>
# **v1ConstituentConstituentRelationships**
> ConstituentRelationships_index v1ConstituentConstituentRelationships(constituent\_id)

Fetch Constituent Relationships for a Constituent

    Lists all the constituent relationships for a constituent.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |

### Return type

[**ConstituentRelationships_index**](../Models/ConstituentRelationships_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1ConstituentRelationship"></a>
# **v1ConstituentRelationship**
> ConstituentRelationships_show v1ConstituentRelationship(id)

Show Constituent Relationship details

    Show details for the constituent relationship.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Constituent Relationship Id | [default to null] |

### Return type

[**ConstituentRelationships_show**](../Models/ConstituentRelationships_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

