# TeamMembersApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1TeamMembers**](TeamMembersApi.md#v1TeamMembers) | **GET** /v1/team_members.json | Fetch Team Members |


<a name="v1TeamMembers"></a>
# **v1TeamMembers**
> TeamMembers_index v1TeamMembers(limit, offset)

Fetch Team Members

    Lists all the team members.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**TeamMembers_index**](../Models/TeamMembers_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

