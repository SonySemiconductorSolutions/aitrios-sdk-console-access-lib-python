# aitrios_console_rest_client_sdk_primitive.model.deploy_configuration.DeployConfiguration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**success_cnt** | decimal.Decimal, int,  | decimal.Decimal,  | Set the success cnt. | 
**config_comment** | str,  | str,  | Set the config comment. | 
**running_cnt** | decimal.Decimal, int,  | decimal.Decimal,  | Set the running cnt. | 
**device_type** | str,  | str,  | Set the device type. | 
**ins_date** | str,  | str,  | Set the date the deployment was created. | 
**upd_id** | str,  | str,  | Set the deployment updater. | 
**config_id** | str,  | str,  | Set the config ID. | 
**upd_date** | str,  | str,  | Set the date the deployment was updated. | 
**fail_cnt** | decimal.Decimal, int,  | decimal.Decimal,  | Set the fail cnt. | 
**[model](#model)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**ins_id** | str,  | str,  | Set the deployment author. | 
**custom_setting** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**[firmware](#firmware)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# firmware

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sensor_loader_file_name** | str,  | str,  | Set the sensor loader filename. | [optional] 
**sensor_loader_version_number** | str,  | str,  | Set the sensor loader version number. | [optional] 
**sensor_loader_firmware_comment** | str,  | str,  | Set the sensor loader firmware comment. | [optional] 
**sensor_file_name** | str,  | str,  | Set the sensor filename. | [optional] 
**sensor_version_number** | str,  | str,  | Set the sensor version number. | [optional] 
**sensor_firmware_comment** | str,  | str,  | Set the sensor firmware comment. | [optional] 
**apfw_file_name** | str,  | str,  | Set the apfw filename. | [optional] 
**apfw_version_number** | str,  | str,  | Set the apfw version number. | [optional] 
**apfw_firmware_comment** | str,  | str,  | Set the apfw firmware comment. | [optional] 
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
**model_version_number** | str,  | str,  | Set the model version number. | [optional] 
**model_comment** | str,  | str,  | Set the model comment. | [optional] 
**model_version_comment** | str,  | str,  | Set the model version comment. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

