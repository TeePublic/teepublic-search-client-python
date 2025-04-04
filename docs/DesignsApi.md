# swagger_client.DesignsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_v1_similar_designs**](DesignsApi.md#post_v1_similar_designs) | **POST** /v1/similar-designs | Returns a list of discoverable designs based on a reference design and/or primary tag.


# **post_v1_similar_designs**
> SimilarDesignsResponse post_v1_similar_designs(body)

Returns a list of discoverable designs based on a reference design and/or primary tag.

Returns a list of discoverable designs based on a reference design and/or primary tag.

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
api_instance = swagger_client.DesignsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SimilarDesignsRequestV1() # SimilarDesignsRequestV1 | Similar Designs Request

try:
    # Returns a list of discoverable designs based on a reference design and/or primary tag.
    api_response = api_instance.post_v1_similar_designs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DesignsApi->post_v1_similar_designs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SimilarDesignsRequestV1**](SimilarDesignsRequestV1.md)| Similar Designs Request | 

### Return type

[**SimilarDesignsResponse**](SimilarDesignsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

