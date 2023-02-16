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
# pylint:disable=too-many-function-args
# pylint:disable=invalid-name

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass
from console_access_library.device_management.get_command_parameter_file import (
    GetCommandParameterFile,
)
from console_access_library.device_management.get_devices import GetDevices
from console_access_library.device_management.start_upload_inference_result import (
    StartUploadInferenceResult,
)
from console_access_library.device_management.stop_upload_inference_result import (
    StopUploadInferenceResult,
)


class DeviceManagement(ConsoleAccessBaseClass):
    """Abstract class to access Console Access Library DeviceManagement component
    APIs from devicemanagement component

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for DeviceManagement Abstract class

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._get_devices_obj = GetDevices(config)
        self._start_upload_inference_result_obj = StartUploadInferenceResult(config)
        self._stop_upload_inference_result_obj = StopUploadInferenceResult(config)
        self._get_command_parameter_file_obj = GetCommandParameterFile(config)

    def get_devices(
        self,
        device_id: str = None,
        device_name: str = None,
        connection_state: str = None,
        device_group_id: str = None,
    ):
        """Abstract function call to ``get_devices`` API

        Args:
            device_id (str, optional): Edge AI Device ID. Partial search, case insensitive.
                Search all device_ids if not specified.
            device_name (str, optional) : Edge AI device name. Partial search, case insensitive.
                If not specified, search all device_names.
            connection_state (str, optional) : Connection status. For connected state: Connected
                Disconnected state: Disconnected
                Exact match search, case insensitive.
                If not specified, search all connection_states.
            device_group_id (str, optional) : Affiliated Edge AI device group.
                Exact match search, case insensitive.
                Search all device_group_id if not specified.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+--------------------+-----------+--------------------------------+
                | *Level1*   | *Level2*           |*Type*     | *Description*                  |
                +------------+--------------------+-----------+--------------------------------+
                | ``devices``|                    |``array``  | The subordinate elements are   |
                |            |                    |           | listed in ascending order by   |
                |            |                    |           | device ID                      |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``device_id``      |``string`` | Set the device ID              |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``place``          |``string`` | Set the location               |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``comment``        |``string`` | Set the device description     |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``property``       |``string`` | Set device properties          |
                |            |                    |           | (device_name, etc.)            |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``ins_id``         |``string`` | Set the creator of the device  |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``ins_date``       |``string`` | Set the date and               |
                |            |                    |           | time the device was created.   |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``upd_id``         |``string`` | Set up an updater for          |
                |            |                    |           | your device                    |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``upd_date``       |``string`` | Set the date and time          |
                |            |                    |           | of the device update.          |
                +------------+--------------------+-----------+--------------------------------+
                |            |``connectionState`` |``string`` | Set the connection status      |
                |            |                    |           | of the device.                 |
                +------------+--------------------+-----------+--------------------------------+
                |            |``lastActivityTime``|``string`` | Set the last connection date   |
                |            |                    |           | and time of the device.        |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``device_groups``  |``array``  | Refer :ref:`device_groups <ds>`|
                |            |                    |           | for more details               |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``models``         |``array``  | Refer :ref:`models <model1>`   |
                |            |                    |           | for more details               |
                +------------+--------------------+-----------+--------------------------------+

                +-------------------+--------------------+------------+--------------------------+
                | device_groups     | .. _ds:                                                    |
                +-------------------+--------------------+------------+--------------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*            |
                +-------------------+--------------------+------------+--------------------------+
                | ``device_groups`` |                    | ``array``  | The subordinate          |
                |                   |                    |            | elements are listed      |
                |                   |                    |            | in ascending order       |
                |                   |                    |            | by device group ID       |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_group_id`` | ``string`` | Set the device group ID  |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_type``     | ``string`` | Set the device type      |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``comment``        |``string``  | Set the device           |
                |                   |                    |            | bdescription             |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``ins_id``         |``string``  | Set the date and time    |
                |                   |                    |            | that the device group    |
                |                   |                    |            | was created.             |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``ins_date``       |``string``  | Set the creator of the   |
                |                   |                    |            | device group.            |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``upd_id``         |``string``  | Set the updater for      |
                |                   |                    |            | the device group         |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``upd_date``       |``string``  | Set the date and time of |
                |                   |                    |            | the device group update. |
                +-------------------+--------------------+------------+--------------------------+

                +-------------------+--------------------+------------+--------------------------+
                | models            | .. _model1:                                                |
                +-------------------+--------------------+------------+--------------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*            |
                +-------------------+--------------------+------------+--------------------------+
                | ``models``        |                    | ``array``  | The subordinate          |
                |                   |                    |            | elements are listed      |
                |                   |                    |            | in ascending order       |
                |                   |                    |            | by device group ID       |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``model_version_id``| ``string`` | Set the model version ID |
                |                   |                    |            | Format: ModelID:v1.0001  |
                |                   |                    |            | * If DnnModelVersion does|
                |                   |                    |            | not exist in the DB, the |
                |                   |                    |            | network_id is displayed. |
                |                   |                    |            | Example) 0201020002370200|
                |                   |                    |            | In the above case, 000237|
                |                   |                    |            | (7~12 digits) If it is 16|
                |                   |                    |            | digits,it is displayed   |
                |                   |                    |            | as is.                   |
                +-------------------+--------------------+------------+--------------------------+

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

        return self._get_devices_obj.get_devices(
            device_id, device_name, connection_state, device_group_id
        )

    def start_upload_inference_result(self, device_id: str):
        """Abstract function call to ``start_upload_inference_result`` API

        Args:
            device_id (str, required): Edge AI Device ID.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------------------+------------+---------------------------+
                | *Level1*               | *Type*     | *Description*             |
                +------------------------+------------+---------------------------+
                | ``result``             | ``string`` | Set "SUCCESS" pinning     |
                +------------------------+------------+---------------------------+
                | ``outputSubDirectory`` | ``string`` | Input Image storage path  |
                |                        |            | UploadMethod:BlobStorage  |
                |                        |            | only                      |
                +------------------------+------------+---------------------------+

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

        return self._start_upload_inference_result_obj.start_upload_inference_result(
            device_id=device_id
        )

    def stop_upload_inference_result(self, device_id: str):
        """Abstract function call to ``stop_upload_inference_result`` API

        Args:
            device_id (str, required): Edge AI Device ID.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-----------------------+------------+---------------------------+
                | *Level1*              | *Type*     | *Description*             |
                +-----------------------+------------+---------------------------+
                | ``result``            | ``string`` | Set "SUCCESS" pinning     |
                +-----------------------+------------+---------------------------+

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

        return self._stop_upload_inference_result_obj.stop_upload_inference_result(
            device_id=device_id
        )

    def get_command_parameter_file(self):
        """Abstract function call to ``get_command_parameter_file`` API

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-------------------+--------------+----------+-------------------------------+
                | *Level1*          |*Level2*      |*Type*    | *Description*                 |
                +-------------------+--------------+----------+-------------------------------+
                | ``parameter_list``|              |``array`` | Parameter file list           |
                +-------------------+--------------+----------+-------------------------------+
                |                   |``parameter`` |``string``| The setting value. json       |
                +-------------------+--------------+----------+-------------------------------+
                |                   |``filename``  |``string``| File Name                     |
                +-------------------+--------------+----------+-------------------------------+
                |                   |``comment``   |``string``| comment                       |
                +-------------------+--------------+----------+-------------------------------+
                |                   |``isdefault`` |``string``| True: Default parameter       |
                |                   |              |          | not False: Default            |
                +-------------------+--------------+----------+-------------------------------+
                |                   |``device_ids``|``List``  | List of target devices.       |
                +-------------------+--------------+----------+-------------------------------+
                |                   |``ins_id``    |``string``| Set the creator of the setting|
                +-------------------+--------------+----------+-------------------------------+
                |                   |``ins_date``  |``string``| Set the date and time that    |
                |                   |              |          | the setting was created       |
                +-------------------+--------------+----------+-------------------------------+
                |                   |``upd_id``    |``string``| Set who updated the settings. |
                +-------------------+--------------+----------+-------------------------------+
                |                   |``upd_date``  |``string``| Set the date and time when    |
                |                   |              |          | the settings were updated     |
                +-------------------+--------------+----------+-------------------------------+

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

        return self._get_command_parameter_file_obj.get_command_parameter_file()
