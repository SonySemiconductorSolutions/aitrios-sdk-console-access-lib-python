# aitrios_console_rest_client_sdk_primitive.model.model_project.ModelProject

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**model_project_id** | str,  | str,  | Set the model project ID. | 
**model_project_name** | str,  | str,  | Set the model project name. | 
**model_platform** | str,  | str,  | Set the model platform. | [optional] 
**model_type** | str,  | str,  | Set the model type. | [optional] 
**project_type** | str,  | str,  | Set the project type. | [optional] 
**device_id** | str,  | str,  | Set the model device id. | [optional] 
**project_model_file_name** | str,  | str,  | Set the project model filename. | [optional] 
**project_model_accuracy** | str,  | str,  | Set the project model accuracy. | [optional] 
**project_comment** | str,  | str,  | Set the project comment. | [optional] 
**[project](#project)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[model](#model)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# project

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**training_kit_id** | str,  | str,  | Set the training kit id. | [optional] 
**training_kit_name** | str,  | str,  | Set the training kit name. | [optional] 
**description** | str,  | str,  | Set the description. | [optional] 
**iteration_id** | str,  | str,  | Set the iteration id. | [optional] 
**iteration_name** | str,  | str,  | Set the iteration name. | [optional] 
**last_modified** | str,  | str,  | Set the last modified. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**model_id** | str,  | str,  | Set the model ID. | [optional] 
**model_type** | str,  | str,  | Set the device type. | [optional] 
**functionality** | str,  | str,  | Set the function descriptions. | [optional] 
**vendor_name** | str,  | str,  | Set the vendor name. | [optional] 
**model_comment** | str,  | str,  | Set the description. | [optional] 
**create_by** | str,  | str,  | Set the create_by. - Value definition   Self: Self-training models   Marketplace: Marketplace purchacing model  | [optional] 
**package_id** | str,  | str,  | Set the marketplace package ID. | [optional] 
**product_id** | str,  | str,  | Set the marketplace product ID. | [optional] 
**metadata_format_id** | str,  | str,  | Set the metadata_format_id. | [optional] 
**latest_version** | [**ModelVersion**](ModelVersion.md) | [**ModelVersion**](ModelVersion.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

