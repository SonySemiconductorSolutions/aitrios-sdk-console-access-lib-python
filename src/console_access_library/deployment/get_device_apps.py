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
# pylint:disable=protected-access
# pylint:disable=broad-except
# pylint:disable=too-many-return-statements

import logging
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import device_app_api

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass

logger = logging.getLogger(__name__)


class GetDeviceApps(ConsoleAccessBaseClass):
    """This class implements GetDeviceApps API.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class GetDeviceApps

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

    def get_device_apps(self):
        """Get the device app list information.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +----------+-------------+------------+------------------------------------------+
                | *Level1* | *Level2*    | *Type*     | *Description*                            |
                +==========+=============+============+==========================================+
                | ``apps`` |             | ``array``  |                                          |
                +----------+-------------+------------+------------------------------------------+
                |          | ``name``    | ``string`` | Set the app name.                        |
                +----------+-------------+------------+------------------------------------------+
                |          |``create_by``| ``string`` | Set the create_by.                       |
                |          |             |            |                                          |
                |          |             |            | - Value definition                       |
                |          |             |            |                                          |
                |          |             |            | Self: Self-training models               |
                |          |             |            |                                          |
                |          |             |            | Marketplace: Marketplace purchacing model|
                +----------+-------------+------------+------------------------------------------+
                |          |``package_   | ``string`` | Set the marketplace package ID.          |
                |          |id``         |            |                                          |
                +----------+-------------+------------+------------------------------------------+
                |          |``product    | ``string`` | Set the marketplace product ID.          |
                |          |_id``        |            |                                          |
                +----------+-------------+------------+------------------------------------------+
                |          |``schema_    | ``array``  | Refer :ref:`schema_info <schema_info>`   |
                |          |info``       |            | for more details                         |
                +----------+-------------+------------+------------------------------------------+
                |          |``versions`` | ``array``  | Refer :ref:`versions <versions_elements>`|
                |          |             |            | for more details                         |
                +----------+-------------+------------+------------------------------------------+


                +-------------------+-----------------+------------+-------------------------------+
                | schema_info       | .. _schema_info:                                             |
                +-------------------+-----------------+------------+-------------------------------+
                | *Level1*          | *Level2*        | *Type*     | *Description*                 |
                +===================+=================+============+===============================+
                | ``schema_info``   |                 | ``array``  | Schema info.                  |
                +-------------------+-----------------+------------+-------------------------------+
                |                   | ``VnSAppId``    | ``string`` | Set the VnS app ID            |
                +-------------------+-----------------+------------+-------------------------------+
                |                   | ``version``     | ``string`` | Set the app version no.       |
                +-------------------+-----------------+------------+-------------------------------+
                |                   | ``interfaces``  | ``array``  |Refer :ref:`interfaces <inter>`|
                |                   |                 |            |for more details               |
                +-------------------+-----------------+------------+-------------------------------+

                +-------------------+-----------------+------------+-------------------------------+
                | interfaces        | .. _inter:                                                   |
                +-------------------+-----------------+------------+-------------------------------+
                | *Level1*          | *Level2*        | *Type*     | *Description*                 |
                +===================+=================+============+===============================+
                | ``interfaces``    |                 | ``array``  | Set the metadata format IDs.  |
                +-------------------+-----------------+------------+-------------------------------+
                |                   | ``in``          | ``array``  | Refer :ref:`in <in>`          |
                |                   |                 |            | for more details              |
                +-------------------+-----------------+------------+-------------------------------+

                +-------------------+-----------------+------------+-------------------------------+
                | in                | .. _in:                                                      |
                +-------------------+-----------------+------------+-------------------------------+
                | *Level1*          | *Level2*        | *Type*     | *Description*                 |
                +===================+=================+============+===============================+
                | ``in``            |                 | ``array``  |                               |
                +-------------------+-----------------+------------+-------------------------------+
                |                   |``metadata       | ``string`` | Set the metadata format ID.   |
                |                   |FormatId``       |            |                               |
                +-------------------+-----------------+------------+-------------------------------+

                +-------------------+--------------------+------------+-------------------+
                | versions          | .. _versions_elements:                              |
                +-------------------+--------------------+------------+-------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*     |
                +===================+====================+============+===================+
                | ``versions``      |                    | ``array``  |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``version``        | ``string`` | Set the app       |
                |                   |                    |            | version number.   |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``compiled_flg``   | ``string`` | Set the compiled  |
                |                   |                    |            | flg.              |
                |                   |                    |            |                   |
                |                   |                    |            | - Value definition|
                |                   |                    |            |                   |
                |                   |                    |            | 0 : Specified App |
                |                   |                    |            | is not compiled   |
                |                   |                    |            |                   |
                |                   |                    |            | 1 : Specified App |
                |                   |                    |            | is compiled       |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``status``         | ``string`` | Set the status.   |
                |                   |                    |            |                   |
                |                   |                    |            | - Value definition|
                |                   |                    |            |                   |
                |                   |                    |            | 0: before         |
                |                   |                    |            | compilation       |
                |                   |                    |            |                   |
                |                   |                    |            | 1: during         |
                |                   |                    |            | compilation       |
                |                   |                    |            |                   |
                |                   |                    |            | 2: successful     |
                |                   |                    |            |                   |
                |                   |                    |            | 3: failed         |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``comment``        | ``string`` | Set the comment.  |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``deploy_count``   | ``string`` | Set the deploy    |
                |                   |                    |            | count.            |
                +-------------------+--------------------+------------+-------------------+
                |                   |  ``ins_id``        |``string``  | Set the settings  |
                |                   |                    |            | author.           |
                +-------------------+--------------------+------------+-------------------+
                |                   |  ``ins_date``      |``string``  | Set the date the  |
                |                   |                    |            | settings were     |
                |                   |                    |            | created.          |
                +-------------------+--------------------+------------+-------------------+
                |                   |  ``upd_id``        |``string``  | Set the settings  |
                |                   |                    |            | updater.          |
                +-------------------+--------------------+------------+-------------------+
                |                   |  ``upd_date``      |``string``  | Set the date the  |
                |                   |                    |            | settings were     |
                |                   |                    |            | updated.          |
                +-------------------+--------------------+------------+-------------------+

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

                # Deployment - GetDeviceApps
                response = deployment_obj.get_device_apps()
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)
        _query_params = {}

        # Enter a context with an instance of the API client
        with aitrios_console_rest_client_sdk_primitive.ApiClient(
            self._config.configuration,
            header_name="Authorization",
            header_value=self._config.get_access_token(),
        ) as api_client:
            # Create an instance of the API class
            get_device_apps_api_instance = device_app_api.DeviceAppApi(api_client)
            try:
                # Adding Parameters to Connect to an Enterprise Edition Environment
                if self._config._application_id:
                    _query_params["grant_type"] = "client_credentials"
                    _return_get_device_apps = get_device_apps_api_instance.get_device_apps(
                        query_params=_query_params)
                else:
                    _return_get_device_apps = get_device_apps_api_instance.get_device_apps()
                return _return_get_device_apps.body

            except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                _return_get_device_apps = self.on_key_error_response(__name__, key_err)

            except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                _return_get_device_apps = self.on_type_error_response(__name__, type_err)

            except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                _return_get_device_apps = self.on_value_error_response(__name__, val_err)

            except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                _return_get_device_apps = self.on_attribute_error_response(__name__, attr_err)

            except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                _return_get_device_apps = self.on_http_error_response(__name__, exception)

            except Exception as exception:
                _return_get_device_apps = self.on_generic_error_response(__name__, exception)

            return _return_get_device_apps
