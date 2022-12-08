"""
Copyright 2022 Sony Semiconductor Solutions Corp. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# pylint:disable=missing-module-docstring
# pylint:disable=import-error
# pylint:disable=wrong-import-position
# pylint:disable=duplicate-code
# pylint:disable=unused-argument
# pylint:disable=redefined-builtin
# pylint:disable=too-many-arguments
# pylint:disable=too-many-locals
# pylint:disable=too-many-return-statements
# pylint:disable=protected-access


import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import device_command_api
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.logger import Logger
from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass


class SchemaStopUploadInferenceResult(Schema):
    """Schema for API for StopUploadInferenceResult

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : Device ID.
    device_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for device_id"}
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if data["device_id"] == "":
            raise ValidationError("device_id is required")


class StopUploadInferenceResult(ConsoleAccessBaseClass):
    """This class implements API to execute instructions to stop acquiring inference result \
        metadata (Output Tensor) and image (Input Tensor) to the specified device.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class GetDevices

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config
        self.logger = Logger().set_logger()

    def stop_upload_inference_result(self, device_id: str):
        """Execute instructions to stop acquiring inference result metadata (Output Tensor) \
            and image (Input Tensor) to the specified device API

        Args:
            device_id (str, required): Device ID. No more than 100 characters.

        Returns:
            dict:
                - **Success Response** : Dictionary with below key and value pairs.

                    - ``result`` (str) : Result

                - **Generic Error Response** :

                    If the http_status returned from the Low Level SDK
                    API is other than 200. Dictionary with below key and value pairs.

                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``error_code`` (str) : "Generic Error"

                - **Validation Error Response** :

                    If incorrect API input parameters. Dictionary with below key and value pairs.

                    - ``message`` (str) : validation error message for respective input parameter
                    - ``error_code`` (str) : "E001"

                - **Key Error Response** :

                    If API key error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``error_code`` (str) : "Key Error"

                - **Type Error Response** :

                    If API type error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``error_code`` (str) : "Type Error"

                - **Attribute Error Response** :

                    If API attribute error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``error_code`` (str) : "Attribute Error"

                - **Value Error Response** :

                    If API value error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``error_code`` (str) : "Value Error"

        Example:
            .. code-block:: python

                import os
                import sys

                from pprint import pprint
                from console_access_library.client import Client

                # For Console Access Library API Usage,
                # edit console access setting configuration parameters with real values.
                # file_path: samples/console_access_settings.yaml
                # console_access_settings:
                #   base_url: "__base_url__"
                #   token_url: "__token_url__"
                #   client_secret: '__client_secret__'
                #   client_id: '__client_id__'

                # Set path for Console Access Library Setting File.
                SETTING_FILE_PATH = os.path.join(os.getcwd(), "samples","console_access_settings.yaml")

                # Instantiate Console Access Library Client.
                console_sdk_client_obj = Client(SETTING_FILE_PATH)

                # set the real value
                device_id = "__device_id__"

                # DeviceManagement - StopUploadInferenceResult
                response = console_sdk_client_obj.device_management.stop_upload_inference_result(
                    device_id)
                pprint(response)
        """

        self.logger.info(sys._getframe().f_code.co_name)

        try:
            # delete local argument 'self' form locals() for validation.
            _local_params = locals()
            if "self" in _local_params:
                del _local_params["self"]

            # Validate schema
            _local_params = SchemaStopUploadInferenceResult().load(_local_params)

            # Enter a context with an instance of the API client
            with aitrios_console_rest_client_sdk_primitive.ApiClient(
                self._config.configuration,
                header_name="Authorization",
                header_value=self._config.get_access_token(),
            ) as api_client:
                # Create an instance of the API class
                device_command_api_instance = device_command_api.StopUploadInferenceResult(
                    api_client
                )

                try:
                    _return_stop_upload_inference_result = (
                        device_command_api_instance.stop_upload_inference_result(
                            path_params=_local_params
                        )
                    )
                    return _return_stop_upload_inference_result.body

                except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                    _return_stop_upload_inference_result = self.on_key_error_response(
                        __name__, key_err
                    )
                    return _return_stop_upload_inference_result

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_stop_upload_inference_result = self.on_type_error_response(
                        __name__, type_err
                    )
                    return _return_stop_upload_inference_result

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_stop_upload_inference_result = self.on_value_error_response(
                        __name__, val_err
                    )
                    return _return_stop_upload_inference_result

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_stop_upload_inference_result = self.on_attribute_error_response(
                        __name__, attr_err
                    )
                    return _return_stop_upload_inference_result

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_stop_upload_inference_result = self.on_generic_error_response(
                        __name__, exception
                    )
                    return _return_stop_upload_inference_result

        except ValidationError as err:
            _return_stop_upload_inference_result = self.on_validation_error_response(__name__, err)
            return _return_stop_upload_inference_result
