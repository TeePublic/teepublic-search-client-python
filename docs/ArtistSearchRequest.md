# ArtistSearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artist_query** | **str** | Search terms. | [optional] 
**sort** | **str** | Sort order | [optional] [default to 'relevance']
**canvases** | **list[str]** | product filter | [optional] 
**per_page** | **int** | Number of results to return per page. | [optional] [default to 36]
**page_offset** | **int** | Page offset to fetch. | [optional] [default to 1]
**explain** | **bool** | whether to return explanation of search results. | [optional] [default to False]
**es_explain** | **bool** | whether to return elasticsearch explanation of search results. | [optional] [default to False]
**bucket** | **str** | AB test bucket. | [optional] 
**safe_search** | **bool** | whether we include mature designs in search results. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


