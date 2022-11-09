<a name="__pageTop"></a>
# aitrios_console_rest_client_sdk_primitive.apis.tags.device_command_api.DeviceCommandApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start_upload_inference_result**](#start_upload_inference_result) | **post** /devices/{device_id}/inferenceresults/collectstart | StartUploadInferenceResult
[**stop_upload_inference_result**](#stop_upload_inference_result) | **post** /devices/{device_id}/inferenceresults/collectstop | StopUploadInferenceResult

# **start_upload_inference_result**
<a name="start_upload_inference_result"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} start_upload_inference_result(device_id)

StartUploadInferenceResult

Start Upload Inference Result.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import device_command_api
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
    api_instance = device_command_api.DeviceCommandApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'device_id': "device_id_example",
    }
    try:
        # StartUploadInferenceResult
        api_response = api_instance.start_upload_inference_result(
            path_params=path_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling DeviceCommandApi->start_upload_inference_result: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
device_id | DeviceIdSchema | | 

# DeviceIdSchema

Device Id

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Device Id | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#start_upload_inference_result.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#start_upload_inference_result.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#start_upload_inference_result.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#start_upload_inference_result.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#start_upload_inference_result.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#start_upload_inference_result.ApiResponseFor503) | Service Unavailable

#### start_upload_inference_result.ApiResponseFor200
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
**result** | str,  | str,  | todo | 
**outputSubDirectory** | str,  | str,  | todo | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### start_upload_inference_result.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### start_upload_inference_result.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### start_upload_inference_result.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### start_upload_inference_result.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### start_upload_inference_result.ApiResponseFor503
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

# **stop_upload_inference_result**
<a name="stop_upload_inference_result"></a>
> SuccessResponse stop_upload_inference_result(device_id)

StopUploadInferenceResult

Stop Upload Inference Result.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import device_command_api
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.success_response import SuccessResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with aitrios_console_rest_client_sdk_primitive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = device_command_api.DeviceCommandApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'device_id': "device_id_example",
    }
    try:
        # StopUploadInferenceResult
        api_response = api_instance.stop_upload_inference_result(
            path_params=path_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling DeviceCommandApi->stop_upload_inference_result: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
device_id | DeviceIdSchema | | 

# DeviceIdSchema

Device Id

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Device Id | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#stop_upload_inference_result.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#stop_upload_inference_result.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#stop_upload_inference_result.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#stop_upload_inference_result.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#stop_upload_inference_result.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#stop_upload_inference_result.ApiResponseFor503) | Service Unavailable

#### stop_upload_inference_result.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResponse**](../../models/SuccessResponse.md) |  | 


#### stop_upload_inference_result.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### stop_upload_inference_result.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### stop_upload_inference_result.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### stop_upload_inference_result.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### stop_upload_inference_result.ApiResponseFor503
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

