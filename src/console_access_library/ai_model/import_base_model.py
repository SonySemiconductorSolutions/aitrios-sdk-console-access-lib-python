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

    #: str, required : Model ID for new registration or version upgrade. Max.
    #:            100 characters.
    model_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for model_id"}, strict=True
    )

    #: str, required : SAS URI or Presigned URI of the model file.
    model = fields.String(
        required=True, error_messages={"invalid": "Invalid string for model"}, strict=True
    )

    #: bool, optional : Specify whether to convert the specified model file.
    converted = fields.Boolean(
        required=False, error_messages={"invalid": "Invalid boolean for converted"}, strict=True
    )

    #: str, optional : Vendor Name. Max. 100 characters.
    #:
    #:                  - Specify only when registering a new base model.
    vendor_name = fields.String(
        required=False, error_messages={"invalid": "Invalid string for vendor_name"}, strict=True
    )

    #: str, optional : Description. Max. 100 characters.
    #:
    #:                  - When saving new, it is set as a description of the model and version.
    #:                  - When saving version-up, it is set as a description of the version.
    comment = fields.String(
        required=False, error_messages={"invalid": "Invalid string for comment"}, strict=True
    )

    #: str, optional : SAS URI or Presigned URI of the input format param file.
    #:
    #:                    - Usage: Packager conversion information (image format information).
    #:                    - The json format is an array of objects. Each object contains the
    #:                      following values.
    #:
    #:                        - ordinal: Order of DNN input to converter (value range: 0 to 2)
    #:                        - format: Format ("RGB" or "BGR")
    input_format_param = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for input_format_param"},
        strict=True,
    )

    #: str, optional : SAS URI or Presigned URI of the network config file.
    #:
    #:                  - Usage: Conversion parameter information of modelconverter.
    #:
    #:                  Therefore, it is not necessary to specify when specifying the
    #:                  model before conversion.
    network_config = fields.String(
        required=False, error_messages={"invalid": "Invalid string for network_config"}, strict=True
    )

    #: str, optional : Specify whether or not application is required for the model.
    #:
    #:                  - Value definition
    #:
    #:                     - 0 : Model required application
    #:                     - 1 : Model do not required application
    network_type = fields.String(
        required=False, error_messages={"invalid": "Invalid string for network_type"}, strict=True
    )

    #: metadata_format_id, optional : metadata_format_id. Max. 100 characters.
    metadata_format_id = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for metadata_format_id"},
        strict=True
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

        if "metadata_format_id" in data and (
            data["metadata_format_id"] is None or str(data["metadata_format_id"]).strip() == ""
        ):
            raise ValidationError("metadata_format_id is required or can't be empty string")


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
        metadata_format_id: str = None,
    ):
        """Import the base model. In addition, in the case of a new model \
        ID, it is newly saved. If you specify a model ID that has already been registered \
        in the system, the version will be upgraded.

        Args:
            model_id (str, required) : Model ID for new registration or version upgrade. \
                Max. 100 characters. \
                The following characters are allowed \
                Alphanumeric characters \
                - hyphen \
                _ Underscore \
                () Small parentheses \
                . dot
            model (str, required) : SAS URI or Presigned URI of the model file.
            converted (bool, optional) : Specify whether to convert the specified model file.
            vendor_name (str, optional) : Vendor Name. Max. 100 characters.

                - Specify only when registering a new base model.
            comment (str, optional) : Description. Max. 100 characters.

                - When saving new, it is set as a description of the model and version.
                - When saving version-up, it is set as a description of the version.
            input_format_param (str, optional) : SAS URI or Presigned URI of the input format \
              param file.

                 - Usage: Packager conversion information (image format information).
                 - The json format is an array of objects. Each object contains the following \
                 values.

                     - ordinal: Order of DNN input to converter (value range: 0 to 2)
                     - format: Format ("RGB" or "BGR") \
                       Example: [{ "ordinal": 0, "format": "RGB" }, { "ordinal": 1, "format": "RGB" }]
            network_config (str, optional) : SAS URI or Presigned URI of the network config file.

                - Usage: Conversion parameter information of modelconverter.

                Therefore, it is not necessary to specify when specifying the model before \
                  conversion. \
                  Example: { "Postprocessor": { "params": { "background": false, "scale_factors": \
                    [ 10.0, 10.0, 5.0, 5.0 ], "score_thresh": 0.01, "max_size_per_class": 64, \
                    "max_total_size": 64, "clip_window": [ 0, 0, 1, 1 ], "iou_threshold": 0.45 } } }
            network_type (str, optional) : Specify whether or not application is required \
            for the model.

                - Value definition

                    - 0 : Model required application
                    - 1 : Model do not required application
            metadata_format_id (str, optional) : Metadata Format ID
                Max. 100 characters.

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
                metadata_format_id =  "__metadata_format_id__"

                # AIModels - ImportBaseModel
                response = ai_model_obj.import_base_model(model_id,
                                                          model,
                                                          converted,
                                                          vendor_name,
                                                          comment,
                                                          input_format_param,
                                                          network_config,
                                                          network_type,
                                                          metadata_format_id)
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

            if (
                "metadata_format_id" in _local_params
                and _local_params["metadata_format_id"] is None
            ):
                del _local_params["metadata_format_id"]

            # Checking the datatype of input parameter "converted" before schema validation
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
                    # Adding Parameters to Connect to Console Enterprise Edition Environment
                    if self._config._application_id:
                        _query_params["grant_type"] = "client_credentials"
                        _return_import_base_model = manage_devices_api_instance.import_base_model(
                            body=_body_params, query_params=_query_params
                        )
                    else:
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
