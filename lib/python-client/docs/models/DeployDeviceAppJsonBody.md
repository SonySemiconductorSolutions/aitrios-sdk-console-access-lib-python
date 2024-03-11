# aitrios_console_rest_client_sdk_primitive.model.deploy_device_app_json_body.DeployDeviceAppJsonBody

DeployDeviceApp Json Body

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DeployDeviceApp Json Body | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**app_name** | str,  | str,  | App name. | 
**version_number** | str,  | str,  | App version number. | 
**device_ids** | str,  | str,  | Specify multiple device IDs separated by commas. | 
**comment** | str,  | str,  | Comment. *Max. 100 characters. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

