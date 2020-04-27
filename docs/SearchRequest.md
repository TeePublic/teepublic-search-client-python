# SearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_terms** | **str** | Search terms. | [optional] 
**sort** | **str** | Sort order | [optional] [default to 'relevance']
**tags_filter** | **list[str]** | Design tags filter. | [optional] 
**product_type** | **str** | product filter | [optional] 
**gender** | **str** | gender filter | [optional] 
**artist_filter** | **list[int]** | artist ids. | [optional] 
**per_page** | **int** | Number of results to return per page. | [optional] [default to 36]
**page_offset** | **int** | Page offset to fetch. | [optional] [default to 1]
**explain** | **bool** | whether to return explanation of search results. | [optional] [default to False]
**es_explain** | **bool** | whether to return elasticsearch explanation of search results. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


