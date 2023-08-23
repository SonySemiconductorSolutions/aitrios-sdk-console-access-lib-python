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
# pylint:disable=too-many-return-statements
# pylint:disable=protected-access
# pylint:disable=too-many-arguments
# pylint:disable=too-many-statements
# pylint:disable=too-many-locals
# pylint:disable=too-many-branches
# pylint:disable=broad-except

import logging
import re
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import train_model_api
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass

logger = logging.getLogger(__name__)


class SchemaImportBaseModel(Schema):
    """Schema for API ImportBaseModel.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : Model ID.
    model_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for model_id"}, strict=True
    )

    #: str, required : Model.
    model = fields.String(
        required=True, error_messages={"invalid": "Invalid string for model"}, strict=True
    )

    #: bool, optional : Convert flag.
    converted = fields.Boolean(
        required=False, error_messages={"invalid": "Invalid boolean for converted"}, strict=True
    )

    #: str, optional : Vendor Name.
    vendor_name = fields.String(
        required=False, error_messages={"invalid": "Invalid string for vendor_name"}, strict=True
    )

    #: str, optional : Comment.
    comment = fields.String(
        required=False, error_messages={"invalid": "Invalid string for comment"}, strict=True
    )

    #: str, optional : Input format param file.
    input_format_param = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for input_format_param"},
        strict=True,
    )

    #: str, optional : network_config.
    network_config = fields.String(
        required=False, error_messages={"invalid": "Invalid string for network_config"}, strict=True
    )

    #: str, optional : network_type.
    network_type = fields.String(
        required=False, error_messages={"invalid": "Invalid string for network_type"}, strict=True
    )

    #: list, optional : labels.
    labels = fields.List(
        fields.String(),
        required=False,
        error_messages={"invalid": "Invalid list for labels"},
        strict=True,
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if str(data["model_id"]).strip() == "":
            raise ValidationError("model_id is required or can't be empty string")

        if str(data["model"]).strip() == "":
            raise ValidationError("model is required or can't be empty string")

        if "converted" in data and data["converted"] is None:
            raise ValidationError("converted is required")

        if "vendor_name" in data and (
            data["vendor_name"] is None or str(data["vendor_name"]).strip() == ""
        ):
            raise ValidationError("vendor_name is required or can't be empty string")

        if "comment" in data and (data["comment"] is None or str(data["comment"]).strip() == ""):
            raise ValidationError("comment is required or can't be empty string")

        if "network_config" in data and (
            data["network_config"] is None or str(data["network_config"]).strip() == ""
        ):
            raise ValidationError("network_config is required or can't be empty string")

        if "network_type" in data and (
            data["network_type"] is None or str(data["network_type"]).strip() == ""
        ):
            raise ValidationError("network_type is required or can't be empty string")

        if "labels" in data and data["labels"] is None:
            raise ValidationError("labels is required")


class ImportBaseModel(ConsoleAccessBaseClass):
    """This class implements API to import base model.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class ImportBaseModel

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

    def import_base_model(
        self,
        model_id: str,
        model: str,
        converted: bool = None,
        vendor_name: str = None,
        comment: str = None,
        input_format_param: str = None,
        network_config: str = None,
        network_type: str = "1",
        labels: list = None,
    ):
        """Import the base model. For a new model ID, save it as a new one. \
        If a model ID already registered in the system is specified, the version is upgraded. \
        Note that it is not possible to create a device model based on the base model \
        imported with this API.

        Args:
            model_id (str, required) : Model ID. \
                The model ID to be saved or upgraded. 100 characters or less \
                The following characters are allowed \
                Alphanumeric characters \
                -hyphen \
                _ Underscore \
                () Small parentheses \
                . dot
            model (str, required) : Model file SAS URI
            converted (bool, optional) : Convert flag. True: Converted Model \
                False: Unconverted Model \
                False if not specified
            vendor_name (str, optional) : Vendor Name.  (specified when saving as new) \
                Up to 100 characters. Not specified for version upgrade. \
                No vendor name if not specified.
            comment (str, optional) : Explanation about the model to be entered when \
                registering a new model. When newly saved, it is set as \
                a description of the model and version. \
                When the version is upgraded, it is set as the \
                description of the version. Within 100 characters If not specified, there is no \
                explanation about the model to be entered when registering a new model.
            input_format_param (str, optional) : input format param file (json format) URI \
                Evaluate Azure: SAS URI+ AWS: Presigned URIs Usage: Packager conversion \
                information (image format information). Illegal characters except for SAS URI \
                format json format is an array of objects (each object contains the following \
                values). Example ordinal: Order of DNN input to converter (value range: 0-2) \
                format: format ("RGB" or "BGR") If not specified, do not evaluate.
            network_config (str, optional) : URI of network config file (json format) \
                Evaluate Azure: SAS URI+ AWS: Presigned URIs In case of pre-conversion \
                model, specify. (=Ignored for post-conversion model) Usage: Conversion parameter \
                information of model converter. Illegal characters except for SAS URI format \
                If not specified, do not evaluate.
            network_type (str, optional) : The Network Type. (Valid only for \
                new model registration).

                - 0: Custom Vision
                - 1: Non Custom Vision

                1 if not specified.
            labels (list, optional) : Label Name. Example: ["label01","label02","label03"]

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+------------+-------------------------------+
                | *Level1*   | *Type*     | *Description*                 |
                +------------+------------+-------------------------------+
                | ``result`` | ``string`` | Set "SUCCESS" pinning         |
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

                # Create Instance for AIModel
                ai_model_obj = client_obj.get_ai_model()

                # set the real value
                model_id =  "__model_id__"
                model =  "__model__"
                converted =  "__converted__"
                vendor_name =  "__vendor_name__"
                comment =  "__comment__"
                input_format_param =  "__input_format_param__"
                network_config =  "__network_config__"
                network_type =  "__network_type__"
                labels =  "__labels__"

                # AIModels - ImportBaseModel
                response = ai_model_obj.import_base_model(model_id,
                                                          model,
                                                          converted,
                                                          vendor_name,
                                                          comment,
                                                          input_format_param,
                                                          network_config,
                                                          network_type,
                                                          labels)
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()
            # delete local argument 'self' form locals() for validation.
            if "self" in _local_params:
                del _local_params["self"]

            # set default values, if not passed.

            if "converted" in _local_params and _local_params["converted"] is None:
                _local_params["converted"] = False

            if "vendor_name" in _local_params and _local_params["vendor_name"] is None:
                del _local_params["vendor_name"]

            if "comment" in _local_params and _local_params["comment"] is None:
                del _local_params["comment"]

            if (
                "input_format_param" in _local_params
                and _local_params["input_format_param"] is None
            ):
                del _local_params["input_format_param"]

            if "network_config" in _local_params and _local_params["network_config"] is None:
                del _local_params["network_config"]

            if "network_type" in _local_params and _local_params["network_type"] is None:
                _local_params["network_type"] = "1"

            if "labels" in _local_params and _local_params["labels"] is None:
                del _local_params["labels"]

            # Checking the datatype of input paramter "labels" before schema validation
            # as Marshmallow is converting tuple to list
            if (
                "labels" in _local_params
                and _local_params["labels"] is not None
                and not isinstance(_local_params["labels"], list)
            ):
                raise ValidationError("Invalid type for labels")

            # Checking the datatype of input paramter "converted" before schema validation
            # as Marshmallow is converting all truthy and falsy value to boolean type
            if (
                "converted" in _local_params
                and _local_params["converted"] is not None
                and not isinstance(_local_params["converted"], bool)
            ):
                raise ValidationError("Invalid type for converted")

            # Validate schema
            _body_params = SchemaImportBaseModel().load(_local_params)

            # model_id
            # Characters other than the following are forbidden characters
            # ・Alphanumeric・Underscore ·Dot ·Hyphen ·Small parentheses
            if _local_params["model_id"] is not None:
                if bool(re.match("^[A-Za-z0-9_()-.]*$", _local_params["model_id"])) is False:
                    raise ValidationError("model_id has forbidden characters")

            # Enter a context with an instance of the API client
            with aitrios_console_rest_client_sdk_primitive.ApiClient(
                self._config.configuration,
                header_name="Authorization",
                header_value=self._config.get_access_token(),
            ) as api_client:
                # Create an instance of the API class
                manage_devices_api_instance = train_model_api.TrainModelApi(api_client)
                try:
                    _return_import_base_model = manage_devices_api_instance.import_base_model(
                        body=_body_params
                    )
                    return _return_import_base_model.body

                except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                    _return_import_base_model = self.on_key_error_response(__name__, key_err)

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_import_base_model = self.on_type_error_response(__name__, type_err)

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_import_base_model = self.on_value_error_response(__name__, val_err)

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_import_base_model = self.on_attribute_error_response(__name__, attr_err)

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_import_base_model = self.on_http_error_response(__name__, exception)

                except Exception as exception:
                    _return_import_base_model = self.on_generic_error_response(__name__, exception)

        except ValidationError as err:
            _return_import_base_model = self.on_validation_error_response(__name__, err)

        return _return_import_base_model
