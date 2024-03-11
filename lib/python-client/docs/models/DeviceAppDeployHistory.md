# aitrios_console_rest_client_sdk_primitive.model.device_app_deploy_history.DeviceAppDeployHistory

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int, float,  | decimal.Decimal,  | Set the deploy id. | [optional] 
**total_status** | str,  | str,  | Set the total status. - Value definition   0: Running   1: Successfully completed   2: Failed   3: Canceled  | [optional] 
**deploy_parameter** | str,  | str,  | Set the deploy parameter. | [optional] 
**[devices](#devices)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | str,  | str,  | Set the device id. | [optional] 
**status** | str,  | str,  | Set the total status. - Value definition   0: Running   1: Successfully completed   2: Failed   3: Canceled  | [optional] 
**latest_deployment_flg** | str,  | str,  | Set the deployment flg. - Value definition   0: Old deployment history   1: Recent deployment history  | [optional] 
**ins_id** | str,  | str,  | Set the settings author. | [optional] 
**ins_date** | str,  | str,  | Set the date the settings were created. | [optional] 
**upd_id** | str,  | str,  | Set the settings updater. | [optional] 
**upd_date** | str,  | str,  | Set the date the settings were updated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

