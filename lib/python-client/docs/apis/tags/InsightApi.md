<a id="__pageTop"></a>
# aitrios_console_rest_client_sdk_primitive.apis.tags.insight_api.InsightApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_images**](#export_images) | **get** /devices/images/export | ExportImages
[**get_image_directories**](#get_image_directories) | **get** /devices/images/directories | GetImageDirectories
[**get_images**](#get_images) | **get** /devices/{device_id}/images/directories/{sub_directory_name} | GetImages
[**get_inference_results**](#get_inference_results) | **get** /devices/{device_id}/inferenceresults | GetInferenceResults

# **export_images**
<a id="export_images"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} export_images(key)

ExportImages

Get the URL to export the images of specified conditions in zip file format. *For encrypted images for learning in other environments  [Prerequisites] - The encryption method is public key cryptography. - A zip file containing the target images can be downloaded by accessing a URL.   Each image is encoded using the method described hereafter. - The key used for encryption is a shared key of 32 characters issued randomly by the API each time. - The image encryption method is AES128, MODE_CBC - The iv (initial vector, 16 digits) and encrypted data are stored in a zip file.  [Generating a Key] - Private keys are issued by Sier itself. - Public and private keys are issued with a length of 1024 or 2048. - The public key (key) specified to the parameter of this API passes the pem file content of the public key in a base64 encoded format.    Example: Base64 encode the entire string as follows:    -----BEGIN PUBLIC KEY-----   MIGfMA0GCSqGSIb3DQEBAQUAA4GNADC   ...   -----END PUBLIC KEY-----

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import insight_api
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
    api_instance = insight_api.InsightApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'key': "key_example",
    }
    try:
        # ExportImages
        api_response = api_instance.export_images(
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling InsightApi->export_images: %s\n" % e)

    # example passing only optional values
    query_params = {
        'grant_type': "client_credentials",
        'key': "key_example",
        'from_datetime': "",
        'to_datetime': "",
        'device_id': "",
        'file_format': "",
    }
    try:
        # ExportImages
        api_response = api_instance.export_images(
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling InsightApi->export_images: %s\n" % e)
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
key | KeySchema | | 
from_datetime | FromDatetimeSchema | | optional
to_datetime | ToDatetimeSchema | | optional
device_id | DeviceIdSchema | | optional
file_format | FileFormatSchema | | optional


# GrantTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "client_credentials"

# KeySchema

Key

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Key | 

# FromDatetimeSchema

Date and time (From). - Format: yyyyMMddhhmm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Date and time (From). - Format: yyyyMMddhhmm | if omitted the server will use the default value of ""

# ToDatetimeSchema

Date/Time (To). - Format: yyyyMMddhhmm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Date/Time (To). - Format: yyyyMMddhhmm | if omitted the server will use the default value of ""

# DeviceIdSchema

Device ID.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Device ID. | if omitted the server will use the default value of ""

# FileFormatSchema

File Format

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | File Format | if omitted the server will use the default value of ""

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#export_images.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#export_images.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#export_images.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#export_images.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#export_images.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#export_images.ApiResponseFor503) | Service Unavailable

#### export_images.ApiResponseFor200
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
**key** | str,  | str,  | Shared key for decrypting images encrypted by a public key. | [optional] 
**url** | str,  | str,  | SUS URI for downloading | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### export_images.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### export_images.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### export_images.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### export_images.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### export_images.ApiResponseFor503
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

# **get_image_directories**
<a id="get_image_directories"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_image_directories()

GetImageDirectories

Get the image save directory list of the devices for each device group.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import insight_api
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
    api_instance = insight_api.InsightApi(api_client)

    # example passing only optional values
    query_params = {
        'grant_type': "client_credentials",
        'device_id': "device_id_example",
    }
    try:
        # GetImageDirectories
        api_response = api_instance.get_image_directories(
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling InsightApi->get_image_directories: %s\n" % e)
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_image_directories.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#get_image_directories.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#get_image_directories.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_image_directories.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_image_directories.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_image_directories.ApiResponseFor503) | Service Unavailable

#### get_image_directories.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

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
**[devices](#devices)** | list, tuple,  | tuple,  |  | 
**group_id** | str,  | str,  | Set the device group ID. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# devices

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
**device_name** | str,  | str,  | Set the device name. | 
**device_id** | str,  | str,  | Set the device ID. | 
**[Image](#Image)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Image

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Set the directory name. | 

#### get_image_directories.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_image_directories.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_image_directories.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_image_directories.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_image_directories.ApiResponseFor503
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

# **get_images**
<a id="get_images"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_images(device_idsub_directory_name)

GetImages

Get the (saved) images for a specified device. *Application: Use to display an image in a UI

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import insight_api
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
    api_instance = insight_api.InsightApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'device_id': "device_id_example",
        'sub_directory_name': "sub_directory_name_example",
    }
    query_params = {
    }
    try:
        # GetImages
        api_response = api_instance.get_images(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling InsightApi->get_images: %s\n" % e)

    # example passing only optional values
    path_params = {
        'device_id': "device_id_example",
        'sub_directory_name': "sub_directory_name_example",
    }
    query_params = {
        'grant_type': "client_credentials",
        'order_by': "ASC",
        'number_of_images': 50,
        'skip': 0,
    }
    try:
        # GetImages
        api_response = api_instance.get_images(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling InsightApi->get_images: %s\n" % e)
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
order_by | OrderBySchema | | optional
number_of_images | NumberOfImagesSchema | | optional
skip | SkipSchema | | optional


# GrantTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "client_credentials"

# OrderBySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "ASC"

# NumberOfImagesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 50

# SkipSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
device_id | DeviceIdSchema | | 
sub_directory_name | SubDirectoryNameSchema | | 

# DeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SubDirectoryNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_images.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#get_images.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#get_images.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_images.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_images.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_images.ApiResponseFor503) | Service Unavailable

#### get_images.ApiResponseFor200
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
**[images](#images)** | list, tuple,  | tuple,  |  | 
**total_image_count** | decimal.Decimal, int,  | decimal.Decimal,  | Set the total number of images. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# images

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
**contents** | str,  | str,  | Images file contents (BASE64 encoding). | 
**name** | str,  | str,  | Set the image filename. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_images.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_images.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_images.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_images.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_images.ApiResponseFor503
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

# **get_inference_results**
<a id="get_inference_results"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_inference_results(device_id)

GetInferenceResults

Get the (saved) inference result metadata list information for a specified device.

### Example

```python
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import insight_api
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.inference import Inference
from aitrios_console_rest_client_sdk_primitive.model.inference_result import InferenceResult
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with aitrios_console_rest_client_sdk_primitive.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = insight_api.InsightApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'device_id': "device_id_example",
    }
    query_params = {
    }
    try:
        # GetInferenceResults
        api_response = api_instance.get_inference_results(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling InsightApi->get_inference_results: %s\n" % e)

    # example passing only optional values
    path_params = {
        'device_id': "device_id_example",
    }
    query_params = {
        'grant_type': "client_credentials",
        'NumberOfInferenceresults': 20,
        'filter': "",
        'raw': 0,
        'time': "",
    }
    try:
        # GetInferenceResults
        api_response = api_instance.get_inference_results(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling InsightApi->get_inference_results: %s\n" % e)
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
NumberOfInferenceresults | NumberOfInferenceresultsSchema | | optional
filter | FilterSchema | | optional
raw | RawSchema | | optional
time | TimeSchema | | optional


# GrantTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "client_credentials"

# NumberOfInferenceresultsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 20

# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

# RawSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 0

# TimeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of ""

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
device_id | DeviceIdSchema | | 

# DeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_inference_results.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#get_inference_results.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_inference_results.ApiResponseFor401) | Authorization Error
403 | [ApiResponseFor403](#get_inference_results.ApiResponseFor403) | Forbidden
500 | [ApiResponseFor500](#get_inference_results.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#get_inference_results.ApiResponseFor503) | Service Unavailable

#### get_inference_results.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

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
**id** | str,  | str,  | Inference result metadata ID. &#x3D;GUID generated automatically by CosmosDB | [optional] 
**device_id** | str,  | str,  | Device ID. | [optional] 
**model_id** | str,  | str,  | Model ID. | [optional] 
**version_number** | str,  | str,  | Version number. | [optional] 
**model_version_id** | str,  | str,  | Model version ID. | [optional] 
**model_type** | str,  | str,  | Model type. 00: Image category 01: Object detection | [optional] 
**training_kit_name** | str,  | str,  |  | [optional] 
**_ts** | decimal.Decimal, int,  | decimal.Decimal,  | Time stamp. &#x3D;_ts of CosmosDB | [optional] 
**inference_result** | [**InferenceResult**]({{complexTypePrefix}}InferenceResult.md) | [**InferenceResult**]({{complexTypePrefix}}InferenceResult.md) |  | [optional] 
**[inferences](#inferences)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# inferences

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Inference**]({{complexTypePrefix}}Inference.md) | [**Inference**]({{complexTypePrefix}}Inference.md) | [**Inference**]({{complexTypePrefix}}Inference.md) |  | 

#### get_inference_results.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_inference_results.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_inference_results.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_inference_results.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_inference_results.ApiResponseFor503
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

