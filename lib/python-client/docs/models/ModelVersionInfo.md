# aitrios_console_rest_client_sdk_primitive.model.model_version_info.ModelVersionInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**version_number** | str,  | str,  | Set the version number. | [optional] 
**iteration_id** | str,  | str,  | Set the iteration ID. | [optional] 
**iteration_name** | str,  | str,  | Set the iteration name. | [optional] 
**accuracy** | str,  | str,  | Set the accuracy. | [optional] 
**[model_performances](#model_performances)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Set the the performance information of the model. | [optional] 
**latest_flg** | str,  | str,  | Set the latest flag. | [optional] 
**publish_latest_flg** | str,  | str,  | Set the latest published flag. | [optional] 
**version_status** | str,  | str,  | Set the status. | [optional] 
**org_file_name** | str,  | str,  | Set the preconversion model filename. | [optional] 
**org_file_size** | decimal.Decimal, int,  | decimal.Decimal,  | Set the publish model file size. | [optional] 
**publish_file_name** | str,  | str,  | Set the publish model filename. | [optional] 
**publish_file_size** | decimal.Decimal, int,  | decimal.Decimal,  | Set the publish model file size. | [optional] 
**model_file_size** | decimal.Decimal, int,  | decimal.Decimal,  | Set the model file size. | [optional] 
**model_framework** | str,  | str,  | Set the model framework. | [optional] 
**conv_id** | str,  | str,  | Set the conversion request ID. | [optional] 
**[labels](#labels)** | list, tuple,  | tuple,  | Set the label array. | [optional] 
**stage** | str,  | str,  | Set the conversion stage. | [optional] 
**result** | str,  | str,  | Set the conversion result. | [optional] 
**[kpi](#kpi)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[converter_log](#converter_log)** | list, tuple,  | tuple,  | converter log. | [optional] 
**convert_start_date** | str,  | str,  | Set the conversion start date. | [optional] 
**convert_end_date** | str,  | str,  | Set the conversion end date. | [optional] 
**publish_start_date** | str,  | str,  | Set the publish start date. | [optional] 
**publish_end_date** | str,  | str,  | Set the publish end date. | [optional] 
**version_comment** | str,  | str,  | Set the description. | [optional] 
**version_ins_date** | str,  | str,  | Set the the created time of the version. | [optional] 
**version_upd_date** | str,  | str,  | Set the the created time of the version. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# model_performances

Set the the performance information of the model.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Set the the performance information of the model. | 

# labels

Set the label array.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Set the label array. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# kpi

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# converter_log

converter log.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | converter log. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

