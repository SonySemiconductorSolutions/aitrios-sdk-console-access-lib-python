<a id="__pageTop"></a>
# aitrios_console_rest_client_sdk_primitive.apis.tags.train_model_api.TrainModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_model**](#delete_model) | **delete** /models/{model_id} | DeleteModel
[**get_base_model_status**](#get_base_model_status) | **get** /models/{model_id}/base | GetBaseModelStatus
[**get_models**](#get_models) | **get** /models | GetModels
[**import_base_model**](#import_base_model) | **post** /models | ImportBaseModel
[**publish_model**](#publish_model) | **post** /models/{model_id} | PublishModel

# **delete_model**
<a id="delete_model"></a>
> SuccessResponse delete_model(model_id)

DeleteModel

Deletes the base model, device model, and project associated with the specified model ID.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import train_model_api
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
    api_instance = train_model_api.TrainModelApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'model_id': "model_id_example",
    }
    query_params = {
    }
    try:
        # DeleteModel
        api_response = api_instance.delete_model(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->delete_model: %s\n" % e)

    # example passing only optional values
    path_params = {
        'model_id': "model_id_example",
    }
    query_params = {
        'grant_type': "client_credentials",
    }
    try:
        # DeleteModel
        api_response = api_instance.delete_model(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->delete_model: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_model.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#delete_model.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#delete_model.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#delete_model.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#delete_model.ApiResponseFor503) | Service Unavailable

#### delete_model.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResponse**](../../models/SuccessResponse.md) |  | 


#### delete_model.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### delete_model.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### delete_model.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### delete_model.ApiResponseFor503
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

# **get_base_model_status**
<a id="get_base_model_status"></a>
> ModelInfo get_base_model_status(model_id)

GetBaseModelStatus

Get the specified base model information.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import train_model_api
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.model_info import ModelInfo
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
        # GetBaseModelStatus
        api_response = api_instance.get_base_model_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->get_base_model_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'model_id': "model_id_example",
    }
    query_params = {
        'grant_type': "client_credentials",
        'latest_type': "1",
    }
    try:
        # GetBaseModelStatus
        api_response = api_instance.get_base_model_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->get_base_model_status: %s\n" % e)
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
grant_type | GrantTypeSchema | | optional
latest_type | LatestTypeSchema | | optional


# GrantTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "client_credentials"

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
200 | [ApiResponseFor200](#get_base_model_status.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#get_base_model_status.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#get_base_model_status.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#get_base_model_status.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_base_model_status.ApiResponseFor503) | Service Unavailable

#### get_base_model_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ModelInfo**](../../models/ModelInfo.md) |  | 


#### get_base_model_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_base_model_status.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_base_model_status.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_base_model_status.ApiResponseFor503
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

# **get_models**
<a id="get_models"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_models()

GetModels

Get the model list information.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import train_model_api
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.model import Model
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
        'grant_type': "client_credentials",
        'model_id': "model_id_example",
        'comment': "comment_example",
        'project_name': "project_name_example",
        'model_platform': "model_platform_example",
        'project_type': "project_type_example",
        'device_id': "device_id_example",
        'latest_type': "1",
    }
    try:
        # GetModels
        api_response = api_instance.get_models(
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->get_models: %s\n" % e)
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
model_id | ModelIdSchema | | optional
comment | CommentSchema | | optional
project_name | ProjectNameSchema | | optional
model_platform | ModelPlatformSchema | | optional
project_type | ProjectTypeSchema | | optional
device_id | DeviceIdSchema | | optional
latest_type | LatestTypeSchema | | optional


# GrantTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "client_credentials"

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
200 | [ApiResponseFor200](#get_models.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#get_models.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#get_models.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#get_models.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_models.ApiResponseFor503) | Service Unavailable

#### get_models.ApiResponseFor200
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
**[models](#models)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# models

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Model**]({{complexTypePrefix}}Model.md) | [**Model**]({{complexTypePrefix}}Model.md) | [**Model**]({{complexTypePrefix}}Model.md) |  | 

#### get_models.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_models.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_models.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_models.ApiResponseFor503
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

# **import_base_model**
<a id="import_base_model"></a>
> SuccessResponse import_base_model(import_base_model_json_body)

ImportBaseModel

Import the base model. In addition, in the case of a new model ID, it is newly saved. If you specify a model ID that has already been registered in the system, the version will be upgraded.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import train_model_api
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.success_response import SuccessResponse
from aitrios_console_rest_client_sdk_primitive.model.import_base_model_json_body import ImportBaseModelJsonBody
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
    query_params = {
    }
    body = ImportBaseModelJsonBody(
        model="model_example",
        input_format_param="input_format_param_example",
        network_config="network_config_example",
        model_id="model_id_example",
        converted=False,
        vendor_name="vendor_name_example",
        comment="comment_example",
        network_type="1",
        metadata_format_id="metadata_format_id_example",
    )
    try:
        # ImportBaseModel
        api_response = api_instance.import_base_model(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->import_base_model: %s\n" % e)

    # example passing only optional values
    query_params = {
        'grant_type': "client_credentials",
    }
    body = ImportBaseModelJsonBody(
        model="model_example",
        input_format_param="input_format_param_example",
        network_config="network_config_example",
        model_id="model_id_example",
        converted=False,
        vendor_name="vendor_name_example",
        comment="comment_example",
        network_type="1",
        metadata_format_id="metadata_format_id_example",
    )
    try:
        # ImportBaseModel
        api_response = api_instance.import_base_model(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->import_base_model: %s\n" % e)
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
[**ImportBaseModelJsonBody**](../../models/ImportBaseModelJsonBody.md) |  | 


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
200 | [ApiResponseFor200](#import_base_model.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#import_base_model.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#import_base_model.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#import_base_model.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#import_base_model.ApiResponseFor503) | Service Unavailable

#### import_base_model.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessResponse**](../../models/SuccessResponse.md) |  | 


#### import_base_model.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### import_base_model.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### import_base_model.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### import_base_model.ApiResponseFor503
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

# **publish_model**
<a id="publish_model"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} publish_model(model_id)

PublishModel

Provide a function to publish a conversion model. As model publishing takes time, this is performed asynchronously. *Check the processing status in the result of the GetBaseModelStatus API or GetDeviceModelStatus API response. If the result is 'Import completed', the process is completed.

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
        # PublishModel
        api_response = api_instance.publish_model(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->publish_model: %s\n" % e)

    # example passing only optional values
    path_params = {
        'model_id': "model_id_example",
    }
    query_params = {
        'grant_type': "client_credentials",
        'device_id': "device_id_example",
    }
    try:
        # PublishModel
        api_response = api_instance.publish_model(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling TrainModelApi->publish_model: %s\n" % e)
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
grant_type | GrantTypeSchema | | optional
device_id | DeviceIdSchema | | optional


# GrantTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "client_credentials"

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
200 | [ApiResponseFor200](#publish_model.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#publish_model.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#publish_model.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#publish_model.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#publish_model.ApiResponseFor503) | Service Unavailable

#### publish_model.ApiResponseFor200
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
**result** | str,  | str,  | Set \&quot;SUCCESS\&quot; fixing | [optional] 
**import_id** | str,  | str,  | Set the conv ID. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### publish_model.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### publish_model.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### publish_model.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### publish_model.ApiResponseFor503
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

