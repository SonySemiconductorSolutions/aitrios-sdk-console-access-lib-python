# ------------------------------------------------------------------------
# Copyright 2022, 2023 Sony Semiconductor Solutions Corp. All rights reserved.

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
# pylint:disable=too-many-locals
# pylint:disable=too-many-return-statements
# pylint:disable=protected-access
# pylint:disable=broad-except

import logging
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import deploy_api
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass

logger = logging.getLogger(__name__)


class SchemaGetDeployHistory(Schema):
    """Schema for GetDeployHistory API

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : Device ID.
    device_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for device_id"}, strict=True
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if str(data["device_id"]).strip() == "":
            raise ValidationError("device_id is required or can't be empty string")


class GetDeployHistory(ConsoleAccessBaseClass):
    """This class implements GetDeployHistory API.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class GetDeployHistory

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

    def get_deploy_history(
        self,
        device_id: str,
    ):
        """Get deploy history for a specified device.

        Args:
            device_id (str, required) : Device ID.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +----------+----------------------+------------+-------------------------------+
                | *Level1* | *Level2*             | *Type*     | *Description*                 |
                +==========+======================+============+===============================+
                |``deploy  |                      | ``array``  |                               |
                |s``       |                      |            |                               |
                +----------+----------------------+------------+-------------------------------+
                |          | ``id``               | ``integer``| Deploy ID.                    |
                +----------+----------------------+------------+-------------------------------+
                |          | ``deploy_type``      | ``string`` | Set the deploy type.          |
                |          |                      |            | - Value definition            |
                |          |                      |            |                               |
                |          |                      |            | 0: Deploy config              |
                |          |                      |            |                               |
                |          |                      |            | 1: Device model               |
                |          |                      |            |                               |
                |          |                      |            | App: DeviceApp                |
                +----------+----------------------+------------+-------------------------------+
                |          |``deploy_status``     | ``string`` | Set the deploy status. Target |
                |          |                      |            | device deployment status.     |
                |          |                      |            | - Value definition            |
                |          |                      |            |                               |
                |          |                      |            | 0: Deploying                  |
                |          |                      |            |                               |
                |          |                      |            | 1: Success                    |
                |          |                      |            |                               |
                |          |                      |            | 2: Fail                       |
                |          |                      |            |                               |
                |          |                      |            | 3: Cancel                     |
                |          |                      |            |                               |
                |          |                      |            | App: DeviceApp undeploy       |
                +----------+----------------------+------------+-------------------------------+
                |          |``update_progress``   | ``string`` | Set the update progress in    |
                |          |                      |            | percentage.                   |
                +----------+----------------------+------------+-------------------------------+
                |          |``deploy_comment``    | ``string`` | Set the deploy comment.       |
                +----------+----------------------+------------+-------------------------------+
                |          |  ``config_id``       | ``string`` | Set the deploy config ID.     |
                +----------+----------------------+------------+-------------------------------+
                |          |``replace_network_id``| ``string`` | Set the replace network ID.   |
                +----------+----------------------+------------+-------------------------------+
                |          | ``current_target``   | ``string`` | Set the current target.       |
                +----------+----------------------+------------+-------------------------------+
                |          |``total_status``      | ``string`` | Set the deploy status.        |
                |          |                      |            | Total status of devices       |
                |          |                      |            | deployed together.            |
                |          |                      |            | - Value definition            |
                |          |                      |            |                               |
                |          |                      |            | 0: Deploying                  |
                |          |                      |            |                               |
                |          |                      |            | 1: Success                    |
                |          |                      |            |                               |
                |          |                      |            | 2: Fail                       |
                |          |                      |            |                               |
                |          |                      |            | 3: Cancel                     |
                +----------+----------------------+------------+-------------------------------+
                |          | ``app_name``         | ``string`` | Set the app name.             |
                +----------+----------------------+------------+-------------------------------+
                |          | ``version_number``   | ``string`` | Set the version number.       |
                +----------+----------------------+------------+-------------------------------+
                |          | ``firmware``         | ``array``  |Refer :ref:`firmware <f8>`     |
                |          |                      |            |for more details               |
                +----------+----------------------+------------+-------------------------------+

                +------------+--------------------+------------+-----------------------------------+
                | firmware   | .. _f8:                                                             |
                +------------+--------------------+------------+-----------------------------------+
                | *Level1*   | *Level2*           | *Type*     | *Description*                     |
                +============+====================+============+===================================+
                |``firmware``|                    | ``array``  |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    | ``string`` | Set the deploy target flg.        |
                |            |target_flg``        |            | - Value definition                |
                |            |                    |            |                                   |
                |            |                    |            | 0: Not for deployment             |
                |            |                    |            |                                   |
                |            |                    |            | 1: Deployment target              |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    |``string``  | Set the deploy status.            |
                |            |status``            |            | - Value definition                |
                |            |                    |            |                                   |
                |            |                    |            | 0: Waiting                        |
                |            |                    |            |                                   |
                |            |                    |            | 1: Deploying                      |
                |            |                    |            |                                   |
                |            |                    |            | 2: Success                        |
                |            |                    |            |                                   |
                |            |                    |            | 3: Fail                           |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    |``integer`` | Set the sensor loader retry count.|
                |            |retry_count``       |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    |``string``  | Set the sensor loader start date. |
                |            |start_date``        |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    | ``string`` | Set the sensor loader end date.   |
                |            |end_date``          |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    |``string``  | Set the sensor loader version     |
                |            |version_number``    |            | number.                           |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    |``string``  | Set the sensor loader version     |
                |            |version_comment``   |            | comment.                          |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_target_    |``string``  | Set the deploy target flg.        |
                |            |flg``               |            | - Value definition                |
                |            |                    |            |                                   |
                |            |                    |            | 0: Not for deployment             |
                |            |                    |            |                                   |
                |            |                    |            | 1: Deployment target              |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_status``   | ``string`` | Set the deploy status.            |
                |            |                    |            |                                   |
                |            |                    |            | - Value definition                |
                |            |                    |            |                                   |
                |            |                    |            | 0: Waiting                        |
                |            |                    |            |                                   |
                |            |                    |            | 1: Deploying                      |
                |            |                    |            |                                   |
                |            |                    |            | 2: Success                        |
                |            |                    |            |                                   |
                |            |                    |            | 3: Fail                           |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_retry_     |``integer`` | Set the sensor retry count.       |
                |            |count``             |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_start_     |``string``  | Set the sensor start date.        |
                |            |date``              |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_end_date`` |``string``  | Set the sensor end date.          |
                |            |                    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_version_   |``string``  | Set the sensor version number.    |
                |            |number``            |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_version_   |``string``  | Set the sensor version comment.   |
                |            |comment``           |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_target_flg`` |``string``  | Set the deploy target flg.        |
                |            |                    |            |                                   |
                |            |                    |            |- Value definition                 |
                |            |                    |            |                                   |
                |            |                    |            | 0: Not for deployment             |
                |            |                    |            |                                   |
                |            |                    |            | 1: Deployment target              |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_status``     |``string``  | Set the deploy status.            |
                |            |                    |            |                                   |
                |            |                    |            | - Value definition                |
                |            |                    |            |                                   |
                |            |                    |            | 0: Waiting                        |
                |            |                    |            |                                   |
                |            |                    |            | 1: Deploying                      |
                |            |                    |            |                                   |
                |            |                    |            | 2: Success                        |
                |            |                    |            |                                   |
                |            |                    |            | 3: Fail                           |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_retry_count``|``integer`` | Set the appfw retry count.        |
                |            |                    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_start_date`` |``string``  | Set the appfw start date.         |
                |            |                    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_end_date``   |``string``  | Set the appfw end date.           |
                |            |                    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_version_     |``string``  | Set the appfw version number.     |
                |            |number``            |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_version_     |``string``  | Set the appfw version comment.    |
                |            |comment``           |            |                                   |
                +------------+--------------------+------------+-----------------------------------+

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
                #     application_id: "__application_id__"

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
                    read_console_access_settings_obj.client_secret,
                    read_console_access_settings_obj.application_id
                )

                # Instantiate Console Access Library Client.
                client_obj = Client(config_obj)

                # Create Instance for Deployment
                deployment_obj = client_obj.get_deployment()

                # set the real value
                device_id =  "__device_id__"

                # Deployment - GetDeployHistory
                response = deployment_obj.get_deploy_history(device_id)
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()
            _query_params = {}
            # delete local argument 'self' form locals() for validation.
            if "self" in _local_params:
                del _local_params["self"]

            # Validate schema
            _local_params = SchemaGetDeployHistory().load(_local_params)

            # Enter a context with an instance of the API client
            with aitrios_console_rest_client_sdk_primitive.ApiClient(
                self._config.configuration,
                header_name="Authorization",
                header_value=self._config.get_access_token(),
            ) as api_client:
                # Create an instance of the API class
                get_deploy_history_api_instance = deploy_api.DeployApi(api_client)
                try:
                    # Adding Parameters to Connect to an Enterprise Edition Environment
                    if self._config._application_id:
                        _query_params["grant_type"] = "client_credentials"
                        # pylint:disable=line-too-long
                        _return_get_deploy_history = get_deploy_history_api_instance.get_deploy_history(
                            path_params=_local_params, query_params=_query_params
                        )
                    else:
                        _return_get_deploy_history = get_deploy_history_api_instance.get_deploy_history(
                            path_params=_local_params
                        )

                    return _return_get_deploy_history.body

                except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                    _return_get_deploy_history = self.on_key_error_response(__name__, key_err)

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_get_deploy_history = self.on_type_error_response(__name__, type_err)

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_get_deploy_history = self.on_value_error_response(__name__, val_err)

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_get_deploy_history = self.on_attribute_error_response(
                        __name__, attr_err
                    )

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_get_deploy_history = self.on_http_error_response(__name__, exception)

                except Exception as exception:
                    _return_get_deploy_history = self.on_generic_error_response(__name__, exception)

        except ValidationError as err:
            _return_get_deploy_history = self.on_validation_error_response(__name__, err)

        return _return_get_deploy_history
