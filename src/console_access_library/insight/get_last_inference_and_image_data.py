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
# pylint:disable=too-many-locals
# pylint:disable=too-many-return-statements
# pylint:disable=protected-access
# pylint:disable=broad-except
# pylint:disable=no-else-return

import logging
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass
from console_access_library.insight.get_images import GetImages
from console_access_library.insight.get_inference_results import GetInferenceresults

logger = logging.getLogger(__name__)


class SchemaGetLastInferenceAndImageData(Schema):
    """Schema for API to get the latest data of saved inference result and image.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : Edge AI Device ID
    device_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for device_id"}, strict=True
    )

    #: str, required : Image storage subdirectory. The subdirectory will be the directory notified
    #:                 in the start_upload_inference_result response.
    sub_directory_name = fields.String(
        required=True,
        error_messages={"invalid": "Invalid string for sub_directory_name"},
        strict=True,
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if str(data["device_id"]).strip() == "":
            raise ValidationError("device_id is required or can't be empty string")

        if str(data["sub_directory_name"]).strip() == "":
            raise ValidationError("sub_directory_name is required or can't be empty string")


class GetLastInferenceAndImageData(ConsoleAccessBaseClass):
    """This class implements API to get the latest data of saved inference result and image.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class GetLastInferenceAndImageData

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

    def _validate_params(self, params):
        """Validates parameters passed to get_last_inference_and_image_data API

        Args:
            params (dict): Dictionary of params with optional default values.

        Returns:
            dict: Updated dictionary of params with optional default values.
        """
        if "self" in params:
            del params["self"]

        return params

    def get_last_inference_and_image_data(
        self,
        device_id: str,
        sub_directory_name: str,
    ):
        """Get the latest data of saved inference result and image.

        Args:
            device_id (str, required) : Edge AI Device ID.
            sub_directory_name (str, required) : Image storage subdirectory Defaults to None.
                The subdirectory will be the directory notified in the
                start_upload_inference_result response.

        Returns:
            **Return Type**

            - On Success Response - dict
            - On Error Response - dict

            **Success Response Schema**

            - when time parameter is not specified

                +--------------------+------------+------------------------------------+
                | *Level1*           | *Type*     | *Description*                      |
                +--------------------+------------+------------------------------------+
                | ``image_data``     |``array``   | Refer :ref:`image_data <id7>`      |
                |                    |            | for more details                   |
                +--------------------+------------+------------------------------------+
                |``inference_data``  |``array``   | Refer :ref:`inference_data <ifd7>` |
                |                    |            | for more details                   |
                +--------------------+------------+------------------------------------+

                +----------------+---------------------------------------------------------------+
                | image_data     | .. _id7:                                                      |
                +----------------+----------------------+------------+---------------------------+
                | *Level1*       | *Level2*             | *Type*     | *Description*             |
                +----------------+----------------------+------------+---------------------------+
                | ``image_data`` |                      | ``array``  | image data                |
                |                |                      |            |                           |
                +----------------+----------------------+------------+---------------------------+
                |                | ``total_image_count``|  ``int``   | Set the total number of   |
                |                |                      |            | images                    |
                +----------------+----------------------+------------+---------------------------+
                |                | ``images``           | ``array``  | Refer :ref:`images <im7>` |
                |                |                      |            | for more details          |
                +----------------+----------------------+------------+---------------------------+

                +-----------------------+-----------------------------------------------------+
                | images                | .. _im7:                                            |
                +-----------------------+------------+------------+---------------------------+
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
                |                       |            |            | * Base64 encoding         |
                +-----------------------+------------+------------+---------------------------+

                +------------------+-------------+-----------+------------------------------------+
                | inference_data   | .. _ifd7:                                                    |
                +------------------+-------------+-----------+------------------------------------+
                | *Level1*         | *Level2*    | *Type*    | *Description*                      |
                +------------------+-------------+-----------+------------------------------------+
                |``inference_data``|             |``array``  | inference_data                     |
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
                |                  |``model      |``string`` |Model type.                         |
                |                  |_type``      |           |                                    |
                |                  |             |           |00: Image classification            |
                |                  |             |           |                                    |
                |                  |             |           |01: Object detection                |
                |                  |             |           |                                    |
                |                  |             |           |In the case of imported             |
                |                  |             |           |models, 01 is fixed at the          |
                |                  |             |           |current level.                      |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``training   |``string`` |Name of the training_kit            |
                |                  |_kit_name``  |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``_ts``      |``string`` |Timestamp. = System                 |
                |                  |             |           |registration date and time          |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``inference  |``string`` |Refer :ref:`inference_result <ifr7>`|
                |                  |_result``    |           |for more details                    |
                +------------------+-------------+-----------+------------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inference_result   | .. _ifr7:                                                 |
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
                |                    |``inferences``|``array``   |Refer :ref:`inferences <if7>`  |
                |                    |              |            |for more details               |
                +--------------------+--------------+------------+-------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inferences         | .. _if7:                                                  |
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

                +--------------------+------------+------------------------------------+
                | *Level1*           | *Type*     | *Description*                      |
                +--------------------+------------+------------------------------------+
                | ``image_data``     |``array``   | Refer :ref:`image_data <id8>`      |
                |                    |            | for more details                   |
                +--------------------+------------+------------------------------------+
                |``inference_data``  |``array``   | Refer :ref:`inference_data <ifd8>` |
                |                    |            | for more details                   |
                +--------------------+------------+------------------------------------+

                +----------------+---------------------------------------------------------------+
                | image_data     | .. _id8:                                                      |
                +----------------+----------------------+------------+---------------------------+
                | *Level1*       | *Level2*             | *Type*     | *Description*             |
                +----------------+----------------------+------------+---------------------------+
                | ``image_data`` |                      | ``array``  | image data                |
                |                |                      |            |                           |
                +----------------+----------------------+------------+---------------------------+
                |                | ``total_image_count``|  ``int``   | Set the total number of   |
                |                |                      |            | images                    |
                +----------------+----------------------+------------+---------------------------+
                |                | ``images``           | ``array``  | Refer :ref:`images <im8>` |
                |                |                      |            | for more details          |
                +----------------+----------------------+------------+---------------------------+

                +-----------------------+-----------------------------------------------------+
                | images                | .. _im8:                                            |
                +-----------------------+------------+------------+---------------------------+
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
                |                       |            |            | * Base64 encoding         |
                +-----------------------+------------+------------+---------------------------+

                +------------------+-----------------------------------------------------------+
                | inference_data   | .. _ifd8:                                                 |
                +------------------+--------------+-----------+--------------------------------+
                | *Level1*         | *Level2*     | *Type*    | *Description*                  |
                +------------------+--------------+-----------+--------------------------------+
                |``inference_data``|              |``array``  | inference_data                 |
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

                # Create Instance for Insight
                insight_obj = client_obj.get_insight()

                # set the real value
                device_id =  "__device_id__"
                sub_directory_name =  "__sub_directory_name__"
                raw =  "__raw__"

                # Insight - GetLastInferenceAndImageData
                response = insight_obj.get_last_inference_and_image_data(
                                                   device_id,
                                                   sub_directory_name,
                                                   )
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()

            # Validate API parameters
            _local_params = self._validate_params(_local_params)

            # Validate schema
            _local_params = SchemaGetLastInferenceAndImageData().load(_local_params)

            try:
                _get_images_obj = GetImages(self._config)
                _return_get_image_data = _get_images_obj.get_images(
                    device_id=_local_params["device_id"],
                    sub_directory_name=_local_params["sub_directory_name"],
                    number_of_images=1,
                    skip=0,
                    order_by="DESC",
                )
                _latest_image_data = ""
                _latest_inference_data = ""

                if len(_return_get_image_data["images"]) != 0:
                    _latest_image_data = _return_get_image_data
                    _latest_image_ts = _latest_image_data["images"][0]["name"].replace(".jpg", "")

                    _get_inference_obj = GetInferenceresults(self._config)
                    _return_get_inference_data = _get_inference_obj.get_inference_results(
                        device_id=_local_params["device_id"],
                        number_of_inference_results=1,
                        raw=1,
                        time=_latest_image_ts,
                    )

                    if len(_return_get_inference_data) != 0:
                        _latest_inference_data = _return_get_inference_data[0]

                    # Prepare the success response:
                    _return_get_last_inference_and_image_data = {
                        "image_data": _latest_image_data,
                        "inference_data": _latest_inference_data,
                    }
                    return _return_get_last_inference_and_image_data

                else:
                    _return_get_last_inference_and_image_data = {
                        "image_data": _latest_image_data,
                        "inference_data": _latest_inference_data,
                    }
                    return _return_get_last_inference_and_image_data

            except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                _return_get_last_inference_and_image_data = self.on_key_error_response(
                    __name__, key_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                _return_get_last_inference_and_image_data = self.on_type_error_response(
                    __name__, type_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                _return_get_last_inference_and_image_data = self.on_value_error_response(
                    __name__, val_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                _return_get_last_inference_and_image_data = self.on_attribute_error_response(
                    __name__, attr_err
                )

            except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                _return_get_last_inference_and_image_data = self.on_http_error_response(
                    __name__, exception
                )

            except Exception as exception:
                _return_get_last_inference_and_image_data = self.on_generic_error_response(
                    __name__, exception
                )

        except ValidationError as err:
            _return_get_last_inference_and_image_data = self.on_validation_error_response(
                __name__, err
            )

        return _return_get_last_inference_and_image_data
