<a name="__pageTop"></a>
# aitrios_console_rest_client_sdk_primitive.apis.tags.train_model_api.TrainModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_model_func**](#delete_model_func) | **delete** /models/{model_id} | DeleteModelFunc
[**get_base_model_status_func**](#get_base_model_status_func) | **get** /models/{model_id}/base | GetBaseModelStatusFunc
[**get_models_func**](#get_models_func) | **get** /models | GetModelsFunc
[**import_base_model_func**](#import_base_model_func) | **post** /models | ImportBaseModelFunc
[**import_non_converted_model_func**](#import_non_converted_model_func) | **post** /models/{model_id} | ImportNonConvertedModelFunc

# **delete_model_func**
<a name="delete_model_func"></a>
> bool, date, datetime, dict, float, int, list, str, none_type delete_model_func(model_id)

DeleteModelFunc

Delete model function.  Parameters: ---------- request(Request): Request from fastapi. session(Any): The result of calling Depends(get_db).  Returns: ------- ret(object): The result of calling main method of delete_model api.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import train_model_api
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
    api_instance = train_model_api.TrainModelApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'model_id': "model_id_example",
    }
    try:
        # DeleteModelFunc
        api_response = api_instance.delete_model_func(
            path_params=path_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->delete_model_func: %s\n" % e)
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
model_id | ModelIdSchema | | 

# ModelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_model_func.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#delete_model_func.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#delete_model_func.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#delete_model_func.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#delete_model_func.ApiResponseFor503) | Service Unavailable

#### delete_model_func.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### delete_model_func.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### delete_model_func.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### delete_model_func.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### delete_model_func.ApiResponseFor503
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

# **get_base_model_status_func**
<a name="get_base_model_status_func"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_base_model_status_func(model_id)

GetBaseModelStatusFunc

Get model of base function.  Parameters: ---------- request(Request): Request from fastapi. session(Any): The result of calling Depends(get_db).  Returns: ------- ret(object): The result of calling main method of get_base_model_status api.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import train_model_api
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
    api_instance = train_model_api.TrainModelApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'model_id': "model_id_example",
    }
    query_params = {
    }
    try:
        # GetBaseModelStatusFunc
        api_response = api_instance.get_base_model_status_func(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->get_base_model_status_func: %s\n" % e)

    # example passing only optional values
    path_params = {
        'model_id': "model_id_example",
    }
    query_params = {
        'latest_type': "1",
    }
    try:
        # GetBaseModelStatusFunc
        api_response = api_instance.get_base_model_status_func(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->get_base_model_status_func: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
latest_type | LatestTypeSchema | | optional


# LatestTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "1"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
model_id | ModelIdSchema | | 

# ModelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_base_model_status_func.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#get_base_model_status_func.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#get_base_model_status_func.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#get_base_model_status_func.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_base_model_status_func.ApiResponseFor503) | Service Unavailable

#### get_base_model_status_func.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### get_base_model_status_func.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_base_model_status_func.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_base_model_status_func.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_base_model_status_func.ApiResponseFor503
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

# **get_models_func**
<a name="get_models_func"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_models_func()

GetModelsFunc

Get model of base function.  Parameters: ---------- request(Request): Request from fastapi. session(Any): The result of calling Depends(get_db).  Returns: ------- ret(object): The result of calling main method of get_models api.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import train_model_api
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
    api_instance = train_model_api.TrainModelApi(api_client)

    # example passing only optional values
    query_params = {
        'model_id': "model_id_example",
        'comment': "comment_example",
        'project_name': "project_name_example",
        'model_platform': "model_platform_example",
        'project_type': "project_type_example",
        'device_id': "device_id_example",
        'latest_type': "1",
    }
    try:
        # GetModelsFunc
        api_response = api_instance.get_models_func(
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->get_models_func: %s\n" % e)
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
model_id | ModelIdSchema | | optional
comment | CommentSchema | | optional
project_name | ProjectNameSchema | | optional
model_platform | ModelPlatformSchema | | optional
project_type | ProjectTypeSchema | | optional
device_id | DeviceIdSchema | | optional
latest_type | LatestTypeSchema | | optional


# ModelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CommentSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModelPlatformSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProjectTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LatestTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "1"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_models_func.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#get_models_func.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#get_models_func.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#get_models_func.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_models_func.ApiResponseFor503) | Service Unavailable

#### get_models_func.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### get_models_func.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_models_func.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_models_func.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_models_func.ApiResponseFor503
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

# **import_base_model_func**
<a name="import_base_model_func"></a>
> bool, date, datetime, dict, float, int, list, str, none_type import_base_model_func(train_model_import_base_model_data_importbasemodelindto_json_body)

ImportBaseModelFunc

import_base_model function.  Parameters: ---------- request(Request): Request from fastapi. session(Any): The result of calling Depends(get_db).  Returns: ------- ret(object): The result of calling main method of import_base_model api.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import train_model_api
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.train_model_import_base_model_data_importbasemodelindto_json_body import TrainModelImportBaseModelDataImportbasemodelindtoJsonBody
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with aitrios_console_rest_client_sdk_primitive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = train_model_api.TrainModelApi(api_client)

    # example passing only required values which don't have defaults set
    body = TrainModelImportBaseModelDataImportbasemodelindtoJsonBody(
        model_id="",
        model="",
        converted=False,
        vendor_name="",
        comment="",
        network_parameter="",
        network_config="",
        network_type="",
        labels=[],
    )
    try:
        # ImportBaseModelFunc
        api_response = api_instance.import_base_model_func(
            body=body,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->import_base_model_func: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TrainModelImportBaseModelDataImportbasemodelindtoJsonBody**](../../models/TrainModelImportBaseModelDataImportbasemodelindtoJsonBody.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#import_base_model_func.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#import_base_model_func.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#import_base_model_func.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#import_base_model_func.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#import_base_model_func.ApiResponseFor503) | Service Unavailable

#### import_base_model_func.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### import_base_model_func.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### import_base_model_func.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### import_base_model_func.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### import_base_model_func.ApiResponseFor503
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

# **import_non_converted_model_func**
<a name="import_non_converted_model_func"></a>
> bool, date, datetime, dict, float, int, list, str, none_type import_non_converted_model_func(model_id)

ImportNonConvertedModelFunc

Import NonConvert Model function.  Parameters: ---------- request(Request): Request from fastapi. session(Any): The result of calling Depends(get_db).  Returns: ------- ret(object): The result of calling main method of convert_model api.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import train_model_api
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
    api_instance = train_model_api.TrainModelApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'model_id': "model_id_example",
    }
    query_params = {
    }
    try:
        # ImportNonConvertedModelFunc
        api_response = api_instance.import_non_converted_model_func(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->import_non_converted_model_func: %s\n" % e)

    # example passing only optional values
    path_params = {
        'model_id': "model_id_example",
    }
    query_params = {
        'device_id': "device_id_example",
    }
    try:
        # ImportNonConvertedModelFunc
        api_response = api_instance.import_non_converted_model_func(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->import_non_converted_model_func: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
device_id | DeviceIdSchema | | optional


# DeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
model_id | ModelIdSchema | | 

# ModelIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#import_non_converted_model_func.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#import_non_converted_model_func.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#import_non_converted_model_func.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#import_non_converted_model_func.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#import_non_converted_model_func.ApiResponseFor503) | Service Unavailable

#### import_non_converted_model_func.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### import_non_converted_model_func.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### import_non_converted_model_func.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### import_non_converted_model_func.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### import_non_converted_model_func.ApiResponseFor503
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

