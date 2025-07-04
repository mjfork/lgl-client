# CampaignsApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1Campaigns**](CampaignsApi.md#v1Campaigns) | **GET** /v1/campaigns.json | Fetch Campaigns |


<a name="v1Campaigns"></a>
# **v1Campaigns**
> Campaigns_index v1Campaigns(limit, offset)

Fetch Campaigns

    Lists all the campaigns.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Campaigns_index**](../Models/Campaigns_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

