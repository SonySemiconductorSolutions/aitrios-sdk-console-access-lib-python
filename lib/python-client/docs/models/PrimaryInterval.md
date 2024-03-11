# aitrios_console_rest_client_sdk_primitive.model.primary_interval.PrimaryInterval

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**BaseTime** | str,  | str,  | Reference time. (Hour: Minute) (Second is fixed at 00) - Value definition   \&quot;00:00\&quot; - \&quot;23:59\&quot; | 
**ConfigInterval** | decimal.Decimal, int,  | decimal.Decimal,  | Interval at which to check for Config updates.Set in minutes.  0 : no Config. - Value definition   5 ~ 1440 :(24 hours) | [optional] if omitted the server will use the default value of 0
**CaptureInterval** | decimal.Decimal, int,  | decimal.Decimal,  | shooting interval. Set in minutes.  0 : no shooting. - Value definition   3 - 1440 :(24 hours) | [optional] if omitted the server will use the default value of 0
**UploadCount** | decimal.Decimal, int,  | decimal.Decimal,  | Primary is fixed at 1 - Value definition   1 | [optional] if omitted the server will use the default value of 1
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

