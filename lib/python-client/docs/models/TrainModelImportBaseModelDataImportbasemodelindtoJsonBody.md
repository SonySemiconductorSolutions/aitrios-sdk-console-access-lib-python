# aitrios_console_rest_client_sdk_primitive.model.train_model_import_base_model_data_importbasemodelindto_json_body.TrainModelImportBaseModelDataImportbasemodelindtoJsonBody

ImportBaseModel API json_body class.  Attributes: ---------- model_id(str): model_id. url(str): url. model(str): model file name. converted(bool): converted flag. vendor_name(str): vendor_name. comment(str): comment. network_parameter(str): network_parameter file name. network_config(str): network_config file name. network_type(str): network type. labels(str): labels.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ImportBaseModel API json_body class.  Attributes: ---------- model_id(str): model_id. url(str): url. model(str): model file name. converted(bool): converted flag. vendor_name(str): vendor_name. comment(str): comment. network_parameter(str): network_parameter file name. network_config(str): network_config file name. network_type(str): network type. labels(str): labels. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**model_id** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**model** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**converted** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**vendor_name** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**comment** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**network_parameter** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**network_config** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**network_type** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**[labels](#labels)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

