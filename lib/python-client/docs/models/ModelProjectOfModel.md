# aitrios_console_rest_client_sdk_primitive.model.model_project_of_model.ModelProjectOfModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**model_project_name** | str,  | str,  | Set the model project name. | [optional] 
**model_project_id** | str,  | str,  | Set the model project ID. | [optional] 
**model_platform** | str,  | str,  | Set the model platform. | [optional] 
**model_type** | str,  | str,  | Set the model type. | [optional] 
**project_type** | str,  | str,  | Set the project type. | [optional] 
**device_id** | str,  | str,  | Set the device ID | [optional] 
**[versions](#versions)** | list, tuple,  | tuple,  | There must be one subordinate element for this API. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# versions

There must be one subordinate element for this API.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | There must be one subordinate element for this API. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelVersion**](ModelVersion.md) | [**ModelVersion**](ModelVersion.md) | [**ModelVersion**](ModelVersion.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

