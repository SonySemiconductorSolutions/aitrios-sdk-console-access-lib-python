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
# pylint:disable=too-many-return-statements
# pylint:disable=protected-access
# pylint:disable=too-many-arguments
# pylint:disable=too-many-locals
# pylint:disable=too-many-branches
# pylint:disable=broad-except

import logging
import re
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import device_app_api
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass

logger = logging.getLogger(__name__)


class SchemaImportDeviceApp(Schema):
    """Schema for API ImportDeviceApp.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : compile flags.
    #:                  0: Specified App is not compiled
    #:                  1: Specified App is compiled
    compiled_flg = fields.String(
        required=True, error_messages={"invalid": "Invalid string for compiled_flg"}, strict=True
    )

    #: str, required :  App name. Allow only the following characters.
    #:
    #:                  - Alphanumeric characters
    #:                  - Under bar
    #:                  - Dot
    #:
    #:                  The maximum number of characters is app_name + version_number <=31.
    app_name = fields.String(
        required=True, error_messages={"invalid": "Invalid string for app_name"}, strict=True
    )

    #: str, required : App version number. Allow only the following characters.
    #:
    #:                  - Alphanumeric characters
    #:                  - Under bar
    #:                  - Dot
    #:
    #:                  The maximum number of characters is app_name + version_number <=31.
    version_number = fields.String(
        required=True, error_messages={"invalid": "Invalid string for version_number"}, strict=True
    )

    #: str, optional : Comment. Max. 100 characters.
    comment = fields.String(
        required=False, error_messages={"invalid": "Invalid string for comment"}, strict=True
    )

    #: str, required : filename.
    file_name = fields.String(
        required=True, error_messages={"invalid": "Invalid string for file_name"}, strict=True
    )

    #: str, required : App file content in base64 encoding.
    file_content = fields.String(
        required=True, error_messages={"invalid": "Invalid string for file_content"}
    )

    #: str, optional : App entry point.
    entry_point = fields.String(
        required=False, error_messages={"invalid": "Invalid string for entry_point"}, strict=True
    )

    #: dict, optional : Schema Info.
    schema_info = fields.Dict(
        required=False, error_messages={"invalid": "Invalid string for schema_info"}, strict=True
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if "compiled_flg" in data and (
            data["compiled_flg"] is None or str(data["compiled_flg"]).strip() == ""
        ):
            raise ValidationError("compiled_flg is required or can't be empty string")

        if "entry_point" in data and (
            data["entry_point"] is None or str(data["entry_point"]).strip() == ""
        ):
            raise ValidationError("entry_point is required or can't be empty string")

        if "app_name" in data and (data["app_name"] is None or str(data["app_name"]).strip() == ""):
            raise ValidationError("app_name is required or can't be empty string")

        if "version_number" in data and (
            data["version_number"] is None or str(data["version_number"]).strip() == ""
        ):
            raise ValidationError("version_number is required or can't be empty string")

        if "comment" in data and (data["comment"] is None or str(data["comment"]).strip() == ""):
            raise ValidationError("comment is required or can't be empty string")

        if "file_name" in data and (
            data["file_name"] is None or str(data["file_name"]).strip() == ""
        ):
            raise ValidationError("file_name is required or can't be empty string")

        if "file_content" in data and (
            data["file_content"] is None or str(data["file_content"]).strip() == ""
        ):
            raise ValidationError("file_content is required or can't be empty string")

        if "entry_point" in data and (
            data["entry_point"] is None or str(data["entry_point"]).strip() == ""
        ):
            raise ValidationError("entry_point is required or can't be empty string")

        if "schema_info" in data and (
            data["schema_info"] is None or not data["schema_info"]
        ):
            raise ValidationError("schema_info is required or can't be empty dict")


class ImportDeviceApp(ConsoleAccessBaseClass):
    """This class implements API to sign and import device apps.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class ImportDeviceApp

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

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

                # Create Instance for Deployment
                deployment_obj = client_obj.get_deployment()

                # set the real value
                compiled_flg =  "__compiled_flg__"
                app_name =  "__app_name__"
                version_number =  "__version_number__"
                file_name =  "__file_name__"
                file_content =  "__file_content__"
                entry_point =  "__entry_point__"
                comment =  "__comment__"
                schema_info = "__schema_info__"

                # Deployment - ImportDeviceApp
                response = deployment_obj.import_device_app(
                    compiled_flg,
                    app_name,
                    version_number,
                    file_name,
                    file_content,
                    entry_point,
                    comment,
                    schema_info
                )
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()
            _query_params = {}
            # delete local argument 'self' form locals() for validation.
            if "self" in _local_params:
                del _local_params["self"]

            # set default values, if not passed.
            if "entry_point" in _local_params and _local_params["entry_point"] is None:
                del _local_params["entry_point"]

            if "comment" in _local_params and _local_params["comment"] is None:
                del _local_params["comment"]

            if "schema_info" in _local_params and _local_params["schema_info"] is None:
                del _local_params["schema_info"]

            # Validate schema
            _body_params = SchemaImportDeviceApp().load(_local_params)

            # app_name, version_number
            # Characters other than the following are forbidden characters
            # ・Alphanumeric・Underbar ·Dot
            if _body_params["app_name"] is not None:
                if bool(re.match("^[A-Za-z0-9_.]*$", _body_params["app_name"])) is False:
                    raise ValidationError("app_name has forbidden characters")

            if _body_params["version_number"] is not None:
                if bool(re.match("^[A-Za-z0-9_.]*$", _body_params["version_number"])) is False:
                    raise ValidationError("version_number has forbidden characters")

            # Enter a context with an instance of the API client
            with aitrios_console_rest_client_sdk_primitive.ApiClient(
                self._config.configuration,
                header_name="Authorization",
                header_value=self._config.get_access_token(),
            ) as api_client:
                # Create an instance of the API class
                manage_devices_api_instance = device_app_api.DeviceAppApi(api_client)
                try:
                    # Adding Parameters to Connect to Console Enterprise Edition Environment
                    if self._config._application_id:
                        _query_params["grant_type"] = "client_credentials"
                        _return_import_device_app = manage_devices_api_instance.import_device_app(
                            body=_body_params, query_params=_query_params
                        )
                    else:
                        _return_import_device_app = manage_devices_api_instance.import_device_app(
                            body=_body_params
                        )
                    return _return_import_device_app.body

                except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                    _return_import_device_app = self.on_key_error_response(__name__, key_err)

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_import_device_app = self.on_type_error_response(__name__, type_err)

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_import_device_app = self.on_value_error_response(__name__, val_err)

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_import_device_app = self.on_attribute_error_response(__name__, attr_err)

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_import_device_app = self.on_http_error_response(__name__, exception)

                except Exception as exception:
                    _return_import_device_app = self.on_generic_error_response(__name__, exception)

        except ValidationError as err:
            _return_import_device_app = self.on_validation_error_response(__name__, err)

        return _return_import_device_app
