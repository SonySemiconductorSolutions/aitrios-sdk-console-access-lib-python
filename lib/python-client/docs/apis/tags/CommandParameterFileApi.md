<a id="__pageTop"></a>
# aitrios_console_rest_client_sdk_primitive.apis.tags.command_parameter_file_api.CommandParameterFileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bind_command_parameter_file_to_device**](#bind_command_parameter_file_to_device) | **put** /devices/configuration/command_parameter_files/{file_name} | BindCommandParameterFileToDevice
[**get_command_parameter_file**](#get_command_parameter_file) | **get** /command_parameter_files | GetCommandParameterFile
[**regist_command_parameter_file**](#regist_command_parameter_file) | **post** /command_parameter_files | RegistCommandParameterFile
[**unbind_command_parameter_file**](#unbind_command_parameter_file) | **delete** /devices/configuration/command_parameter_files/{file_name} | UnbindCommandParameterFile
[**update_command_parameter_file**](#update_command_parameter_file) | **patch** /command_parameter_files/{file_name} | UpdateCommandParameterFile

# **bind_command_parameter_file_to_device**
<a id="bind_command_parameter_file_to_device"></a>
> SuccessResponse bind_command_parameter_file_to_device(file_namebind_command_parameter_file_to_device_json_body)

BindCommandParameterFileToDevice

Bind command parameter file to device.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import command_parameter_file_api
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.success_response import SuccessResponse
from aitrios_console_rest_client_sdk_primitive.model.bind_command_parameter_file_to_device_json_body import BindCommandParameterFileToDeviceJsonBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with aitrios_console_rest_client_sdk_primitive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = command_parameter_file_api.CommandParameterFileApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'file_name': "file_name_example",
    }
    query_params = {
    }
    body = BindCommandParameterFileToDeviceJsonBody(
        device_ids="device_ids_example",
    )
    try:
        # BindCommandParameterFileToDevice
        api_response = api_instance.bind_command_parameter_file_to_device(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling CommandParameterFileApi->bind_command_parameter_file_to_device: %s\n" % e)

    # example passing only optional values
    path_params = {
        'file_name': "file_name_example",
    }
    query_params = {
        'grant_type': "client_credentials",
    }
    body = BindCommandParameterFileToDeviceJsonBody(
        device_ids="device_ids_example",
    )
    try:
        # BindCommandParameterFileToDevice
        api_response = api_instance.bind_command_parameter_file_to_device(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling CommandParameterFileApi->bind_command_parameter_file_to_device: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BindCommandParameterFileToDeviceJsonBody**](../../models/BindCommandParameterFileToDeviceJsonBody.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
grant_type | GrantTypeSchema | | optional


# GrantTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "client_credentials"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
file_name | FileNameSchema | | 

# FileNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#bind_command_parameter_file_to_device.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#bind_command_parameter_file_to_device.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#bind_command_parameter_file_to_device.ApiResponseFor401) | Authorization Error
500 | [ApiResponseFor500](#bind_command_parameter_file_to_device.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#bind_command_parameter_file_to_device.ApiResponseFor503) | Service Unavailable

#### bind_command_parameter_file_to_device.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResponse**](../../models/SuccessResponse.md) |  | 


#### bind_command_parameter_file_to_device.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### bind_command_parameter_file_to_device.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### bind_command_parameter_file_to_device.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### bind_command_parameter_file_to_device.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_command_parameter_file**
<a id="get_command_parameter_file"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_command_parameter_file()

GetCommandParameterFile

Get the command parameter file list information..

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import command_parameter_file_api
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with aitrios_console_rest_client_sdk_primitive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = command_parameter_file_api.CommandParameterFileApi(api_client)

    # example passing only optional values
    query_params = {
        'grant_type': "client_credentials",
    }
    try:
        # GetCommandParameterFile
        api_response = api_instance.get_command_parameter_file(
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling CommandParameterFileApi->get_command_parameter_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
grant_type | GrantTypeSchema | | optional


# GrantTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "client_credentials"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_command_parameter_file.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#get_command_parameter_file.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#get_command_parameter_file.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#get_command_parameter_file.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_command_parameter_file.ApiResponseFor503) | Service Unavailable

#### get_command_parameter_file.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[parameter_list](#parameter_list)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# parameter_list

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ins_date** | str,  | str,  | Set the date the settings were created. | 
**upd_id** | str,  | str,  | Set the settings updater. | 
**upd_date** | str,  | str,  | Set the date the settings were updated. | 
**file_name** | str,  | str,  | Name of file | 
**[parameter](#parameter)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Setting value. json | 
**isdefault** | str,  | str,  | True: Default parameter; False: Not default | 
**ins_id** | str,  | str,  | Set the settings author. | 
**comment** | str,  | str,  | Comment | [optional] 
**[device_ids](#device_ids)** | list, tuple,  | tuple,  | Target device list. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# parameter

Setting value. json

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Setting value. json | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[commands](#commands)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# commands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**command_name** | str,  | str,  | Command name. | 
**[parameters](#parameters)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# parameters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Mode** | decimal.Decimal, int,  | decimal.Decimal,  | Collection mode. - Value definition   0 : Input Image only   1 : Input Image &amp; Inference Result   2 : Inference Result only | [optional] 
**UploadMethod** | str,  | str,  | It specifies how to upload Input Image. - Value definition   BlobStorage | [optional] 
**FileFormat** | str,  | str,  | Image file format. - Value definition   JPG   BMP | [optional] 
**UploadMethodIR** | str,  | str,  | It specifies how to Inference Result. - Value definition   Mqtt | [optional] 
**CropHOffset** | decimal.Decimal, int,  | decimal.Decimal,  | Hoffset for Image crop. - Value range : 0 to 4055 | [optional] 
**CropVOffset** | decimal.Decimal, int,  | decimal.Decimal,  | Hoffset for Image crop. - Value range : 0 to 3039 | [optional] 
**CropHSize** | decimal.Decimal, int,  | decimal.Decimal,  | Hoffset for Image crop. - Value range : 0 to 4056 | [optional] 
**CropVSize** | decimal.Decimal, int,  | decimal.Decimal,  | Hoffset for Image crop. - Value range : 0 to 3040 | [optional] 
**NumberOfImages** | decimal.Decimal, int,  | decimal.Decimal,  | Number of images to fetch(Input Image). When it is 0, continue fetching images until stop instruction is mentioned explicitly. - Value range : 0 to 10000 | [optional] 
**UploadInterval** | decimal.Decimal, int,  | decimal.Decimal,  | Upload interval. - Value range : 1 to 2592000 *If 60 is specified, 0.5FPS (&#x3D;30/60) | [optional] 
**NumberOfInferencesPerMessage** | decimal.Decimal, int,  | decimal.Decimal,  | Number of inference results to include in one message (Inference Result). - Value range : 1  to 100 | [optional] 
**MaxDetectionsPerFrame** | decimal.Decimal, int,  | decimal.Decimal,  | No. of Objects included in 1 frame with respect to the Inference results metadata. - Value range : 1 to 5 | [optional] 
**ModelId** | str,  | str,  | Model ID. | [optional] 
**[PPLParameter](#PPLParameter)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | PPL parameter | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# PPLParameter

PPL parameter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PPL parameter | 

# device_ids

Target device list.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Target device list. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### get_command_parameter_file.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_command_parameter_file.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_command_parameter_file.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_command_parameter_file.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **regist_command_parameter_file**
<a id="regist_command_parameter_file"></a>
> SuccessResponse regist_command_parameter_file(regist_command_parameter_file_body)

RegistCommandParameterFile

Register CommandParameterFile.  This API can be used to register the following API parameters in advance: - StartUploadInferenceData API  The following are the APIs for file management and application to the device:  < Parameter file management > - RegistCommandParameterFile API - GetCommandParameterFile API - UpdateCommandParameterFile API - DeleteCommandParameterFile API  < Bind to/Unbind from device > - BindCommandParameterFileToDevice API - UnbindCommandParameterFile API  If the parameter file is not applied to the device, operate using the default value. APIs with required parameters will result in an error when the API is executed. The default file can be specified using the following API: - SetDefaultCommandParameterFile API

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import command_parameter_file_api
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.success_response import SuccessResponse
from aitrios_console_rest_client_sdk_primitive.model.regist_command_parameter_file_body import RegistCommandParameterFileBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with aitrios_console_rest_client_sdk_primitive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = command_parameter_file_api.CommandParameterFileApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = RegistCommandParameterFileBody(
        file_name="file_name_example",
        parameter="parameter_example",
        comment="comment_example",
    )
    try:
        # RegistCommandParameterFile
        api_response = api_instance.regist_command_parameter_file(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling CommandParameterFileApi->regist_command_parameter_file: %s\n" % e)

    # example passing only optional values
    query_params = {
        'grant_type': "client_credentials",
    }
    body = RegistCommandParameterFileBody(
        file_name="file_name_example",
        parameter="parameter_example",
        comment="comment_example",
    )
    try:
        # RegistCommandParameterFile
        api_response = api_instance.regist_command_parameter_file(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling CommandParameterFileApi->regist_command_parameter_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RegistCommandParameterFileBody**](../../models/RegistCommandParameterFileBody.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
grant_type | GrantTypeSchema | | optional


# GrantTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "client_credentials"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#regist_command_parameter_file.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#regist_command_parameter_file.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#regist_command_parameter_file.ApiResponseFor401) | Authorization Error
500 | [ApiResponseFor500](#regist_command_parameter_file.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#regist_command_parameter_file.ApiResponseFor503) | Service Unavailable

#### regist_command_parameter_file.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResponse**](../../models/SuccessResponse.md) |  | 


#### regist_command_parameter_file.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### regist_command_parameter_file.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### regist_command_parameter_file.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### regist_command_parameter_file.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **unbind_command_parameter_file**
<a id="unbind_command_parameter_file"></a>
> SuccessResponse unbind_command_parameter_file(file_nameunbind_command_parameter_file_json_body)

UnbindCommandParameterFile

Unbind command parameter file.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import command_parameter_file_api
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.success_response import SuccessResponse
from aitrios_console_rest_client_sdk_primitive.model.unbind_command_parameter_file_json_body import UnbindCommandParameterFileJsonBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with aitrios_console_rest_client_sdk_primitive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = command_parameter_file_api.CommandParameterFileApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'file_name': "file_name_example",
    }
    query_params = {
    }
    body = UnbindCommandParameterFileJsonBody(
        device_ids="device_ids_example",
    )
    try:
        # UnbindCommandParameterFile
        api_response = api_instance.unbind_command_parameter_file(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling CommandParameterFileApi->unbind_command_parameter_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'file_name': "file_name_example",
    }
    query_params = {
        'grant_type': "client_credentials",
    }
    body = UnbindCommandParameterFileJsonBody(
        device_ids="device_ids_example",
    )
    try:
        # UnbindCommandParameterFile
        api_response = api_instance.unbind_command_parameter_file(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling CommandParameterFileApi->unbind_command_parameter_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnbindCommandParameterFileJsonBody**](../../models/UnbindCommandParameterFileJsonBody.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
grant_type | GrantTypeSchema | | optional


# GrantTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "client_credentials"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
file_name | FileNameSchema | | 

# FileNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#unbind_command_parameter_file.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#unbind_command_parameter_file.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#unbind_command_parameter_file.ApiResponseFor401) | Authorization Error
500 | [ApiResponseFor500](#unbind_command_parameter_file.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#unbind_command_parameter_file.ApiResponseFor503) | Service Unavailable

#### unbind_command_parameter_file.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResponse**](../../models/SuccessResponse.md) |  | 


#### unbind_command_parameter_file.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### unbind_command_parameter_file.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### unbind_command_parameter_file.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### unbind_command_parameter_file.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_command_parameter_file**
<a id="update_command_parameter_file"></a>
> SuccessResponse update_command_parameter_file(file_nameupdate_command_parameter_file_body)

UpdateCommandParameterFile

Update command parameter file.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import command_parameter_file_api
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.success_response import SuccessResponse
from aitrios_console_rest_client_sdk_primitive.model.update_command_parameter_file_body import UpdateCommandParameterFileBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with aitrios_console_rest_client_sdk_primitive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = command_parameter_file_api.CommandParameterFileApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'file_name': "file_name_example",
    }
    query_params = {
    }
    body = UpdateCommandParameterFileBody(
        parameter="parameter_example",
        comment="comment_example",
    )
    try:
        # UpdateCommandParameterFile
        api_response = api_instance.update_command_parameter_file(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling CommandParameterFileApi->update_command_parameter_file: %s\n" % e)

    # example passing only optional values
    path_params = {
        'file_name': "file_name_example",
    }
    query_params = {
        'grant_type': "client_credentials",
    }
    body = UpdateCommandParameterFileBody(
        parameter="parameter_example",
        comment="comment_example",
    )
    try:
        # UpdateCommandParameterFile
        api_response = api_instance.update_command_parameter_file(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling CommandParameterFileApi->update_command_parameter_file: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateCommandParameterFileBody**](../../models/UpdateCommandParameterFileBody.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
grant_type | GrantTypeSchema | | optional


# GrantTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "client_credentials"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
file_name | FileNameSchema | | 

# FileNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_command_parameter_file.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#update_command_parameter_file.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_command_parameter_file.ApiResponseFor401) | Authorization Error
500 | [ApiResponseFor500](#update_command_parameter_file.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#update_command_parameter_file.ApiResponseFor503) | Service Unavailable

#### update_command_parameter_file.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResponse**](../../models/SuccessResponse.md) |  | 


#### update_command_parameter_file.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_command_parameter_file.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_command_parameter_file.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### update_command_parameter_file.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

