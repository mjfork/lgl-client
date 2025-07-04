# GroupsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1GroupsCreate**](GroupsApi.md#lglApiV1GroupsCreate) | **POST** /v1/groups.json | Create new Group |
| [**lglApiV1GroupsDestroy**](GroupsApi.md#lglApiV1GroupsDestroy) | **DELETE** /v1/groups/{id}.json | Delete Group |
| [**lglApiV1GroupsUpdate**](GroupsApi.md#lglApiV1GroupsUpdate) | **PATCH** /v1/groups/{id}.json | Update Group |
| [**v1Group**](GroupsApi.md#v1Group) | **GET** /v1/groups/{id}.json | Show Group details |
| [**v1Groups**](GroupsApi.md#v1Groups) | **GET** /v1/groups.json | Fetch Groups |


<a name="lglApiV1GroupsCreate"></a>
# **lglApiV1GroupsCreate**
> Groups_show lglApiV1GroupsCreate(body)

Create new Group

    Add group.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**Groups_show**](../Models/Groups_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1GroupsDestroy"></a>
# **lglApiV1GroupsDestroy**
> lglApiV1GroupsDestroy(id)

Delete Group

    Delete the group.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Group Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1GroupsUpdate"></a>
# **lglApiV1GroupsUpdate**
> Groups_show lglApiV1GroupsUpdate(id, body)

Update Group

    Update the group.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Group Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**Groups_show**](../Models/Groups_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1Group"></a>
# **v1Group**
> Groups_show v1Group(id)

Show Group details

    Show details for the group.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Group Id | [default to null] |

### Return type

[**Groups_show**](../Models/Groups_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1Groups"></a>
# **v1Groups**
> Groups_index v1Groups(limit, offset)

Fetch Groups

    Lists all the groups.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Groups_index**](../Models/Groups_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

