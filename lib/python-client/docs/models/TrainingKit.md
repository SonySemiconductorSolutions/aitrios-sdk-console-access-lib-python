# aitrios_console_rest_client_sdk_primitive.model.training_kit.TrainingKit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Set the training kit ID. | [optional] 
**name** | str,  | str,  | Set the training kit name. | [optional] 
**description** | str,  | str,  | Set the tag description. | [optional] 
**created_on** | str,  | str,  | Set the date the training kit was created. | [optional] 
**status** | str,  | str,  | Set the status. | [optional] 
**training_kit_type** | str,  | str,  | Set the training kit type. | [optional] 
**default_dataset_split_percentage** | decimal.Decimal, int, float,  | decimal.Decimal,  | Set the default dataset split percentage. | [optional] 
**[framework](#framework)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**owner** | str,  | str,  | Set the owner. | [optional] 
**is_public** | bool,  | BoolClass,  | Set whether or not to publish. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# framework

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Set the framework name. | [optional] 
**version** | str,  | str,  | Set the framework version. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

