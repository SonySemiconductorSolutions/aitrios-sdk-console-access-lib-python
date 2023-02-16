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
# pylint:disable=too-many-nested-blocks
# pylint:disable=too-many-branches
# pylint:disable=anomalous-backslash-in-string

import logging
import math
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass
from console_access_library.insight.get_images import GetImages

logger = logging.getLogger(__name__)


class SchemaGetImageData(Schema):
    """Schema for API to get a (saved) image of the specified device.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : Edge AI Device ID
    device_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for device_id"}, strict=True
    )

    #: str, required : Image storage subdirectory. The subdirectory is the directory
    #:                 notified by the response of start_upload_inference_result or the
    #:                 directory obtained by get_image_directories.
    sub_directory_name = fields.String(
        required=True,
        error_messages={"invalid": "Invalid string for sub_directory_name"},
        strict=True,
    )

    #: int, optional : Number of images acquired. If not specified defauls to 50.
    number_of_images = fields.Integer(
        required=False,
        error_messages={"invalid": "Invalid integer for number_of_images"},
        strict=True,
    )

    #: int, optional : Skip.
    skip = fields.Integer(
        required=False, error_messages={"invalid": "Invalid integer for skip"}, strict=True
    )

    #: str, optional : Sort Order, Sort order by date and time the image was created.
    #:                 Values allowed: DESC, ASC, desc, asc. If not specified defauls to ASC.
    order_by = fields.String(
        required=False, error_messages={"invalid": "Invalid string for order_by"}, strict=True
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if str(data["device_id"]).strip() == "":
            raise ValidationError("device_id is required or can't be empty string")

        if str(data["sub_directory_name"]).strip() == "":
            raise ValidationError("sub_directory_name is required or can't be empty string")

        if "number_of_images" in data and (
            data["number_of_images"] is None
            or isinstance(data["number_of_images"], int) is False
            or data["number_of_images"] < 0
        ):
            raise ValidationError(
                "number_of_images is required or number_of_images must be integer or"
                " can't be negative"
            )

        if "skip" in data and (
            data["skip"] is None or isinstance(data["skip"], int) is False or data["skip"] < 0
        ):
            raise ValidationError("skip is required or skip must be integer or can't be negative")

        if "order_by" in data and (data["order_by"] is None or str(data["order_by"]).strip() == ""):
            raise ValidationError("order_by is required or can't be empty string")


class GetImageData(ConsoleAccessBaseClass):
    """This class implements API to get image data.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class GetImageData

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

    def _validate_params(self, params):
        """Validates parameters passed to get_image_data API

        Args:
            params (dict): Dictionary of params with optional default values.

        Returns:
            dict: Updated dictionary of params with optional default values.
        """
        if "self" in params:
            del params["self"]

        # set default values, if not passed.
        if "number_of_images" in params and params["number_of_images"] is None:
            params["number_of_images"] = 50

        if "skip" in params and params["skip"] is None:
            params["skip"] = 0

        if "order_by" in params and params["order_by"] is None:
            params["order_by"] = "ASC"
        return params

    def get_image_data(
        self,
        device_id: str,
        sub_directory_name: str,
        number_of_images: int = None,
        skip: int = None,
        order_by: str = None,
    ):
        """Get a (saved) image of the specified device.

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
                device_id = "__device_id__"
                sub_directory_name = "__sub_directory_name__"
                number_of_images = __number_of_images__
                skip = __skip__
                order_by = "__get_image_data_order_by__"

                # Insight - GetImageData
                response = insight_obj.get_image_data(device_id,
                                                      sub_directory_name,
                                                      number_of_images,
                                                      skip,
                                                      order_by)
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()

            # Validate API parameters
            _local_params = self._validate_params(_local_params)

            # Validate schema
            _local_params = SchemaGetImageData().load(_local_params)

            try:
                # Get the Available Images Count for the specified Device
                _get_images_obj = GetImages(self._config)

                capacity = 256
                number_of_images = 0
                requested = _local_params["number_of_images"]
                _skip = _local_params["skip"]
                get_image_data_response = {"total_image_count": 0, "images": []}
                iteration = math.ceil(requested / capacity)

                for _ in range(1, iteration + 1):
                    if requested < capacity:
                        number_of_images = requested
                    else:
                        number_of_images = capacity

                    response = _get_images_obj.get_images(
                        device_id=device_id,
                        sub_directory_name=sub_directory_name,
                        number_of_images=number_of_images,
                        skip=_skip,
                        order_by=order_by,
                    )
                    if response["total_image_count"] > 0:
                        if get_image_data_response["total_image_count"] == 0:
                            get_image_data_response["total_image_count"] = response[
                                "total_image_count"
                            ]
                        for data in response["images"]:
                            get_image_data_response["images"].append(data)
                    else:
                        # If total_image_count is 0, not need next loop.
                        break
                    requested -= number_of_images
                    _skip += number_of_images
                    if _skip > response["total_image_count"]:
                        # If _skip over total_image_count, not need next loop.
                        break
                return get_image_data_response

            except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                _return_get_image_data = self.on_key_error_response(__name__, key_err)

            except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                _return_get_image_data = self.on_type_error_response(__name__, type_err)

            except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                _return_get_image_data = self.on_value_error_response(__name__, val_err)

            except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                _return_get_image_data = self.on_attribute_error_response(__name__, attr_err)

            except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                _return_get_image_data = self.on_http_error_response(__name__, exception)

            except Exception as exception:
                _return_get_image_data = self.on_generic_error_response(__name__, exception)

        except ValidationError as err:
            _return_get_image_data = self.on_validation_error_response(__name__, err)

        return _return_get_image_data
