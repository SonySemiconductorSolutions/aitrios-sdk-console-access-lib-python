# aitrios_console_rest_client_sdk_primitive.model.create_firmware_json_body.CreateFirmwareJsonBody

CreateFirmware API model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CreateFirmware API model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**file_content** | str,  | str,  | Firmware File (BASE64 encoding). | 
**file_name** | str,  | str,  | Firmware filename | 
**version_number** | str,  | str,  | Firmware version number. | 
**firmware_type** | str,  | str,  | Firmware type ID. - Value definition   00: MCU(AppFw)   01: IMX500(Sensor)   02: IMX500(SensorLoader) | 
**comment** | str,  | str,  | Comment. *Max. 100 characters. | [optional] if omitted the server will use the default value of ""
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

