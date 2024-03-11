# aitrios_console_rest_client_sdk_primitive.model.aws.AWS

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_key_id** | str,  | str,  | AWS Access key ID. | 
**endpoint** | str,  | str,  | Destination AWS S3 endpoint. | 
**bucket_name** | str,  | str,  | AWS S3 Bucket name. | 
**secret_access_key** | str,  | str,  | AWS Secret Access key. | 
**region** | str,  | str,  | AWS Region. *Need to choose from the official list. | 
**type** | str,  | str,  | Set the storage service type. Specify \&quot;AWS\&quot; as the value. - Value definition   AWS | 
**mode** | decimal.Decimal, int,  | decimal.Decimal,  | Set the mode. Specifies the input image , inference result or both to be streamed. - Value definition   0 : input image only   1 : input image and inference result   2 : inference result only | [optional] if omitted the server will use the default value of 0
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

