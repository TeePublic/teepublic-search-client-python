# swagger_client.TagApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_v1_design_tags**](TagApi.md#get_v1_design_tags) | **GET** /v1/design-tags | Gets tags for a design
[**get_v1_link_graph**](TagApi.md#get_v1_link_graph) | **GET** /v1/link-graph | Retrieves the status of tags considered for our link graph.
[**get_v1_related_tags**](TagApi.md#get_v1_related_tags) | **GET** /v1/related-tags | Gets related tags based on given term(s)
[**get_v1_tag_suggestions**](TagApi.md#get_v1_tag_suggestions) | **GET** /v1/tag-suggestions | Returns a list of tag suggestions based on search prefix.
[**get_v1_tags**](TagApi.md#get_v1_tags) | **GET** /v1/tags | Gets tags data based on name(s)
[**post_v1_design_tags**](TagApi.md#post_v1_design_tags) | **POST** /v1/design-tags | Sets taggings for designs
[**post_v1_link_graph**](TagApi.md#post_v1_link_graph) | **POST** /v1/link-graph | Sets the status of tags considered for our link graph.
[**post_v1_tags**](TagApi.md#post_v1_tags) | **POST** /v1/tags | Sets tags properties


# **get_v1_design_tags**
> DesignTagsResponse get_v1_design_tags(design_id)

Gets tags for a design

Gets tags for a design

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
design_id = 56 # int | Design id to pull tags for

try:
    # Gets tags for a design
    api_response = api_instance.get_v1_design_tags(design_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->get_v1_design_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_id** | **int**| Design id to pull tags for | 

### Return type

[**DesignTagsResponse**](DesignTagsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v1_link_graph**
> LinkGraphResponse get_v1_link_graph(tag_name)

Retrieves the status of tags considered for our link graph.

This endpoint allows a user to view the canonical and duplicate status of tags from the tag deduplication workflow.

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
tag_name = NULL # object | Tag name for which we pull link graph data

try:
    # Retrieves the status of tags considered for our link graph.
    api_response = api_instance.get_v1_link_graph(tag_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->get_v1_link_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | [**object**](.md)| Tag name for which we pull link graph data | 

### Return type

[**LinkGraphResponse**](LinkGraphResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v1_related_tags**
> RelatedTagResponse get_v1_related_tags(tag_list, include_deleted=include_deleted, bucket=bucket)

Gets related tags based on given term(s)

Gets related tags based on given term(s)

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
tag_list = 'tag_list_example' # str | Tag list to pull from related tags from
include_deleted = false # bool | Only return tags that are not soft deleted (optional) (default to false)
bucket = 'default' # str | AB test bucket (optional) (default to default)

try:
    # Gets related tags based on given term(s)
    api_response = api_instance.get_v1_related_tags(tag_list, include_deleted=include_deleted, bucket=bucket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->get_v1_related_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_list** | **str**| Tag list to pull from related tags from | 
 **include_deleted** | **bool**| Only return tags that are not soft deleted | [optional] [default to false]
 **bucket** | **str**| AB test bucket | [optional] [default to default]

### Return type

[**RelatedTagResponse**](RelatedTagResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v1_tag_suggestions**
> AutocompleteResponse get_v1_tag_suggestions(prefix, limit=limit, explain=explain)

Returns a list of tag suggestions based on search prefix.

Returns a list of tag suggestions based on search prefix.

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
prefix = 'prefix_example' # str | search prefix
limit = 6 # int | Number of results to return. (optional) (default to 6)
explain = false # bool | Whether to return explanation of results. (optional) (default to false)

try:
    # Returns a list of tag suggestions based on search prefix.
    api_response = api_instance.get_v1_tag_suggestions(prefix, limit=limit, explain=explain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->get_v1_tag_suggestions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| search prefix | 
 **limit** | **int**| Number of results to return. | [optional] [default to 6]
 **explain** | **bool**| Whether to return explanation of results. | [optional] [default to false]

### Return type

[**AutocompleteResponse**](AutocompleteResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v1_tags**
> TagsResponse get_v1_tags(tag_names_list)

Gets tags data based on name(s)

Gets tags data based on name(s)

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
tag_names_list = 'tag_names_list_example' # str | comma separated list of tag names

try:
    # Gets tags data based on name(s)
    api_response = api_instance.get_v1_tags(tag_names_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->get_v1_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_names_list** | **str**| comma separated list of tag names | 

### Return type

[**TagsResponse**](TagsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v1_design_tags**
> SetDesignsTagsResponse post_v1_design_tags(body)

Sets taggings for designs

Sets taggings for designs

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetDesignsTaggingsRequest() # SetDesignsTaggingsRequest | request body

try:
    # Sets taggings for designs
    api_response = api_instance.post_v1_design_tags(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->post_v1_design_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetDesignsTaggingsRequest**](SetDesignsTaggingsRequest.md)| request body | 

### Return type

[**SetDesignsTagsResponse**](SetDesignsTagsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v1_link_graph**
> SetLinkGraphResponse post_v1_link_graph(body)

Sets the status of tags considered for our link graph.

This endpoint allows a user to edit the canonical and duplicate status of tags from the tag deduplication workflow.

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetLinkGraphRequest() # SetLinkGraphRequest | request body

try:
    # Sets the status of tags considered for our link graph.
    api_response = api_instance.post_v1_link_graph(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->post_v1_link_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetLinkGraphRequest**](SetLinkGraphRequest.md)| request body | 

### Return type

[**SetLinkGraphResponse**](SetLinkGraphResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v1_tags**
> SetTagsResponse post_v1_tags(body)

Sets tags properties

Sets tags properties

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
api_instance = swagger_client.TagApi(swagger_client.ApiClient(configuration))
body = swagger_client.SetTagsRequest() # SetTagsRequest | request body

try:
    # Sets tags properties
    api_response = api_instance.post_v1_tags(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApi->post_v1_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetTagsRequest**](SetTagsRequest.md)| request body | 

### Return type

[**SetTagsResponse**](SetTagsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

