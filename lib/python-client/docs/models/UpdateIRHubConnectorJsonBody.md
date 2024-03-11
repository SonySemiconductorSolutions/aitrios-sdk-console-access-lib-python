# aitrios_console_rest_client_sdk_primitive.model.update_ir_hub_connector_json_body.UpdateIRHubConnectorJsonBody

UpdateIRHubConnector JsonBody.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | UpdateIRHubConnector JsonBody. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**url** | str,  | str,  | Connection string for Azure Event Hubs forwarding inference result. *Do not specify when returning to the initial value. In the case of the initial value, it will be streamed within this service. | [optional] 
**name** | str,  | str,  | Azure Event Hubs namespace. *Do not specify when returning to the initial value. In the case of the initial value, it will be streamed within this service. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

