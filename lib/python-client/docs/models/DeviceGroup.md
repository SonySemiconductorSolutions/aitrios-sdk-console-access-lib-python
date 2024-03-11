# aitrios_console_rest_client_sdk_primitive.model.device_group.DeviceGroup

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_group_id** | str,  | str,  | Set the device group ID. | [optional] 
**device_type** | str,  | str,  | Set the device type. | [optional] 
**comment** | str,  | str,  | Set the device group comment. | [optional] 
**ins_id** | str,  | str,  | Set the device group author. | [optional] 
**ins_date** | str,  | str,  | Set the date the device group was created. | [optional] 
**upd_id** | str,  | str,  | Set the device group updater. | [optional] 
**upd_date** | str,  | str,  | Set the date the device group was updated. | [optional] 
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
**device_id** | str,  | str,  | Set the device ID. | [optional] 
**[property](#property)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**device_type** | str,  | str,  | Set the device type. | [optional] 
**display_device_type** | str,  | str,  | Set the display device type. | [optional] 
**place** | str,  | str,  | Set the location. | [optional] 
**comment** | str,  | str,  | Set the device comment. | [optional] 
**ins_id** | str,  | str,  | Set the device author. | [optional] 
**ins_date** | str,  | str,  | Set the date the device was created. | [optional] 
**upd_id** | str,  | str,  | Set the device updater. | [optional] 
**upd_date** | str,  | str,  | Set the date the device was updated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# property

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_name** | str,  | str,  | Set the device name. | 
**internal_device_id** | str,  | str,  | Set the internal device id. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

