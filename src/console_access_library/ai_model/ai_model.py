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
# pylint:disable=too-many-instance-attributes
# pylint:disable=too-many-public-methods
# pylint:disable=duplicate-code
# pylint:disable=too-many-function-args
# pylint:disable=too-many-arguments
# pylint:disable=unused-argument
# pylint:disable=too-many-lines

from console_access_library.ai_model.delete_model import DeleteModel
from console_access_library.ai_model.get_base_model_status import GetBaseModelStatus
from console_access_library.ai_model.get_models import GetModels
from console_access_library.ai_model.import_base_model import ImportBaseModel
from console_access_library.ai_model.publish_model import PublishModel
from console_access_library.ai_model.publish_model_wait_response import (
    PublishModelStatus,
    PublishModelWaitResponse,
)
from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass


class AIModel(ConsoleAccessBaseClass):
    """Abstract class to access Console Access Library AIModel component \
    APIs from AIModel component

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for AIModel Abstract class

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._get_models_obj = GetModels(config)
        self._get_base_model_status_obj = GetBaseModelStatus(config)
        self._delete_model_obj = DeleteModel(config)
        self._import_base_model_obj = ImportBaseModel(config)
        self._publish_model_obj = PublishModel(config)
        self._publish_model_wait_response_obj = PublishModelWaitResponse(config)
        self.publish_status = PublishModelStatus

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
        """Abstract function call to ``get_models`` API

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

            device_id (str, optional) : Device Id. (specified if you \
                want to search for the device model). Exact search \
                Search all device_ids if not specified.

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
                |            | ``projects``      | ``array``  | Refer :ref:`projects <p2>`    |
                |            |                   |            | for more details              |
                +------------+-------------------+------------+-------------------------------+

                +------------+--------------------+------------+-----------------------------------+
                | projects   | .. _p2:                                                             |
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
                |            |``versions``        |``array``   |Refer :ref:`versions <v2>`         |
                |            |                    |            |for more details                   |
                +------------+--------------------+------------+-----------------------------------+

                +------------+--------------------+------------+-----------------------------------+
                | versions   | .. _v2:                                                             |
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
                |            |``labels``          |``string``  |Set the label array                |
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
        """

        return self._get_models_obj.get_models(
            model_id, comment, project_name, model_platform, project_type, device_id, latest_type
        )

    def import_base_model(
        self,
        model_id: str,
        model: str,
        converted: bool = False,
        vendor_name: str = None,
        comment: str = None,
        input_format_param: str = None,
        network_config: str = None,
        network_type: str = "1",
        labels: list = None,
    ):
        """Abstract function call to ``import_base_model`` API

        Args:
            model_id (str, required) : Model ID. (model ID for new \
                saving or version upgrade). Within 100 characters.
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
        """

        return self._import_base_model_obj.import_base_model(
            model_id,
            model,
            converted,
            vendor_name,
            comment,
            input_format_param,
            network_config,
            network_type,
            labels,
        )

    def get_base_model_status(
        self,
        model_id: str,
        latest_type: str = "1",
    ):
        """Abstract function call to ``get_base_model_status`` API

        Args:
            model_id (str, required) : The Model ID.
            latest_type (str, optional) : Latest version type.

                - 0: latest published version
                - 1: Latest version (latest including model version in process of \
                conversion/publishing)

                Exact search, 1 if not specified.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-----------------+----------+----------+-----------------------------------------+
                | *Level1*        | *Level2* | *Type*   |*Description*                            |
                +-----------------+----------+----------+-----------------------------------------+
                |``model_id``     |          |``string``|Set the model ID                         |
                +-----------------+----------+----------+-----------------------------------------+
                |``device_type``  |          |``string``|Set the model type                       |
                +-----------------+----------+----------+-----------------------------------------+
                |``functionality``|          |``string``|Set the feature                          |
                |                 |          |          |description                              |
                +-----------------+----------+----------+-----------------------------------------+
                |``vendor_name``  |          |``string``|Set the vendor name                      |
                +-----------------+----------+----------+-----------------------------------------+
                |``model_comment``|          |``string``|Set the description                      |
                +-----------------+----------+----------+-----------------------------------------+
                |``network_type`` |          |``string``|0: Custom Vision                         |
                |                 |          |          |                                         |
                |                 |          |          |1: Non Custom Vision                     |
                +-----------------+----------+----------+-----------------------------------------+
                |``projects``     |          |``array`` |                                         |
                +-----------------+----------+----------+-----------------------------------------+
                |                 |``model_  |``string``|Set the model project name               |
                |                 |project_  |          |                                         |
                |                 |name``    |          |                                         |
                +-----------------+----------+----------+-----------------------------------------+
                |                 |``model_  |``string``|Set the model project                    |
                |                 |project_  |          |ID                                       |
                |                 |id``      |          |                                         |
                +-----------------+----------+----------+-----------------------------------------+
                |                 |``model_  |``string``|Set up the model platform                |
                |                 |platform``|          |                                         |
                +-----------------+----------+----------+-----------------------------------------+
                |                 |``model_  |``string``|Set the model type                       |
                |                 |type``    |          |                                         |
                |                 |          |          |                                         |
                +-----------------+----------+----------+-----------------------------------------+
                |                 |``project_|``string``|Set the project type                     |
                |                 |type``    |          |                                         |
                +-----------------+----------+----------+-----------------------------------------+
                |                 |``device_ |``string``|Set the device ID                        |
                |                 |id``      |          |                                         |
                +-----------------+----------+----------+-----------------------------------------+
                |                 |``versi   |``array`` |Refer :ref:`versions <versions_element2>`|
                |                 |ons``     |          |for more details                         |
                +-----------------+----------+----------+-----------------------------------------+

                +------------+--------------------+-----------+-----------------------------------+
                | versions   | .. _versions_element2:                                             |
                +------------+--------------------+-----------+-----------------------------------+
                | *Level1*   | *Level2*           | *Type*    | *Description*                     |
                +------------+--------------------+-----------+-----------------------------------+
                |``versions``|                    | ``array`` |Although it is a subordinate       |
                |            |                    |           |element, in the case of this       |
                |            |                    |           |API, there is always one.          |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``version_number``  | ``string``|Set the version number             |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``iteration_id``    |``string`` |Set the iteration ID               |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``iteration_name``  |``string`` |Set the iteration name             |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``accuracy``        |``string`` |Set the precision                  |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``model_            |``string`` |Refer :ref:`model_performance <m3>`|
                |            |performance``       |           |for more details                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``latest_flg``      |``string`` |Set the latest flag                |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``publish_latest_   |``string`` |Set the latest published flag      |
                |            |flg``               |           |                                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``version_status``  |``string`` |Set your status                    |
                |            |                    |           |                                   |
                |            |                    |           |'01': 'Before conversion'          |
                |            |                    |           |                                   |
                |            |                    |           |'02': 'Converting'                 |
                |            |                    |           |                                   |
                |            |                    |           |'03': 'Conversion failed'          |
                |            |                    |           |                                   |
                |            |                    |           |'04': 'Conversion complete'        |
                |            |                    |           |                                   |
                |            |                    |           |'05': 'Adding to configuration'    |
                |            |                    |           |                                   |
                |            |                    |           |'06': 'Add to configuration failed'|
                |            |                    |           |                                   |
                |            |                    |           |'07': 'Add to configuration        |
                |            |                    |           |complete                           |
                |            |                    |           |                                   |
                |            |                    |           |'11': 'Saving' Model saving        |
                |            |                    |           |status in Model Retrainer case     |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``org_file_name``   |``string`` |Set the file name of the model     |
                |            |                    |           |before conversion                  |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``org_file_size``   |``integer``|Set the publishing model file size |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``publish_file_     |``string`` |Set the publishing model file name |
                |            |name``              |           |                                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``publish_file_     |``integer``|Set the publishing model file size |
                |            |size``              |           |                                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``model_file_size`` |``integer``|Deployment model file size         |
                |            |                    |           |* However, TBD is set as the       |
                |            |                    |           |calculation method                 |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``model_framework`` |``string`` |Set up the model framework         |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``conv_id``         |``string`` |Set the conversion request ID      |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``labels``          |``string`` |Set the label array                |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``stage``           |``string`` |Set the conversion stage           |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``result``          |``string`` |Set the conversion result          |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``kpi``             |``string`` |Refer :ref:`kpi <kpi1>`            |
                |            |                    |           |for more details                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``convert_start_    |``string`` |Set the conversion start date and  |
                |            |date``              |           |time                               |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``convert_end_date``|``string`` |Set the conversion end date and    |
                |            |                    |           |time                               |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``publish_start_    |``string`` |Set the publish start date and time|
                |            |date``              |           |                                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``publish_end_date``|``string`` |Set the publication end date and   |
                |            |                    |           |time                               |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``version_comment`` |``string`` |Set the description                |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``version_ins_date``|``date``   |Set the version creation time      |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``version_upd_date``|``date``   |Set the version creation time      |
                +------------+--------------------+-----------+-----------------------------------+

                +------------+--------------------+------------+----------------------------------+
                |``model_p   | .. _m3:                                                            |
                |erformance``|                                                                    |
                +------------+--------------------+------------+----------------------------------+
                | *Level1*   | *Level2*           | *Type*     | *Description*                    |
                +------------+--------------------+------------+----------------------------------+
                |``model_p   |                    | ``string`` |Set model performance             |
                |erformance``|                    |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``perTag            |``string``  |Refer :ref:`pTP <pTP_element1>`   |
                |            |Performance``       |            |for more details                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``precision``       |``string``  |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``precisionStd      |``string``  |                                  |
                |            |Deviation``         |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``recall``          |``string``  |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``recallStd         |``string``  |                                  |
                |            |Deviation``         |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``averagePrecision``|``string``  |                                  |
                +------------+--------------------+------------+----------------------------------+

                +------------+--------------------+------------+----------------------------------+
                | kpi        | .. _kpi1:                                                          |
                +------------+--------------------+------------+----------------------------------+
                | *Level1*   | *Level2*           | *Type*     | *Description*                    |
                +------------+--------------------+------------+----------------------------------+
                |``kpi``     |                    | ``string`` |Set KPIs                          |
                +------------+--------------------+------------+----------------------------------+
                |            |``Memory Report``   |``string``  |Refer :ref:`MP <MP_element1>`     |
                |            |                    |            |for more details                  |
                +------------+--------------------+------------+----------------------------------+

                +------------+--------------------+------------+----------------------------------+
                | pTP        | .. _pTP_element1:                                                  |
                +------------+--------------------+------------+----------------------------------+
                | *Level1*   | *Level2*           | *Type*     | *Description*                    |
                +------------+--------------------+------------+----------------------------------+
                |``perTagP   |                    | ``string`` |                                  |
                |erformance``|                    |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``id``              |``string``  |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``name``            |``string``  |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``precision``       |``string``  |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``precisionStd      |``string``  |                                  |
                |            |Deviation``         |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``recallStd         |``string``  |                                  |
                |            |Deviation``         |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``averagePrecision``|``string``  |                                  |
                +------------+--------------------+------------+----------------------------------+

                +------------+--------------------+------------+----------------------------------+
                |MP          |.. _MP_element1:                                                    |
                +------------+--------------------+------------+----------------------------------+
                | *Level1*   | *Level2*           | *Type*     | *Description*                    |
                +------------+--------------------+------------+----------------------------------+
                |``Memory    |                    | ``string`` |                                  |
                |Report``    |                    |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Name``            |``string``  |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Runtime Memory    |``string``  |                                  |
                |            |Physical Size``     |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Model Memory      |``string``  |                                  |
                |            |Physical Size``     |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Reserved Memory`` |``string``  |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Memory Usage``    |``string``  |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Total Memory      |``string``  |                                  |
                |            |Available On Chip`` |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Memory            |``string``  |                                  |
                |            |Utilization``       |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Fit In Chip``     |``string``  |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Input Persistent``|            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Networks``        |            |Refer :ref:`Networks <Ne1>`       |
                |            |                    |            |for more details                  |
                +------------+--------------------+------------+----------------------------------+

                +------------+--------------------+------------+----------------------------------+
                |Networks    |.. _Ne1:                                                            |
                +------------+--------------------+------------+----------------------------------+
                | *Level1*   | *Level2*           | *Type*     | *Description*                    |
                +------------+--------------------+------------+----------------------------------+
                |``Networks``|                    |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Hash``            |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Name``            |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Runtime Memory    |            |                                  |
                |            |Physical Size``     |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Model Memory      |            |                                  |
                |            |Physical Size``     |            |                                  |
                +------------+--------------------+------------+----------------------------------+
                |            |``Input Persistence |            |                                  |
                |            |Cost``              |            |                                  |
                +------------+--------------------+------------+----------------------------------+

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

        return self._get_base_model_status_obj.get_base_model_status(model_id, latest_type)

    def delete_model(
        self,
        model_id: str,
    ):
        """Abstract function call to ``delete_model`` API

        Args:
            model_id (str, required) : The Model ID.

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
        """
        return self._delete_model_obj.delete_model(model_id)

    def publish_model(
        self,
        model_id: str,
        device_id: str = None,
    ):
        """Abstract function call to ``publish_model`` API

        Args:
            model_id (str, required) : The Model ID.
            device_id (str, optional) : The ID of edge AI device. \
                Specify when the device model is the target \
                If the base model is the target, do not specify.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +----------------+------------+-------------------------------+
                | *Level1*       | *Type*     | *Description*                 |
                +----------------+------------+-------------------------------+
                | ``result``     | ``string`` | Set "SUCCESS" pinning         |
                +----------------+------------+-------------------------------+
                | ``import_id``  | ``string`` | Set the import_id of          |
                |                |            | Model Import Rest API         |
                |                |            | (model-import) response       |
                +----------------+------------+-------------------------------+

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

        return self._publish_model_obj.publish_model(model_id, device_id)

    def publish_model_wait_response(self, model_id: str, device_id: str = None, callback=None):
        """Abstract function call to ``publish_model_wait_response`` API

        Args:
            model_id (str, required) : The Model ID.
            device_id (str, optional) : ID of edge AI device. Specify when the device \
                model is the target, If the base model is the target, do not specify.
            callback (function, optional) : A function handle of the form - \
                ``publish_callback(status)``, where ``status`` is the notified publish status. \
                Callback Function to check the publishing status with ``get_base_model_status``,
                and if not completed, call the callback function to notify the publishing status.\
                If not specified, no callback notification.

        Returns:
            **Return Type**

            - On Success Response - dict
            - On Error Response - dict

            **Success Response Schema**

                +-------------------+------------+-------------------------------+
                | *Level1*          | *Type*     | *Description*                 |
                +-------------------+------------+-------------------------------+
                | ``result``        | ``string`` | "SUCCESS"                     |
                +-------------------+------------+-------------------------------+
                | ``process time``  | ``string`` | Processing Time               |
                +-------------------+------------+-------------------------------+

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

        return self._publish_model_wait_response_obj.publish_model_wait_response(
            model_id, device_id, callback
        )
