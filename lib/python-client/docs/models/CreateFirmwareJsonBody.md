# aitrios_console_rest_client_sdk_primitive.model.create_firmware_json_body.CreateFirmwareJsonBody

CreateFirmware API model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CreateFirmware API model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**firmware_type** | str,  | str,  | Firmware Type | [optional] if omitted the server will use the default value of ""
**version_number** | str,  | str,  | Version Number | [optional] if omitted the server will use the default value of ""
**comment** | str,  | str,  | Comment | [optional] if omitted the server will use the default value of ""
**file_name** | str,  | str,  | FileName | [optional] if omitted the server will use the default value of ""
**file_content** | str,  | str,  | File Content | [optional] if omitted the server will use the default value of ""
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

