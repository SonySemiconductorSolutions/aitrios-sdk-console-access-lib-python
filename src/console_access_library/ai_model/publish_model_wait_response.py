# ------------------------------------------------------------------------
# Copyright 2022 Sony Semiconductor Solutions Corp. All rights reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------

# pylint:disable=missing-module-docstring
# pylint:disable=import-error
# pylint:disable=wrong-import-position
# pylint:disable=duplicate-code
# pylint:disable=unused-argument
# pylint:disable=redefined-builtin
# pylint:disable=too-many-branches
# pylint:disable=too-many-statements
# pylint:disable=too-many-locals
# pylint:disable=too-many-return-statements
# pylint:disable=protected-access
# pylint:disable=broad-except
# pylint:disable=no-else-break

import logging
import sys
import types
import warnings
from datetime import timedelta
from enum import Enum
from time import time

import aitrios_console_rest_client_sdk_primitive
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.ai_model.get_base_model_status import GetBaseModelStatus
from console_access_library.ai_model.publish_model import PublishModel
from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass

logger = logging.getLogger(__name__)


class SchemaPublishModelWaitResponse(Schema):
    """Schema for API to publish model and wait for completion.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : Model ID.
    model_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for model_id"}, strict=True
    )

    #: str, optional : The ID of edge AI device.
    device_id = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for device_id"},
        strict=True,
        allow_none=True,
    )

    #: function, optional : Callback function.
    callback = fields.Function(
        required=False,
        error_messages={"invalid": "Invalid return for callback"},
        strict=True,
        allow_none=True,
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if str(data["model_id"]).strip() == "":
            raise ValidationError("model_id is required or can't be empty string")

        if "device_id" in data and (
            data["device_id"] is not None and str(data["device_id"]).strip() == ""
        ):
            raise ValidationError("device_id is required or can't be empty string")

        if (
            "callback" in data
            and data["callback"] is not None
            and (
                str(data["callback"]).strip() == ""
                or not isinstance(data["callback"], (types.FunctionType, types.MethodType))
            )
        ):
            raise ValidationError("callback is required or need to be a function/method")


class PublishModelStatus(Enum):
    """Publish Model Status Enum Values"""

    BEFORE_CONVERSION = "01"
    CONVERTING = "02"
    CONVERSION_FAILED = "03"
    CONVERSION_COMPLETE = "04"
    ADDING_TO_CONFIGURATION = "05"
    ADD_TO_CONFIGURATION_FAILED = "06"
    ADD_TO_CONFIGURATION_COMPLETE = "07"
    SAVING = "11"


class PublishModelWaitResponse(ConsoleAccessBaseClass):
    """This class implements API to publish model and wait for completion

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class PublishModelWaitResponse

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config
        self._publish_model_obj = PublishModel(self._config)
        self._get_base_model_status_obj = GetBaseModelStatus(self._config)

    def publish_model_wait_response(self, model_id: str, device_id: str = None, callback=None):
        """Publish model and wait for completion

        Args:
            model_id (str, required) : The Model ID.
            device_id (str, optional) : ID of edge AI device. Specify when the device \
                model is the target, If the base model is the target, do not specify.
            callback (function, optional) : A function handle of the form - \
                ``publish_callback(status)``, where ``status`` is the notified publish status. \
                Callback Function to check the publishing status with ``get_base_model_status``,
                and if not completed, call the callback function to notify the publishing status.\
                If not specified, no callback notification.

        Returns:
            **Return Type**

            - On Success Response - dict
            - On Error Response - dict

            **Success Response Schema**

                +-------------------+------------+-------------------------------+
                | *Level1*          | *Type*     | *Description*                 |
                +-------------------+------------+-------------------------------+
                | ``result``        | ``string`` | "SUCCESS"                     |
                +-------------------+------------+-------------------------------+
                | ``process time``  | ``string`` | Processing Time               |
                +-------------------+------------+-------------------------------+

            **Error Response Schema**

                - **Generic Error Response** :

                    If Any generic error returned from the Low Level SDK
                    Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``code`` (str) : "Generic Error"
                    - ``datetime`` (str) : Time

                - **Validation Error Response** :

                    If incorrect API input parameters OR
                    if any input string parameter found empty OR
                    if type of callback paramter not a function.
                    Then, Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : validation error message for respective input parameter
                    - ``code`` (str) : "E001"
                    - ``datetime`` (str) : Time

                - **Key Error Response** :

                    If API key error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``code`` (str) : "Key Error"
                    - ``datetime`` (str) : Time

                - **Type Error Response** :

                    If API type error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``code`` (str) : "Type Error"
                    - ``datetime`` (str) : Time

                - **Attribute Error Response** :

                    If API attribute error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``code`` (str) : "Attribute Error"
                    - ``datetime`` (str) : Time

                - **Value Error Response** :

                    If API value error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``code`` (str) : "Value Error"
                    - ``datetime`` (str) : Time

                - **HTTP Error Response** :

                    If the API http_status returned from the Console Server
                    is other than 200. Dictionary with below key and value pairs.

                    - ``result`` (str) : "ERROR"
                    - ``message`` (str) : error message returned from the Console server.
                    - ``code`` (str) : error code received from the Console server.
                    - ``datetime`` (str) : Time

        Example:
            .. code-block:: python

                import os
                import sys
                from pprint import pprint

                from console_access_library.client import Client
                from console_access_library.common.config import Config
                from console_access_library.common.read_console_access_settings
                import ReadConsoleAccessSettings

                # For Console Access Library API Usage,
                # edit console access setting configuration parameters with real values.
                # file_path: samples/console_access_settings.yaml
                # console_access_settings:
                #     console_endpoint: "__console_endpoint__"
                #     portal_authorization_endpoint: "__portal_authorization_endpoint__"
                #     client_secret: "__client_secret__"
                #     client_id: "__client_id__"

                # Set path for Console Access Library Setting File.
                SETTING_FILE_PATH = os.path.join(os.getcwd(),
                                                 "samples",
                                                 "console_access_settings.yaml")

                # Instantiate Console Access Library ReadConsoleAccessSettings.
                read_console_access_settings_obj = ReadConsoleAccessSettings(SETTING_FILE_PATH)

                # Instantiate Console Access Library Config.
                config_obj = Config(
                    read_console_access_settings_obj.console_endpoint,
                    read_console_access_settings_obj.portal_authorization_endpoint,
                    read_console_access_settings_obj.client_id,
                    read_console_access_settings_obj.client_secret
                )

                # Instantiate Console Access Library Client.
                client_obj = Client(config_obj)

                # Create Instance for AIModel
                ai_model_obj = client_obj.get_ai_model()

                # set the real value
                model_id =  "__model_id__"
                device_id =  "__device_id__"
                callback = "__callback__"

                # callback is user defined method
                def publish_callback(status):
                    # Process callback received for the ``status``.

                # AIModel - PublishModelWaitResponse
                response = ai_model_obj.publish_model_wait_response(model_id, device_id, callback)
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()
            # delete local argument 'self' form locals() for validation.
            if "self" in _local_params:
                del _local_params["self"]

            # Validate schema
            _local_params = SchemaPublishModelWaitResponse().load(_local_params)
            _return_publish_model_wait_response = {}
            _return_publish_model = None
            publish_start_time = time()
            try:
                logger.info("Publishing... ")

                _return_publish_model = self._publish_model_obj.publish_model(
                    model_id=_local_params["model_id"],
                    device_id=_local_params["device_id"],
                )
                if (
                    "result" in _return_publish_model
                    and _return_publish_model["result"] == "SUCCESS"
                ):
                    # Wait till publish status is failed or success
                    _publish_status = None
                    while True:
                        _model_status = self._get_base_model_status_obj.get_base_model_status(
                            model_id=model_id, latest_type="1"
                        )
                        _publish_status = _model_status["projects"][0]["versions"][0][
                            "version_status"
                        ]

                        # if callback parameter is not None then
                        # invoke callback function with `publish_status`
                        if callback is not None:
                            callback(_publish_status)

                        # if `publish_status` is error, during conversion
                        # stop polling for model publish status
                        if _publish_status == PublishModelStatus.CONVERSION_FAILED.value:
                            message = "Conversion failed"
                            _return_publish_model_wait_response = self.on_generic_error_response(
                                __name__, message
                            )
                            break

                        # if `publish_status` is error during add to configuration then
                        # stop polling for model publish status
                        elif (
                            _publish_status == PublishModelStatus.ADD_TO_CONFIGURATION_FAILED.value
                        ):
                            message = "Add to configuration failed"
                            _return_publish_model_wait_response = self.on_generic_error_response(
                                __name__, message
                            )
                            break

                        # if `publish_status` is success then calculate process time and
                        # stop polling for model publish status
                        elif _publish_status == (
                            PublishModelStatus.ADD_TO_CONFIGURATION_COMPLETE.value
                        ):
                            _return_publish_model_wait_response["result"] = "SUCCESS"
                            publish_end_time = time()
                            publish_time_seconds = publish_end_time - publish_start_time

                            # convert seconds to "HH:MM:SS" format
                            total_publish_time_str = (
                                f"{str(timedelta(seconds=publish_time_seconds))}"
                            )
                            _return_publish_model_wait_response[
                                "process_time"
                            ] = total_publish_time_str
                            break
                        else:
                            logger.info(_publish_status)
                else:
                    _return_publish_model_wait_response = _return_publish_model

            except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                _return_publish_model_wait_response = self.on_key_error_response(__name__, key_err)

            except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                _return_publish_model_wait_response = self.on_type_error_response(
                    __name__, type_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                _return_publish_model_wait_response = self.on_value_error_response(
                    __name__, val_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                _return_publish_model_wait_response = self.on_attribute_error_response(
                    __name__, attr_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                _return_publish_model_wait_response = self.on_http_error_response(
                    __name__, exception
                )

            except Exception as exception:
                _return_publish_model_wait_response = self.on_generic_error_response(
                    __name__, exception
                )

        except ValidationError as err:
            _return_publish_model_wait_response = self.on_validation_error_response(__name__, err)

        return _return_publish_model_wait_response
