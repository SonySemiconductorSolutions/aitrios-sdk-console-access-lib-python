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
# pylint:disable=too-many-arguments
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
        device_ids: str = None,
        scope: str = None,
    ):
        """Get the device list information

        Args:
            device_id (str, optional) : Device ID. Partial match search. Default:""
            device_name (str, optional) : Device name. Partial match search. Default:""
            connection_state (str, optional) : Connection status.

                Value definition

                    - Connected
                    - Disconnected

                Default:""
            device_group_id (str, optional) : Device group ID. Default:""
            device_ids (str, optional): Specify multiple device IDs separated by commas.
                                              Default:""
            scope (str, optional) : Specify the scope of response parameters to return.
                Default: "full"

                Value definition

                    - full : Return full parameters
                    - minimal : Return minimal parameters fast response speed

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+--------------------+-----------+--------------------------------+
                | *Level1*   | *Level2*           |*Type*     | *Description*                  |
                +============+====================+===========+================================+
                | ``devices``|                    |``array``  |                                |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``device_id``      |``string`` | Set the device ID              |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``place``          |``string`` | Set the location               |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``comment``        |``string`` | Set the device description     |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``property``       |``array``  | Refer :ref:`property <pro2>`   |
                |            |                    |           | for more details               |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``device_type``    |``string`` | Set the device type.           |
                +------------+--------------------+-----------+--------------------------------+
                |            |``display_device_   |``string`` | Set the display device type.   |
                |            |type``              |           |                                |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``ins_id``         |``string`` | Set the device author.         |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``ins_date``       |``string`` | Set the date                   |
                |            |                    |           | the device was created.        |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``upd_id``         |``string`` | Set the device updater.        |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``upd_date``       |``string`` | Set the date the device was    |
                |            |                    |           | updated.                       |
                +------------+--------------------+-----------+--------------------------------+
                |            |``connectionState`` |``string`` | Set the device connection state|
                +------------+--------------------+-----------+--------------------------------+
                |            |``lastActivityTime``|``string`` | Set the date the device last   |
                |            |                    |           | connected.                     |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``models``         |``array``  | Refer :ref:`models <model1>`   |
                |            |                    |           | for more details               |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``configuration``  |``array``  |                                |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``state``          |``array``  |                                |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``device_groups``  |``array``  | Refer :ref:`device_groups <ds>`|
                |            |                    |           | for more details               |
                +------------+--------------------+-----------+--------------------------------+

                +-------------------+--------------------+------------+--------------------------+
                | property          | .. _pro2:                                                  |
                +-------------------+--------------------+------------+--------------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*            |
                +===================+====================+============+==========================+
                | ``property``      |                    | ``array``  |                          |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_name``     | ``string`` | Set the device name.     |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``internal_device_  | ``string`` | Set the internal device  |
                |                   |id``                |            | id.                      |
                +-------------------+--------------------+------------+--------------------------+

                +-------------------+--------------------+------------+--------------------------+
                | device_groups     | .. _ds:                                                    |
                +-------------------+--------------------+------------+--------------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*            |
                +===================+====================+============+==========================+
                | ``device_groups`` |                    | ``array``  |                          |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_group_id`` | ``string`` | Set the device group ID  |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_type``     | ``string`` | Set the device type      |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``comment``        |``string``  | Set the device           |
                |                   |                    |            | group comment.           |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``ins_id``         |``string``  | Set the date the device  |
                |                   |                    |            | group was created.       |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``ins_date``       |``string``  | Set the device group     |
                |                   |                    |            | author.                  |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``upd_id``         |``string``  | Set the device group     |
                |                   |                    |            | updater                  |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``upd_date``       |``string``  | Set the date the device  |
                |                   |                    |            | group was updated.       |
                +-------------------+--------------------+------------+--------------------------+

                +-------------------+--------------------+------------+--------------------------+
                | models            | .. _model1:                                                |
                +-------------------+--------------------+------------+--------------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*            |
                +===================+====================+============+==========================+
                | ``models``        |                    | ``array``  |                          |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``model_version_id``| ``string`` | Set the model version ID.|
                |                   |                    |            | Format: modelid:v1.01    |
                |                   |                    |            | For model that does not  |
                |                   |                    |            | exist in the system,     |
                |                   |                    |            | display network_id       |
                |                   |                    |            | Example: 000237          |
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
            device_id, device_name, connection_state, device_group_id, device_ids, scope
        )

    def start_upload_inference_result(self, device_id: str):
        """Implement instructions to a specified device to start to get the\
             inference result metadata (Output Tensor) and image (Input image).

        Args:
            device_id (str, required): Device ID.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +--------------------------+------------+---------------------------+
                | *Level1*                 | *Type*     | *Description*             |
                +==========================+============+===========================+
                | ``result``               | ``string`` | Set "SUCCESS" fixing      |
                +--------------------------+------------+---------------------------+
                | ``outputSubDirectory``   | ``string`` | Input Image storage path, |
                |                          |            | UploadMethod:BlobStorage  |
                |                          |            | only                      |
                +--------------------------+------------+---------------------------+
                | ``outputSubDirectoryIR`` | ``string`` | Input Inference result    |
                |                          |            | storage path,             |
                |                          |            | UploadMethodIR:BlobStorage|
                |                          |            | only                      |
                +--------------------------+------------+---------------------------+

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
        """Implement instructions to a specified device to stop getting the\
             inference result metadata (Output Tensor) and image (Input image).

        Args:
            device_id (str, required): Device ID.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-----------------------+------------+---------------------------+
                | *Level1*              | *Type*     | *Description*             |
                +=======================+============+===========================+
                | ``result``            | ``string`` | Set "SUCCESS" fixing      |
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
        """Get the command parameter file list information.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-------------------+--------------+------------+-------------------------------+
                | *Level1*          |*Level2*      |*Type*      | *Description*                 |
                +===================+==============+============+===============================+
                | ``parameter_list``|              |``array``   |                               |
                +-------------------+--------------+------------+-------------------------------+
                |                   |``parameter`` |``array``   | Refer :ref:`parameter <par2>` |
                |                   |              |            | for more details              |
                +-------------------+--------------+------------+-------------------------------+
                |                   |``filename``  |``string``  | Name of file                  |
                +-------------------+--------------+------------+-------------------------------+
                |                   |``comment``   |``string``  | Comment                       |
                +-------------------+--------------+------------+-------------------------------+
                |                   |``isdefault`` |``string``  | True: Default parameter;      |
                |                   |              |            | False: Not default            |
                +-------------------+--------------+------------+-------------------------------+
                |                   |``device_ids``|``string[]``| Target device list.           |
                +-------------------+--------------+------------+-------------------------------+
                |                   |``ins_id``    |``string``  | Set the settings author.      |
                +-------------------+--------------+------------+-------------------------------+
                |                   |``ins_date``  |``string``  | Set the date the settings     |
                |                   |              |            | were created.                 |
                +-------------------+--------------+------------+-------------------------------+
                |                   |``upd_id``    |``string``  | Set the settings updater.     |
                +-------------------+--------------+------------+-------------------------------+
                |                   |``upd_date``  |``string``  | Set the date the settings     |
                |                   |              |            | were updated.                 |
                +-------------------+--------------+------------+-------------------------------+

                +-------------------+-----------------+------------+----------------------------+
                | parameter         | .. _par2:                                                 |
                +-------------------+-----------------+------------+----------------------------+
                | *Level1*          | *Level2*        | *Type*     | *Description*              |
                +===================+=================+============+============================+
                | ``parameter``     |                 | ``array``  | Setting value. json        |
                +-------------------+-----------------+------------+----------------------------+
                |                   |``commands``     | ``array``  | Refer :ref:`commands <c2>` |
                |                   |                 |            | for more details           |
                +-------------------+-----------------+------------+----------------------------+

                +-------------------+-----------------+------------+-----------------------------+
                | commands          | .. _c2:                                                    |
                +-------------------+-----------------+------------+-----------------------------+
                | *Level1*          | *Level2*        | *Type*     | *Description*               |
                +===================+=================+============+=============================+
                | ``commands``      |                 | ``array``  |                             |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``command_name`` | ``string`` | Command name.               |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``parameters``   | ``array``  | Refer :ref:`parameters <P2>`|
                |                   |                 |            | for more details            |
                +-------------------+-----------------+------------+-----------------------------+

                +-------------------+-----------------+------------+-----------------------------+
                | parameters        | .. _P2:                                                    |
                +-------------------+-----------------+------------+-----------------------------+
                | *Level1*          | *Level2*        | *Type*     | *Description*               |
                +===================+=================+============+=============================+
                | ``parameters``    |                 | ``array``  |                             |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``Mode``         | ``integer``| Collection mode.            |
                |                   |                 |            | - Value definition          |
                |                   |                 |            | 0 : Input Image only        |
                |                   |                 |            | 1 : Input Image & Inference |
                |                   |                 |            | Result                      |
                |                   |                 |            | 2 : Inference Result only   |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``UploadMethod`` | ``string`` | It specifies how to upload  |
                |                   |                 |            | Input Image.                |
                |                   |                 |            | - Value definition          |
                |                   |                 |            | BlobStorage                 |
                |                   |                 |            | HttpStorage                 |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``FileFormat``   | ``string`` | Image file format.          |
                |                   |                 |            | - Value definition: JPG, BMP|
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``UploadMethod   | ``string`` | It specifies how to         |
                |                   |IR``             |            | Inference Result.           |
                |                   |                 |            | - Value definition          |
                |                   |                 |            | BlobStorage                 |
                |                   |                 |            | HttpStorage                 |
                |                   |                 |            | Mqtt                        |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``CropHOffset``  | ``integer``| Hoffset for Image crop.     |
                |                   |                 |            | - Value range : 0 to 4055   |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``CropVOffset``  | ``integer``| Voffset for Image crop.     |
                |                   |                 |            | - Value range : 0 to 3039   |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``CropHSize``    | ``integer``| Hsize for Image crop.       |
                |                   |                 |            | - Value range : 0 to 4056   |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``CropVSize``    | ``integer``| Vsize for Image crop.       |
                |                   |                 |            | - Value range : 0 to 3040   |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``NumberOf       | ``integer``| Number of images to fetch   |
                |                   |Images``         |            | (Input Image).              |
                |                   |                 |            | When it is 0, continue      |
                |                   |                 |            | fetching images until stop  |
                |                   |                 |            | instruction is mentioned    |
                |                   |                 |            | explicitly.                 |
                |                   |                 |            | - Value range : 0 to 10000  |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``Upload         | ``integer``| Upload interval.            |
                |                   |Interval``       |            | - Value range : 1 to 2592000|
                |                   |                 |            | If 60 is specified,         |
                |                   |                 |            | 0.5FPS (=30/60)             |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``NumberOfInferen| ``integer``| Number of inference         |
                |                   |cesPerMessage``  |            | results to include in one   |
                |                   |                 |            | message (Inference Result). |
                |                   |                 |            | - Value range : 1  to 100   |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``MaxDetections  | ``integer``| No. of Objects included in  |
                |                   |PerFrame``       |            | 1 frame with respect to the |
                |                   |                 |            | Inference results metadata. |
                |                   |                 |            | - Value range : 1 to 5      |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``ModelId``      | ``string`` | Model ID.                   |
                +-------------------+-----------------+------------+-----------------------------+
                |                   |``PPLParameter`` | ``object`` |PPL parameter                |
                +-------------------+-----------------+------------+-----------------------------+

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
