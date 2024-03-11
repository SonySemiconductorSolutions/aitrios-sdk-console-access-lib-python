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
        """Get the device app list information

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
                |          |``schema_    | ``array``  | Refer :ref:`schema_info <schema_info1>`  |
                |          |info``       |            | for more details                         |
                +----------+-------------+------------+------------------------------------------+
                |          |``versions`` | ``array``  | Refer :ref:`versions <versions_element>` |
                |          |             |            | for more details                         |
                +----------+-------------+------------+------------------------------------------+


                +-------------------+-----------------+------------+-------------------------------+
                | schema_info       | .. _schema_info1:                                            |
                +-------------------+-----------------+------------+-------------------------------+
                | *Level1*          | *Level2*        | *Type*     | *Description*                 |
                +===================+=================+============+===============================+
                | ``schema_info``   |                 | ``array``  | Schema info.                  |
                +-------------------+-----------------+------------+-------------------------------+
                |                   | ``VnSAppId``    | ``string`` | Set the VnS app ID            |
                +-------------------+-----------------+------------+-------------------------------+
                |                   | ``version``     | ``string`` | Set the app version no.       |
                +-------------------+-----------------+------------+-------------------------------+
                |                   | ``interfaces``  | ``array``  |Refer :ref:`interfaces <int1>` |
                |                   |                 |            |for more details               |
                +-------------------+-----------------+------------+-------------------------------+

                +-------------------+-----------------+------------+-------------------------------+
                | interfaces        | .. _int1:                                                    |
                +-------------------+-----------------+------------+-------------------------------+
                | *Level1*          | *Level2*        | *Type*     | *Description*                 |
                +===================+=================+============+===============================+
                | ``interfaces``    |                 | ``array``  | Set the metadata format IDs.  |
                +-------------------+-----------------+------------+-------------------------------+
                |                   | ``in``          | ``array``  | Refer :ref:`in <in1>`         |
                |                   |                 |            | for more details              |
                +-------------------+-----------------+------------+-------------------------------+

                +-------------------+-----------------+------------+-------------------------------+
                | in                | .. _in1:                                                     |
                +-------------------+-----------------+------------+-------------------------------+
                | *Level1*          | *Level2*        | *Type*     | *Description*                 |
                +===================+=================+============+===============================+
                | ``in``            |                 | ``array``  |                               |
                +-------------------+-----------------+------------+-------------------------------+
                |                   |``metadata       | ``string`` | Set the metadata format ID.   |
                |                   |FormatId``       |            |                               |
                +-------------------+-----------------+------------+-------------------------------+

                +-------------------+--------------------+------------+-------------------+
                | versions          | .. _versions_element:                               |
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
        """
        return self._get_device_apps_obj.get_device_apps()

    def delete_device_app(self, app_name: str, version_number: str):
        """Delete device app

        Args:
            app_name (str, required): App name
            version_number (str, required): App version number

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+------------+-------------------------------+
                | *Level1*   | *Type*     | *Description*                 |
                +============+============+===============================+
                | ``result`` | ``string`` | Set "SUCCESS" fixing          |
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
        schema_info: dict = None
    ):
        """Import Device app

        Args:
            compiled_flg (str, required): Set the compiled flg.

                - Value definition

                    - 0 : Specified App is not compiled
                    - 1 : Specified App is compiled

            app_name (str, required): App name.
                Allow only the following characters.

                    - Alphanumeric characters
                    - Under bar
                    - Dot

                The maximum number of characters is app_name + version_number <=31.

            version_number (str, required): App version number.
                Allow only the following characters.

                    - Alphanumeric characters
                    - Under bar
                    - Dot

                The maximum number of characters is app_name + version_number <=31.

            comment (str, optional): Comment. Max. 100 characters.
            file_name (str, required): filename.
            file_content (str, required): App file content in base64 encoding.
            entry_point (str, optional): App entry point.
            schema_info (dict, optional) : Schema info. Example:

                .. code-block:: console

                    {
                        interfaces: {
                            in:
                            [
                                { metadataFormatId: "string_value1"},
                                { metadataFormatId: "string_value2"}
                            ]
                        }
                    }

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+------------+-------------------------------+
                | *Level1*   | *Type*     | *Description*                 |
                +============+============+===============================+
                | ``result`` | ``string`` | Set "SUCCESS" fixing          |
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
            compiled_flg, app_name, version_number, file_name, file_content,
            entry_point, comment, schema_info
        )

    def get_deploy_configurations(self):
        """Get the deploy config list

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-----------------+------------+------------+---------------------------------+
                | *Level1*        | *Level2*   | *Type*     | *Description*                   |
                +=================+============+============+=================================+
                |``deploy_        |            | ``array``  |                                 |
                |configurations`` |            |            |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``config_   | ``string`` | Set the config ID.              |
                |                 |id``        |            |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``device_   | ``string`` | Set the device type.            |
                |                 |type``      |            |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``config_   | ``string`` | Set the config comment.         |
                |                 |comment``   |            |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``running_  | ``integer``| Set the running cnt.            |
                |                 |cnt``       |            |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``success_  | ``integer``| Set the success cnt.            |
                |                 |cnt``       |            |                                 |
                +-----------------+------------+------------+---------------------------------+
                |                 |``fail_cnt``| ``integer``| Set the fail cnt.               |
                +-----------------+------------+------------+---------------------------------+
                |                 |``firmware``| ``array``  | Refer :ref:`firmware <f9>`      |
                |                 |            |            | for more details                |
                +-----------------+------------+------------+---------------------------------+
                |                 |``model``   | ``array``  | Refer :ref:`model <mm>`         |
                |                 |            |            | for more details                |
                +-----------------+------------+------------+---------------------------------+
                |                 |``ins_id``  | ``string`` | Set the deployment author.      |
                +-----------------+------------+------------+---------------------------------+
                |                 |``ins_date``| ``string`` | Set the date the deployment     |
                |                 |            |            | was created.                    |
                +-----------------+------------+------------+---------------------------------+
                |                 |``upd_id``  | ``string`` | Set the deployment updater.     |
                +-----------------+------------+------------+---------------------------------+
                |                 |``upd_date``| ``string`` | Set the date the deployment     |
                |                 |            |            | was updated.                    |
                +-----------------+------------+------------+---------------------------------+

                +-------------------+--------------------+------------+-------------------+
                | firmware          | .. _f9:                                             |
                +-------------------+--------------------+------------+-------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*     |
                +===================+====================+============+===================+
                | ``firmware``      |                    | ``array``  |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``sensor_loader_    | ``string`` | Set the sensor    |
                |                   |file_name``         |            | loader filename.  |
                +-------------------+--------------------+------------+-------------------+
                |                   |``sensor_loader_    | ``string`` | Set the sensor    |
                |                   |version_number``    |            | loader version    |
                |                   |                    |            | number.           |
                +-------------------+--------------------+------------+-------------------+
                |                   |``sensor_loader_    | ``string`` | Set the sensor    |
                |                   |firmware_comment``  |            | loader firmware   |
                |                   |                    |            | comment.          |
                +-------------------+--------------------+------------+-------------------+
                |                   |``sensor_file_name``| ``string`` | Set the sensor    |
                |                   |                    |            | filename.         |
                +-------------------+--------------------+------------+-------------------+
                |                   |``sensor_           | ``string`` | Set the sensor    |
                |                   |version_number``    |            | version number.   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``sensor_           |``string``  | Set the sensor    |
                |                   |firmware_comment``  |            | firmware comment. |
                +-------------------+--------------------+------------+-------------------+
                |                   |``apfw_file_name``  |``string``  | Set the apfw      |
                |                   |                    |            | filename.         |
                +-------------------+--------------------+------------+-------------------+
                |                   |``apfw_version_     |``string``  | Set the apfw      |
                |                   |number``            |            | version number.   |
                +-------------------+--------------------+------------+-------------------+
                |                   |``apfw_firmware_    |``string``  | Set the apfw      |
                |                   |comment``           |            | firmware comment. |
                +-------------------+--------------------+------------+-------------------+

                +-------------------+--------------------+------------+-------------------+
                | model             | .. _mm:                                             |
                +-------------------+--------------------+------------+-------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*     |
                +===================+====================+============+===================+
                | ``model``         |                    | ``array``  |                   |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``model_id``       | ``string`` | Set the model ID. |
                +-------------------+--------------------+------------+-------------------+
                |                   |``model_            | ``string`` | Set the model     |
                |                   |version_number``    |            | version number.   |
                +-------------------+--------------------+------------+-------------------+
                |                   | ``model_comment``  | ``string`` | Set the model     |
                |                   |                    |            | comment.          |
                +-------------------+--------------------+------------+-------------------+
                |                   |``model_            | ``string`` | Set the model     |
                |                   |version_comment``   |            | version comment.  |
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
        return self._get_deploy_configurations_obj.get_deploy_configurations()

    def get_deploy_history(self, device_id: str):
        """Get the deploy history for a specified device

        Args:
            device_id (str, required): Device ID.

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
                |          | ``firmware``         | ``array``  |Refer :ref:`firmware <f7>`     |
                |          |                      |            |for more details               |
                +----------+----------------------+------------+-------------------------------+

                +------------+--------------------+------------+-----------------------------------+
                | firmware   | .. _f7:                                                             |
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
        """
        return self._get_deploy_history_obj.get_deploy_history(device_id=device_id)

    def get_device_app_deploys(self, app_name: str, version_number: str):
        """Get Device App Deploys

        Args:
            app_name (str, required): App name
            version_number (str, required): App version number.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-----------+--------------------+-----------+---------------------------+
                | *Level1*  | *Level2*           | *Type*    | *Description*             |
                +===========+====================+===========+===========================+
                |``deploys``|                    | ``array`` |                           |
                +-----------+--------------------+-----------+---------------------------+
                |           | ``id``             | ``number``| Set the deploy id.        |
                +-----------+--------------------+-----------+---------------------------+
                |           | ``total_status``   | ``string``| Set the total status.     |
                |           |                    |           |                           |
                |           |                    |           | - Value definition        |
                |           |                    |           |                           |
                |           |                    |           | 0: Running                |
                |           |                    |           |                           |
                |           |                    |           | 1: Successfully completed |
                |           |                    |           |                           |
                |           |                    |           | 2: Failed                 |
                |           |                    |           |                           |
                |           |                    |           | 3: Canceled               |
                +-----------+--------------------+-----------+---------------------------+
                |           |``deploy_parameter``| ``string``| Set the deploy parameter. |
                +-----------+--------------------+-----------+---------------------------+
                |           |``devices``         | ``array`` | Refer :ref:`devices <d2>` |
                |           |                    |           | for more details          |
                +-----------+--------------------+-----------+---------------------------+

                +-------------------+-----------------+-----------+---------------------------+
                | devices           | .. _d2:                                                 |
                +-------------------+-----------------+------------+--------------------------+
                | *Level1*          | *Level2*        | *Type*     | *Description*            |
                +===================+=================+============+==========================+
                |``devices``        |                 | ``array``  |                          |
                +-------------------+-----------------+------------+--------------------------+
                |                   |``device_id``    | ``string`` | Set the device id.       |
                +-------------------+-----------------+------------+--------------------------+
                |                   |``status``       | ``string`` | Set the total status.    |
                |                   |                 |            |                          |
                |                   |                 |            | - Value definition       |
                |                   |                 |            |                          |
                |                   |                 |            | 0: Running               |
                |                   |                 |            |                          |
                |                   |                 |            | 1: Successfully completed|
                |                   |                 |            |                          |
                |                   |                 |            | 2: Failed                |
                |                   |                 |            |                          |
                |                   |                 |            | 3: Canceled              |
                +-------------------+-----------------+------------+--------------------------+
                |                   |``latest_        | ``string`` | Set the deployment flg.  |
                |                   |deployment_flg`` |            |                          |
                |                   |                 |            | - Value definition       |
                |                   |                 |            |                          |
                |                   |                 |            | 0: Old deployment history|
                |                   |                 |            |                          |
                |                   |                 |            | 1: Recent deployment     |
                |                   |                 |            | history                  |
                +-------------------+-----------------+------------+--------------------------+
                |                   |``ins_id``       | ``string`` | Set the settings author. |
                +-------------------+-----------------+------------+--------------------------+
                |                   |``ins_date``     | ``string`` | Set the date the settings|
                |                   |                 |            | were created.            |
                +-------------------+-----------------+------------+--------------------------+
                |                   |``upd_id``       | ``string`` | Set the settings updater.|
                +-------------------+-----------------+------------+--------------------------+
                |                   |``upd_date``     | ``string`` | Set the date the settings|
                |                   |                 |            | were updated.            |
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
        """Register the deploy config information to deploy to the following devices. \
        ・Firmware ・AI model

        Args:
            config_id (str, required) : Max. 20 single characters, single-byte characters only. \
                The following characters are allowed \
                Alphanumeric characters \
                -hyphen \
                _ Underscore \
                () Small parentheses \
                . dot
            comment (str, optional) : Max. 100 characters. Default : "".
            sensor_loader_version_number (str, optional) : Sensor loader version number.
                Default is "".
            sensor_version_number (str, optional) : Sensor version number. Default is "".
            model_id (str, optional) : The model_id.
            model_version_number (str, optional) : The Model version number. Default: "".
            ap_fw_version_number (str, optional) : The ApFw version number. Default : "".

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+------------+-------------------------------+
                | *Level1*   | *Type*     | *Description*                 |
                +============+============+===============================+
                | ``result`` | ``string`` | Set "SUCCESS" fixing          |
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
        comment: str = None,
    ):
        """Deploy device app

        Args:
            app_name (str, required) : App name
            version_number (str, required) : App version number
            device_ids (str, required) : Device IDS. Specify multiple device IDs separated\
                by commas.
            comment (str, optional) : Comment. Max. 100 characters.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+------------+-------------------------------+
                | *Level1*   | *Type*     | *Description*                 |
                +============+============+===============================+
                | ``result`` | ``string`` | Set "SUCCESS" fixing          |
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
            app_name, version_number, device_ids, comment
        )

    def deploy_by_configuration(
        self,
        config_id: str,
        device_ids: str,
        replace_model_id: str = None,
        comment: str = None,
    ):
        """Provide a function for deploying the following to devices \
            specified with deploy config\
            ・Firmware\
            ・AI model

        Args:
            config_id (str, required) : Setting ID
            device_ids (str, required) : Specify multiple device IDs separated by commas.
            replace_model_id (str, optional) : Specify the model ID or network_id.\
                If the model with the specified model ID does not exist in the database,\
                treat the entered value as the network_id and process it. Default : "".
            comment (str, optional) : Max 100 characters. Default : "".

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+------------+-------------------------------+
                | *Level1*   | *Type*     | *Description*                 |
                +============+============+===============================+
                | ``result`` | ``string`` | Set "SUCCESS" fixing          |
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
        """Force cancellation of the device deployment status

        Args:
            device_id (str, required) : Device ID.
            deploy_id (str, required) : Deploy ID.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+------------+-------------------------------+
                | *Level1*   | *Type*     | *Description*                 |
                +============+============+===============================+
                | ``result`` | ``string`` | Set "SUCCESS" fixing          |
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
        """Delete the information for a specified deploy config

        Args:
            config_id (str, required): Config ID

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+------------+-------------------------------+
                | *Level1*   | *Type*     | *Description*                 |
                +============+============+===============================+
                | ``result`` | ``string`` | Set "SUCCESS" fixing          |
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
        """Undeploy device app

        Args:
            device_ids (str, required): Device IDs.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+------------+-------------------------------+
                | *Level1*   | *Type*     | *Description*                 |
                +============+============+===============================+
                | ``result`` | ``string`` | Set "SUCCESS" fixing          |
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
        comment: str = None,
        callback=None,
    ):
        """Deploy and wait for completion

        Args:
            app_name (str, required) : App name
            version_number (str, required) : App version number
            device_ids (str, required) : Device IDS. Specify multiple device IDs separated\
                by commas.
            comment (str, optional) : Comment. Max. 100 characters.
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
                +===================+===================+============+============================+
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
            app_name, version_number, device_ids, comment, callback
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
        """Provides a function to deploy the following to the device specified from the
        deployment config.

        Args:
            config_id (str, required) : Setting ID
            device_ids (str, required) : Specify multiple device IDs separated by commas.
            replace_model_id (str, optional) : Specify the model ID or network_id.\
                If the model with the specified model ID does not exist in the database,\
                treat the entered value as the network_id and process it. Default : "".
            comment (str, optional) : Max 100 characters. Default : "".
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
                +===================+===================+============+============================+
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
