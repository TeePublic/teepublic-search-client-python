# swagger_client.LookupApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v1_lookup_by_id**](LookupApi.md#get_v1_lookup_by_id) | **GET** /v1/lookup/{design_id} | Returns a published designs based on id.


# **get_v1_lookup_by_id**
> Design get_v1_lookup_by_id(design_id)

Returns a published designs based on id.

Returns a published designs based on id.

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
api_instance = swagger_client.LookupApi(swagger_client.ApiClient(configuration))
design_id = 789 # int | id of the design to return

try:
    # Returns a published designs based on id.
    api_response = api_instance.get_v1_lookup_by_id(design_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LookupApi->get_v1_lookup_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_id** | **int**| id of the design to return | 

### Return type

[**Design**](Design.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

