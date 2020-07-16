# swagger_client.RelatedApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v1_related_search**](RelatedApi.md#get_v1_related_search) | **GET** /v1/related-search | Gets related searches based on given term


# **get_v1_related_search**
> InlineResponse200 get_v1_related_search(search_term)

Gets related searches based on given term

Gets related searches based on given term

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
api_instance = swagger_client.RelatedApi(swagger_client.ApiClient(configuration))
search_term = 'search_term_example' # str | Search term to pull related searches from

try:
    # Gets related searches based on given term
    api_response = api_instance.get_v1_related_search(search_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelatedApi->get_v1_related_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| Search term to pull related searches from | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

