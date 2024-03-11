# aitrios_console_rest_client_sdk_primitive.model.fw_operation.FWOperation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ErrorHandling** | str,  | str,  |  | must be one of ["ManualReset", "AutoReboot", ] 
**OperatingMode** | str,  | str,  |  | [optional] must be one of ["Manual", "Periodic", ] if omitted the server will use the default value of "Manual"
**[PeriodicParameter](#PeriodicParameter)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# PeriodicParameter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[UploadInferenceParameter](#UploadInferenceParameter)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**[PrimaryInterval](#PrimaryInterval)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**[SecondaryInterval](#SecondaryInterval)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**NetworkParameter** | str,  | str,  |  | [optional] must be one of ["Save", "DHCP", ] if omitted the server will use the default value of "Save"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# PrimaryInterval

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# SecondaryInterval

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# UploadInferenceParameter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

