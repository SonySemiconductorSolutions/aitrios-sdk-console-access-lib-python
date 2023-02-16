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
# pylint:disable=too-many-locals
# pylint:disable=too-many-branches
# pylint:disable=broad-except

import logging
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import train_model_api
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass

logger = logging.getLogger(__name__)


class SchemaGetModels(Schema):
    """Schema for API GetModels.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, optional : Model ID.
    model_id = fields.String(
        required=False, error_messages={"invalid": "Invalid string for model_id"}, strict=True
    )

    #: str, optional : Model Description.
    comment = fields.String(
        required=False, error_messages={"invalid": "Invalid string for comment"}, strict=True
    )

    #: str, optional : Project Name.
    project_name = fields.String(
        required=False, error_messages={"invalid": "Invalid string for project_name"}, strict=True
    )

    #: str, optional : Model Platform.
    model_platform = fields.String(
        required=False, error_messages={"invalid": "Invalid string for model_platform"}, strict=True
    )

    #: str, optional : Project Type.
    project_type = fields.String(
        required=False, error_messages={"invalid": "Invalid string for project_type"}, strict=True
    )

    #: str, optional : Device ID.
    device_id = fields.String(
        required=False, error_messages={"invalid": "Invalid string for device_id"}, strict=True
    )

    #: str, optional : Latest version type.
    latest_type = fields.String(
        required=False, error_messages={"invalid": "Invalid string for latest_type"}, strict=True
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if "model_id" in data and (data["model_id"] is None or str(data["model_id"]).strip() == ""):
            raise ValidationError("model_id is required or can't be empty string")

        if "comment" in data and (data["comment"] is None or str(data["comment"]).strip() == ""):
            raise ValidationError("comment is required or can't be empty string")

        if "project_name" in data and (
            data["project_name"] is None or str(data["project_name"]).strip() == ""
        ):
            raise ValidationError("project_name is required or can't be empty string")

        if "model_platform" in data and (
            data["model_platform"] is None or str(data["model_platform"]).strip() == ""
        ):
            raise ValidationError("model_platform is required or can't be empty string")

        if "project_type" in data and (
            data["project_type"] is None or str(data["project_type"]).strip() == ""
        ):
            raise ValidationError("project_type is required or can't be empty string")

        if "device_id" in data and (
            data["device_id"] is None or str(data["device_id"]).strip() == ""
        ):
            raise ValidationError("device_id is required or can't be empty string")

        if "latest_type" in data and (
            data["latest_type"] is None or str(data["latest_type"]).strip() == ""
        ):
            raise ValidationError("latest_type is required or can't be empty string")


class GetModels(ConsoleAccessBaseClass):
    """This class implements API to get model information list.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class GetModels

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

    def get_models(
        self,
        model_id: str = None,
        comment: str = None,
        project_name: str = None,
        model_platform: str = None,
        project_type: str = None,
        device_id: str = None,
        latest_type: str = "1",
    ):
        """Get model information list

        Args:
            model_id (str, optional) : Model ID. Partial search \
                If not specified, all model_id searches.
            comment (str, optional) : Model Description. Partial search \
                If not specified, search all comments.
            project_name(str, optional) : Project Name. Partial search \
                Search all project_name if not specified.
            model_platform(str, optional) : Model platform

                - 0 : Custom Vision
                - 1 : Non Custom Vision
                - 2 : Model Retrainer

                Exact search, If not specified, search all model_platforms.

            project_type (str, optional) : Project Type.

                - 0 : Base
                - 1 : Device

                Exact search, Search all project_types if not specified.

            device_id (str, optional) : Device Id. \
                Specify when you want to search for device models. \
                Exact match search criteria. Case-sensitive.

            latest_type (str, optional) : Latest version type.

                - 0 : latest published version
                - 1 : Latest version (latest including model version in process of \
                conversion/publishing)

                Exact search, 1 if not specified.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+-------------------+------------+-------------------------------+
                | *Level1*   | *Level2*          | *Type*     | *Description*                 |
                +------------+-------------------+------------+-------------------------------+
                | ``models`` |                   | ``array``  | The subordinate elements are  |
                |            |                   |            | listed in ascending order of  |
                |            |                   |            | model ID                      |
                +------------+-------------------+------------+-------------------------------+
                |            | ``model_id``      | ``string`` | Set the model ID              |
                +------------+-------------------+------------+-------------------------------+
                |            | ``device_type``   | ``string`` | Set the model type            |
                +------------+-------------------+------------+-------------------------------+
                |            | ``functionality`` | ``string`` | Set the feature description   |
                +------------+-------------------+------------+-------------------------------+
                |            | ``vendor_name``   | ``string`` | Set the vendor name           |
                +------------+-------------------+------------+-------------------------------+
                |            | ``model_comment`` | ``string`` | Set the description           |
                +------------+-------------------+------------+-------------------------------+
                |            | ``network_type``  | ``string`` | 0: Custom Vision              |
                |            |                   |            |                               |
                |            |                   |            | 1: Non Custom Vision          |
                +------------+-------------------+------------+-------------------------------+
                |            | ``projects``      | ``array``  | Refer :ref:`projects <p1>`    |
                |            |                   |            | for more details              |
                +------------+-------------------+------------+-------------------------------+

                +------------+--------------------+------------+-----------------------------------+
                | projects   | .. _p1:                                                             |
                +------------+--------------------+------------+-----------------------------------+
                | *Level1*   | *Level2*           | *Type*     | *Description*                     |
                +------------+--------------------+------------+-----------------------------------+
                |``projects``|                    | ``array``  |The subordinate elements are listed|
                |            |                    |            |in ascending order of project type |
                |            |                    |            |and model project name.            |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_project_    | ``string`` |Set the model project name         |
                |            |name``              |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_platform``  |``string``  |Set up the model platform          |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_type``      |``string``  |Set the model type                 |
                +------------+--------------------+------------+-----------------------------------+
                |            |``project_type``    |``string``  |Set the project type               |
                +------------+--------------------+------------+-----------------------------------+
                |            |``device_id``       |``string``  |Set the device ID * This is not an |
                |            |                    |            |internal ID                        |
                +------------+--------------------+------------+-----------------------------------+
                |            |``versions``        |``array``   |Refer :ref:`versions <v1>`         |
                |            |                    |            |for more details                   |
                +------------+--------------------+------------+-----------------------------------+

                +------------+--------------------+------------+-----------------------------------+
                | versions   | .. _v1:                                                             |
                +------------+--------------------+------------+-----------------------------------+
                | *Level1*   | *Level2*           | *Type*     | *Description*                     |
                +------------+--------------------+------------+-----------------------------------+
                |``versions``|                    | ``array``  |Although it is a subordinate       |
                |            |                    |            |element, in the case of this API,  |
                |            |                    |            |there is always one.               |
                +------------+--------------------+------------+-----------------------------------+
                |            |``version_number``  | ``string`` |Set the version number             |
                +------------+--------------------+------------+-----------------------------------+
                |            |``iteration_id``    |``string``  |Set the iteration ID               |
                +------------+--------------------+------------+-----------------------------------+
                |            |``iteration_name``  |``string``  |Set the iteration name             |
                +------------+--------------------+------------+-----------------------------------+
                |            |``accuracy``        |``string``  |Set the precision                  |
                +------------+--------------------+------------+-----------------------------------+
                |            |``latest_flg``      |``string``  |Set the latest flag                |
                +------------+--------------------+------------+-----------------------------------+
                |            |``publish_latest    |``string``  |Set the latest published flag      |
                |            |_flg``              |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``version_status``  |``string``  |Set your status                    |
                |            |                    |            |                                   |
                |            |                    |            |'01': 'Before conversion'          |
                |            |                    |            |                                   |
                |            |                    |            |'02': 'Converting'                 |
                |            |                    |            |                                   |
                |            |                    |            |'03': 'Conversion failed'          |
                |            |                    |            |                                   |
                |            |                    |            |'04': 'Conversion complete'        |
                |            |                    |            |                                   |
                |            |                    |            |'05': 'Adding to configuration'    |
                |            |                    |            |                                   |
                |            |                    |            |'06': 'Add to configuration failed'|
                |            |                    |            |                                   |
                |            |                    |            |'07': Add to configuration         |
                |            |                    |            |complete                           |
                |            |                    |            |                                   |
                |            |                    |            |'11': 'Saving' Model saving        |
                |            |                    |            |status in Model Retrainer case     |
                +------------+--------------------+------------+-----------------------------------+
                |            |``org_file_name``   |``string``  |Set the file name of the model     |
                |            |                    |            |before conversion                  |
                +------------+--------------------+------------+-----------------------------------+
                |            |``org_file_size``   |``integer`` |Set the publishing model file size |
                +------------+--------------------+------------+-----------------------------------+
                |            |``publish_file_     |``string``  |Set the publishing model file name |
                |            |name``              |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``publish_file_     |``integer`` |Set the publishing model file size |
                |            |size``              |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_file_size`` |``integer`` |Set the model file size            |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_framework`` |``string``  |Set up the model framework         |
                +------------+--------------------+------------+-----------------------------------+
                |            |``conv_id``         |``string``  |Set the conversion request ID      |
                +------------+--------------------+------------+-----------------------------------+
                |            |``labels``          |``string[]``|Set the label array                |
                +------------+--------------------+------------+-----------------------------------+
                |            |``stage``           |``string``  |Set the conversion stage           |
                +------------+--------------------+------------+-----------------------------------+
                |            |``result``          |``string``  |Set the conversion result          |
                +------------+--------------------+------------+-----------------------------------+
                |            |``convert_start_    |``string``  |Set the conversion start date and  |
                |            |date``              |            |time                               |
                +------------+--------------------+------------+-----------------------------------+
                |            |``convert_end_date``|``string``  |Set the conversion end date and    |
                |            |                    |            |time                               |
                +------------+--------------------+------------+-----------------------------------+
                |            |``publish_start     |``string``  |Set the publish start date and time|
                |            |_date``             |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``publish_end_date``|``string``  |Set the publication end date and   |
                |            |                    |            |time                               |
                +------------+--------------------+------------+-----------------------------------+
                |            |``version_comment`` |``string``  |Set the description                |
                +------------+--------------------+------------+-----------------------------------+
                |            |``version_ins_date``|``date``    |Set the version creation time      |
                +------------+--------------------+------------+-----------------------------------+
                |            |``version_upd_date``|``date``    |Set the version creation time      |
                +------------+--------------------+------------+-----------------------------------+

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

                # AIModels - GetModels
                response = ai_model_obj.get_models(
                    model_id,
                    comment,
                    project_name,
                    model_platform,
                    project_type,
                    device_id,
                    latest_type
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
            if "model_id" in _local_params and _local_params["model_id"] is None:
                del _local_params["model_id"]

            if "comment" in _local_params and _local_params["comment"] is None:
                del _local_params["comment"]

            if "project_name" in _local_params and _local_params["project_name"] is None:
                del _local_params["project_name"]

            if "model_platform" in _local_params and _local_params["model_platform"] is None:
                del _local_params["model_platform"]

            if "project_type" in _local_params and _local_params["project_type"] is None:
                del _local_params["project_type"]

            if "device_id" in _local_params and _local_params["device_id"] is None:
                del _local_params["device_id"]

            if "latest_type" in _local_params and _local_params["latest_type"] is None:
                _local_params["latest_type"] = "1"

            # Validate schema
            _query_params = SchemaGetModels().load(_local_params)

            # Enter a context with an instance of the API client
            with aitrios_console_rest_client_sdk_primitive.ApiClient(
                self._config.configuration,
                header_name="Authorization",
                header_value=self._config.get_access_token(),
            ) as api_client:
                # Create an instance of the API class
                manage_devices_api_instance = train_model_api.TrainModelApi(api_client)
                try:
                    _return_get_models = manage_devices_api_instance.get_models(_query_params)
                    return _return_get_models.body

                except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                    _return_get_models = self.on_key_error_response(__name__, key_err)

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_get_models = self.on_type_error_response(__name__, type_err)

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_get_models = self.on_value_error_response(__name__, val_err)

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_get_models = self.on_attribute_error_response(__name__, attr_err)

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_get_models = self.on_http_error_response(__name__, exception)

                except Exception as exception:
                    _return_get_models = self.on_generic_error_response(__name__, exception)

        except ValidationError as err:
            _return_get_models = self.on_validation_error_response(__name__, err)

        return _return_get_models
