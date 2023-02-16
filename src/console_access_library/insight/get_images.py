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
# pylint:disable=anomalous-backslash-in-string

import logging
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import insight_api
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass

logger = logging.getLogger(__name__)


class SchemaGetImages(Schema):
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


class GetImages(ConsoleAccessBaseClass):
    """This class implements API to get images.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class GetImages

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

    def get_images(
        self,
        device_id: str,
        sub_directory_name: str,
        number_of_images: int = 50,
        skip: int = 0,
        order_by: str = "ASC",
    ):
        """Get a (saved) image of the specified device.

        Args:
            device_id (str, required) : Device ID. Case-sensitive
            sub_directory_name (str, required) : Image storage subdirectory. \
                The subdirectory is the directory notified by the response of \
                start_upload_inference_result or the directory obtained by \
                get_image_directories.
            number_of_images (int, optional) : Number of images acquired. \
                0-256. If not specified: 50.
            skip (int, optional) : Number of images to skip fetching. \
                If not specified: 0.
            order_by (str, optional) : Sort Order: Sort order by date and time the \
                image was created. DESC, ASC, desc, asc.
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
                device_id =  "__device_id__"
                sub_directory_name =  "__sub_directory_name__"
                number_of_images =  "__number_of_images__"
                skip =  "__skip__"
                order_by =  "__get_images_order_by__"

                # Insight - GetImages
                response = insight_obj.get_images(device_id,
                                                  sub_directory_name,
                                                  number_of_images,
                                                  skip,
                                                  order_by)
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()
            # delete local argument 'self' form locals() for validation.
            if "self" in _local_params:
                del _local_params["self"]

            if "number_of_images" in _local_params and _local_params["number_of_images"] is None:
                _local_params["number_of_images"] = 50

            if "skip" in _local_params and _local_params["skip"] is None:
                _local_params["skip"] = 0

            if "order_by" in _local_params and _local_params["order_by"] is None:
                _local_params["order_by"] = "ASC"

            # Validate schema
            _local_params = SchemaGetImages().load(_local_params)

            _path_params = {
                "device_id": _local_params["device_id"],
                "sub_directory_name": _local_params["sub_directory_name"],
            }
            _query_params = {
                "order_by": _local_params["order_by"],
                "number_of_images": _local_params["number_of_images"],
                "skip": _local_params["skip"],
            }

            # Enter a context with an instance of the API client
            with aitrios_console_rest_client_sdk_primitive.ApiClient(
                self._config.configuration,
                header_name="Authorization",
                header_value=self._config.get_access_token(),
            ) as api_client:
                # Create an instance of the API class
                insight_api_instance = insight_api.InsightApi(api_client)

                try:
                    _return_get_images = insight_api_instance.get_images(
                        path_params=_path_params, query_params=_query_params
                    )
                    return _return_get_images.body

                except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                    _return_get_images = self.on_key_error_response(__name__, key_err)

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_get_images = self.on_type_error_response(__name__, type_err)

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_get_images = self.on_value_error_response(__name__, val_err)

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_get_images = self.on_attribute_error_response(__name__, attr_err)

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_get_images = self.on_http_error_response(__name__, exception)

                except Exception as exception:
                    _return_get_images = self.on_generic_error_response(__name__, exception)

        except ValidationError as err:
            _return_get_images = self.on_validation_error_response(__name__, err)

        return _return_get_images
