# swagger_client.SearchApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_v1_search**](SearchApi.md#post_v1_search) | **POST** /v1/search | Returns a list of published designs based on search query.
[**post_v2_search**](SearchApi.md#post_v2_search) | **POST** /v2/search | Returns a list of published designs based on search query.


# **post_v1_search**
> SearchResponse post_v1_search(body)

Returns a list of published designs based on search query.

Returns a list of published designs based on search query.

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.SearchRequest() # SearchRequest | User Search Request

try:
    # Returns a list of published designs based on search query.
    api_response = api_instance.post_v1_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_v1_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)| User Search Request | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_search**
> SearchResponse post_v2_search(body)

Returns a list of published designs based on search query.

Returns a list of published designs based on search query.

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
api_instance = swagger_client.SearchApi(swagger_client.ApiClient(configuration))
body = swagger_client.SearchRequestV2() # SearchRequestV2 | User Search Request

try:
    # Returns a list of published designs based on search query.
    api_response = api_instance.post_v2_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_v2_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequestV2**](SearchRequestV2.md)| User Search Request | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

