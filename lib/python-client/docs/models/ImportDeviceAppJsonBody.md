# aitrios_console_rest_client_sdk_primitive.model.import_device_app_json_body.ImportDeviceAppJsonBody

ImportDeviceApp Json Body

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ImportDeviceApp Json Body | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**app_name** | str,  | str,  | App name | 
**file_content** | str,  | str,  | File content | 
**compiled_flg** | str,  | str,  | Compiled flg(0:not compiled, 1:Compiled) | 
**file_name** | str,  | str,  | FileName | 
**version_number** | str,  | str,  | App version number123 | 
**entry_point** | str,  | str,  | App entry point | [optional] if omitted the server will use the default value of "ppl"
**comment** | str,  | str,  | Comment | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

