# aitrios_console_rest_client_sdk_primitive.model.model.Model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**model_id** | str,  | str,  | Set the model ID. | [optional] 
**model_type** | str,  | str,  | Set the model type. | [optional] 
**functionality** | str,  | str,  | Set the function descriptions. | [optional] 
**vendor_name** | str,  | str,  | Set the vendor name. | [optional] 
**model_comment** | str,  | str,  | Set the description. | [optional] 
**network_type** | str,  | str,  | Set the network type. | [optional] 
**create_by** | str,  | str,  | Set the create_by. - Value definition   Self: Self-training models   Marketplace: Marketplace purchacing model  | [optional] 
**package_id** | str,  | str,  | Set the marketplace package ID. | [optional] 
**product_id** | str,  | str,  | Set the marketplace product ID. | [optional] 
**metadata_format_id** | str,  | str,  | Set the metadata_format_id. | [optional] 
**[projects](#projects)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# projects

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelProjectOfModel**](ModelProjectOfModel.md) | [**ModelProjectOfModel**](ModelProjectOfModel.md) | [**ModelProjectOfModel**](ModelProjectOfModel.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

