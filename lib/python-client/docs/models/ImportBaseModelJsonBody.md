# aitrios_console_rest_client_sdk_primitive.model.import_base_model_json_body.ImportBaseModelJsonBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**model** | str,  | str,  | SAS URI or Presigned URI of the model file. | 
**model_id** | str,  | str,  | Model ID for new registration or version upgrade. Max. 100 characters. | 
**input_format_param** | str,  | str,  | SAS URI or Presigned URI of the input format param file. *Usage: Packager conversion information (image format information). *The json format is an array of objects. Each object contains the following values. &amp;nbsp; - ordinal: Order of DNN input to converter (value range: 0 to 2) &amp;nbsp; - format: Format (\&quot;RGB\&quot; or \&quot;BGR\&quot;) *Example: &amp;nbsp;[{ &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;ordinal\&quot;: 0, &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;format\&quot;: \&quot;RGB\&quot; &amp;nbsp;}, &amp;nbsp;{ &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;ordinal\&quot;: 1, &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;format\&quot;: \&quot;RGB\&quot; &amp;nbsp;}] | [optional] 
**network_config** | str,  | str,  | SAS URI or Presigned URI of the network config file. *Usage: Conversion parameter information of modelconverter. Therefore, it is not necessary to specify when specifying the model before conversion. *Example: &amp;nbsp;{ &amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;Postprocessor\&quot;: { &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;params\&quot;: { &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;background\&quot;: false, &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;scale_factors\&quot;: [ &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;10.0, &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;10.0, &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;5.0, &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;5.0 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;], &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;score_thresh\&quot;: 0.01, &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;max_size_per_class\&quot;: 64, &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;max_total_size\&quot;: 64, &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;clip_window\&quot;: [ &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;0, &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;0, &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;1, &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;1 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;], &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;\&quot;iou_threshold\&quot;: 0.45 &amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;} &amp;nbsp;&amp;nbsp;&amp;nbsp;} &amp;nbsp;} | [optional] 
**converted** | bool,  | BoolClass,  | Specify whether to convert the specified model file. | [optional] if omitted the server will use the default value of False
**vendor_name** | str,  | str,  | Vendor Name. Max. 100 characters. *Specify only when registering a new base model. | [optional] 
**comment** | str,  | str,  | Description. Max. 100 characters. *When saving new, it is set as a description of the model and version. *When saving version-up, it is set as a description of the version. | [optional] 
**network_type** | str,  | str,  | Specify whether or not application is required for the model. - Value definition   0 : Model required application   1 : Model do not required application | [optional] if omitted the server will use the default value of "1"
**metadata_format_id** | str,  | str,  | Metadata Format ID. Max. 100 characters. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
