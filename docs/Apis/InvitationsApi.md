# InvitationsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1InvitationsCreate**](InvitationsApi.md#lglApiV1InvitationsCreate) | **POST** /v1/events/{event_id}/invitations.json | Create new Invitation |
| [**lglApiV1InvitationsDestroy**](InvitationsApi.md#lglApiV1InvitationsDestroy) | **DELETE** /v1/invitations/{id}.json | Delete Invitation |
| [**lglApiV1InvitationsUpdate**](InvitationsApi.md#lglApiV1InvitationsUpdate) | **PATCH** /v1/invitations/{id}.json | Update Invitation |
| [**v1ConstituentInvitations**](InvitationsApi.md#v1ConstituentInvitations) | **GET** /v1/constituents/{constituent_id}/invitations.json | Fetch Invitations for Constituent |
| [**v1CreateInvitationV1ConstituentInvitations**](InvitationsApi.md#v1CreateInvitationV1ConstituentInvitations) | **POST** /v1/constituents/{constituent_id}/invitations.json | Create new Invitation for Constituent |
| [**v1EventInvitations**](InvitationsApi.md#v1EventInvitations) | **GET** /v1/events/{event_id}/invitations.json | Fetch Invitations for Event |
| [**v1Invitation**](InvitationsApi.md#v1Invitation) | **GET** /v1/invitations/{id}.json | Show Invitation details |


<a name="lglApiV1InvitationsCreate"></a>
# **lglApiV1InvitationsCreate**
> Invitations_show lglApiV1InvitationsCreate(event\_id, body)

Create new Invitation

    Add invitation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **event\_id** | **Integer**| Event Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**Invitations_show**](../Models/Invitations_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1InvitationsDestroy"></a>
# **lglApiV1InvitationsDestroy**
> lglApiV1InvitationsDestroy(id)

Delete Invitation

    Delete the invitation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Invitation Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1InvitationsUpdate"></a>
# **lglApiV1InvitationsUpdate**
> Invitations_show lglApiV1InvitationsUpdate(id, body)

Update Invitation

    Update the invitation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Invitation Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**Invitations_show**](../Models/Invitations_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1ConstituentInvitations"></a>
# **v1ConstituentInvitations**
> Invitations_index v1ConstituentInvitations(constituent\_id, limit, offset)

Fetch Invitations for Constituent

    Lists all the invitations for a constituent.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Invitations_index**](../Models/Invitations_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1CreateInvitationV1ConstituentInvitations"></a>
# **v1CreateInvitationV1ConstituentInvitations**
> Invitations_show v1CreateInvitationV1ConstituentInvitations(constituent\_id, body)

Create new Invitation for Constituent

    Add invitation to constituent.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody_Const**](../Models/CreateBody_Const.md)| Create Objects | |

### Return type

[**Invitations_show**](../Models/Invitations_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1EventInvitations"></a>
# **v1EventInvitations**
> Invitations_index v1EventInvitations(event\_id, limit, offset)

Fetch Invitations for Event

    Lists all the invitations for an event.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **event\_id** | **Integer**| Event Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Invitations_index**](../Models/Invitations_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1Invitation"></a>
# **v1Invitation**
> Invitations_show v1Invitation(id)

Show Invitation details

    Show details for the invitation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Invitation Id | [default to null] |

### Return type

[**Invitations_show**](../Models/Invitations_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

