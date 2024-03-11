# aitrios_console_rest_client_sdk_primitive.model.azure.Azure

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Set the storage service type. Specify \&quot;AZURE\&quot; as the value. - Value definition   AZURE | [optional] if omitted the server will use the default value of "AZURE"
**mode** | decimal.Decimal, int,  | decimal.Decimal,  | Set the mode. Specifies the input image, inferences result or both to be streamed. - Value definition   0 : input image only   1 : input image and inference result   2 : inference result only | [optional] if omitted the server will use the default value of 0
**endpoint** | str,  | str,  | Destination Azure Blob Storage endpoint. *Do not specify \&quot;endpoint\&quot;, \&quot;connection_string\&quot;, or \&quot;container_name when returning to the initial value. In the case of the initial value when input image is specified in \&quot;mode\&quot;, it will be streamed within this service and then when inference result is specified in \&quot;mode\&quot;, The settings for inference are deleted. | [optional] 
**connection_string** | str,  | str,  | Connection string for Azure Blob Storage. *When initializing, see the description of \&quot;endpoint\&quot;. | [optional] 
**container_name** | str,  | str,  | Container name of Azure Blob Storage. *When initializing, see the description of \&quot;endpoint\&quot;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

