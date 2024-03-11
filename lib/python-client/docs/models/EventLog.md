# aitrios_console_rest_client_sdk_primitive.model.event_log.EventLog

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Set the event ID. | [optional] 
**DeviceID** | str,  | str,  | Set the device ID. | [optional] 
**Level** | str,  | str,  | Set the log level.   Example: Warn, Error | [optional] 
**Component** | str,  | str,  | Set the event component code. | [optional] 
**ErrorCode** | str,  | str,  | Set the error code. | [optional] 
**Description** | str,  | str,  | Set the description. | [optional] 
**Time** | str,  | str,  | Set the event time. | [optional] 
**ingestion_time** | str,  | str,  | Set the event log time ingested in system. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

