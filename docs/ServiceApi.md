# swagger_client.ServiceApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthcheck_get**](ServiceApi.md#healthcheck_get) | **GET** /healthcheck | Check if the service is running


# **healthcheck_get**
> healthcheck_get()

Check if the service is running

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceApi()

try:
    # Check if the service is running
    api_instance.healthcheck_get()
except ApiException as e:
    print("Exception when calling ServiceApi->healthcheck_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

