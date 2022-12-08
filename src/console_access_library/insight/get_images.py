"""
Copyright 2022 Sony Semiconductor Solutions Corp. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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


import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import insight_api
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.logger import Logger
from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass


class SchemaGetImages(Schema):
    """Schema for API to get a (saved) image of the specified device.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : Device ID.
    device_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for device_id"}
    )

    #: str, required : Sub Directory Name.
    sub_directory_name = fields.String(
        required=True, error_messages={"invalid": "Invalid string for sub_directory_name"}
    )

    #: int, optional : Number Of Images.
    number_of_images = fields.Integer(
        required=False, error_messages={"invalid": "Invalid integer for number_of_images"}
    )

    #: int, optional : Skip.
    skip = fields.Integer(required=False, error_messages={"invalid": "Invalid integer for skip"})

    #: str, optional : Order By.
    order_by = fields.String(
        required=False, error_messages={"invalid": "Invalid string for order_by"}
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if data["device_id"] == "":
            raise ValidationError("device_id is required")

        if data["sub_directory_name"] == "":
            raise ValidationError("sub_directory_name is required")

        if "number_of_images" in data and data["number_of_images"] is None:
            raise ValidationError("number_of_images is required")

        if "skip" in data and data["skip"] is None:
            raise ValidationError("skip is required")

        if "order_by" in data and data["order_by"] == "":
            raise ValidationError("order_by is required")


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
        self.logger = Logger().set_logger()

    def get_images(
        self,
        device_id: str,
        sub_directory_name: str,
        number_of_images: int = None,
        skip: int = None,
        order_by: str = None,
    ):
        """Get a (saved) image of the specified device.

        Args:
            device_id (str, required) : The Device ID.
            sub_directory_name (str, required) : The Sub Directory Name.
                The subdirectory will be the directory notified in the response
                of start_upload_inference_result.

            number_of_images (int, optional) : The Number Of Images. 0-256. If not specified: 50
            skip (int, optional) : The Skip. If not specified: 0
            order_by (str, optional) : The Order By. DESC, ASC, desc, asc. If not specified:ASC

        Returns:
            dict:
                - **Success Response** : Dictionary with below key and value pairs.

                    - ``total_image_count`` (int) : Total number of images
                    - ``images`` (object) : Image filename and image file data
                            (base64 encoded data)

                - **Generic Error Response** :

                    If the http_status returned from the Low Level SDK
                    API is other than 200. Dictionary with below key and value pairs.

                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``error_code`` (str) : "Generic Error"

                - **Validation Error Response** :

                    If incorrect API input parameters. Dictionary with below key and value pairs.

                    - ``message`` (str) : validation error message for respective input parameter
                    - ``error_code`` (str) : "E001"

                - **Key Error Response** :

                    If API key error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``error_code`` (str) : "Key Error"

                - **Type Error Response** :

                    If API type error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``error_code`` (str) : "Type Error"

                - **Attribute Error Response** :

                    If API attribute error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``error_code`` (str) : "Attribute Error"

                - **Value Error Response** :

                    If API value error returned from the Low Level SDK API.
                    Dictionary with below key and value pairs.

                    - ``message`` (str) : error message returned from the Low Level SDK API
                    - ``error_code`` (str) : "Value Error"

        Example:
            .. code-block:: python

                import os
                import sys

                from pprint import pprint
                from console_access_library.client import Client

                # For Console Access Library API Usage,
                # edit console access setting configuration parameters with real values.
                # file_path: samples/console_access_settings.yaml
                # console_access_settings:
                # 	base_url: "__base_url__"
                # 	token_url: "__token_url__"
                # 	client_secret: '__client_secret__'
                # 	client_id: '__client_id__'

                # Set path for Console Access Library Setting File.
                SETTING_FILE_PATH = os.path.join(os.getcwd(), "samples","console_access_settings.yaml")

                # Instantiate Console Access Library Client.
                console_sdk_client_obj = Client(SETTING_FILE_PATH)

                # set the real value
                device_id =  "__device_id__"
                sub_directory_name =  "__sub_directory_name__"
                number_of_images =  "__number_of_images__"
                skip =  "__skip__"
                order_by =  "__get_images_order_by__"

                # Insight - GetImages
                response = console_sdk_client_obj.insight.get_images(device_id,
                                                                 sub_directory_name,
                                                                 number_of_images,
                                                                 skip,
                                                                 order_by)
                pprint(response)
        """

        self.logger.info(sys._getframe().f_code.co_name)

        try:
            # delete local argument 'self' form locals() for validation.
            _local_params = locals()
            if "self" in _local_params:
                del _local_params["self"]

            # set default values, if not passed.
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
                    return _return_get_images

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_get_images = self.on_type_error_response(__name__, type_err)
                    return _return_get_images

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_get_images = self.on_value_error_response(__name__, val_err)
                    return _return_get_images

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_get_images = self.on_attribute_error_response(__name__, attr_err)
                    return _return_get_images

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_get_images = self.on_generic_error_response(__name__, exception)
                    return _return_get_images

        except ValidationError as err:
            _return_get_images = self.on_validation_error_response(__name__, err)
            return _return_get_images
