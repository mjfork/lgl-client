# MembershipLevelsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1MembershipLevelsCreate**](MembershipLevelsApi.md#lglApiV1MembershipLevelsCreate) | **POST** /v1/membership_levels.json | Create new Membership Level |
| [**lglApiV1MembershipLevelsDestroy**](MembershipLevelsApi.md#lglApiV1MembershipLevelsDestroy) | **DELETE** /v1/membership_levels/{id}.json | Delete Membership Level |
| [**lglApiV1MembershipLevelsUpdate**](MembershipLevelsApi.md#lglApiV1MembershipLevelsUpdate) | **PATCH** /v1/membership_levels/{id}.json | Update Membership Level |
| [**v1MembershipLevel**](MembershipLevelsApi.md#v1MembershipLevel) | **GET** /v1/membership_levels/{id}.json | Show Membership Level details |
| [**v1MembershipLevels**](MembershipLevelsApi.md#v1MembershipLevels) | **GET** /v1/membership_levels.json | Fetch Membership Levels |


<a name="lglApiV1MembershipLevelsCreate"></a>
# **lglApiV1MembershipLevelsCreate**
> MembershipLevels_show lglApiV1MembershipLevelsCreate(body)

Create new Membership Level

    Add membership level.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**MembershipLevels_show**](../Models/MembershipLevels_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1MembershipLevelsDestroy"></a>
# **lglApiV1MembershipLevelsDestroy**
> lglApiV1MembershipLevelsDestroy(id)

Delete Membership Level

    Delete the membership level.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Membership Level Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1MembershipLevelsUpdate"></a>
# **lglApiV1MembershipLevelsUpdate**
> MembershipLevels_show lglApiV1MembershipLevelsUpdate(id, body)

Update Membership Level

    Update the membership level.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Membership Level Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**MembershipLevels_show**](../Models/MembershipLevels_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1MembershipLevel"></a>
# **v1MembershipLevel**
> MembershipLevels_show v1MembershipLevel(id)

Show Membership Level details

    Show details for the membership level.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Membership Level Id | [default to null] |

### Return type

[**MembershipLevels_show**](../Models/MembershipLevels_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1MembershipLevels"></a>
# **v1MembershipLevels**
> MembershipLevels_index v1MembershipLevels(limit, offset)

Fetch Membership Levels

    Lists all the membership levels.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**MembershipLevels_index**](../Models/MembershipLevels_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

