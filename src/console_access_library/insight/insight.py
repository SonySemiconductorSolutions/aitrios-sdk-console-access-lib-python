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
        """Get the image save directory list of the devices for each device group

        Args:
            device_id (str, optional): Device ID. \
                If this is specified, return an image directory list linked\
                    to the specified device ID.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------------+------------+------------+--------------------------------+
                | *Level1*         | *Level2*   | *Type*     | *Description*                  |
                +==================+============+============+================================+
                | ``No_item_name`` |            | ``array``  |                                |
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
                +===================+====================+============+==========================+
                | ``devices``       |  ``array``         |            |                          |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_id``       | ``string`` | Set the device ID.       |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_name``     | ``string`` | Set the device name.     |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``Image``           | ``array``  | Refer :ref:`img <img1>`  |
                |                   |                    |            | for more details         |
                +-------------------+--------------------+------------+--------------------------+

                +-------------------+--------------------+------------+--------------------------+
                | Image             | .. _img1:                                                  |
                +-------------------+--------------------+------------+--------------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*            |
                +===================+====================+============+==========================+
                | ``Image``         |  ``array``         |            |                          |
                +-------------------+--------------------+------------+--------------------------+
                |                   |  ``No_item_name``  | ``string`` | Set the directory name.  |
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
        """Get the (saved) images for a specified device. \
            Application: Use to display an image in a UI

        Args:
            device_id (str, required) : Device ID.
            sub_directory_name (str, required) : Directory name.
            number_of_images (int, optional) : Number of images to fetch. \
                Value range: 0-256. \
                default: 50
            skip (int, optional) : Number of images to skip fetching. \
                default: 0
            order_by (str, optional) : Sort Order: Sort order by date image was created. \
                Value range: DESC, ASC.
                default: ASC

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-----------------------+------------+------------+---------------------------+
                | *Level1*              | *Level2*   | *Type*     | *Description*             |
                +=======================+============+============+===========================+
                | ``total_image_count`` |            | ``integer``| Set the total number of   |
                |                       |            |            | images                    |
                +-----------------------+------------+------------+---------------------------+
                |``images``             |            | ``array``  |                           |
                +-----------------------+------------+------------+---------------------------+
                |                       | ``name``   | ``string`` | Set the image filename.   |
                +-----------------------+------------+------------+---------------------------+
                |                       |``contents``| ``string`` | Images file contents      |
                |                       |            |            | (BASE64 encoding)         |
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
        """Get the (saved) inference result metadata list information for a specified device

        Args:
            device_id (str, required) : Device ID
            filter (str, optional) : Search filter.
                The specifications are the same except for those of Cosmos DB UI \
                    of the Azure portal and those listed below.

                - A where string does not need to be added to the heading.
                - deviceID does not need to be added.

                        Filter Example:

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

                Default = ''

            number_of_inference_results (int, optional) :Number of cases to get.
                Return the latest record of the specified number of cases. Maximum value: 10000.
                default: 20

            raw (int, optional) : If 1 is specified, add a record stored to Cosmos DB and return it.

                - Value definitions

                    - 0: Do not add
                    - 1: Add

                default: 1

            time (str, optional) : When this value is specified,\
                    extract the inference result metadata within the following range. \
                    Default:""

                    - Extraction range:
                      (time - threshold) <= T

                      Time in inference result metadata < (time + threshold)

                    - Value definition

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

                +------------------+-------------+-----------+------------------------------------+
                | *Level1*         | *Level2*    | *Type*    | *Description*                      |
                +==================+============+============+====================================+
                | ``No_item_name`` |             |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``id``       | ``string``| Inference result metadata ID.      |
                |                  |             |           | =GUID generated automatically by   |
                |                  |             |           | CosmosDB                           |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``device_id``| ``string``| Device ID.                         |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model_id`` | ``string``| Model ID.                          |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``version    | ``string``| Version number.                    |
                |                  |_number``    |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model      |``string`` | Model version ID.                  |
                |                  |_version_id``|           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model      |``string`` | Model type                         |
                |                  |_type``      |           |                                    |
                |                  |             |           | 00: Image category                 |
                |                  |             |           |                                    |
                |                  |             |           | 01: Object detection               |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``training   |``string`` |                                    |
                |                  |_kit_name``  |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``_ts``      |``integer``| Timestamp.                         |
                |                  |             |           | =_ts of CosmosDB                   |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``inference  |           |Refer :ref:`inference_result <ifr9>`|
                |                  |_result``    |           |for more details                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``inferenc   |``array``  |Refer :ref:`inferences <if9>`       |
                |                  |es``         |           |for more details                    |
                +------------------+-------------+-----------+------------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inference_result   | .. _ifr9:                                                 |
                +--------------------+--------------+------------+-------------------------------+
                | *Level1*           | *Level2*     | *Type*     | *Description*                 |
                +====================+==============+============+===============================+
                |``inference_result``|              |            |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``DeviceID``  | ``string`` |Device ID                      |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``ModelID``   |``string``  |DnnModelVersion                |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``Image``     |``boolean`` |Synchronized to the            |
                |                    |              |            |InputTensor output.            |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``Inferences``|``array``   |Refer :ref:`inferences <if9>`  |
                |                    |              |            |for more details               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``id``        |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``ttl``       |``integer`` |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_rid``      |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_self``     |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_etag``     |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_attachm    |``string``  |                               |
                |                    |ents``        |            |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_ts``       |``integer`` |                               |
                +--------------------+--------------+------------+-------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inferences         | .. _if9:                                                  |
                +--------------------+--------------+------------+-------------------------------+
                | *Level1*           | *Level2*     | *Type*     | *Description*                 |
                +====================+==============+============+===============================+
                |``inferences``      |              | ``array``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``T``         | ``string`` |Time when retrieving           |
                |                    |              |            |data from the sensor.          |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``O``         |``string``  |Output tensor (Encoding format)|
                +--------------------+--------------+------------+-------------------------------+

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
            device_id (str, required) : Device ID.
            sub_directory_name (str, required) : Directory name.
            number_of_images (int, optional) : Number of images to fetch. \
                Value range: 0-256. If not specified: 50.
            skip (int, optional) : Number of images to skip fetching. \
                If not specified: 0.
            order_by (str, optional) : Sort Order: Sort order by date image was created. \
                Value range: DESC, ASC.
                If not specified: ASC.

        Returns:
            **Return Type**

            - On Success Response - dict
            - On Error Response - dict

            **Success Response Schema**

                +-----------------------+------------+------------+---------------------------+
                | *Level1*              | *Level2*   | *Type*     | *Description*             |
                +=======================+============+============+===========================+
                | ``total_image_count`` |            | ``integer``| Set the total number of   |
                |                       |            |            | images                    |
                +-----------------------+------------+------------+---------------------------+
                |``images``             |            | ``array``  |                           |
                +-----------------------+------------+------------+---------------------------+
                |                       | ``name``   | ``string`` | Set the image filename.   |
                +-----------------------+------------+------------+---------------------------+
                |                       |``contents``| ``string`` | Images file contents      |
                |                       |            |            | (BASE64 encoding)         |
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
            device_id (str, required) : Device ID

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------------+-------------+-----------+------------------------------------+
                | *Level1*         | *Level2*    | *Type*    | *Description*                      |
                +==================+============+============+====================================+
                | ``No_item_name`` |             |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``id``       | ``string``| Inference result metadata ID.      |
                |                  |             |           | =GUID generated automatically by   |
                |                  |             |           | CosmosDB                           |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``device_id``| ``string``| Device ID.                         |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model_id`` | ``string``| Model ID.                          |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``version    | ``string``| Version number.                    |
                |                  |_number``    |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model      |``string`` | Model version ID.                  |
                |                  |_version_id``|           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model      |``string`` | Model type                         |
                |                  |_type``      |           |                                    |
                |                  |             |           | 00: Image category                 |
                |                  |             |           |                                    |
                |                  |             |           | 01: Object detection               |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``training   |``string`` |                                    |
                |                  |_kit_name``  |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``_ts``      |``integer``| Timestamp.                         |
                |                  |             |           | =_ts of CosmosDB                   |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``inference  |           |Refer :ref:`inference_result <ifr4>`|
                |                  |_result``    |           |for more details                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``inferenc   |``array``  |Refer :ref:`inferences <if4>`       |
                |                  |es``         |           |for more details                    |
                +------------------+-------------+-----------+------------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inference_result   | .. _ifr4:                                                 |
                +--------------------+--------------+------------+-------------------------------+
                | *Level1*           | *Level2*     | *Type*     | *Description*                 |
                +====================+==============+============+===============================+
                |``inference_result``|              |            |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``DeviceID``  | ``string`` |Device ID                      |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``ModelID``   |``string``  |DnnModelVersion                |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``Image``     |``boolean`` |Synchronized to the            |
                |                    |              |            |InputTensor output.            |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``Inferences``|``array``   |Refer :ref:`inferences <if4>`  |
                |                    |              |            |for more details               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``id``        |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``ttl``       |``integer`` |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_rid``      |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_self``     |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_etag``     |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_attachm    |``string``  |                               |
                |                    |ents``        |            |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_ts``       |``integer`` |                               |
                +--------------------+--------------+------------+-------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inferences         | .. _if4:                                                  |
                +--------------------+--------------+------------+-------------------------------+
                | *Level1*           | *Level2*     | *Type*     | *Description*                 |
                +====================+==============+============+===============================+
                |``inferences``      |              | ``array``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``T``         | ``string`` |Time when retrieving           |
                |                    |              |            |data from the sensor.          |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``O``         |``string``  |Output tensor (Encoding format)|
                +--------------------+--------------+------------+-------------------------------+

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
        """Get the latest data of saved inference result and image.

        Args:
            device_id (str, required) : Device ID
            sub_directory_name (str, required) : Directory name

        Returns:
            **Return Type**

            - On Success Response - dict
            - On Error Response - dict

            **Success Response Schema**

                +--------------------+------------+------------------------------------+
                | *Level1*           | *Type*     | *Description*                      |
                +====================+============+====================================+
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
                +================+======================+============+===========================+
                | ``image_data`` |                      | ``array``  | image data                |
                |                |                      |            |                           |
                +----------------+----------------------+------------+---------------------------+
                |                | ``total_image_count``| ``integer``| Set the total number of   |
                |                |                      |            | images                    |
                +----------------+----------------------+------------+---------------------------+
                |                | ``images``           | ``array``  | Refer :ref:`images <im1>` |
                |                |                      |            | for more details          |
                +----------------+----------------------+------------+---------------------------+

                +-----------------------+-----------------------------------------------------+
                | images                | .. _im1:                                            |
                +-----------------------+------------+------------+---------------------------+
                | *Level1*              | *Level2*   | *Type*     | *Description*             |
                +=======================+============+============+===========================+
                |``images``             |            | ``array``  |                           |
                +-----------------------+------------+------------+---------------------------+
                |                       | ``name``   | ``string`` | Set the image filename.   |
                +-----------------------+------------+------------+---------------------------+
                |                       |``contents``| ``string`` | Images file contents      |
                |                       |            |            | (BASE64 encoding)         |
                +-----------------------+------------+------------+---------------------------+

                +------------------+-------------+-----------+------------------------------------+
                | inference_data   | .. _ifd1:                                                    |
                +------------------+-------------+-----------+------------------------------------+
                | *Level1*         | *Level2*    | *Type*    | *Description*                      |
                +==================+=============+===========+====================================+
                |``inference_data``|             |``array``  | inference_data                     |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``id``       | ``string``| Inference result metadata ID.      |
                |                  |             |           | =GUID generated automatically by   |
                |                  |             |           | CosmosDB                           |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``device_id``| ``string``| Device ID.                         |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model_id`` | ``string``| Model ID.                          |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``version    | ``string``| Version number.                    |
                |                  |_number``    |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model      |``string`` | Model version ID.                  |
                |                  |_version_id``|           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model      |``string`` | Model type                         |
                |                  |_type``      |           |                                    |
                |                  |             |           | 00: Image category                 |
                |                  |             |           |                                    |
                |                  |             |           | 01: Object detection               |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``training   |``string`` |                                    |
                |                  |_kit_name``  |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``_ts``      |``integer``| Timestamp.                         |
                |                  |             |           | =_ts of CosmosDB                   |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``inference  |           |Refer :ref:`inference_result <ifr1>`|
                |                  |_result``    |           |for more details                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``inferenc   |``array``  |Refer :ref:`inferences <if1>`       |
                |                  |es``         |           |for more details                    |
                +------------------+-------------+-----------+------------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inference_result   | .. _ifr1:                                                 |
                +--------------------+--------------+------------+-------------------------------+
                | *Level1*           | *Level2*     | *Type*     | *Description*                 |
                +====================+==============+============+===============================+
                |``inference_result``|              |            |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``DeviceID``  | ``string`` |Device ID                      |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``ModelID``   |``string``  |DnnModelVersion                |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``Image``     |``boolean`` |Synchronized to the            |
                |                    |              |            |InputTensor output.            |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``Inferences``|``array``   |Refer :ref:`inferences <if1>`  |
                |                    |              |            |for more details               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``id``        |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``ttl``       |``integer`` |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_rid``      |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_self``     |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_etag``     |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_attachm    |``string``  |                               |
                |                    |ents``        |            |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_ts``       |``integer`` |                               |
                +--------------------+--------------+------------+-------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inferences         | .. _if1:                                                  |
                +--------------------+--------------+------------+-------------------------------+
                | *Level1*           | *Level2*     | *Type*     | *Description*                 |
                +====================+==============+============+===============================+
                |``inferences``      |              | ``array``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``T``         | ``string`` |Time when retrieving           |
                |                    |              |            |data from the sensor.          |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``O``         |``string``  |Output tensor (Encoding format)|
                +--------------------+--------------+------------+-------------------------------+

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
        """Get the URL to export the images of specified conditions in zip file format. \
            For encrypted images for learning in other environments

            [Prerequisites]

            - The encryption method is public key cryptography.
            - A zip file containing the target images can be downloaded by accessing a URL. \
                Each image is encoded using the method described hereafter.
            - The key used for encryption is a shared key of 32 characters issued randomly by \
                the API each time.
            - The image encryption method is AES128, MODE_CBC
            - The iv (initial vector, 16 digits) and encrypted data are stored in a zip file.

            [Generating a Key]

            - Private keys are issued by Sier itself.
            - Public and private keys are issued with a length of 1024 or 2048.
            - The public key (key) specified to the parameter of this API passes the pem file\
                content of the public key in a base64 encoded format.

            Example: Base64 encode the entire string as follows:

            -----BEGIN PUBLIC KEY-----

            MIGfMA0GCSqGSIb3DQEBAQUAA4GNADC

            ...

            -----END PUBLIC KEY-----

        Args:
            key (str, required) : Public key. \
                Base64-encoded format of the entire pem file contents of the public key
            from_datetime (str, optional) : Date and time (From). Form: yyyyMMddhhmm \
                Default:""
            to_datetime (str, optional) : Date/Time (To). Form: yyyyMMddhhmm \
                Default:""
            device_id (str, optional) : Device ID.
            file_format (str, optional) : Image file format. Default:""\
                If this is not specified, there is no filtering.

                - Value definition

                    - JPG
                    - BMP

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-------------+------------+---------------------------+
                | *Level1*    | *Type*     | *Description*             |
                +=============+============+===========================+
                | ``key``     | ``string`` | Shared key for decrypting |
                |             |            | images encrypted by       |
                |             |            | a public key.             |
                +-------------+------------+---------------------------+
                | ``url``     | ``string`` | SUS URI for downloading   |
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
