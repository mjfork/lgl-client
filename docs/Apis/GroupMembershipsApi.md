# GroupMembershipsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1GroupMembershipsCreate**](GroupMembershipsApi.md#lglApiV1GroupMembershipsCreate) | **POST** /v1/constituents/{constituent_id}/group_memberships.json | Create new Group Membership |
| [**lglApiV1GroupMembershipsDestroy**](GroupMembershipsApi.md#lglApiV1GroupMembershipsDestroy) | **DELETE** /v1/group_memberships/{id}.json | Delete Group Membership |
| [**lglApiV1GroupMembershipsUpdate**](GroupMembershipsApi.md#lglApiV1GroupMembershipsUpdate) | **PATCH** /v1/group_memberships/{id}.json | Update Group Membership |
| [**v1ConstituentGroupMemberships**](GroupMembershipsApi.md#v1ConstituentGroupMemberships) | **GET** /v1/constituents/{constituent_id}/group_memberships.json | Fetch Group Memberships |
| [**v1GroupMembership**](GroupMembershipsApi.md#v1GroupMembership) | **GET** /v1/group_memberships/{id}.json | Show Group Membership details |


<a name="lglApiV1GroupMembershipsCreate"></a>
# **lglApiV1GroupMembershipsCreate**
> GroupMemberships_show lglApiV1GroupMembershipsCreate(constituent\_id, body)

Create new Group Membership

    Add group membership.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**GroupMemberships_show**](../Models/GroupMemberships_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1GroupMembershipsDestroy"></a>
# **lglApiV1GroupMembershipsDestroy**
> lglApiV1GroupMembershipsDestroy(id)

Delete Group Membership

    Delete the group membership.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Group Membership Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1GroupMembershipsUpdate"></a>
# **lglApiV1GroupMembershipsUpdate**
> GroupMemberships_show lglApiV1GroupMembershipsUpdate(id, body)

Update Group Membership

    Update the group membership.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Group Membership Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**GroupMemberships_show**](../Models/GroupMemberships_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1ConstituentGroupMemberships"></a>
# **v1ConstituentGroupMemberships**
> GroupMemberships_index v1ConstituentGroupMemberships(constituent\_id, limit, offset)

Fetch Group Memberships

    Lists all the group memberships.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**GroupMemberships_index**](../Models/GroupMemberships_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1GroupMembership"></a>
# **v1GroupMembership**
> GroupMemberships_show v1GroupMembership(id)

Show Group Membership details

    Show details for the group membership.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Group Membership Id | [default to null] |

### Return type

[**GroupMemberships_show**](../Models/GroupMemberships_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

