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
# pylint:disable=broad-except

import logging
import re
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import deploy_api
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass

logger = logging.getLogger(__name__)


class SchemaCreateDeployConfiguration(Schema):
    """Schema for API to create deployment configuration.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : config_id.
    config_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for config_id"}, strict=True
    )

    #: str, optional : Config Description.
    comment = fields.String(
        required=False, error_messages={"invalid": "Invalid string for comment"}, strict=True
    )

    #: str, optional : SensorLoader version number
    sensor_loader_version_number = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for sensor_loader_version_number"},
        strict=True,
    )

    #: str, optional : Sensor version number
    sensor_version_number = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for sensor_version_number"},
        strict=True,
    )

    #: str, optional : Model ID
    model_id = fields.String(
        required=False, error_messages={"invalid": "Invalid string for model_id"}, strict=True
    )

    #: str, optional : Model version number
    model_version_number = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for model_version_number"},
        strict=True,
    )

    #: str, optional : ApFw version number
    ap_fw_version_number = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for ap_fw_version_number"},
        strict=True,
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if str(data["config_id"]).strip() == "":
            raise ValidationError("config_id is required or can't be empty string")

        if "comment" in data and (data["comment"] is None or str(data["comment"]).strip() == ""):
            raise ValidationError("comment is required or can't be empty string")

        if "sensor_loader_version_number" in data and (
            data["sensor_loader_version_number"] is None
            or str(data["sensor_loader_version_number"]).strip() == ""
        ):
            raise ValidationError(
                "sensor_loader_version_number is required or can't be empty string"
            )

        if "sensor_version_number" in data and (
            data["sensor_version_number"] is None
            or str(data["sensor_version_number"]).strip() == ""
        ):
            raise ValidationError("sensor_version_number is required or can't be empty string")

        if "model_id" in data and (data["model_id"] is None or str(data["model_id"]).strip() == ""):
            raise ValidationError("model_id is required or can't be empty string")

        if "model_version_number" in data and (
            data["model_version_number"] is None or str(data["model_version_number"]).strip() == ""
        ):
            raise ValidationError("model_version_number is required or can't be empty string")

        if "ap_fw_version_number" in data and (
            data["ap_fw_version_number"] is None or str(data["ap_fw_version_number"]).strip() == ""
        ):
            raise ValidationError("ap_fw_version_number is required or can't be empty string")


class CreateDeployConfiguration(ConsoleAccessBaseClass):
    """This class implements CreateDeployConfiguration API.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class CreateDeployConfiguration

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

    def create_deploy_configuration(
        self,
        config_id: str,
        comment: str = None,
        sensor_loader_version_number: str = None,
        sensor_version_number: str = None,
        model_id: str = None,
        model_version_number: str = None,
        ap_fw_version_number: str = None,
    ):
        """	Register the deployment config information to deploy the following to the device. \
        ・Firmware ・AI model

        Args:
            config_id (str, required) : The config ID. Up to 20 characters \
                half-width only. \
                The following characters are allowed \
                Alphanumeric characters \
                -hyphen \
                _ Underscore \
                () Small parentheses \
                . dot
            comment (str, optional) : 100 characters or less
            sensor_loader_version_number (str, optional) : If -1 is specified \
                the default version is applied The default value is system setting "DVC0017"
            sensor_version_number (str, optional) : If -1 is specified \
                the default version is applied The default value is system setting "DVC0018"
            model_id (str, optional) : The model_id. \
                If not specified, no model deployment.
            model_version_number (str, optional) : The Model version number. \
                If not specified, the latest version is applied.
            ap_fw_version_number (str, optional) : The ApFw version number. \
                If not specified, no firmware deployment.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+------------+-------------------------------+
                | *Level1*   | *Type*     | *Description*                 |
                +------------+------------+-------------------------------+
                | ``result`` | ``string`` | Set "SUCCESS" pinning         |
                +------------+------------+-------------------------------+

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
                    if any input string parameter found empty.
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
                comment = "__comment__"
                sensor_loader_version_number = "__sensor_loader_version_number__"
                sensor_version_number = "__sensor_version_number__"
                model_id = "__model_id__"
                model_version_number = "__model_version_number__"
                ap_fw_version_number = "__ap_fw_version_number__"

                # Deployment - CreateDeployConfiguration
                response = deployment_obj.create_deploy_configuration(
                    config_id,
                    comment,
                    sensor_loader_version_number,
                    sensor_version_number,
                    model_id,
                    model_version_number,
                    ap_fw_version_number,
                )
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()
            # delete local argument 'self' form locals() for validation.
            if "self" in _local_params:
                del _local_params["self"]

            # set default values, if not passed.
            if "comment" in _local_params and _local_params["comment"] is None:
                del _local_params["comment"]

            if (
                "sensor_loader_version_number" in _local_params
                and _local_params["sensor_loader_version_number"] is None
            ):
                del _local_params["sensor_loader_version_number"]

            if (
                "sensor_version_number" in _local_params
                and _local_params["sensor_version_number"] is None
            ):
                del _local_params["sensor_version_number"]

            if "model_id" in _local_params and _local_params["model_id"] is None:
                del _local_params["model_id"]

            if (
                "model_version_number" in _local_params
                and _local_params["model_version_number"] is None
            ):
                del _local_params["model_version_number"]

            if (
                "ap_fw_version_number" in _local_params
                and _local_params["ap_fw_version_number"] is None
            ):
                del _local_params["ap_fw_version_number"]

            # Validate Schema
            _local_params = SchemaCreateDeployConfiguration().load(_local_params)

            # config_id
            # Characters other than the following are forbidden characters
            # ・Alphanumeric・Underscore ·Dot ·Hyphen ·Small parentheses
            if _local_params["config_id"] is not None:
                if bool(re.match("^[A-Za-z0-9_()-.]*$", _local_params["config_id"])) is False:
                    raise ValidationError("config_id has forbidden characters")

            # Enter a context with an instance of the API client
            with aitrios_console_rest_client_sdk_primitive.ApiClient(
                self._config.configuration,
                header_name="Authorization",
                header_value=self._config.get_access_token(),
            ) as api_client:
                # Create an instance of the API class
                create_deploy_configurations_api_instance = deploy_api.DeployApi(api_client)
                try:
                    _return_create_deploy_configurations = (
                        create_deploy_configurations_api_instance.create_deploy_configuration(
                            query_params=_local_params
                        )
                    )
                    return _return_create_deploy_configurations.body

                except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                    _return_create_deploy_configurations = self.on_key_error_response(
                        __name__, key_err
                    )

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_create_deploy_configurations = self.on_type_error_response(
                        __name__, type_err
                    )

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_create_deploy_configurations = self.on_value_error_response(
                        __name__, val_err
                    )

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_create_deploy_configurations = self.on_attribute_error_response(
                        __name__, attr_err
                    )

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_create_deploy_configurations = self.on_http_error_response(
                        __name__, exception
                    )

                except Exception as exception:
                    _return_create_deploy_configurations = self.on_generic_error_response(
                        __name__, exception
                    )

        except ValidationError as err:
            _return_create_deploy_configurations = self.on_validation_error_response(__name__, err)

        return _return_create_deploy_configurations
