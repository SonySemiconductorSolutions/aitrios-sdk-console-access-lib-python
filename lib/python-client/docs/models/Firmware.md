# aitrios_console_rest_client_sdk_primitive.model.firmware.Firmware

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**firmware_id** | str,  | str,  | Set the firmware ID. | [optional] 
**firmware_type** | str,  | str,  | Set the firmware type. | [optional] 
**comment** | str,  | str,  | Set the firmware description. | [optional] 
**ins_id** | str,  | str,  | Set the firmware author. | [optional] 
**ins_date** | str,  | str,  | Set the date the firmware was created. | [optional] 
**upd_id** | str,  | str,  | Set the firmware updater. | [optional] 
**upd_date** | str,  | str,  | Set the date the firmware was updated. | [optional] 
**[versions](#versions)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# versions

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
**file_name** | str,  | str,  | Set the firmware filename. | [optional] 
**version_number** | str,  | str,  | Set the version number. | [optional] 
**ppl** | str,  | str,  | Set the ppl information. | [optional] 
**stored_type** | str,  | str,  | Set the storage location type. | [optional] 
**stored_uri** | str,  | str,  | Set the storage location URI. | [optional] 
**comment** | str,  | str,  | Set the firmware description. | [optional] 
**ins_id** | str,  | str,  | Set the firmware author. | [optional] 
**ins_date** | str,  | str,  | Set the date the firmware was created. | [optional] 
**upd_id** | str,  | str,  | Set the firmware updater. | [optional] 
**upd_date** | str,  | str,  | Set the date the firmware was updated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

