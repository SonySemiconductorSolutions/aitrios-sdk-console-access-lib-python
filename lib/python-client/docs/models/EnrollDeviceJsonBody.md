# aitrios_console_rest_client_sdk_primitive.model.enroll_device_json_body.EnrollDeviceJsonBody

EnrollDevice Json Body

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | EnrollDevice Json Body | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_name** | str,  | str,  | Device name. *Max. 255 characters | 
**primary_certificate** | str,  | str,  | X.509 primary certificate (.pem file or .cer file or .crt file) . *Specify the following certificate without the leading and trailing signatures. -----BEGIN CERTIFICATE-----  -----END CERTIFICATE-----  Also, do not include line breaks. | 
**device_type** | str,  | str,  | Device type include \&quot;t3p\&quot;, \&quot;t3w\&quot;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

