# aitrios_console_rest_client_sdk_primitive.InsightApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image_directories**](InsightApi.md#get_image_directories) | **GET** /api/v1/devices/images/directories | GetImageDirectories
[**get_images**](InsightApi.md#get_images) | **GET** /api/v1/devices/{device_id}/images/directories/{sub_directory_name} | GetImages
[**get_inferenceresults**](InsightApi.md#get_inferenceresults) | **GET** /api/v1/devices/{device_id}/inferenceresults | GetInferenceresults


# **get_image_directories**
> [GetImageDirectories200ResponseInner] get_image_directories()

GetImageDirectories

Get image directories function.  Parameters: ---------- request(Request): Request from fastapi. session(Any): The result of calling Depends(get_db).  Returns: ------- ret(object): The result of calling main method of get_image_directories api.

### Example


```python
import time
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.api import insight_api
from aitrios_console_rest_client_sdk_primitive.model.get_image_directories200_response_inner import GetImageDirectories200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aitrios_console_rest_client_sdk_primitive.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = insight_api.InsightApi(api_client)
    device_id = "device_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetImageDirectories
        api_response = api_instance.get_image_directories(device_id=device_id)
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling InsightApi->get_image_directories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | [optional]

### Return type

[**[GetImageDirectories200ResponseInner]**](GetImageDirectories200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Authorization Error |  -  |
**404** | Not Found |  -  |
**422** | FastApi Validation Error |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> GetImages200Response get_images(device_id, sub_directory_name)

GetImages

Get_images function.  Parameters: ---------- request(Request): Request from fastapi. session(Any): The result of calling Depends(get_db).  Returns: ------- ret(object): The result of calling main method of get_images api.

### Example


```python
import time
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.api import insight_api
from aitrios_console_rest_client_sdk_primitive.model.get_images200_response import GetImages200Response
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aitrios_console_rest_client_sdk_primitive.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = insight_api.InsightApi(api_client)
    device_id = "device_id_example" # str | 
    sub_directory_name = "sub_directory_name_example" # str | 
    order_by = "ASC" # str |  (optional) if omitted the server will use the default value of "ASC"
    number_of_images = 50 # int |  (optional) if omitted the server will use the default value of 50
    skip = 0 # int |  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # GetImages
        api_response = api_instance.get_images(device_id, sub_directory_name)
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling InsightApi->get_images: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetImages
        api_response = api_instance.get_images(device_id, sub_directory_name, order_by=order_by, number_of_images=number_of_images, skip=skip)
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling InsightApi->get_images: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  |
 **sub_directory_name** | **str**|  |
 **order_by** | **str**|  | [optional] if omitted the server will use the default value of "ASC"
 **number_of_images** | **int**|  | [optional] if omitted the server will use the default value of 50
 **skip** | **int**|  | [optional] if omitted the server will use the default value of 0

### Return type

[**GetImages200Response**](GetImages200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Authorization Error |  -  |
**404** | Not Found |  -  |
**422** | FastApi Validation Error |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inferenceresults**
> [GetInferenceresults200ResponseInner] get_inferenceresults(device_id)

GetInferenceresults

Get inference results function.  Parameters: ---------- request(Request): Request from fastapi. session(Any): The result of calling Depends(get_db).  Returns: ------- ret(object): The result of calling main method of get_inference_results api.

### Example


```python
import time
import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.api import insight_api
from aitrios_console_rest_client_sdk_primitive.model.get_inferenceresults200_response_inner import GetInferenceresults200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aitrios_console_rest_client_sdk_primitive.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = insight_api.InsightApi(api_client)
    device_id = "device_id_example" # str | 
    number_of_inferenceresults = 20 # int |  (optional) if omitted the server will use the default value of 20
    filter = "filter_example" # str |  (optional)
    raw = "0" # str |  (optional) if omitted the server will use the default value of "0"
    time = "time_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # GetInferenceresults
        api_response = api_instance.get_inferenceresults(device_id)
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling InsightApi->get_inferenceresults: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetInferenceresults
        api_response = api_instance.get_inferenceresults(device_id, number_of_inferenceresults=number_of_inferenceresults, filter=filter, raw=raw, time=time)
        pprint(api_response)
    except aitrios_console_rest_client_sdk_primitive.ApiException as e:
        print("Exception when calling InsightApi->get_inferenceresults: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  |
 **number_of_inferenceresults** | **int**|  | [optional] if omitted the server will use the default value of 20
 **filter** | **str**|  | [optional]
 **raw** | **str**|  | [optional] if omitted the server will use the default value of "0"
 **time** | **str**|  | [optional]

### Return type

[**[GetInferenceresults200ResponseInner]**](GetInferenceresults200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Authorization Error |  -  |
**404** | Not Found |  -  |
**422** | FastApi Validation Error |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

