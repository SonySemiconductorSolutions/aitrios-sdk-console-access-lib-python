# aitrios_console_rest_client_sdk_primitive.model.deploy_history.DeployHistory

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ins_date** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**upd_id** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**replace_network_id** | str,  | str,  | Set the replace network ID. | 
**current_target** | str,  | str,  | Set the current target. | 
**upd_date** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**model** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Deploy ID. | 
**deploy_status** | str,  | str,  | Set the deploy status. *Target device deployment status. - Value definition   0: Deploying   1: Success   2: Fail   3: Cancel   App: DeviceApp undeploy | 
**deploy_type** | str,  | str,  | Set the deploy type. - Value definition   0: Deploy config   1: Device Model   App: DeviceApp | 
**ins_id** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**custom_setting** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**[firmware](#firmware)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**update_progress** | str,  | str,  | Set the update progress in percentage. | [optional] 
**deploy_comment** | str,  | str,  | Set the deploy comment. | [optional] 
**config_id** | str,  | str,  | Set the deploy config ID. | [optional] 
**total_status** | str,  | str,  | Set the deploy status. *Total status of devices deployed together. - Value definition   0: Deploying   1: Success   2: Fail   3: Cancel | [optional] 
**app_name** | str,  | str,  | Set the app name. | [optional] 
**version_number** | str,  | str,  | Set the version number. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# firmware

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sensor_loader_target_flg** | str,  | str,  | Set the deploy target flg. - Value definition   0: Not for deployment   1: Deployment target | [optional] 
**sensor_loader_status** | str,  | str,  | Set the deploy status. - Value definition   0: Waiting   1: Deploying   2: Success   3: Fail | [optional] 
**sensor_loader_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | Set the sensor loader retry count. | [optional] 
**sensor_loader_start_date** | str,  | str,  | Set the sensor loader start date. | [optional] 
**sensor_loader_end_date** | str,  | str,  | Set the sensor loader end date. | [optional] 
**sensor_loader_version_number** | str,  | str,  | Set the sensor loader version number. | [optional] 
**sensor_loader_version_comment** | str,  | str,  | Set the sensor loader version comment. | [optional] 
**sensor_target_flg** | str,  | str,  | Set the deploy target flg. - Value definition   0: Not for deployment   1: Deployment target | [optional] 
**sensor_status** | str,  | str,  | Set the deploy status. - Value definition   0: Waiting   1: Deploying   2: Success   3: Fail | [optional] 
**sensor_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | Set the sensor retry count. | [optional] 
**sensor_start_date** | str,  | str,  | Set the sensor start date. | [optional] 
**sensor_end_date** | str,  | str,  | Set the sensor end date. | [optional] 
**sensor_version_number** | str,  | str,  | Set the sensor version number. | [optional] 
**sensor_version_comment** | str,  | str,  | Set the sensor version comment. | [optional] 
**apfw_target_flg** | str,  | str,  | Set the deploy target flg. - Value definition   0: Not for deployment   1: Deployment target | [optional] 
**apfw_status** | str,  | str,  | Set the deploy status. - Value definition   0: Waiting   1: Deploying   2: Success   3: Fail | [optional] 
**apfw_retry_count** | decimal.Decimal, int,  | decimal.Decimal,  | Set the appfw retry count. | [optional] 
**apfw_start_date** | str,  | str,  | Set the appfw start date. | [optional] 
**apfw_end_date** | str,  | str,  | Set the appfw end date. | [optional] 
**apfw_version_number** | str,  | str,  | Set the appfw version number. | [optional] 
**apfw_version_comment** | str,  | str,  | Set the appfw version comment. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

