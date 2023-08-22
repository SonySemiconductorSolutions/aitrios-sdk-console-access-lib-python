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
# pylint:disable=too-many-nested-blocks
# pylint:disable=protected-access
# pylint:disable=no-value-for-parameter
# pylint:disable=too-many-statements
# pylint:disable=broad-except

import logging
import sys
import types
import warnings
from datetime import datetime, timedelta
from enum import Enum
from time import time

import aitrios_console_rest_client_sdk_primitive
from marshmallow import Schema, ValidationError, fields, validates_schema

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass
from console_access_library.deployment.deploy_by_configuration import DeployByConfiguration
from console_access_library.deployment.get_deploy_history import GetDeployHistory

warnings.filterwarnings("ignore")
sys.path.append(".")

logger = logging.getLogger(__name__)


class SchemaDeployByConfigurationWaitResponse(Schema):
    """Schema for API to deployment by configuration wait response.
    Args:
        Schema (object): Inherited from Schema class of marshmallow
    """

    #: str, required : Configuration ID.
    config_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for config_id"}, strict=True
    )

    #: str, required :  Device ID. Specify multiple device IDs separated by commas.
    device_ids = fields.String(
        required=True, error_messages={"invalid": "Invalid string for device_id"}, strict=True
    )

    #: str, optional : Model ID to be replaced. Specify "Model ID" or "network_id".
    #:                 If the specified model ID does not exist in the DB, the
    #:                 entered value is regarded as a network_id and processed is performed.
    replace_model_id = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for replace_model_id"},
        strict=True,
        allow_none=True,
    )

    #: str, optional : Deploy comment .
    comment = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for comment"},
        strict=True,
        allow_none=True,
    )

    #: int, optional : Timeout waiting for completion. There are cases where the edge
    #:                  AI device hangs up during the deployment process, so there
    #:                  are cases where the process remains in progress, so timeout to exit
    #:                  the process, 3600 seconds if not specified.
    timeout = fields.Integer(
        required=False,
        error_messages={"invalid": "Invalid Integer for timeout"},
        strict=True,
        allow_none=True,
    )

    #: function, optional : callback (function, optional) : A function handle of the form -
    #: ``deploy_callback(device_status_array)``, where ``device_status_array``
    #: is the array of the dictionary for each device :
    #: [
    #:     {
    #:         <device_id> : {
    #:             "status":<status>,
    #:         }
    #:     },
    #: ]

    #: here - ``device_id``: is device ID,
    #:     - ``status``: is the notified deployment status for that device_id,

    #: Callback function to check the deploying status with ``get_deploy_history``,
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
        if str(data["config_id"]).strip() == "":
            raise ValidationError("config_id is required or can't be empty string")

        if str(data["device_ids"]).strip() == "":
            raise ValidationError("device_ids is required or can't be empty string")

        if "replace_model_id" in data and (
            data["replace_model_id"] is None and str(data["replace_model_id"]).strip() == ""
        ):
            raise ValidationError("replace_model_id is required or can't be empty string")

        if "comment" in data and data["comment"] is not None and str(data["comment"]).strip() == "":
            raise ValidationError("comment is required or can't be empty string")

        if (
            "timeout" in data
            and data["timeout"] is None
            and (isinstance(data["timeout"], int) is False or data["timeout"] < 0)
        ):
            raise ValidationError(
                "timeout is required or timeout must be integer or can't be negative"
            )

        if (
            "callback" in data
            and data["callback"] is not None
            and (
                str(data["callback"]).strip() == ""
                or not isinstance(data["callback"], (types.FunctionType, types.MethodType))
            )
        ):
            raise ValidationError("callback is required or need to be a function/method")


class DeployByConfigurationStatus(Enum):
    """Deploy By Configuration Status Enum Values"""

    DEPLOYING = "0"
    SUCCESSFUL = "1"
    FAILED = "2"
    CANCELED = "3"
    DEVICEAPP_UNDEPLOY = "9"


class DeployByConfigurationWaitResponse(ConsoleAccessBaseClass):
    """This class implements API to wait completion for Deploy By Configuration.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class DeployByConfigurationWaitResponse

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config
        self._get_deploy_history_obj = GetDeployHistory(self._config)
        self._deploy_by_config_obj = DeployByConfiguration(self._config)
        self._deploy_callback_status_array = []

    def _set_values(self, device_id, status=""):
        """Update the device id deploy status information to global array

        Args:
            device_id (str): Device ID, Case sensitive
            status (str, optional): The notified deployment status for that device_id.
        """
        dict_ = {}
        if device_id is not None or device_id != "":
            if device_id not in [
                list(d.keys())[0] for i, d in enumerate(self._deploy_callback_status_array)
            ]:
                dict_[device_id] = {
                    "status": status,
                }
                self._deploy_callback_status_array.append(dict_)
            elif len(self._deploy_callback_status_array) != 0:
                for i, devices_array in enumerate(self._deploy_callback_status_array):
                    if device_id in devices_array:
                        self._deploy_callback_status_array[i][device_id] = {
                            "status": status,
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

    def deploy_by_configuration_wait_response(
        self,
        config_id: str,
        device_ids: str,
        replace_model_id: str = None,
        comment: str = None,
        timeout: int = None,
        callback=None,
    ):
        """Provides a function to deploy the following to the device specified from the
        deployment config.

        Args:
            config_id (str, required) : Configuration ID.
            device_ids (str, required) : Device ID. Specify multiple device IDs separated by commas.
            replace_model_id (str, optional) : Model ID to be replaced. Specify "Model ID" or \
                "network_id". If the specified model ID does not exist in the DB, the \
                entered value is regarded as a network_id and processed is performed.
            comment (str, optional) : Deploy comment .
            timeout (int, optional) : Timeout waiting for completion. There are cases where the \
                edge AI device hangs up during the deployment process,\
                so there are cases where the process remains in progress,\
                so timeout to exit the process,  3600 seconds if not specified.
            callback (function, optional) : A function handle of the form - \
                ``deploy_callback(device_status_array)``, where ``device_status_array`` \
                is the array of the dictionary for each device :

                .. code-block:: console

                    [
                        {
                            "<device_id>" : { "status":<status>,  }
                        },
                    ]

                - ``device_id``: is device ID,
                - ``status``: is the notified deployment status for that device_id,

                Callback function to check the deploying status with ``get_deploy_history``,\
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
                | ``No_item_name``  |                   | ``array``  | deploy by configuration    |
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
                    if any input integer parameter found negative OR
                    if any input non integer parameter found OR
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
                config_id = "__config_id__"
                device_ids = "__device_ids__",
                replace_model_id = "__replace_model_id__"
                comment = "__comment__"
                timeout = "__timeout__"
                callback = "__callback__"

                # callback is user defined method
                def deploy_callback(deploy_status_array):
                    # Process callback received for the ``device_id`` with ``status`` from \
                    # ``device_status_array``:
                    # is the array of the dictionary for each device :
                    # [
                    #     {
                    #         <device_id> : {
                    #             "status":<status>,
                    #         }
                    #     },
                    # ]\

                    # here - ``device_id``: is device ID,
                    #     - ``status``: is the notified deployment status for that device_id,

                # Deployment - DeployByConfigurationWaitResponse
                response = deployment_obj.deploy_by_configuration_wait_response(
                    config_id,
                    device_ids,
                    replace_model_id,
                    comment,
                    timeout,
                    callback
                )
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()
            _loop_timeout = None
            _return_deploy_by_configuration_wait_response = {}

            # delete local argument 'self' form locals() for validation.
            if "self" in _local_params:
                del _local_params["self"]

            # set default values, if not passed.
            if "timeout" in _local_params and _local_params["timeout"] is None:
                _local_params["timeout"] = 3600
                _loop_timeout = datetime.now() + timedelta(seconds=_local_params["timeout"])

            # Validate Schema
            _local_params = SchemaDeployByConfigurationWaitResponse().load(_local_params)
            _deploy_status = {
                DeployByConfigurationStatus.DEPLOYING.value: "deploying",
                DeployByConfigurationStatus.SUCCESSFUL.value: "successful",
                DeployByConfigurationStatus.FAILED.value: "failed",
                DeployByConfigurationStatus.CANCELED.value: "canceled",
                DeployByConfigurationStatus.DEVICEAPP_UNDEPLOY.value: "deviceapp_undeploy",
            }
            _return_deploy_by_configuration = None
            _return_deploy_by_configuration_wait_response_all_device_ids = []
            if not isinstance(device_ids, list):
                device_ids_list = [item.strip() for item in device_ids.split(",")]
            try:
                logger.info("Deploying... ")
                _deploy_start_time = time()

                _return_deploy_by_configuration = (
                    self._deploy_by_config_obj.deploy_by_configuration(
                        config_id=_local_params["config_id"],
                        device_ids=_local_params["device_ids"],
                        replace_model_id=_local_params["replace_model_id"],
                        comment=_local_params["comment"],
                    )
                )

                _count = 0
                if _return_deploy_by_configuration["result"] == "SUCCESS":
                    # Wait till Deploy status is canceled, failed or success
                    while True:
                        # Check deployment status for individual device_id
                        for _device_id in device_ids_list:
                            _total_status = None

                            # get deploy history for all devices
                            _return_get_deploy_history = (
                                self._get_deploy_history_obj.get_deploy_history(
                                    device_id=_device_id
                                )
                            )

                            # Check Get Deploy History is not None
                            if _return_get_deploy_history is not None:
                                # total number of deploy history configurations
                                _no_of_configs = len(_return_get_deploy_history["deploys"])
                                if _no_of_configs > 0:
                                    # loop through all deploy configurations to check the
                                    # deploy status of `config_id` passed as parameter
                                    for _config_id_index in range(_no_of_configs):
                                        _get_config_id = _return_get_deploy_history["deploys"][
                                            _config_id_index
                                        ]["config_id"]
                                        # check if config_id from response matches config_id
                                        # from user
                                        if _get_config_id == config_id:
                                            _total_status = _return_get_deploy_history["deploys"][
                                                _config_id_index
                                            ]["total_status"]

                                    # Check if the device_id is not present in global array,
                                    # Then, add the first occurence of device_id to the
                                    # global array.
                                    if _device_id not in [
                                        list(d.keys())[0]
                                        for i, d in enumerate(self._deploy_callback_status_array)
                                    ]:
                                        self._set_values(
                                            device_id=_device_id,
                                            status=_total_status,
                                        )

                                    # Check whether it's first occurence
                                    # Then update status of the added device to
                                    # the global array
                                    if _device_id in [
                                        list(d.keys())[0]
                                        for i, d in enumerate(self._deploy_callback_status_array)
                                    ]:
                                        self._set_values(
                                            device_id=_device_id,
                                            status=_total_status,
                                        )

                                        # Check whether the deployment for requested device_id
                                        # updated if deployment status is completed successfully
                                        # or failed, prepare response with required information
                                        if _total_status in [
                                            DeployByConfigurationStatus.SUCCESSFUL.value,
                                            DeployByConfigurationStatus.FAILED.value,
                                            DeployByConfigurationStatus.DEVICEAPP_UNDEPLOY.value,
                                            DeployByConfigurationStatus.CANCELED.value,
                                        ]:
                                            _return_deploy_by_configuration_wait_response = {}
                                            # deployment status is completed successfully,
                                            # prepare response with required information
                                            _return_deploy_by_configuration_wait_response[
                                                "result"
                                            ] = _deploy_status[_total_status]

                                            _return_deploy_by_configuration_wait_response[
                                                "device_id"
                                            ] = _device_id
                                            _deploy_end_time = time()
                                            _deploy_time_seconds = (
                                                _deploy_end_time - _deploy_start_time
                                            )

                                            # convert seconds to "HH:MM:SS" format
                                            _total_deploy_time_str = (
                                                f"{str(timedelta(seconds=_deploy_time_seconds))}"
                                            )
                                            _return_deploy_by_configuration_wait_response[
                                                "process_time"
                                            ] = _total_deploy_time_str

                                            # append the respective device_id's
                                            # deploy_by_configuration_wait_response to the array
                                            # pylint:disable=line-too-long
                                            # _return_deploy_by_configuration_wait_response_all_device_ids
                                            _return_deploy_by_configuration_wait_response_all_device_ids.append(
                                                _return_deploy_by_configuration_wait_response
                                            )

                                            _count += 1

                        # Update Callback function
                        if callback is not None:
                            callback(self._deploy_callback_status_array)

                        # Break the loop, if the deployment for all device_ids updated
                        if _count == len(device_ids_list):
                            break

                        # stop while loop, if deployment is taking more than
                        # `_loop_timeout` (in minutes)
                        _current_time = datetime.now()
                        if _current_time >= _loop_timeout:
                            break

                    return _return_deploy_by_configuration_wait_response_all_device_ids

                _return_deploy_by_configuration_wait_response = _return_deploy_by_configuration

            except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                _return_deploy_by_configuration_wait_response = self.on_key_error_response(
                    __name__, key_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                _return_deploy_by_configuration_wait_response = self.on_type_error_response(
                    __name__, type_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                _return_deploy_by_configuration_wait_response = self.on_value_error_response(
                    __name__, val_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                _return_deploy_by_configuration_wait_response = self.on_attribute_error_response(
                    __name__, attr_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                _return_deploy_by_configuration_wait_response = self.on_http_error_response(
                    __name__, exception
                )

            except Exception as exception:
                _return_deploy_by_configuration_wait_response = self.on_generic_error_response(
                    __name__, exception
                )

        except ValidationError as err:
            _return_deploy_by_configuration_wait_response = self.on_validation_error_response(
                __name__, err
            )

        return _return_deploy_by_configuration_wait_response
