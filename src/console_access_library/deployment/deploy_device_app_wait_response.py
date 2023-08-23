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
# pylint:disable=too-many-arguments
# pylint:disable=too-many-branches
# pylint:disable=too-many-locals
# pylint:disable=too-many-return-statements
# pylint:disable=protected-access
# pylint:disable=no-value-for-parameter
# pylint:disable=too-many-nested-blocks
# pylint:disable=too-many-statements
# pylint:disable=broad-except
# pylint:disable=unused-variable

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

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass
from console_access_library.deployment.deploy_device_app import DeployDeviceApp
from console_access_library.deployment.get_device_app_deploys import GetDeviceAppDeploys

logger = logging.getLogger(__name__)


class SchemaDeployDeviceAppWaitResponse(Schema):
    """Schema for DeployDeviceAppWaitResponse API.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : App name
    app_name = fields.String(
        required=True, error_messages={"invalid": "Invalid string for app_name"}, strict=True
    )

    #: str, required : App version
    version_number = fields.String(
        required=True, error_messages={"invalid": "Invalid string for version_number"}, strict=True
    )

    #: str, required : IDs of edge AI devices
    device_ids = fields.String(
        required=True, error_messages={"invalid": "Invalid Value for device_ids"}, strict=True
    )

    #: str, optional : Deployment parameters
    deploy_parameter = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for deploy_parameter"},
        strict=True,
        allow_none=True,
    )

    #: str, optional : deploy comment
    comment = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for comment"},
        strict=True,
        allow_none=True,
    )

    #: function, optional : callback (function, optional) : A function handle of the form -
    #: ``deploy_device_app_callback(device_status_array)``, where ``device_status_array``
    #: is the array of the dictionary for each device :
    #: [
    #:     {
    #:         <device_id> : {
    #:             "status":<status>,
    #:             "found_position":<found_position>,
    #:             "skip":<skip>
    #:         }
    #:     },
    #: ]

    #: here - ``device_id``: is device ID,
    #:     - ``status``: is the notified deployment status for that device_id,
    #:     - ``found_position``: index of the device id from devices array of the
    #:             ``get_device_app_deploys`` response
    #:     - ``skip``: deploy status has captured, so skip for next iteration
    #:             inside the loop

    #: Callback function to check the deploying status with ``get_device_app_deploys``,
    #: and if not completed, call the callback function and notify the deploying status.
    #: If not specified, no callback notification.
    callback = fields.Function(
        required=False,
        error_messages={"invalid": "Invalid return for callback"},
        strict=True,
        allow_none=True,
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if str(data["app_name"]).strip() == "":
            raise ValidationError("app_name is required or can't be empty string")

        if str(data["version_number"]).strip() == "":
            raise ValidationError("version_number is required or can't be empty string")

        if str(data["device_ids"]).strip() == "":
            raise ValidationError("device_ids is required or can't be empty string")

        if "deploy_parameter" in data and (
            data["deploy_parameter"] is None and str(data["deploy_parameter"]).strip() == ""
        ):
            raise ValidationError("deploy_parameter is required or can't be empty string")

        if "comment" in data and data["comment"] is not None and str(data["comment"]).strip() == "":
            raise ValidationError("comment is required or can't be empty string")

        if (
            "callback" in data
            and data["callback"] is not None
            and (
                str(data["callback"]).strip() == ""
                or not isinstance(data["callback"], (types.FunctionType, types.MethodType))
            )
        ):
            raise ValidationError("callback is required or need to be a function/method")


class DeployDeviceAppStatus(Enum):
    """Deploy Device App Enum Status"""

    DEPLOYING = "0"
    DEPLOYMENT_DONE = "1"
    DEPLOYMENT_FAILED = "2"
    DEPLOYMENT_CANCELED = "3"


class DeployDeviceAppWaitResponse(ConsoleAccessBaseClass):
    """This class implements DeployDeviceAppWaitResponse API.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class DeployDeviceAppWaitResponse

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config
        self._deploy_device_app_obj = DeployDeviceApp(self._config)
        self._get_device_app_deploy_status_obj = GetDeviceAppDeploys(self._config)
        self._deploy_callback_status_array = []

    def _set_values(self, device_id, status="", found_position=0, skip=0):
        """Update the device id deploy status information to global array

        Args:
            device_id (str): Device ID, Case sensitive
            status (str, optional): The notified deployment status for that device_id.
            found_position (int, optional): index of the device id from devices array \
                of the ``get_device_app_deploys`` response. Defaults to 0.
            skip (int, optional): deploy status has captured, so skip for next iteration\
                inside the loop. Defaults to 0.
        """
        dict_ = {}
        if device_id is not None or device_id != "":
            if device_id not in [
                list(d.keys())[0] for i, d in enumerate(self._deploy_callback_status_array)
            ]:
                dict_[device_id] = {
                    "status": status,
                    "found_position": found_position,
                    "skip": skip,
                }
                self._deploy_callback_status_array.append(dict_)
            elif len(self._deploy_callback_status_array) != 0:
                for i, devices_array in enumerate(self._deploy_callback_status_array):
                    if device_id in devices_array:
                        self._deploy_callback_status_array[i][device_id] = {
                            "status": status,
                            "found_position": found_position,
                            "skip": skip,
                        }

    def _get_values(self, device_id):
        """Get device id deploy status information from the global array

        Args:
            device_id (str): Device ID, Case sensitive

        Returns:
            dict: if device ID found.
            None: if device ID not found.
        """
        if len(self._deploy_callback_status_array) != 0:
            for devices_array in self._deploy_callback_status_array:
                if device_id in devices_array:
                    return devices_array[device_id]
        return None

    def deploy_device_app_wait_response(
        self,
        app_name: str,
        version_number: str,
        device_ids: str,
        deploy_parameter: str = None,
        comment: str = None,
        callback=None,
    ):
        """Deploy and wait for completion

        Args:
            app_name (str, required) : App name
            version_number (str, required) : App version
            device_ids (str, required) : IDs of edge AI devices \
                Specify multiple device IDs separated by commas
            deploy_parameter (str, optional) : Deployment parameters \
                Base64 encoded string in Json format No parameters if not specified.
            comment (str, optional) : deploy comment \
                up to 100 characters \
                No comment if not specified.
            callback (function, optional) : A function handle of the form - \
                ``deploy_device_app_callback(device_status_array)``, where ``device_status_array``\
                is the array of the dictionary for each device :

                .. code-block:: console

                    [
                        {
                            <device_id> : {
                                "status":<status>,
                                "found_position":<found_position>,
                                "skip":<skip>
                            }
                        },
                    ]

                - ``device_id``: is device ID,
                - ``status``: is the notified deployment status for that device_id,
                - ``found_position``: index of the device id from devices array of the \
                        ``get_device_app_deploys`` response
                - ``skip``: deploy status has captured, so skip for next iteration \
                        inside the loop

                Callback function to check the deploying status with ``get_device_app_deploys``,\
                and if not completed, call the callback function and notify the deploying status.
                If not specified, no callback notification.

        Returns:
            **Return Type**

            - On Success Response - dict
            - On Error Response - dict

            **Success Response Schema**

                +-------------------+-------------------+------------+----------------------------+
                | *Level1*          | *Level2*          | *Type*     | *Description*              |
                +-------------------+-------------------+------------+----------------------------+
                | ``No_item_name``  |                   | ``array``  | deploy device app          |
                |                   |                   |            | wait response array        |
                +-------------------+-------------------+------------+----------------------------+
                |                   | ``device_id``     | ``string`` | Set the device id          |
                +-------------------+-------------------+------------+----------------------------+
                |                   | ``result``        | ``string`` | "SUCCESS"                  |
                +-------------------+-------------------+------------+----------------------------+
                |                   | ``process_time``  | ``string`` | Processing Time            |
                +-------------------+-------------------+------------+----------------------------+

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

                # Create Instance for Deployment
                deployment_obj = client_obj.get_deployment()

                # set the real value
                app_name = "__app_name__",
                version_number = "__version_number__",
                device_ids = "__device_ids__",
                deploy_parameter = "__deploy_parameter__",
                comment = "__comment__"
                callback = "__callback__"

                # callback is user defined method
                def deploy_device_app_callback(deploy_status_array):
                    # Process callback received for the ``device_id`` with ``status`` from \
                    # ``deploy_status_array``:
                    # is the array of the dictionary for each device :
                    # [
                    #     {
                    #         <device_id> : {
                    #             "status":<status>,
                    #             "found_position":<found_position>,
                    #             "skip":<skip>
                    #         }
                    #     },
                    # ]\

                    # here - ``device_id``: is device ID,
                    #     - ``status``: is the notified deployment status for that device_id,
                    #     - ``found_position``: index of the device id from devices array of \
                    #               the ``get_device_app_deploys`` response
                    #     - ``skip``: deploy status has captured, so skip for next iteration \
                    #               inside the loop

                # Deployment - DeployDeviceApps
                response = deployment_obj.deploy_device_app_wait_response(
                    app_name,
                    version_number,
                    device_ids,
                    deploy_parameter,
                    comment,
                    callback
                )
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()
            # delete local argument 'self' form locals() for validation.
            if "self" in _local_params:
                del _local_params["self"]

            # Validate Schema
            _local_params = SchemaDeployDeviceAppWaitResponse().load(_local_params)

            _deploy_status = {
                DeployDeviceAppStatus.DEPLOYING.value: "deploying",
                DeployDeviceAppStatus.DEPLOYMENT_DONE.value: "deployment_done",
                DeployDeviceAppStatus.DEPLOYMENT_FAILED.value: "deployment_failed",
                DeployDeviceAppStatus.DEPLOYMENT_CANCELED.value: "deployment_canceled",
            }
            _return_deploy_device_app = None
            _return_deploy_device_app_wait_response_all_device_ids = []
            deploy_device_app_start_time = time()
            try:
                logger.info("Deploying Device App... ")

                _return_deploy_device_app = self._deploy_device_app_obj.deploy_device_app(
                    app_name=_local_params["app_name"],
                    version_number=_local_params["version_number"],
                    device_ids=_local_params["device_ids"],
                    deploy_parameter=_local_params["deploy_parameter"],
                    comment=_local_params["comment"],
                )
                if (
                    "result" in _return_deploy_device_app
                    and _return_deploy_device_app["result"] == "SUCCESS"
                ):
                    device_ids_list = [item.strip() for item in device_ids.split(",")]
                    _deploy_device_app_status = None
                    _count = 0

                    # Wait till Deploy status is canceled, failed or success
                    while True:
                        # Get Device App Deploys Status
                        _return_get_device_app_deploy_status = (
                            self._get_device_app_deploy_status_obj.get_device_app_deploys(
                                app_name=_local_params["app_name"],
                                version_number=_local_params["version_number"],
                            )
                        )

                        # Check Get Device App Deploys Status is not None
                        if _return_get_device_app_deploy_status:
                            # Get the length of the "deploys" array
                            deploy_response_length = len(
                                _return_get_device_app_deploy_status["deploys"]
                            )

                            # traverse "devices" array from the "deploys" array
                            for index in range(deploy_response_length):
                                _deploy_device_app_status_json = (
                                    _return_get_device_app_deploy_status["deploys"][index][
                                        "devices"
                                    ]
                                )
                                # traverse device_id status from the "devices" array
                                for devices_id_index, devices_json in enumerate(
                                    _deploy_device_app_status_json
                                ):
                                    _deploy_device_app_status = _deploy_device_app_status_json[
                                        devices_id_index
                                    ]["status"]
                                    devices_id_from_response = _deploy_device_app_status_json[
                                        devices_id_index
                                    ]["device_id"]

                                    # check if the device_id is present in user provided
                                    # devices list
                                    if devices_id_from_response in device_ids_list:
                                        # Check if the device_id is not present in global array,
                                        # Then, add the first occurence of device_id to the
                                        # global array.
                                        # Set found_position of the first occurence of device_id
                                        # to the global array
                                        if devices_id_from_response not in [
                                            list(d.keys())[0]
                                            for i, d in enumerate(
                                                self._deploy_callback_status_array
                                            )
                                        ]:
                                            self._set_values(
                                                device_id=devices_id_from_response,
                                                found_position=index + 1,
                                                status=_deploy_device_app_status,
                                            )

                                        # Check if the device_id is present in global array,
                                        # Then get the found_position of the first occurence
                                        # of device_id from the global array
                                        # and get the skip value of the first occurence of
                                        # device_id from the global array
                                        elif (
                                            devices_id_from_response
                                            in [
                                                list(d.keys())[0]
                                                for i, d in enumerate(
                                                    self._deploy_callback_status_array
                                                )
                                            ]
                                            and len(self._deploy_callback_status_array) != 0
                                        ):
                                            array_device_json = self._get_values(
                                                devices_id_from_response
                                            )
                                            _found_position = array_device_json["found_position"]
                                            _skip = array_device_json["skip"]

                                            # Check whether it's first occurence
                                            # Then Add status of the added device to
                                            # the global array
                                            if index + 1 == _found_position and _skip == 0:
                                                self._set_values(
                                                    device_id=devices_id_from_response,
                                                    status=_deploy_device_app_status,
                                                    found_position=_found_position,
                                                    skip=_skip,
                                                )

                                                # if deployment status is canceled,
                                                # completed successfully or failed,
                                                # then set the skip value as 1 of the respective
                                                # device in global array
                                                # and prepare response with required information
                                                if _deploy_device_app_status in [
                                                    DeployDeviceAppStatus.DEPLOYMENT_DONE.value,
                                                    DeployDeviceAppStatus.DEPLOYMENT_CANCELED.value,
                                                    DeployDeviceAppStatus.DEPLOYMENT_FAILED.value,
                                                ]:
                                                    # Set the skip value as 1 of the respective
                                                    # device in global array
                                                    self._set_values(
                                                        device_id=devices_id_from_response,
                                                        status=_deploy_device_app_status,
                                                        found_position=_found_position,
                                                        skip=1,
                                                    )

                                                    # Fill Response information for selected
                                                    # device_id
                                                    _return_deploy_device_app_wait_response = {}

                                                    # "result"
                                                    _return_deploy_device_app_wait_response[
                                                        "result"
                                                    ] = _deploy_status[_deploy_device_app_status]

                                                    # "device_id"
                                                    _return_deploy_device_app_wait_response[
                                                        "device_id"
                                                    ] = devices_id_from_response

                                                    # "process_time"
                                                    deploy_device_app_end_time = time()
                                                    deploy_time_seconds = (
                                                        deploy_device_app_end_time
                                                        - deploy_device_app_start_time
                                                    )
                                                    # convert seconds to "HH:MM:SS" format
                                                    # pylint:disable=line-too-long
                                                    total_deploy_device_app_time_str = f"{str(timedelta(seconds=deploy_time_seconds))}"
                                                    _return_deploy_device_app_wait_response[
                                                        "process_time"
                                                    ] = total_deploy_device_app_time_str

                                                    # append the respective device_id's
                                                    # deploy_by_configuration_wait_response
                                                    # to the array
                                                    # _return_deploy_device_app_wait_response_all_device_ids

                                                    _return_deploy_device_app_wait_response_all_device_ids.append(
                                                        _return_deploy_device_app_wait_response
                                                    )

                                                    _count += 1

                                    # break the for loop
                                    # traverse device_id status from the "devices" array
                                    elif len(device_ids_list) == _count:
                                        break

                                    # ignore the devices_id_from_response as not available
                                    # in device_ids_list
                                    else:
                                        continue

                                # break the for loop
                                # traverse "devices" array from the "deploys" array
                                if len(device_ids_list) == _count:
                                    break

                            # Update Callback function
                            if callback is not None:
                                callback(self._deploy_callback_status_array)

                            # break the main loop if all device ids are updated
                            if len(device_ids_list) == _count:
                                break

                    return _return_deploy_device_app_wait_response_all_device_ids

                # Return deploy_device_app response
                _return_deploy_device_app_wait_response = _return_deploy_device_app

            except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                _return_deploy_device_app_wait_response = self.on_key_error_response(
                    __name__, key_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                _return_deploy_device_app_wait_response = self.on_type_error_response(
                    __name__, type_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                _return_deploy_device_app_wait_response = self.on_value_error_response(
                    __name__, val_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                _return_deploy_device_app_wait_response = self.on_attribute_error_response(
                    __name__, attr_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                _return_deploy_device_app_wait_response = self.on_http_error_response(
                    __name__, exception
                )

            except Exception as exception:
                _return_deploy_device_app_wait_response = self.on_generic_error_response(
                    __name__, exception
                )

        except ValidationError as err:
            _return_deploy_device_app_wait_response = self.on_validation_error_response(
                __name__, err
            )

        return _return_deploy_device_app_wait_response
