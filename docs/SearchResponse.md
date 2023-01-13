# SearchResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_score** | **float** | max score for search query. | [optional] 
**total** | **int** | total number of documents matching our search criteria. | [optional] 
**explain** | [**Explain**](Explain.md) |  | [optional] 
**dym_suggest** | **str** | did you mean spell suggestion. | [optional] 
**designs** | [**list[DesignSlim]**](DesignSlim.md) | list of designs. | [optional] 
**promoted_filters_suggest** | **list[str]** | List of terms that may be used to further refine the result set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


