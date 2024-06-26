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
# pylint:disable=wrong-import-position
# pylint:disable=duplicate-code
# pylint:disable=unused-argument
# pylint:disable=redefined-builtin
# pylint:disable=too-many-arguments
# pylint:disable=too-many-locals
# pylint:disable=too-many-branches
# pylint:disable=too-many-return-statements
# pylint:disable=protected-access
# pylint:disable=broad-except

import logging
import sys
import warnings
from datetime import datetime

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import insight_api
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass

logger = logging.getLogger(__name__)


class SchemaExportImages(Schema):
    """Schema for API to export images.
    Args:
        Schema (object): Inherited from Schema class of marshmallow
    """

    #: str, required : Public key.
    #:                 Base64-encoded format of the entire pem file contents of the public key
    key = fields.String(
        required=True, error_messages={"invalid": "Invalid string for key"}, strict=True
    )

    #: str, optional : Date and time (From).
    #:                 Form: yyyyMMddhhmm. Default:""
    from_datetime = fields.String(
        required=False, error_messages={"invalid": "Invalid string for from_datetime"}, strict=True
    )

    #: str, optional : Date and time (To).
    #:                 Form: yyyyMMddhhmm. Default:""
    to_datetime = fields.String(
        required=False, error_messages={"invalid": "Invalid string for to_datetime"}, strict=True
    )

    #: str, optional : Device ID.
    device_id = fields.String(
        required=False, error_messages={"invalid": "Invalid string for device_id"}, strict=True
    )

    #: str, optional : Image file format. If this is not specified, there is no filtering.
    #:                 Default:""
    #:
    #:                 - Value definition
    #:
    #:                  - JPG
    #:                  - BMP
    file_format = fields.String(
        required=False, error_messages={"invalid": "Invalid string for file_format"}, strict=True
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if str(data["key"]).strip() == "":
            raise ValidationError("key is required or can't be empty string")

        date_format = "%Y%m%d%H%M"
        if (
            "from_datetime" in data
            and data["from_datetime"] is not None
            and str(data["from_datetime"]).strip() != ""
        ):
            try:
                datetime.strptime(data["from_datetime"], date_format)
            except Exception as ex:
                logger.error(str(ex))
                raise ValidationError("Invalid time format") from ex
        elif "from_datetime" in data and (
            data["from_datetime"] is None or str(data["from_datetime"]).strip() == ""
        ):
            raise ValidationError("from_datetime is required or can't be empty string")

        if (
            "to_datetime" in data
            and data["to_datetime"] is not None
            and str(data["to_datetime"]).strip() != ""
        ):
            try:
                datetime.strptime(data["to_datetime"], date_format)
            except Exception as ex:
                logger.error(str(ex))
                raise ValidationError("Invalid time format") from ex
        elif "to_datetime" in data and (
            data["to_datetime"] is None or str(data["to_datetime"]).strip() == ""
        ):
            raise ValidationError("to_datetime is required or can't be empty string")

        if "device_id" in data and (
            data["device_id"] is None or str(data["device_id"]).strip() == ""
        ):
            raise ValidationError("device_id is required or can't be empty string")

        if "file_format" in data and (
            data["file_format"] is None or str(data["file_format"]).strip() == ""
        ):
            raise ValidationError("file_format is required or can't be empty string")


class ExportImages(ConsoleAccessBaseClass):
    """This class implements API to export images.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class ExportImages

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

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
                #     application_id: "__application_id__"

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
                    read_console_access_settings_obj.client_secret,
                    read_console_access_settings_obj.application_id
                )

                # Instantiate Console Access Library Client.
                client_obj = Client(config_obj)

                # Create Instance for Insight
                insight_obj = client_obj.get_insight()

                # set the real value
                key =  "__key__"
                from_datetime =  "__from_datetime__"
                to_datetime =  "__to_datetime__"
                device_id =  "__device_id__"
                file_format =  "__file_format__"

                # Insight - ExportImages
                response = insight_obj.export_images(
                    key,
                    from_datetime,
                    to_datetime,
                    device_id,
                    file_format
                )
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()
            # delete local argument 'self' form locals() for validation.
            if "self" in _local_params:
                del _local_params["self"]

            # set default values, if not passed.
            if "from_datetime" in _local_params and _local_params["from_datetime"] is None:
                del _local_params["from_datetime"]

            if "to_datetime" in _local_params and _local_params["to_datetime"] is None:
                del _local_params["to_datetime"]

            if "device_id" in _local_params and _local_params["device_id"] is None:
                del _local_params["device_id"]

            if "file_format" in _local_params and _local_params["file_format"] is None:
                del _local_params["file_format"]

            # Validate schema
            _query_params = SchemaExportImages().load(_local_params)

            # Enter a context with an instance of the API client
            with aitrios_console_rest_client_sdk_primitive.ApiClient(
                self._config.configuration,
                header_name="Authorization",
                header_value=self._config.get_access_token(),
            ) as api_client:

                # Adding Parameters to Connect to Console Enterprise Edition Environment
                if self._config._application_id:
                    _query_params["grant_type"] = "client_credentials"

                # Create an instance of the API class
                insight_api_instance = insight_api.InsightApi(api_client)

                try:
                    _return_export_images = insight_api_instance.export_images(
                        query_params=_query_params
                    )
                    return _return_export_images.body

                except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                    _return_export_images = self.on_key_error_response(__name__, key_err)

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_export_images = self.on_type_error_response(__name__, type_err)

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_export_images = self.on_value_error_response(__name__, val_err)

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_export_images = self.on_attribute_error_response(__name__, attr_err)

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_export_images = self.on_http_error_response(__name__, exception)

                except Exception as exception:
                    _return_export_images = self.on_generic_error_response(__name__, exception)

        except ValidationError as err:
            _return_export_images = self.on_validation_error_response(__name__, err)

        return _return_export_images
