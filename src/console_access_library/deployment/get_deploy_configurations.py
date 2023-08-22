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
# pylint:disable=protected-access
# pylint:disable=broad-except

import logging
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import deploy_api

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass

logger = logging.getLogger(__name__)


class GetDeployConfigurations(ConsoleAccessBaseClass):
    """This class implements GetDeployConfigurations API.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class GetDeployConfigurations

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

    def get_deploy_configurations(self):
        """Get deployment config information list.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-----------------+------------+------------+---------------------------------+
                | *Level1*        | *Level2*   | *Type*     | *Description*                   |
                +-----------------+------------+------------+---------------------------------+
                |``deploy_        |            | ``array``  | Ascending order of              |
                |configurations`` |            |            | config_id                       |
                +-----------------+------------+------------+---------------------------------+
                |                 |``config_   | ``string`` |                                 |
                |                 |id``        |            |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``device_   | ``string`` |                                 |
                |                 |type``      |            |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``config_   | ``string`` |                                 |
                |                 |comment``   |            |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``running_  | ``int``    |                                 |
                |                 |cnt``       |            |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``success_  | ``int``    |                                 |
                |                 |cnt``       |            |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``fail_cnt``| ``int``    |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``firmware``| ``array``  | Refer :ref:`firmware <f1>`      |
                |                 |            |            | for more details                |
                +-----------------+------------+------------+---------------------------------+
                |                 |``model``   | ``array``  | Refer :ref:`model <m1>`         |
                |                 |            |            | for more details                |
                +-----------------+------------+------------+---------------------------------+
                |                 |``custom_   | ``array``  | Refer :ref:`custom_setting <c1>`|
                |                 |setting``   |            | for more details                |
                +-----------------+------------+------------+---------------------------------+
                |                 |``ins_id``  | ``string`` |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``ins_date``| ``string`` |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``upd_id``  | ``string`` |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``upd_date``| ``string`` |                                 |
                +-----------------+------------+------------+---------------------------------+

                +-------------------+--------------------+------------+-------------------+
                | firmware          | .. _f1:                                             |
                +-------------------+--------------------+------------+-------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*     |
                +-------------------+--------------------+------------+-------------------+
                | ``firmware``      |                    | ``array``  |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``sensor_loader_    | ``string`` |                   |
                |                   |file_name``         |            |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``sensor_loader_    | ``string`` |                   |
                |                   |version_number``    |            |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``sensor_loader_    | ``string`` |                   |
                |                   |firmware_comment``  |            |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``sensor_file_name``| ``string`` |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``sensor_           | ``string`` |                   |
                |                   |version_number``    |            |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``sensor_           |``string``  |                   |
                |                   |firmware_comment``  |            |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``apfw_file_name``  |``string``  |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``apfw_version_     |``string``  |                   |
                |                   |number``            |            |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``apfw_firmware_    |``string``  |                   |
                |                   |comment``           |            |                   |
                +-------------------+--------------------+------------+-------------------+

                +-------------------+--------------------+------------+-------------------+
                | model             | .. _m1:                                             |
                +-------------------+--------------------+------------+-------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*     |
                +-------------------+--------------------+------------+-------------------+
                | ``model``         |                    | ``array``  |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``model_id``       | ``string`` |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``model_            | ``string`` |                   |
                |                   |version_number``    |            |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``model_comment``  | ``string`` |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``model_            | ``string`` |                   |
                |                   |version_comment``   |            |                   |
                +-------------------+--------------------+------------+-------------------+

                +--------------+--------------------+------------+---------------+
                |custom_setting| .. _c1:                                         |
                +--------------+--------------------+------------+---------------+
                | *Level1*     | *Level2*           | *Type*     | *Description* |
                +--------------+--------------------+------------+---------------+
                |``custom_     |                    | ``array``  |               |
                |setting``     |                    |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``color_matrix_     |``string``  |               |
                |              |mode``              |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``color_matrix_     | ``string`` |               |
                |              |file_name``         |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``color_matrix_     |``string``  |               |
                |              |comment``           |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``gamma_            |``string``  |               |
                |              |mode``              |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``gamma_            |``string``  |               |
                |              |file_name``         |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``gamma_            |``string``  |               |
                |              |comment``           |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``lscisp_           |``string``  |               |
                |              |mode``              |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``lscisp_           |``string``  |               |
                |              |file_name``         |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``lscisp_           |``string``  |               |
                |              |comment``           |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``lscraw_           |``string``  |               |
                |              |mode``              |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``lscraw_           |``string``  |               |
                |              |file_name``         |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``lscraw_           |``string``  |               |
                |              |comment``           |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``prewb_            |``string``  |               |
                |              |mode``              |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``prewb_            |``string``  |               |
                |              |file_name``         |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``prewb_            |``string``  |               |
                |              |comment``           |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``dewarp_           |``string``  |               |
                |              |mode``              |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``dewarp_           |``string``  |               |
                |              |file_name``         |            |               |
                +--------------+--------------------+------------+---------------+
                |              |``dewarp_           |``string``  |               |
                |              |comment``           |            |               |
                +--------------+--------------------+------------+---------------+

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

                # Deployment - GetDeployConfigurations
                response = deployment_obj.get_deploy_configurations()
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        # Enter a context with an instance of the API client
        with aitrios_console_rest_client_sdk_primitive.ApiClient(
            self._config.configuration,
            header_name="Authorization",
            header_value=self._config.get_access_token(),
        ) as api_client:
            # Create an instance of the API class
            get_deploy_configurations_api_instance = deploy_api.DeployApi(api_client)
            try:
                _return_get_deploy_configurations = (
                    get_deploy_configurations_api_instance.get_deploy_configurations()
                )
                return _return_get_deploy_configurations.body

            except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                _return_get_deploy_configurations = self.on_key_error_response(__name__, key_err)

            except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                _return_get_deploy_configurations = self.on_type_error_response(__name__, type_err)

            except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                _return_get_deploy_configurations = self.on_value_error_response(__name__, val_err)

            except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                _return_get_deploy_configurations = self.on_attribute_error_response(
                    __name__, attr_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                _return_get_deploy_configurations = self.on_http_error_response(__name__, exception)

            except Exception as exception:
                _return_get_deploy_configurations = self.on_generic_error_response(
                    __name__, exception
                )

            return _return_get_deploy_configurations
