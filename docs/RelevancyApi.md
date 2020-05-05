# swagger_client.RelevancyApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v1_relevancy_configuration**](RelevancyApi.md#delete_v1_relevancy_configuration) | **DELETE** /v1/relevancy-configurations/{config_id} | Deletes search relevancy configuration.
[**get_v1_relevancy_configuration**](RelevancyApi.md#get_v1_relevancy_configuration) | **GET** /v1/relevancy-configurations/{config_id} | Gets a search relevancy configuration.
[**get_v1_relevancy_configurations**](RelevancyApi.md#get_v1_relevancy_configurations) | **GET** /v1/relevancy-configurations | Gets all relevancy configurations.
[**post_v1_relevancy_configurations**](RelevancyApi.md#post_v1_relevancy_configurations) | **POST** /v1/relevancy-configurations | Saves search relevancy configuration.
[**put_v1_relevancy_configuration**](RelevancyApi.md#put_v1_relevancy_configuration) | **PUT** /v1/relevancy-configurations/{config_id} | Updates search relevancy configuration.


# **delete_v1_relevancy_configuration**
> delete_v1_relevancy_configuration(config_id)

Deletes search relevancy configuration.

Deletes search relevancy configuration.

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
api_instance = swagger_client.RelevancyApi(swagger_client.ApiClient(configuration))
config_id = 'config_id_example' # str | search relevancy configuration id

try:
    # Deletes search relevancy configuration.
    api_instance.delete_v1_relevancy_configuration(config_id)
except ApiException as e:
    print("Exception when calling RelevancyApi->delete_v1_relevancy_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| search relevancy configuration id | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v1_relevancy_configuration**
> object get_v1_relevancy_configuration(config_id)

Gets a search relevancy configuration.

Gets a search relevancy configuration.

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
api_instance = swagger_client.RelevancyApi(swagger_client.ApiClient(configuration))
config_id = 'config_id_example' # str | search relevancy configuration id

try:
    # Gets a search relevancy configuration.
    api_response = api_instance.get_v1_relevancy_configuration(config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelevancyApi->get_v1_relevancy_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| search relevancy configuration id | 

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v1_relevancy_configurations**
> list[object] get_v1_relevancy_configurations()

Gets all relevancy configurations.

Gets all relevancy configurations.

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
api_instance = swagger_client.RelevancyApi(swagger_client.ApiClient(configuration))

try:
    # Gets all relevancy configurations.
    api_response = api_instance.get_v1_relevancy_configurations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelevancyApi->get_v1_relevancy_configurations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v1_relevancy_configurations**
> post_v1_relevancy_configurations(body)

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
api_instance = swagger_client.RelevancyApi(swagger_client.ApiClient(configuration))
body = NULL # object | Relevancy Configuration

try:
    # Saves search relevancy configuration.
    api_instance.post_v1_relevancy_configurations(body)
except ApiException as e:
    print("Exception when calling RelevancyApi->post_v1_relevancy_configurations: %s\n" % e)
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

# **put_v1_relevancy_configuration**
> put_v1_relevancy_configuration(config_id, body)

Updates search relevancy configuration.

Updates search relevancy configuration.

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
api_instance = swagger_client.RelevancyApi(swagger_client.ApiClient(configuration))
config_id = 'config_id_example' # str | search relevancy configuration id
body = NULL # object | Relevancy Configuration

try:
    # Updates search relevancy configuration.
    api_instance.put_v1_relevancy_configuration(config_id, body)
except ApiException as e:
    print("Exception when calling RelevancyApi->put_v1_relevancy_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**| search relevancy configuration id | 
 **body** | **object**| Relevancy Configuration | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

