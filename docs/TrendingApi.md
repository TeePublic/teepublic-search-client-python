# swagger_client.TrendingApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_v1_trending_search**](TrendingApi.md#post_v1_trending_search) | **POST** /v1/trending-search | Saves trending search results.


# **post_v1_trending_search**
> post_v1_trending_search(body)

Saves trending search results.

Saves trending search results.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TrendingApi(swagger_client.ApiClient(configuration))
body = swagger_client.TrendingRequest() # TrendingRequest | Trending search request

try:
    # Saves trending search results.
    api_instance.post_v1_trending_search(body)
except ApiException as e:
    print("Exception when calling TrendingApi->post_v1_trending_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrendingRequest**](TrendingRequest.md)| Trending search request | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

