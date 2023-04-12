# CategorySearchRequestV1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **list[str]** | list of categories to apply to the search algorithm | [optional] 
**sort** | **str** | ranking algorithm to apply | [optional] [default to 'relevance']
**canvas** | **str** | filter for document availability on products | [optional] 
**per_page** | **int** | number of results to return per page | [optional] [default to 36]
**page_offset** | **int** | number of hits to skip | [optional] [default to 1]
**safe_search** | **bool** | whether we include mature designs in search results | [optional] [default to True]
**bucket** | **str** | AB test bucket | [optional] 
**explain** | **bool** | whether to return an Elaticsearch explanation of search results | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


