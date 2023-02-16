# aitrios_console_rest_client_sdk_primitive.model.deploy_history.DeployHistory

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**current_target** | str,  | str,  | todo | 
**deploy_status** | str,  | str,  | todo | 
**deploy_type** | str,  | str,  | todo | 
**ins_date** | str,  | str,  | todo | 
**upd_id** | str,  | str,  | todo | 
**replace_network_id** | str,  | str,  | todo | 
**config_id** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**upd_date** | str,  | str,  | todo | 
**[model](#model)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | todo | 
**ins_id** | str,  | str,  | todo | 
**[custom_setting](#custom_setting)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**[firmware](#firmware)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**deploy_comment** | str,  | str,  | todo | [optional] 
**total_status** | str,  | str,  | todo | [optional] 
**app_name** | str,  | str,  | todo | [optional] 
**version_number** | str,  | str,  | todo | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# firmware

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sensor_loader_target_flg** | str,  | str,  | todo | [optional] 
**sensor_loader_status** | str,  | str,  | todo | [optional] 
**sensor_loader_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | todo | [optional] 
**sensor_loader_start_date** | str,  | str,  | todo | [optional] 
**sensor_loader_end_date** | str,  | str,  | todo | [optional] 
**sensor_loader_version_number** | str,  | str,  | todo | [optional] 
**sensor_loader_version_comment** | str,  | str,  | todo | [optional] 
**sensor_target_flg** | str,  | str,  | todo | [optional] 
**sensor_status** | str,  | str,  | todo | [optional] 
**sensor_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | todo | [optional] 
**sensor_start_date** | str,  | str,  | todo | [optional] 
**sensor_end_date** | str,  | str,  | todo | [optional] 
**sensor_version_number** | str,  | str,  | todo | [optional] 
**sensor_version_comment** | str,  | str,  | todo | [optional] 
**apfw_target_flg** | str,  | str,  | todo | [optional] 
**apfw_status** | str,  | str,  | todo | [optional] 
**apfw_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | todo | [optional] 
**apfw_start_date** | str,  | str,  | todo | [optional] 
**apfw_end_date** | str,  | str,  | todo | [optional] 
**apfw_version_number** | str,  | str,  | todo | [optional] 
**apfw_version_comment** | str,  | str,  | todo | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**model_target_flg** | str,  | str,  | todo | [optional] 
**model_status** | str,  | str,  | todo | [optional] 
**model_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | todo | [optional] 
**model_start_date** | str,  | str,  | todo | [optional] 
**model_end_date** | str,  | str,  | todo | [optional] 
**model_id** | str,  | str,  | todo | [optional] 
**model_version_number** | str,  | str,  | todo | [optional] 
**model_comment** | str,  | str,  | todo | [optional] 
**model_version_comment** | str,  | str,  | todo | [optional] 
**dnn_param_setting_target_flg** | str,  | str,  | todo | [optional] 
**dnn_param_setting_status** | str,  | str,  | todo | [optional] 
**dnn_param_setting_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | todo | [optional] 
**dnn_param_setting_start_date** | str,  | str,  | todo | [optional] 
**dnn_param_setting_end_date\&quot;** | str,  | str,  | todo | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# custom_setting

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**color_matrix_target_flg** | str,  | str,  | todo | [optional] 
**color_matrix_status** | str,  | str,  | todo | [optional] 
**color_matrix_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | todo | [optional] 
**color_matrix_start_date** | str,  | str,  | todo | [optional] 
**color_matrix_end_date** | str,  | str,  | todo | [optional] 
**color_matrix_mode** | str,  | str,  | todo | [optional] 
**color_matrix_file_name** | str,  | str,  | todo | [optional] 
**color_matrix_comment** | str,  | str,  | todo | [optional] 
**gamma_target_flg** | str,  | str,  | todo | [optional] 
**gamma_status** | str,  | str,  | todo | [optional] 
**gamma_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | todo | [optional] 
**gamma_start_date** | str,  | str,  | todo | [optional] 
**gamma_end_date** | str,  | str,  | todo | [optional] 
**gamma_mode** | str,  | str,  | todo | [optional] 
**gamma_file_name** | str,  | str,  | todo | [optional] 
**gamma_comment** | str,  | str,  | todo | [optional] 
**lscisp_target_flg** | str,  | str,  | todo | [optional] 
**lscisp_status** | str,  | str,  | todo | [optional] 
**lscisp_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | todo | [optional] 
**lscisp_start_date** | str,  | str,  | todo | [optional] 
**lscisp_end_date** | str,  | str,  | todo | [optional] 
**lscisp_mode** | str,  | str,  | todo | [optional] 
**lscisp_file_name** | str,  | str,  | todo | [optional] 
**lscisp_comment** | str,  | str,  | todo | [optional] 
**lscraw_target_flg** | str,  | str,  | todo | [optional] 
**lscraw_status** | str,  | str,  | todo | [optional] 
**lscraw_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | todo | [optional] 
**lscraw_start_date** | str,  | str,  | todo | [optional] 
**lscraw_end_date** | str,  | str,  | todo | [optional] 
**lscraw_mode** | str,  | str,  | todo | [optional] 
**lscraw_file_name** | str,  | str,  | todo | [optional] 
**lscraw_comment** | str,  | str,  | todo | [optional] 
**prewb_target_flg** | str,  | str,  | todo | [optional] 
**prewb_status** | str,  | str,  | todo | [optional] 
**prewb_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | todo | [optional] 
**prewb_start_date** | str,  | str,  | todo | [optional] 
**prewb_end_date** | str,  | str,  | todo | [optional] 
**prewb_mode** | str,  | str,  | todo | [optional] 
**prewb_file_name** | str,  | str,  | todo | [optional] 
**prewb_comment** | str,  | str,  | todo | [optional] 
**dewarp_target_flg** | str,  | str,  | todo | [optional] 
**dewarp_status** | str,  | str,  | todo | [optional] 
**dewarp_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | todo | [optional] 
**dewarp_start_date** | str,  | str,  | todo | [optional] 
**dewarp_end_date** | str,  | str,  | todo | [optional] 
**dewarp_mode** | str,  | str,  | todo | [optional] 
**dewarp_file_name** | str,  | str,  | todo | [optional] 
**dewarp_comment** | str,  | str,  | todo | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

