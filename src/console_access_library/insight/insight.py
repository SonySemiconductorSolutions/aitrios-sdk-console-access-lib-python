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
# pylint:disable=anomalous-backslash-in-string

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass
from console_access_library.insight.get_image_data import GetImageData
from console_access_library.insight.get_image_directories import GetImageDirectories
from console_access_library.insight.get_images import GetImages
from console_access_library.insight.get_inference_results import GetInferenceresults
from console_access_library.insight.get_last_inference_and_image_data import (
    GetLastInferenceAndImageData,
)
from console_access_library.insight.get_last_inference_data import GetLastInferenceData
from console_access_library.insight.export_images import ExportImages


class Insight(ConsoleAccessBaseClass):
    """Abstract class to access Console Access Library Insight component APIs from Insight component

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for Insight Abstract class

        Args:
            config(object): Object of Configuration Class
        """
        super().__init__()
        self._get_image_directories_obj = GetImageDirectories(config)
        self._get_images_obj = GetImages(config)
        self._get_inference_results_obj = GetInferenceresults(config)
        self._get_image_data_obj = GetImageData(config)
        self._get_last_inference_data_obj = GetLastInferenceData(config)
        self._get_last_inference_and_image_data_obj = GetLastInferenceAndImageData(config)
        self._export_images_obj = ExportImages(config)

    def get_image_directories(self, device_id: str = None):
        """Abstract function call to ``get_image_directories`` API

        Args:
            device_id (str, optional): Edge AI Device ID. \
                If not specified, returns all device_id information.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------------+------------+------------+--------------------------------+
                | *Level1*         | *Level2*   | *Type*     | *Description*                  |
                +------------------+------------+------------+--------------------------------+
                | ``No_item_name`` |            |            | Device Affiliation Group Array |
                +------------------+------------+------------+--------------------------------+
                |                  |``group_id``| ``string`` | Set the device group ID.       |
                +------------------+------------+------------+--------------------------------+
                |                  | ``devices``| ``array``  | Refer :ref:`devices <devices1>`|
                |                  |            |            | for more details               |
                +------------------+------------+------------+--------------------------------+

                +-------------------+--------------------+------------+--------------------------+
                | devices           | .. _devices1:                                              |
                +-------------------+--------------------+------------+--------------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*            |
                +-------------------+--------------------+------------+--------------------------+
                | ``devices``       |  ``array``         |            | Device Array.            |
                |                   |                    |            | The subordinate          |
                |                   |                    |            | elements are listed      |
                |                   |                    |            | in ascending order       |
                |                   |                    |            | by device ID             |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_id``       | ``string`` | Device ID.               |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_name``     | ``string`` | Device name at the time  |
                |                   |                    |            | of registration          |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``Image``           | ``array``  | The descendant elements  |
                |                   |                    |            | are listed in ascending  |
                |                   |                    |            | order by directory name. |
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
        return self._get_image_directories_obj.get_image_directories(device_id)

    def get_images(
        self,
        device_id: str,
        sub_directory_name: str,
        number_of_images: int = 50,
        skip: int = 0,
        order_by: str = "ASC",
    ):
        """Abstract function call to ``get_images`` API

        Args:
            device_id (str, required) : Edge AI Device ID.
            sub_directory_name (str, required) : Image storage subdirectory. \
                The subdirectory is the directory notified by the response of \
                start_upload_inference_result or the directory obtained by \
                get_image_directories.
            number_of_images (int, optional) : Number of images acquired. \
                0-256. If not specified: 50.
            skip (int, optional) : Number of images to skip fetching. \
                If not specified: 0.
            order_by (str, optional) : Sort Order: Sort order by date and time the \
                image was created. DESC, ASC, desc, asc. \
                If not specified: ASC.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-----------------------+------------+------------+---------------------------+
                | *Level1*              | *Level2*   | *Type*     | *Description*             |
                +-----------------------+------------+------------+---------------------------+
                | ``total_image_count`` |            |  ``int``   | Set the total number of   |
                |                       |            |            | images                    |
                +-----------------------+------------+------------+---------------------------+
                |``images``             |            | ``array``  | Image file name array     |
                |                       |            |            | The descendant elements   |
                |                       |            |            | are listed in ascending   |
                |                       |            |            | order by image file name. |
                +-----------------------+------------+------------+---------------------------+
                |                       | ``name``   | ``string`` | Set the image file name.  |
                +-----------------------+------------+------------+---------------------------+
                |                       |``contents``| ``string`` | Image file contents       |
                |                       |            |            | \*Base64 encoding         |
                +-----------------------+------------+------------+---------------------------+

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
        return self._get_images_obj.get_images(
            device_id, sub_directory_name, number_of_images, skip, order_by
        )

    def get_inference_results(
        self,
        device_id: str,
        filter: str = None,
        number_of_inference_results: int = 20,
        raw: int = 1,
        time: str = None,
    ):
        """Abstract function call to ``get_inference_results`` API

        Args:
            device_id (str, required) : Edge AI Device ID.
            filter (str, optional) : The Filter. Search filter (same specifications as Cosmos DB UI\
                                     on Azure portal except for the following)

                                        - No need to prepend where string
                                        - It is not necessary to add a deviceID.

                                    Filter Samples:

                                    * ModelID: string  match filter

                                        eg. "c.ModelID=\"0300000001590100\""

                                    * Image: boolean  match filter eg. "c.Image=true"

                                    * T: string  match or more filter

                                        eg. "c.Inferences[0].T>=\"20230412140050618\""

                                    * T: string  range filter

                                        eg. "EXISTS(SELECT VALUE i FROM i IN c.Inferences \
                                            WHERE i.T >= \"20230412140023098\" AND \
                                            i.T <= \"20230412140029728\")"

                                    * _ts: number  match filter

                                        eg. "c._ts=1681308028"

            number_of_inference_results (int, optional) :Number of acquisitions.\
                                                         If not specified: 20

            raw (int, optional) : Data format of inference results.

                                    - 1:Append records stored in Cosmos DB.
                                    - 0:Not granted.

                                        If not specified: 1

            time (str, optional) : The Time. Inference result data stored in Cosmos DB.\
                                   yyyyMMddHHmmssfff

                                    - yyyy: 4-digit year string
                                    - MM: 2-digit month string
                                    - dd: 2-digit day string
                                    - HH: 2-digit hour string
                                    - mm: 2-digit minute string
                                    - ss: 2-digit seconds string
                                    - fff: 3-digit millisecond string

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

            - when time parameter is not specified

                +------------------+-------------+-----------+------------------------------------+
                | *Level1*         | *Level2*    | *Type*    | *Description*                      |
                +------------------+-------------+-----------+------------------------------------+
                | ``No_item_name`` |             |           | The subordinate elements are       |
                |                  |             |           | listed in descending order         |
                |                  |             |           | by system registration date        |
                |                  |             |           | and time.                          |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``id``       | ``string``| The ID of the inference            |
                |                  |             |           | result metadata.                   |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``device_id``| ``string``| Device ID.                         |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model_id`` | ``string``| Model ID.                          |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model      |``string`` | Dnn Model Version                  |
                |                  |_version_id``|           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model      |``string`` | Model type.                        |
                |                  |_type``      |           |                                    |
                |                  |             |           | 00: Image classification           |
                |                  |             |           |                                    |
                |                  |             |           | 01: Object detection               |
                |                  |             |           |                                    |
                |                  |             |           | In the case of imported            |
                |                  |             |           | models, 01 is fixed at the         |
                |                  |             |           | current level.                     |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``training   |``string`` | Name of the training_kit           |
                |                  |_kit_name``  |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``_ts``      |``string`` | Timestamp. = System                |
                |                  |             |           | registration date and time         |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``inference  |``string`` |Refer :ref:`inference_result <ifr9>`|
                |                  |_result``    |           |for more details                    |
                +------------------+-------------+-----------+------------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inference_result   | .. _ifr9:                                                 |
                +--------------------+--------------+------------+-------------------------------+
                | *Level1*           | *Level2*     | *Type*     | *Description*                 |
                +--------------------+--------------+------------+-------------------------------+
                |``inference_result``|              | ``array``  |Raw data for inference result  |
                |                    |              |            |in ascending order of project  |
                |                    |              |            |type and model project name.   |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``device_id`` | ``string`` |Device ID                      |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``model_id``  |``string``  |DnnModelVersion                |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``image``     |``boolean`` |Is it synchronized with        |
                |                    |              |            |the output of InputTensor?     |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``inferences``|``array``   |Refer :ref:`inferences <if9>`  |
                |                    |              |            |for more details               |
                +--------------------+--------------+------------+-------------------------------+
                +--------------------+--------------+------------+-------------------------------+
                | inferences         | .. _if9:                                                  |
                +--------------------+--------------+------------+-------------------------------+
                | *Level1*           | *Level2*     | *Type*     | *Description*                 |
                +--------------------+--------------+------------+-------------------------------+
                |``inferences``      |              | ``array``  |Inference result Array         |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``T``         | ``string`` |The time at which the data     |
                |                    |              |            |was acquired from the sensor.  |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``O``         |``string``  |Outputtensor output without    |
                |                    |              |            |going through PPL              |
                +--------------------+--------------+------------+-------------------------------+

            - when time parameter is specified

                +------------------+--------------+-----------+--------------------------------+
                | *Level1*         | *Level2*     | *Type*    | *Description*                  |
                +------------------+--------------+-----------+--------------------------------+
                | ``No_item_name`` |              |           | The subordinate elements are   |
                |                  |              |           | listed in descending order     |
                |                  |              |           | by system registration date    |
                |                  |              |           | and time.                      |
                +------------------+--------------+-----------+--------------------------------+
                |                  |``id``        | ``string``| The ID of the inference result |
                |                  |              |           | metadata. = GUID automatically |
                |                  |              |           | fired by CosmosDB              |
                +------------------+--------------+-----------+--------------------------------+
                |                  |``device_id`` | ``string``| Device ID.                     |
                +------------------+--------------+-----------+--------------------------------+
                |                  |``model_id``  | ``string``| Model ID.                      |
                +------------------+--------------+-----------+--------------------------------+
                |                  |``_ts``       |``string`` | Timestamp. = System            |
                |                  |              |           | registration date and time     |
                +------------------+--------------+-----------+--------------------------------+
                |                  |``inferences``|``array``  |Refer :ref:`inferences <if7>`   |
                |                  |              |           |for more details                |
                +------------------+--------------+-----------+--------------------------------+

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
        return self._get_inference_results_obj.get_inference_results(
            device_id, filter, number_of_inference_results, raw, time
        )

    def get_image_data(
        self,
        device_id: str,
        sub_directory_name: str,
        number_of_images: int = 50,
        skip: int = 0,
        order_by: str = "ASC",
    ):
        """Abstract function call to ``get_image_data`` API

        Args:
            device_id (str, required) : Edge AI Device ID.
            sub_directory_name (str, required) : Image storage subdirectory. \
                The subdirectory is the directory notified by the response of \
                start_upload_inference_resultor the directory obtained by get_image_directories.
            number_of_images (int, optional) : Number of images acquired. If not specified: 50
            skip (int, optional) : number of images to skip fetching. If not specified: 0
            order_by (str, optional) : Sort Order: Sort order by date \
                and time the image was created. Values allowed: DESC, ASC, desc, asc. \
                If not specified: ASC.

        Returns:
            **Return Type**

            - On Success Response - dict
            - On Error Response - dict

            **Success Response Schema**

                +-----------------------+------------+------------+---------------------------+
                | *Level1*              | *Level2*   | *Type*     | *Description*             |
                +-----------------------+------------+------------+---------------------------+
                | ``total_image_count`` |            |  ``int``   | Set the total number of   |
                |                       |            |            | images                    |
                +-----------------------+------------+------------+---------------------------+
                |``images``             |            | ``array``  | Image file name array     |
                |                       |            |            | The descendant elements   |
                |                       |            |            | are listed in ascending   |
                |                       |            |            | order by image file name. |
                +-----------------------+------------+------------+---------------------------+
                |                       | ``name``   | ``string`` | Set the image file name.  |
                +-----------------------+------------+------------+---------------------------+
                |                       |``contents``| ``string`` | Image file contents       |
                |                       |            |            | \*Base64 encoding         |
                +-----------------------+------------+------------+---------------------------+

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
        return self._get_image_data_obj.get_image_data(
            device_id, sub_directory_name, number_of_images, skip, order_by
        )

    def get_last_inference_data(
        self,
        device_id: str,
    ):
        """Abstract function call to ``get_last_inference_data`` API

        Args:
            device_id (str, required) : The Device ID.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

            - when time parameter is not specified

                +-------------+-----------+------------------------------------+
                | *Level1*    | *Type*    | *Description*                      |
                +-------------+-----------+------------------------------------+
                |``id``       | ``string``| The ID of the inference            |
                |             |           | result metadata.                   |
                +-------------+-----------+------------------------------------+
                |``device_id``| ``string``| Device ID.                         |
                +-------------+-----------+------------------------------------+
                |``model_id`` | ``string``| Model ID.                          |
                +-------------+-----------+------------------------------------+
                |``model      |``string`` | Dnn Model Version                  |
                |_version_id``|           |                                    |
                +-------------+-----------+------------------------------------+
                |``model      |``string`` | Model type.                        |
                |_type``      |           |                                    |
                |             |           | 00: Image classification           |
                |             |           |                                    |
                |             |           | 01: Object detection               |
                |             |           |                                    |
                |             |           | In the case of imported            |
                |             |           | models, 01 is fixed at the         |
                |             |           | current level.                     |
                +-------------+-----------+------------------------------------+
                |``training   |``string`` | Name of the training_kit           |
                |_kit_name``  |           |                                    |
                +-------------+-----------+------------------------------------+
                |``_ts``      |``string`` | Timestamp. = System                |
                |             |           | registration date and time         |
                +-------------+-----------+------------------------------------+
                |``inference  |``string`` |Refer :ref:`inference_result <ifr4>`|
                |_result``    |           |for more details                    |
                +-------------+-----------+------------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inference_result   | .. _ifr4:                                                 |
                +--------------------+--------------+------------+-------------------------------+
                | *Level1*           | *Level2*     | *Type*     | *Description*                 |
                +--------------------+--------------+------------+-------------------------------+
                |``inference_result``|              | ``array``  |Raw data for inference result  |
                |                    |              |            |in ascending order of project  |
                |                    |              |            |type and model project name.   |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``device_id`` | ``string`` |Device ID                      |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``model_id``  |``string``  |DnnModelVersion                |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``image``     |``boolean`` |Is it synchronized with        |
                |                    |              |            |the output of InputTensor?     |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``inferences``|``array``   |Refer :ref:`inferences <if4>`  |
                |                    |              |            |for more details               |
                +--------------------+--------------+------------+-------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inferences         | .. _if4:                                                  |
                +--------------------+--------------+------------+-------------------------------+
                | *Level1*           | *Level2*     | *Type*     | *Description*                 |
                +--------------------+--------------+------------+-------------------------------+
                |``inferences``      |              | ``array``  |Inference result Array         |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``T``         | ``string`` |The time at which the data     |
                |                    |              |            |was acquired from the sensor.  |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``O``         |``string``  |Outputtensor output without    |
                |                    |              |            |going through PPL              |
                +--------------------+--------------+------------+-------------------------------+

            - when time parameter is specified

                +--------------+-----------+--------------------------------+
                | *Level1*     | *Type*    | *Description*                  |
                +--------------+-----------+--------------------------------+
                |``id``        | ``string``| The ID of the inference result |
                |              |           | metadata. = GUID automatically |
                |              |           | fired by CosmosDB              |
                +--------------+-----------+--------------------------------+
                |``device_id`` | ``string``| Device ID.                     |
                +--------------+-----------+--------------------------------+
                |``model_id``  | ``string``| Model ID.                      |
                +--------------+-----------+--------------------------------+
                |``_ts``       |``string`` | Timestamp. = System            |
                |              |           | registration date and time     |
                +--------------+-----------+--------------------------------+
                |``inferences``|``array``  |Refer :ref:`inferences <if4>`   |
                |              |           |for more details                |
                +--------------+-----------+--------------------------------+

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
        return self._get_last_inference_data_obj.get_last_inference_data(device_id)

    def get_last_inference_and_image_data(
        self,
        device_id: str,
        sub_directory_name: str,
    ):
        """Abstract function call to ``get_last_inference_and_image_data`` API

        Args:
            device_id (str, required) : The Device ID.
            sub_directory_name (str, required) : The Sub Directory Name.
                The subdirectory will be the directory notified in the response
                of start_upload_inference_result.

        Returns:
            **Return Type**

            - On Success Response - dict
            - On Error Response - dict

            **Success Response Schema**

                +--------------------+------------+------------------------------------+
                | *Level1*           | *Type*     | *Description*                      |
                +--------------------+------------+------------------------------------+
                | ``image_data``     |``array``   | Refer :ref:`image_data <id1>`      |
                |                    |            | for more details                   |
                +--------------------+------------+------------------------------------+
                |``inference_data``  |``array``   | Refer :ref:`inference_data <ifd1>` |
                |                    |            | for more details                   |
                +--------------------+------------+------------------------------------+

                +----------------+---------------------------------------------------------------+
                | image_data     | .. _id1:                                                      |
                +----------------+----------------------+------------+---------------------------+
                | *Level1*       | *Level2*             | *Type*     | *Description*             |
                +----------------+----------------------+------------+---------------------------+
                | ``image_data`` |                      | ``array``  | image data                |
                |                |                      |            |                           |
                +----------------+----------------------+------------+---------------------------+
                |                | ``total_image_count``|  ``int``   | Set the total number of   |
                |                |                      |            | images                    |
                +----------------+----------------------+------------+---------------------------+
                |                | ``images``           | ``array``  | Refer :ref:`images <im1>` |
                |                |                      |            | for more details          |
                +----------------+----------------------+------------+---------------------------+

                +-----------------------+-----------------------------------------------------+
                | images                | .. _im1:                                            |
                +-----------------------+------------+----------------------------------------+
                | *Level1*              | *Level2*   | *Type*     | *Description*             |
                +-----------------------+------------+------------+---------------------------+
                |``images``             |            | ``array``  | Image file name array     |
                |                       |            |            | The descendant elements   |
                |                       |            |            | are listed in ascending   |
                |                       |            |            | order by image file name. |
                +-----------------------+------------+------------+---------------------------+
                |                       | ``name``   | ``string`` | Set the image file name.  |
                +-----------------------+------------+------------+---------------------------+
                |                       |``contents``| ``string`` | Image file contents       |
                |                       |            |            | \*Base64 encoding         |
                +-----------------------+------------+------------+---------------------------+

                +------------------+----------------------------------------------------------+
                | inference_data   | .. _ifd1:                                                |
                +------------------+------------------+------------+--------------------------+
                | *Level1*         | *Level2*         | *Type*     | *Description*            |
                +------------------+------------------+------------+--------------------------+
                |``inference_data``|                  |``array``   | inference_data           |
                +------------------+------------------+------------+--------------------------+
                |                  |``id``            | ``string`` | The ID of the inference  |
                |                  |                  |            | result metadata.         |
                +------------------+------------------+------------+--------------------------+
                |                  |``device_id``     | ``string`` | Device ID.               |
                +------------------+------------------+------------+--------------------------+
                |                  |``model_id``      | ``string`` | Model ID.                |
                +------------------+------------------+------------+--------------------------+
                |                  |``model           |``string``  | Dnn Model Version        |
                |                  |_version_id``     |            |                          |
                +------------------+------------------+------------+--------------------------+
                |                  |``model           |``string``  |Model type                |
                |                  |_type``           |            |                          |
                |                  |                  |            |00: Image classification  |
                |                  |                  |            |                          |
                |                  |                  |            |01: Object detection      |
                |                  |                  |            |                          |
                |                  |                  |            |In the case of imported   |
                |                  |                  |            |models, 01 is fixed at the|
                |                  |                  |            |current level.            |
                +------------------+------------------+------------+--------------------------+
                |                  |``training        |``string``  |Name of the training_kit  |
                |                  |_kit_name``       |            |                          |
                +------------------+------------------+------------+--------------------------+
                |                  |``_ts``           |``string``  |Timestamp. = System       |
                |                  |                  |            |registration date and time|
                +------------------+------------------+------------+--------------------------+
                |                  |``inference       |``string``  | Raw data for inference   |
                |                  |_result``         |            | result metadata          |
                +------------------+------------------+------------+--------------------------+

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
        return self._get_last_inference_and_image_data_obj.get_last_inference_and_image_data(
            device_id=device_id, sub_directory_name=sub_directory_name
        )

    def export_images(
        self,
        key: str,
        from_datetime: str = None,
        to_datetime: str = None,
        device_id: str = None,
        file_format: str = None,
    ):
        """Abstract function call to ``export_images`` API

        Args:
            key (str, required) : The public key. \
                Base64-encoded format of the entire contents of the public key PEM file
            from_datetime (str, optional) : Date and time (From). Form: yyyyMMddhhmm
            to_datetime (str, optional) : Date and time (To). Form: yyyyMMddhhmm
            device_id (str, optional) : Device ID.
            file_format (str, optional) : Image file format. \
                If not specified, no filtering. \
                Value definition

                - JPG
                - BMP
                - RAW

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-------------+------------+---------------------------+
                | *Level1*    | *Type*     | *Description*             |
                +-------------+------------+---------------------------+
                | ``key``     | ``string`` | A common key for image    |
                |             |            | decryption encrypted with |
                |             |            | a public key.             |
                +-------------+------------+---------------------------+
                | ``url``     | ``string`` | SUS URI for download      |
                +-------------+------------+---------------------------+

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
        return self._export_images_obj.export_images(
            key,
            from_datetime,
            to_datetime,
            device_id,
            file_format,
        )
