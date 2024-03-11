# aitrios_console_rest_client_sdk_primitive.model.set_image_configuration_json_body.SetImageConfigurationJsonBody

SetImageConfiguration JsonBody.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | SetImageConfiguration JsonBody. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**frame_rate** | decimal.Decimal, int,  | decimal.Decimal,  | Set the frame rate. *Set an integer value multiplied by 100 for the frame rate that comes up from the sensor. The maximum value of the frame rate depends on the value of DriveMode (see the Drive mode spec of drive_mode parameters for details). - Value definition   99   499   999   1248   1498   1998   2497   2997 | [optional] if omitted the server will use the default value of 2997
**drive_mode** | decimal.Decimal, int,  | decimal.Decimal,  | Set the drive mode. - Value definition   1   2   3   4 - Drive mode spec   &lt;table&gt;     &lt;thead&gt;       &lt;tr&gt;         &lt;th&gt;Mode&lt;/th&gt;         &lt;th&gt;Binning&lt;/th&gt;         &lt;th&gt;Scale&lt;/th&gt;         &lt;th&gt;Crop&lt;/th&gt;         &lt;th&gt;Raw Size&lt;/th&gt;         &lt;th&gt;Max Frame Rate&lt;/th&gt;       &lt;/tr&gt;     &lt;/thead&gt;     &lt;tbody&gt;       &lt;tr&gt;         &lt;td&gt;1&lt;/td&gt;         &lt;td&gt;On&lt;/td&gt;         &lt;td&gt;-&lt;/td&gt;         &lt;td&gt;-&lt;/td&gt;         &lt;td&gt;2028x1520&lt;/td&gt;         &lt;td&gt;30(29.97)fps&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;         &lt;td&gt;2&lt;/td&gt;         &lt;td&gt;Off&lt;/td&gt;         &lt;td&gt;On&lt;/td&gt;         &lt;td&gt;-&lt;/td&gt;         &lt;td&gt;2028x1520&lt;/td&gt;         &lt;td&gt;20(19.98)fps&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;         &lt;td&gt;3&lt;/td&gt;         &lt;td&gt;Off&lt;/td&gt;         &lt;td&gt;Off&lt;/td&gt;         &lt;td&gt;On&lt;/td&gt;         &lt;td&gt;2028x1520&lt;/td&gt;         &lt;td&gt;20(19.98)fps&lt;/td&gt;       &lt;/tr&gt;       &lt;tr&gt;         &lt;td&gt;4&lt;/td&gt;         &lt;td&gt;Off&lt;/td&gt;         &lt;td&gt;Off&lt;/td&gt;         &lt;td&gt;Off&lt;/td&gt;         &lt;td&gt;4056x3040&lt;/td&gt;         &lt;td&gt;10(9.99)fps&lt;/td&gt;       &lt;/tr&gt;     &lt;/tbody&gt;   &lt;/table&gt; | [optional] if omitted the server will use the default value of 1
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

