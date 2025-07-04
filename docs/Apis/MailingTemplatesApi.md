# MailingTemplatesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1MailingTemplates**](MailingTemplatesApi.md#v1MailingTemplates) | **GET** /v1/mailing_templates.json | Fetch Mailing Templates |


<a name="v1MailingTemplates"></a>
# **v1MailingTemplates**
> MailingTemplates_index v1MailingTemplates(mailing\_type\_id, limit, offset)

Fetch Mailing Templates

    Lists all the mailing templates.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **mailing\_type\_id** | **String**| Mailing type ID | [optional] [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**MailingTemplates_index**](../Models/MailingTemplates_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

