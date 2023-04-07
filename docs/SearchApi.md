# swagger_client.SearchApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_artist_search**](SearchApi.md#post_artist_search) | **POST** /v1/artist-search | Performs search on active designs by artist
[**post_v1_category_search**](SearchApi.md#post_v1_category_search) | **POST** /v1/category-search | Endpoint to retrieve discoverable designs associated with a given category.
[**post_v2_dmca_search**](SearchApi.md#post_v2_dmca_search) | **POST** /v2/dmca-search | Performs search on publishable designs.
[**post_v2_search**](SearchApi.md#post_v2_search) | **POST** /v2/search | Returns a list of discoverable designs based on search query.


# **post_artist_search**
> SearchResponse post_artist_search(body)

Performs search on active designs by artist

Performs search on designs by artist username or slug which are discoverable and non-affiliate

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
body = swagger_client.ArtistSearchRequest() # ArtistSearchRequest | User Search Request

try:
    # Performs search on active designs by artist
    api_response = api_instance.post_artist_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_artist_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ArtistSearchRequest**](ArtistSearchRequest.md)| User Search Request | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v1_category_search**
> SearchResponse post_v1_category_search(body)

Endpoint to retrieve discoverable designs associated with a given category.

Returns a list of discoverable designs associated with a given category.

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
body = swagger_client.CategorySearchRequestV1() # CategorySearchRequestV1 | Request object for category search.

try:
    # Endpoint to retrieve discoverable designs associated with a given category.
    api_response = api_instance.post_v1_category_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_v1_category_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CategorySearchRequestV1**](CategorySearchRequestV1.md)| Request object for category search. | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_dmca_search**
> SearchResponse post_v2_dmca_search(body)

Performs search on publishable designs.

Performs search on publishable designs that have not had a a DMCA takedown. Supports filtering of teepublic approved/unapproved designs.

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
body = swagger_client.DmcaSearchRequestV2() # DmcaSearchRequestV2 | User Search Request

try:
    # Performs search on publishable designs.
    api_response = api_instance.post_v2_dmca_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->post_v2_dmca_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DmcaSearchRequestV2**](DmcaSearchRequestV2.md)| User Search Request | 

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

Returns a list of discoverable designs based on search query.

Returns a list of discoverable designs based on search query.

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
    # Returns a list of discoverable designs based on search query.
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

