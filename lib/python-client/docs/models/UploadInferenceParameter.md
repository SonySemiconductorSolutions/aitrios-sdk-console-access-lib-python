# aitrios_console_rest_client_sdk_primitive.model.upload_inference_parameter.UploadInferenceParameter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**StorageNameIR** | str,  | str,  | Maximum 64 characters | 
**StorageSubDirectoryPathIR** | str,  | str,  | Maximum 256 characters | 
**UploadMethodIR** | str,  | str,  | Only BlobStorage is supported. | [optional] if omitted the server will use the default value of "BlobStorage"
**PPLParameter** | str,  | str,  | Maximum 1364 characters. Please add base64 Encoding to PPLparameter. | [optional] 
**CropHOffset** | decimal.Decimal, int,  | decimal.Decimal,  | - Value definition   0 ~ 4055 | [optional] if omitted the server will use the default value of 0
**CropVOffset** | decimal.Decimal, int,  | decimal.Decimal,  | - Value definition   0 ~ 3039 | [optional] if omitted the server will use the default value of 0
**CropHSize** | decimal.Decimal, int,  | decimal.Decimal,  | - Value definition   0 ~ 4056 | [optional] if omitted the server will use the default value of 4056
**CropVSize** | decimal.Decimal, int,  | decimal.Decimal,  | - Value definition   0 ~ 3040 | [optional] if omitted the server will use the default value of 3040
**NetworkId** | str,  | str,  | Empty characters are also allowed. The operation in the case of an empty string is as follows. A. If the number of arrays notified by Version.DnnModelVersion is 1 or more, it works with the DNN model of the first element. B. If the number of arrays notified by Version.DnnModelVersion is 0, it will be treated as an invalid parameter, it will sleep immediately, and the next startup will operate in Config mode. - Value definition   \&quot;000000\&quot; ~ \&quot;999999\&quot; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

