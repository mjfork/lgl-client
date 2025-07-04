# CategoriesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lglApiV1CategoriesCreate**](CategoriesApi.md#lglApiV1CategoriesCreate) | **POST** /v1/categories.json | Create new Category |
| [**lglApiV1CategoriesDestroy**](CategoriesApi.md#lglApiV1CategoriesDestroy) | **DELETE** /v1/categories/{id}.json | Delete Category |
| [**lglApiV1CategoriesUpdate**](CategoriesApi.md#lglApiV1CategoriesUpdate) | **PATCH** /v1/categories/{id}.json | Update Category |
| [**v1Categories**](CategoriesApi.md#v1Categories) | **GET** /v1/categories.json | Fetch Categories for Account |
| [**v1Category**](CategoriesApi.md#v1Category) | **GET** /v1/categories/{id}.json | Show Category details |
| [**v1ConstituentCategories**](CategoriesApi.md#v1ConstituentCategories) | **GET** /v1/constituents/{constituent_id}/categories.json | Fetch Categories for Constituent |


<a name="lglApiV1CategoriesCreate"></a>
# **lglApiV1CategoriesCreate**
> Categories_show lglApiV1CategoriesCreate(body)

Create new Category

    Add a category to an account.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateBody**](../Models/CreateBody.md)| Create Objects | |

### Return type

[**Categories_show**](../Models/Categories_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="lglApiV1CategoriesDestroy"></a>
# **lglApiV1CategoriesDestroy**
> lglApiV1CategoriesDestroy(id)

Delete Category

    Delete the category.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Category Id | [default to null] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="lglApiV1CategoriesUpdate"></a>
# **lglApiV1CategoriesUpdate**
> Categories_show lglApiV1CategoriesUpdate(id, body)

Update Category

    Update the category.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Category Id | [default to null] |
| **body** | [**UpdateBody**](../Models/UpdateBody.md)| Update Objects | |

### Return type

[**Categories_show**](../Models/Categories_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: */*

<a name="v1Categories"></a>
# **v1Categories**
> Categories_index v1Categories(item\_type, limit, offset)

Fetch Categories for Account

    Lists all the categories for an account.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **item\_type** | **String**| Categories for type (default: Constituent). Available: Constituent, Gift, VolunteerTime | [optional] [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Categories_index**](../Models/Categories_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1Category"></a>
# **v1Category**
> Categories_show v1Category(id)

Show Category details

    Show details for the category.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Category Id | [default to null] |

### Return type

[**Categories_show**](../Models/Categories_show.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

<a name="v1ConstituentCategories"></a>
# **v1ConstituentCategories**
> Categories_index v1ConstituentCategories(constituent\_id, limit, offset)

Fetch Categories for Constituent

    Lists all the categories for a constituent.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **constituent\_id** | **Integer**| Constituent Id | [default to null] |
| **limit** | **Integer**| Number of entries to return. Default: 25 | [optional] [default to 25] |
| **offset** | **Integer**| Start at given entry. Default: 0 | [optional] [default to 0] |

### Return type

[**Categories_index**](../Models/Categories_index.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyQuery](../README.md#ApiKeyQuery), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

