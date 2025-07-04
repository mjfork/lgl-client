# MembershipsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1MembershipsCreate**](MembershipsApi.md#lglApiV1MembershipsCreate) | **POST** /v1/constituents/{constituent_id}/memberships.json | Create new Membership |
| [**lglApiV1MembershipsDestroy**](MembershipsApi.md#lglApiV1MembershipsDestroy) | **DELETE** /v1/memberships/{id}.json | Delete Membership |
| [**lglApiV1MembershipsUpdate**](MembershipsApi.md#lglApiV1MembershipsUpdate) | **PATCH** /v1/memberships/{id}.json | Update Membership |
| [**v1ConstituentMemberships**](MembershipsApi.md#v1ConstituentMemberships) | **GET** /v1/constituents/{constituent_id}/memberships.json | Fetch Memberships |
| [**v1Membership**](MembershipsApi.md#v1Membership) | **GET** /v1/memberships/{id}.json | Show Membership details |


<a name="lglApiV1MembershipsCreate"></a>
# **lglApiV1MembershipsCreate**
> Memberships_show lglApiV1MembershipsCreate(constituent\_id, body)

Create new Membership

    Add membership.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**Memberships_show**](../Models/Memberships_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1MembershipsDestroy"></a>
# **lglApiV1MembershipsDestroy**
> lglApiV1MembershipsDestroy(id)

Delete Membership

    Delete the membership.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Membership Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1MembershipsUpdate"></a>
# **lglApiV1MembershipsUpdate**
> Memberships_show lglApiV1MembershipsUpdate(id, body)

Update Membership

    Update the membership.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Membership Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**Memberships_show**](../Models/Memberships_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1ConstituentMemberships"></a>
# **v1ConstituentMemberships**
> Memberships_index v1ConstituentMemberships(constituent\_id, limit, offset)

Fetch Memberships

    Lists all the memberships.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Memberships_index**](../Models/Memberships_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1Membership"></a>
# **v1Membership**
> Memberships_show v1Membership(id)

Show Membership details

    Show details for the membership.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Membership Id | [default to null] |

### Return type

[**Memberships_show**](../Models/Memberships_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

