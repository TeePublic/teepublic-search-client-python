# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.17
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = swagger_client.AutocompleteApi(swagger_client.ApiClient(configuration))
prefix = 'prefix_example' # str | search prefix
limit = 6 # int | Number of results to return. (optional) (default to 6)
explain = false # bool | Whether to return explanation of results. (optional) (default to false)

try:
    # Returns a list of suggestions based on search prefix.
    api_response = api_instance.get_v1_autocomplete(prefix, limit=limit, explain=explain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutocompleteApi->get_v1_autocomplete: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AutocompleteApi* | [**get_v1_autocomplete**](docs/AutocompleteApi.md#get_v1_autocomplete) | **GET** /v1/autocomplete | Returns a list of suggestions based on search prefix.
*AutocompleteApi* | [**post_v1_autocomplete**](docs/AutocompleteApi.md#post_v1_autocomplete) | **POST** /v1/autocomplete | Returns a list of suggestions based on search prefix.
*LookupApi* | [**get_v1_lookup_by_id**](docs/LookupApi.md#get_v1_lookup_by_id) | **GET** /v1/lookup/{design_id} | Returns a published designs based on id.
*RelatedApi* | [**get_v1_related_search**](docs/RelatedApi.md#get_v1_related_search) | **GET** /v1/related-search | Gets related searches based on given term
*RelevancyApi* | [**delete_v1_relevancy_configuration**](docs/RelevancyApi.md#delete_v1_relevancy_configuration) | **DELETE** /v1/relevancy-configurations/{config_id} | Deletes search relevancy configuration.
*RelevancyApi* | [**get_v1_relevancy_configuration**](docs/RelevancyApi.md#get_v1_relevancy_configuration) | **GET** /v1/relevancy-configurations/{config_id} | Gets a search relevancy configuration.
*RelevancyApi* | [**get_v1_relevancy_configurations**](docs/RelevancyApi.md#get_v1_relevancy_configurations) | **GET** /v1/relevancy-configurations | Gets all relevancy configurations.
*RelevancyApi* | [**post_v1_relevancy_configurations**](docs/RelevancyApi.md#post_v1_relevancy_configurations) | **POST** /v1/relevancy-configurations | Saves search relevancy configuration.
*RelevancyApi* | [**put_v1_relevancy_configuration**](docs/RelevancyApi.md#put_v1_relevancy_configuration) | **PUT** /v1/relevancy-configurations/{config_id} | Updates search relevancy configuration.
*SearchApi* | [**post_v2_dmca_search**](docs/SearchApi.md#post_v2_dmca_search) | **POST** /v2/dmca-search | Performs search on publishable designs.
*SearchApi* | [**post_v2_search**](docs/SearchApi.md#post_v2_search) | **POST** /v2/search | Returns a list of discoverable designs based on search query.
*TagApi* | [**get_v1_design_tags**](docs/TagApi.md#get_v1_design_tags) | **GET** /v1/design-tags | Gets tags for a design
*TagApi* | [**get_v1_related_tags**](docs/TagApi.md#get_v1_related_tags) | **GET** /v1/related-tags | Gets related tags based on given term(s)
*TagApi* | [**get_v1_tag_suggestions**](docs/TagApi.md#get_v1_tag_suggestions) | **GET** /v1/tag-suggestions | Returns a list of tag suggestions based on search prefix.
*TagApi* | [**get_v1_tags**](docs/TagApi.md#get_v1_tags) | **GET** /v1/tags | Gets tags data based on name(s)
*TrendingApi* | [**get_v1_trending_search**](docs/TrendingApi.md#get_v1_trending_search) | **GET** /v1/trending-search | Gets trending search results.
*TrendingApi* | [**post_v1_trending_search**](docs/TrendingApi.md#post_v1_trending_search) | **POST** /v1/trending-search | Saves trending search results.


## Documentation For Models

 - [AutocompleteRequest](docs/AutocompleteRequest.md)
 - [AutocompleteResponse](docs/AutocompleteResponse.md)
 - [AutocompleteSuggestion](docs/AutocompleteSuggestion.md)
 - [Design](docs/Design.md)
 - [DesignSlim](docs/DesignSlim.md)
 - [DesignTagsResponse](docs/DesignTagsResponse.md)
 - [DmcaSearchRequestV2](docs/DmcaSearchRequestV2.md)
 - [EsAutocompleteSuggest](docs/EsAutocompleteSuggest.md)
 - [EsCompletionSuggest](docs/EsCompletionSuggest.md)
 - [EsCompletionSuggestOption](docs/EsCompletionSuggestOption.md)
 - [EsHit](docs/EsHit.md)
 - [EsHits](docs/EsHits.md)
 - [EsLookupResponse](docs/EsLookupResponse.md)
 - [EsSearchResponse](docs/EsSearchResponse.md)
 - [Explain](docs/Explain.md)
 - [RelatedResponse](docs/RelatedResponse.md)
 - [RelatedResult](docs/RelatedResult.md)
 - [RelatedTagObject](docs/RelatedTagObject.md)
 - [RelatedTagResponse](docs/RelatedTagResponse.md)
 - [RelatedTagResult](docs/RelatedTagResult.md)
 - [SearchRequest](docs/SearchRequest.md)
 - [SearchRequestV2](docs/SearchRequestV2.md)
 - [SearchResponse](docs/SearchResponse.md)
 - [TagResult](docs/TagResult.md)
 - [TagsResponse](docs/TagsResponse.md)
 - [TrendingRequest](docs/TrendingRequest.md)
 - [TrendingResult](docs/TrendingResult.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author



