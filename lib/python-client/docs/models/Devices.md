# aitrios_console_rest_client_sdk_primitive.model.devices.Devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | str,  | str,  | Set the device ID. | 
**place** | str,  | str,  | Set the location. | [optional] 
**comment** | str,  | str,  | Set the device description. | [optional] 
**[property](#property)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**device_type** | str,  | str,  | Set the device type. | [optional] 
**display_device_type** | str,  | str,  | Set the display device type. | [optional] 
**ins_id** | str,  | str,  | Set the device author. | [optional] 
**ins_date** | str,  | str,  | Set the date the device was created. | [optional] 
**upd_id** | str,  | str,  | Set the device updater. | [optional] 
**upd_date** | str,  | str,  | Set the date the device was updated. | [optional] 
**connectionState** | str,  | str,  | Set the device connection state. | [optional] 
**lastActivityTime** | str,  | str,  | Set the date the device last connected. | [optional] 
**[models](#models)** | list, tuple,  | tuple,  |  | [optional] 
**[configuration](#configuration)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[state](#state)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[device_groups](#device_groups)** | list, tuple,  | tuple,  |  | [optional] 
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

# models

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
**model_version_id** | str,  | str,  | Set the model version ID. Format: modelid:v1.01 *For model that does not exist in the system, display network_id   Example: 000237 | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# configuration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# state

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# device_groups

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
**device_group_id** | str,  | str,  | Set the device group ID. | 
**device_type** | str,  | str,  | Set the device type. | 
**comment** | str,  | str,  | Set the device group comment. | [optional] 
**ins_id** | str,  | str,  | Set the date the device group was created. | [optional] 
**ins_date** | str,  | str,  | Set the device group author. | [optional] 
**upd_id** | str,  | str,  | Set the device group updater. | [optional] 
**upd_date** | str,  | str,  | Set the date the device group was updated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

