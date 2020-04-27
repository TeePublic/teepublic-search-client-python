# swagger_client.AdminApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_v1_admin_relevancy**](AdminApi.md#post_v1_admin_relevancy) | **POST** /v1/admin/relevancy | Saves search relevancy configuration.


# **post_v1_admin_relevancy**
> post_v1_admin_relevancy(body)

Saves search relevancy configuration.

Saves search relevancy configuration.

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
api_instance = swagger_client.AdminApi(swagger_client.ApiClient(configuration))
body = NULL # object | Relevancy Configuration

try:
    # Saves search relevancy configuration.
    api_instance.post_v1_admin_relevancy(body)
except ApiException as e:
    print("Exception when calling AdminApi->post_v1_admin_relevancy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Relevancy Configuration | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

