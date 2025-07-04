# NotesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1NotesCreate**](NotesApi.md#lglApiV1NotesCreate) | **POST** /v1/constituents/{constituent_id}/notes.json | Create new Note |
| [**lglApiV1NotesDestroy**](NotesApi.md#lglApiV1NotesDestroy) | **DELETE** /v1/notes/{id}.json | Delete Note |
| [**lglApiV1NotesUpdate**](NotesApi.md#lglApiV1NotesUpdate) | **PATCH** /v1/notes/{id}.json | Update Note |
| [**v1ConstituentNotes**](NotesApi.md#v1ConstituentNotes) | **GET** /v1/constituents/{constituent_id}/notes.json | Fetch Notes for Constituent |
| [**v1Note**](NotesApi.md#v1Note) | **GET** /v1/notes/{id}.json | Show Note details |
| [**v1Notes**](NotesApi.md#v1Notes) | **GET** /v1/notes.json | Fetch Notes for Account |


<a name="lglApiV1NotesCreate"></a>
# **lglApiV1NotesCreate**
> Notes_show lglApiV1NotesCreate(constituent\_id, body)

Create new Note

    Add note.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**Notes_show**](../Models/Notes_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1NotesDestroy"></a>
# **lglApiV1NotesDestroy**
> lglApiV1NotesDestroy(id)

Delete Note

    Delete the note.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Note Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1NotesUpdate"></a>
# **lglApiV1NotesUpdate**
> Notes_show lglApiV1NotesUpdate(id, body)

Update Note

    Update the note.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Note Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**Notes_show**](../Models/Notes_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1ConstituentNotes"></a>
# **v1ConstituentNotes**
> Notes_index v1ConstituentNotes(constituent\_id, limit, offset)

Fetch Notes for Constituent

    Lists all the notes for a constituent.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Notes_index**](../Models/Notes_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1Note"></a>
# **v1Note**
> Notes_show v1Note(id)

Show Note details

    Show details for the note.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Note Id | [default to null] |

### Return type

[**Notes_show**](../Models/Notes_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1Notes"></a>
# **v1Notes**
> Notes_index v1Notes(limit, offset)

Fetch Notes for Account

    Lists all the notes for an account.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Notes_index**](../Models/Notes_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

