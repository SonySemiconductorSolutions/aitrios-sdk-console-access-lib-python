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
# pylint:disable=too-many-instance-attributes
# pylint:disable=too-many-public-methods
# pylint:disable=duplicate-code
# pylint:disable=redefined-builtin
# pylint:disable=too-many-arguments
# pylint:disable=too-many-locals
# pylint:disable=too-many-lines
# pylint:disable=too-many-return-statements
# pylint:disable=too-many-function-args
# pylint:disable=no-value-for-parameter
# pylint:disable=unexpected-keyword-arg

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass
from console_access_library.deployment.cancel_deployment import CancelDeployment
from console_access_library.deployment.create_deploy_configuration import CreateDeployConfiguration
from console_access_library.deployment.delete_deploy_configuration import DeleteDeployConfiguration
from console_access_library.deployment.delete_device_app import DeleteDeviceApp
from console_access_library.deployment.deploy_by_configuration import DeployByConfiguration
from console_access_library.deployment.deploy_by_configuration_wait_response import (
    DeployByConfigurationStatus,
    DeployByConfigurationWaitResponse,
)
from console_access_library.deployment.deploy_device_app import DeployDeviceApp
from console_access_library.deployment.deploy_device_app_wait_response import (
    DeployDeviceAppStatus,
    DeployDeviceAppWaitResponse,
)
from console_access_library.deployment.get_deploy_configurations import GetDeployConfigurations
from console_access_library.deployment.get_deploy_history import GetDeployHistory
from console_access_library.deployment.get_device_app_deploys import GetDeviceAppDeploys
from console_access_library.deployment.get_device_apps import GetDeviceApps
from console_access_library.deployment.import_device_app import ImportDeviceApp
from console_access_library.deployment.undeploy_device_app import UndeployDeviceApp


class Deployment(ConsoleAccessBaseClass):
    """Abstract class to access Console Access Library Deployment \
        component APIs from Deployment component

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for Deployment Abstract class

        Args:
            config(object): Object of Configuration Class
        """
        super().__init__()
        self._get_device_apps_obj = GetDeviceApps(config)
        self._delete_device_app_obj = DeleteDeviceApp(config)
        self._import_device_app_obj = ImportDeviceApp(config)
        self._get_deploy_configurations_obj = GetDeployConfigurations(config)
        self._get_deploy_history_obj = GetDeployHistory(config)
        self._get_device_app_deploys_obj = GetDeviceAppDeploys(config)
        self._delete_deploy_configuration_obj = DeleteDeployConfiguration(config)
        self._undeploy_device_app_obj = UndeployDeviceApp(config)
        self._deploy_by_configuration_obj = DeployByConfiguration(config)
        self._create_deploy_configuration_obj = CreateDeployConfiguration(config)
        self._deploy_device_app_obj = DeployDeviceApp(config)
        self._cancel_deployment_obj = CancelDeployment(config)
        self._deploy_device_app_wait_response_obj = DeployDeviceAppWaitResponse(config)
        self._deploy_by_configuration_wait_response_obj = DeployByConfigurationWaitResponse(config)
        self.deploy_by_configuration_status_obj = DeployByConfigurationStatus
        self.deploy_device_app_status_obj = DeployDeviceAppStatus

    def get_device_apps(self):
        """Abstract function call to ``get_device_apps`` API

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +----------+-------------+------------+------------------------------------------+
                | *Level1* | *Level2*    | *Type*     | *Description*                            |
                +----------+-------------+------------+------------------------------------------+
                | ``apps`` |             | ``array``  | App array                                |
                +----------+-------------+------------+------------------------------------------+
                |          | ``name``    | ``string`` | App name                                 |
                +----------+-------------+------------+------------------------------------------+
                |          | ``versions``| ``array``  | Refer :ref:`versions <element1>`         |
                |          |             |            | for more details                         |
                +----------+-------------+------------+------------------------------------------+

                +-------------------+--------------------+------------+-------------------+
                | versions          | .. _element1:                                       |
                +-------------------+--------------------+------------+-------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*     |
                +-------------------+--------------------+------------+-------------------+
                | ``versions``      |                    | ``array``  |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``version``        | ``string`` |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``compiled_flg``   | ``string`` | 0: Uncompiled     |
                |                   |                    |            | (compile process) |
                |                   |                    |            |                   |
                |                   |                    |            | 1: Compiled (no   |
                |                   |                    |            | compilation       |
                |                   |                    |            | process)          |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``status``         | ``string`` | 0: Before         |
                |                   |                    |            | compilation       |
                |                   |                    |            |                   |
                |                   |                    |            | 1: Compiling      |
                |                   |                    |            |                   |
                |                   |                    |            | 2: Successful     |
                |                   |                    |            |                   |
                |                   |                    |            | 3: Failed         |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``comment``        | ``string`` |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``deploy_count``   | ``string`` |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |  ``ins_id``        |``string``  | App Version       |
                |                   |                    |            | Author            |
                +-------------------+--------------------+------------+-------------------+
                |                   |  ``ins_date``      |``string``  | Date and time the |
                |                   |                    |            | app version was   |
                |                   |                    |            | created           |
                +-------------------+--------------------+------------+-------------------+
                |                   |  ``upd_id``        |``string``  | App version       |
                |                   |                    |            | updated by        |
                +-------------------+--------------------+------------+-------------------+
                |                   |  ``upd_date``      |``string``  | Date and time the |
                |                   |                    |            | app version was   |
                |                   |                    |            | updated           |
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
        """
        return self._get_device_apps_obj.get_device_apps()

    def delete_device_app(self, app_name: str, version_number: str):
        """Abstract function call to ``delete_device_app`` API

        Args:
            app_name (str, required): DeviceApp name
            version_number (str, required): DeviceApp version

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
        """

        return self._delete_device_app_obj.delete_device_app(
            app_name=app_name, version_number=version_number
        )

    def import_device_app(
        self,
        compiled_flg: str,
        app_name: str,
        version_number: str,
        file_name: str,
        file_content: str,
        entry_point: str = None,
        comment: str = None,
    ):
        """Abstract function call to ``import_device_app`` API

        Args:
            compiled_flg (str, required): Compile flags.

                - 0: Not compiled (perform compilation)
                - 1: Compiled (Do not compile)

            app_name (str, required): DeviceApp name. The maximum number of \
                characters is app_name + version_number ⇐31. Characters other than the \
                following are forbidden characters

                    - Alphanumeric
                    - Underbar
                    - Dot

            version_number (str, required): DeviceApp version. The maximum number of \
                characters is app_name + version_number ⇐31. Characters other than the \
                following are forbidden characters

                    - Alphanumeric
                    - Underbar
                    - Dot

            comment (str, optional): DeviceApp Description. up to 100 characters \
                No comment if not specified.
            file_name (str, required): DeviceApp file name.
            file_content (str, required): Contents of DeviceApp file. Base64 encoded string.
            entry_point (str, optional): EVP module entry point. "ppl" if not specified.

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
        """
        return self._import_device_app_obj.import_device_app(
            compiled_flg, app_name, version_number, file_name, file_content, entry_point, comment
        )

    def get_deploy_configurations(self):
        """Abstract function call to ``get_deploy_configurations`` API

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
                |                 |``firmware``| ``array``  | Refer :ref:`firmware <f9>`      |
                |                 |            |            | for more details                |
                +-----------------+------------+------------+---------------------------------+
                |                 |``model``   | ``array``  | Refer :ref:`model <mm>`         |
                |                 |            |            | for more details                |
                +-----------------+------------+------------+---------------------------------+
                |                 |``custom_   | ``array``  | Refer :ref:`custom_setting <cc>`|
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
                | firmware          | .. _f9:                                             |
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
                | model             | .. _mm:                                             |
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
                |custom_setting| .. _cc:                                         |
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
        """
        return self._get_deploy_configurations_obj.get_deploy_configurations()

    def get_deploy_history(self, device_id: str):
        """Abstract function call to ``get_deploy_history`` API

        Args:
            device_id (str, required): ID of Edge AI device.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +----------+----------------------+------------+-------------------------------+
                | *Level1* | *Level2*             | *Type*     | *Description*                 |
                +----------+----------------------+------------+-------------------------------+
                |``deploy``|                      | ``array``  | Descending order of           |
                |          |                      |            | ins_date                      |
                +----------+----------------------+------------+-------------------------------+
                |          | ``id``               | ``number`` |                               |
                +----------+----------------------+------------+-------------------------------+
                |          | ``deploy_type``      | ``string`` | 0: Deployment configuration   |
                |          |                      |            |                               |
                |          |                      |            | 1: Device model, App:DeviceApp|
                +----------+----------------------+------------+-------------------------------+
                |          |``deploy_status``     | ``string`` | Total deployment status       |
                |          |                      |            | including other devices       |
                |          |                      |            |                               |
                |          |                      |            | 0: Deploying                  |
                |          |                      |            |                               |
                |          |                      |            | 1: Succeeding                 |
                |          |                      |            |                               |
                |          |                      |            | 2: failed                     |
                |          |                      |            |                               |
                |          |                      |            | 3: canceled                   |
                |          |                      |            |                               |
                |          |                      |            | 9: DeviceApp Undeploy         |
                +----------+----------------------+------------+-------------------------------+
                |          |``deploy_comment``    | ``string`` |                               |
                +----------+----------------------+------------+-------------------------------+
                |          |  ``config_id``       | ``string`` |                               |
                +----------+----------------------+------------+-------------------------------+
                |          |``replace_network_id``| ``string`` |                               |
                +----------+----------------------+------------+-------------------------------+
                |          | ``current_target``   | ``string`` |                               |
                +----------+----------------------+------------+-------------------------------+
                |          |``total_status``      | ``string`` | Total deployment status       |
                |          |                      |            | including other devices       |
                |          |                      |            |                               |
                |          |                      |            | 0: Deploying                  |
                |          |                      |            |                               |
                |          |                      |            | 1: Succeeding                 |
                |          |                      |            |                               |
                |          |                      |            | 2: failed                     |
                |          |                      |            |                               |
                |          |                      |            | 3: canceled                   |
                |          |                      |            |                               |
                |          |                      |            | 9: DeviceApp Undeploy         |
                +----------+----------------------+------------+-------------------------------+
                |          | ``firmware``         | ``array``  |Refer :ref:`firmware <f7>`     |
                |          |                      |            |for more details               |
                +----------+----------------------+------------+-------------------------------+
                |          |  ``model``           | ``array``  |Refer :ref:`model <m7>`        |
                |          |                      |            |for more details               |
                +----------+----------------------+------------+-------------------------------+
                |          |``custom_setting``    | ``array``  |Refer :ref:`custom_setting <s>`|
                |          |                      |            |for more details               |
                +----------+----------------------+------------+-------------------------------+
                |          |``ins_id``            | ``string`` |                               |
                +----------+----------------------+------------+-------------------------------+
                |          |``ins_date``          | ``string`` |                               |
                +----------+----------------------+------------+-------------------------------+
                |          |``upd_id``            | ``string`` |                               |
                +----------+----------------------+------------+-------------------------------+
                |          |``upd_date``          | ``string`` |                               |
                +----------+----------------------+------------+-------------------------------+

                +------------+--------------------+------------+-----------------------------------+
                | firmware   | .. _f7:                                                             |
                +------------+--------------------+------------+-----------------------------------+
                | *Level1*   | *Level2*           | *Type*     | *Description*                     |
                +------------+--------------------+------------+-----------------------------------+
                |``firmware``|                    | ``array``  |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    | ``string`` | 0: Not eligible                   |
                |            |target_flg``        |            |                                   |
                |            |                    |            | 1: Eligible                       |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    |``string``  | 0: Waiting to run                 |
                |            |status``            |            |                                   |
                |            |                    |            | 1: Running                        |
                |            |                    |            |                                   |
                |            |                    |            | 2: Successful                     |
                |            |                    |            |                                   |
                |            |                    |            | 3: Failed                         |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    |``string``  |                                   |
                |            |retry_count``       |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    |``string``  |                                   |
                |            |start_date``        |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    | ``string`` |                                   |
                |            |end_date``          |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    |``string``  |                                   |
                |            |version_number``    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_loader_    |``string``  |                                   |
                |            |version_comment``   |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_target_    |``string``  | 0: Not eligible                   |
                |            |flg``               |            |                                   |
                |            |                    |            | 1: Eligible                       |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_status``   | ``string`` | 0: Waiting to run                 |
                |            |                    |            |                                   |
                |            |                    |            | 1: Running                        |
                |            |                    |            |                                   |
                |            |                    |            | 2: Successful                     |
                |            |                    |            |                                   |
                |            |                    |            | 3: Failed                         |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_retry_     |``string``  |                                   |
                |            |count``             |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_start_     |``string``  |                                   |
                |            |date``              |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_end_date`` |``string``  |                                   |
                |            |                    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_version_   |``string``  |                                   |
                |            |number``            |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``sensor_version_   |``string``  |                                   |
                |            |comment``           |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_target_flg`` |``string``  | 0: Not eligible                   |
                |            |                    |            |                                   |
                |            |                    |            | 1: Eligible                       |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_status``     |``string``  | 0: Waiting to run                 |
                |            |                    |            |                                   |
                |            |                    |            | 1: Running                        |
                |            |                    |            |                                   |
                |            |                    |            | 2: Successful                     |
                |            |                    |            |                                   |
                |            |                    |            | 3: Failed                         |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_retry_count``|``string``  |                                   |
                |            |                    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_start_date`` |``string``  |                                   |
                |            |                    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_end_date``   |``string``  |                                   |
                |            |                    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_version_     |``string``  |                                   |
                |            |number``            |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``apfw_version_     |``string``  |                                   |
                |            |comment``           |            |                                   |
                +------------+--------------------+------------+-----------------------------------+

                +------------+--------------------+------------+-----------------------------------+
                | model      | .. _m7:                                                             |
                +------------+--------------------+------------+-----------------------------------+
                | *Level1*   | *Level2*           | *Type*     | *Description*                     |
                +------------+--------------------+------------+-----------------------------------+
                |``model``   |                    | ``array``  |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_target_flg``| ``string`` | 0: Not eligible                   |
                |            |                    |            |                                   |
                |            |                    |            | 1: Eligible                       |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_status``    |``string``  | 0: Waiting to run                 |
                |            |                    |            |                                   |
                |            |                    |            | 1: Running                        |
                |            |                    |            |                                   |
                |            |                    |            | 2: Successful                     |
                |            |                    |            |                                   |
                |            |                    |            | 3: Failed                         |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_retry_      |``string``  |                                   |
                |            |count``             |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_start_date``|``string``  |                                   |
                |            |                    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_end_date``  | ``string`` |                                   |
                |            |                    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_id``        |``string``  |                                   |
                |            |                    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_version_    |``string``  |                                   |
                |            |number``            |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_comment``   |``string``  |                                   |
                |            |                    |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_version_    | ``string`` |                                   |
                |            |comment``           |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``dnn_parame_set    |``string``  |                                   |
                |            |ting_target_flg``   |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``dnn_parame_       |``string``  |                                   |
                |            |settingstatus``     |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``dnn_parame_sett   |``string``  |                                   |
                |            |ing_retry_count``   |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``dnn_parame_set    |``string``  |                                   |
                |            |ting_start_date``   |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``dnn_parame_set    |``string``  |                                   |
                |            |ting_end_date``     |            |                                   |
                +------------+--------------------+------------+-----------------------------------+

                +--------------+--------------------+------------+---------------------------------+
                |custom_setting| .. _s:                                                            |
                +--------------+--------------------+------------+---------------------------------+
                | *Level1*     | *Level2*           | *Type*     | *Description*                   |
                +--------------+--------------------+------------+---------------------------------+
                |``custom_     |                    | ``array``  |                                 |
                |setting``     |                    |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``color_matrix_     | ``string`` | 0: Not eligible                 |
                |              |target_flg``        |            |                                 |
                |              |                    |            | 1: Eligible                     |
                +--------------+--------------------+------------+---------------------------------+
                |              |``color_matrix_     |``string``  | 0: Waiting to run               |
                |              |status``            |            |                                 |
                |              |                    |            | 1: Running                      |
                |              |                    |            |                                 |
                |              |                    |            | 2: Successful                   |
                |              |                    |            |                                 |
                |              |                    |            | 3: Failed                       |
                +--------------+--------------------+------------+---------------------------------+
                |              |``color_matrix_     | ``string`` |                                 |
                |              |retry_count``       |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``color_matrix_     |``string``  |                                 |
                |              |start_date``        |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``color_matrix_     | ``string`` |                                 |
                |              |end_date``          |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``color_matrix_     |``string``  |                                 |
                |              |mode``              |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``color_matrix_     | ``string`` |                                 |
                |              |file_name``         |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``color_matrix_     |``string``  |                                 |
                |              |comment``           |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``gamma_            |``string``  | 0: Not eligible                 |
                |              |target_flg``        |            |                                 |
                |              |                    |            | 1: Eligible                     |
                +--------------+--------------------+------------+---------------------------------+
                |              |``gamma_            |``string``  | 0: Waiting to run               |
                |              |status``            |            |                                 |
                |              |                    |            | 1: Running                      |
                |              |                    |            |                                 |
                |              |                    |            | 2: Successful                   |
                |              |                    |            |                                 |
                |              |                    |            | 3: Failed                       |
                +--------------+--------------------+------------+---------------------------------+
                |              |``gamma_            |``string``  |                                 |
                |              |retry_count``       |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``gamma_            |``string``  |                                 |
                |              |start_date``        |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``gamma_            |``string``  |                                 |
                |              |end_date``          |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``gamma_            |``string``  |                                 |
                |              |mode``              |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``gamma_            |``string``  |                                 |
                |              |file_name``         |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``gamma_            |``string``  |                                 |
                |              |comment``           |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscisp_           |``string``  | 0: Not eligible                 |
                |              |target_flg``        |            |                                 |
                |              |                    |            | 1: Eligible                     |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscisp_           |``string``  | 0: Waiting to run               |
                |              |status``            |            |                                 |
                |              |                    |            | 1: Running                      |
                |              |                    |            |                                 |
                |              |                    |            | 2: Successful                   |
                |              |                    |            |                                 |
                |              |                    |            | 3: Failed                       |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscisp_           |``string``  |                                 |
                |              |retry_count``       |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscisp_           |``string``  |                                 |
                |              |start_date``        |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscisp_           |``string``  |                                 |
                |              |end_date``          |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscisp_           |``string``  |                                 |
                |              |mode``              |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscisp_           |``string``  |                                 |
                |              |file_name``         |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscisp_           |``string``  |                                 |
                |              |comment``           |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscraw_           |``string``  | 0: Not eligible                 |
                |              |target_flg``        |            |                                 |
                |              |                    |            | 1: Eligible                     |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscraw_           |``string``  | 0: Waiting to run               |
                |              |status``            |            |                                 |
                |              |                    |            | 1: Running                      |
                |              |                    |            |                                 |
                |              |                    |            | 2: Successful                   |
                |              |                    |            |                                 |
                |              |                    |            | 3: Failed                       |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscraw_           |``string``  |                                 |
                |              |retry_count``       |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscraw_           |``string``  |                                 |
                |              |start_date``        |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscraw_           |``string``  |                                 |
                |              |end_date``          |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscraw_           |``string``  |                                 |
                |              |mode``              |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscraw_           |``string``  |                                 |
                |              |file_name``         |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``lscraw_           |``string``  |                                 |
                |              |comment``           |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``prewb_            |``string``  | 0: Not eligible                 |
                |              |target_flg``        |            |                                 |
                |              |                    |            | 1: Eligible                     |
                +--------------+--------------------+------------+---------------------------------+
                |              |``prewb_            |``string``  | 0: Waiting to run               |
                |              |status``            |            |                                 |
                |              |                    |            | 1: Running                      |
                |              |                    |            |                                 |
                |              |                    |            | 2: Successful                   |
                |              |                    |            |                                 |
                |              |                    |            | 3: Failed                       |
                +--------------+--------------------+------------+---------------------------------+
                |              |``prewb_            |``string``  |                                 |
                |              |retry_count``       |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``prewb_            |``string``  |                                 |
                |              |start_date``        |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``prewb_            |``string``  |                                 |
                |              |end_date``          |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``prewb_            |``string``  |                                 |
                |              |mode``              |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``prewb_            |``string``  |                                 |
                |              |file_name``         |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``prewb_            |``string``  |                                 |
                |              |comment``           |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``dewarp_           |``string``  | 0: Not eligible                 |
                |              |target_flg``        |            |                                 |
                |              |                    |            | 1: Eligible                     |
                +--------------+--------------------+------------+---------------------------------+
                |              |``dewarp_           |``string``  | 0: Waiting to run               |
                |              |status``            |            |                                 |
                |              |                    |            | 1: Running                      |
                |              |                    |            |                                 |
                |              |                    |            | 2: Successful                   |
                |              |                    |            |                                 |
                |              |                    |            | 3: Failed                       |
                +--------------+--------------------+------------+---------------------------------+
                |              |``dewarp_           |``string``  |                                 |
                |              |retry_count``       |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``dewarp_           |``string``  |                                 |
                |              |start_date``        |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``dewarp_           |``string``  |                                 |
                |              |end_date``          |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``dewarp_           |``string``  |                                 |
                |              |mode``              |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``dewarp_           |``string``  |                                 |
                |              |file_name``         |            |                                 |
                +--------------+--------------------+------------+---------------------------------+
                |              |``dewarp_           |``string``  |                                 |
                |              |comment``           |            |                                 |
                +--------------+--------------------+------------+---------------------------------+

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
        """
        return self._get_deploy_history_obj.get_deploy_history(device_id=device_id)

    def get_device_app_deploys(self, app_name: str, version_number: str):
        """Abstract function call to ``get_device_app_deploys`` API

        Args:
            app_name (str, required): App name
            version_number (str, required): Version Number.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-----------+--------------------+-----------+---------------------------+
                | *Level1*  | *Level2*           | *Type*    | *Description*             |
                +-----------+--------------------+-----------+---------------------------+
                |``deploy`` |                    | ``array`` | Descending order of       |
                |           |                    |           | ins_date                  |
                +-----------+--------------------+-----------+---------------------------+
                |           | ``id``             | ``number``|                           |
                +-----------+--------------------+-----------+---------------------------+
                |           | ``total_status``   | ``string``| 0: Running                |
                |           |                    |           |                           |
                |           |                    |           | 1: Normal completion      |
                |           |                    |           |                           |
                |           |                    |           | 2: Failure                |
                |           |                    |           |                           |
                |           |                    |           | 3: Cancellation           |
                +-----------+--------------------+-----------+---------------------------+
                |           |``deploy_parameter``| ``dict``  |                           |
                +-----------+--------------------+-----------+---------------------------+
                |           |``devices``         | ``array`` | Refer :ref:`devices <d2>` |
                |           |                    |           | for more details          |
                +-----------+--------------------+-----------+---------------------------+
                |           |``ins_id``          | ``string``|                           |
                +-----------+--------------------+-----------+---------------------------+
                |           |``ins_date``        | ``string``|                           |
                +-----------+--------------------+-----------+---------------------------+
                |           |``upd_id``          | ``string``|                           |
                +-----------+--------------------+-----------+---------------------------+
                |           |``upd_date``        | ``string``|                           |
                +-----------+--------------------+-----------+---------------------------+

                +-------------------+-----------------+-----------+---------------------------+
                | devices           | .. _d2:                                                 |
                +-------------------+-----------------+------------+--------------------------+
                | *Level1*          | *Level2*        | *Type*     | *Description*            |
                +-------------------+-----------------+------------+--------------------------+
                |``devices``        |                 | ``array``  | Ascending order of       |
                |                   |                 |            | device IDs               |
                +-------------------+-----------------+------------+--------------------------+
                |                   |``device_id``    | ``string`` |                          |
                +-------------------+-----------------+------------+--------------------------+
                |                   |``status``       | ``string`` | 0: Running               |
                |                   |                 |            |                          |
                |                   |                 |            | 1: Successful            |
                |                   |                 |            |                          |
                |                   |                 |            | 2: Failed                |
                |                   |                 |            |                          |
                |                   |                 |            | 3: Canceled              |
                |                   |                 |            |                          |
                |                   |                 |            | Cancellation supplement  |
                |                   |                 |            | During deployment, if    |
                |                   |                 |            | the device is deleted,it |
                |                   |                 |            | will be in this status   |
                +-------------------+-----------------+------------+--------------------------+
                |                   |``latest_        | ``string`` | 0: Not Latest            |
                |                   |deployment_flg`` |            |                          |
                |                   |                 |            |                          |
                |                   |                 |            | 1: Latest                |
                +-------------------+-----------------+------------+--------------------------+

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
        """

        return self._get_device_app_deploys_obj.get_device_app_deploys(
            app_name=app_name, version_number=version_number
        )

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
        """Abstract function call to ``create_deploy_configuration`` API

        Args:
            config_id (str, required) : config ID \
                up to 20 characters half-width only
            comment (str, optional) : Config Description \
                up to 100 characters No comment if not specified
            sensor_loader_version_number (str, optional) : SensorLoader version number \
                When -1 is specified, the default version (system\
                setting "DVC0017") is applied\
                If not specified, no SensorLoader deployment
            sensor_version_number (str, optional) : Sensor version number\
                When -1 is specified, the default version (system \
                setting "DVC0018") is applied\
                No Sensor deployment if not specified
            model_id (str, optional) : Model ID \
                If not specified, no model deployment
            model_version_number (str, optional) : Model version number \
                If not specified, the latest version is applied.
            ap_fw_version_number (str, optional) : ApFw version number\
                If not specified, no firmware deployment

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
        """
        return self._create_deploy_configuration_obj.create_deploy_configuration(
            config_id,
            comment,
            sensor_loader_version_number,
            sensor_version_number,
            model_id,
            model_version_number,
            ap_fw_version_number,
        )

    def deploy_device_app(
        self,
        app_name: str,
        version_number: str,
        device_ids: str,
        deploy_parameter: str = None,
        comment: str = None,
    ):
        """Abstract function call to ``deploy_device_app`` API

        Args:
            app_name (str, required) : App Name.
            version_number (str, required) : Version Number.
            device_ids (str, required) : IDs of edge AI devices \
                Specify multiple device IDs of edge AI devices separated by comma.
            deploy_parameter (str, optional) : The Deployment parameters. \
                (JSON format) The contents are Base64 encoded strings.\
                No parameters if not specified
            comment (str, optional) : deploy comment\
                up to 100 characters No comment if not specified

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
        """
        return self._deploy_device_app_obj.deploy_device_app(
            app_name, version_number, device_ids, deploy_parameter, comment
        )

    def deploy_by_configuration(
        self,
        config_id: str,
        device_ids: str,
        replace_model_id: str = None,
        comment: str = None,
    ):
        """Abstract function call to ``deploy_by_configuration`` API

        Args:
            config_id (str, required) : config ID
            device_ids (str, required) : IDs of edge AI devices \
            Specify multiple device IDs of edge AI devices separated by comma.
            replace_model_id (str, optional) : Replacement target model ID.\
                Specify "model_id" or "network_id"\
                If the specified model ID does not exist in the DB, treat the\
                input value as network_id (console internal\
                management ID) and perform processing\
                If not specified, do not replace.
            comment (str, optional) : deploy comment\
                up to 100 characters No comment if not specified

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
        """
        return self._deploy_by_configuration_obj.deploy_by_configuration(
            config_id, device_ids, replace_model_id, comment
        )

    def cancel_deployment(
        self,
        device_id: str,
        deploy_id: str,
    ):
        """Abstract function call to ``cancel_deployment`` API

        Args:
            device_id (str, required) : ID of edge AI device.
            deploy_id (str, required) : Deploy ID \
                id that can be obtained with get_deploy_history

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
                    if any input string parameter found empty OR
                    if any input integer parameter found negative OR
                    if any input non integer parameter found.
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
        """
        return self._cancel_deployment_obj.cancel_deployment(device_id, deploy_id)

    def delete_deploy_configuration(self, config_id: str):
        """Abstract function call to ``delete_deploy_configuration`` API

        Args:
            config_id (str, required): config Id

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
        """

        return self._delete_deploy_configuration_obj.delete_deploy_configuration(
            config_id=config_id
        )

    def undeploy_device_app(self, device_ids: str):
        """Abstract function call to ``undeploy_device_app`` API

        Args:
            device_ids (str, required): Multiple IDs of edge AI devices separated by commas.

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
        """

        return self._undeploy_device_app_obj.undeploy_device_app(device_ids=device_ids)

    def deploy_device_app_wait_response(
        self,
        app_name: str,
        version_number: str,
        device_ids: str,
        deploy_parameter: str = None,
        comment: str = None,
        callback=None,
    ):
        """Abstract function call to ``deploy_device_app_wait_response`` API

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
        """
        return self._deploy_device_app_wait_response_obj.deploy_device_app_wait_response(
            app_name, version_number, device_ids, deploy_parameter, comment, callback
        )

    def deploy_by_configuration_wait_response(
        self,
        config_id: str,
        device_ids: str,
        replace_model_id: str = None,
        comment: str = None,
        timeout: int = None,
        callback=None,
    ):
        """Abstract function call to ``deploy_by_configuration_wait_response`` API

        Args:
            config_id (str, required) : Configuration ID.
            device_ids (str, required) : Device ID. Specify multiple device IDs separated by commas.
            replace_model_id (str, optional) : Model ID to be replaced. Specify "Model ID" or \
                "network_id". If the specified model ID does not exist in the DB, the \
                entered value is regarded as a network_id and processed is performed.
            comment (str, optional) : Deploy comment.
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
        """
        return (
            self._deploy_by_configuration_wait_response_obj.deploy_by_configuration_wait_response(
                config_id, device_ids, replace_model_id, comment, timeout, callback
            )
        )
