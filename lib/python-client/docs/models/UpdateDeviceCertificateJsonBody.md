# aitrios_console_rest_client_sdk_primitive.model.update_device_certificate_json_body.UpdateDeviceCertificateJsonBody

UpdateDeviceCertificate Json Body

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | UpdateDeviceCertificate Json Body | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**primary_certificate** | str,  | str,  | Device certificate  X.509 primary certificate (.pem file or .cer file)  *Specify the following certificate without the leading and trailing signatures -----BEGIN CERTIFICATE-----  -----END CERTIFICATE-----  Also, do not include line breaks. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

