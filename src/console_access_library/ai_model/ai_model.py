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
        """Get the model list information

        Args:
            model_id (str, optional) : Model ID. Partial match search
            comment (str, optional) : Model description. Partial match search
            project_name(str, optional) : Project name. Partial match search
            model_platform(str, optional) : Model platform

                - Value definition

                    - 0 : Custom Vision
                    - 1 : Non Custom Vision

            project_type (str, optional) : Project Type.

                - Value definition

                    - 0 : Base model
                    - 1 : Device model

            device_id (str, optional) : Device Id. \

            latest_type (str, optional) : Latest version type.

                - Value definition

                    - 0 : latest published version
                    - 1 : Latest version (latest including model version being \
                    converted/published)

                default: 1

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+-------------------+------------+-------------------------------+
                | *Level1*   | *Level2*          | *Type*     | *Description*                 |
                +============+===================+============+===============================+
                | ``models`` |                   | ``array``  |                               |
                +------------+-------------------+------------+-------------------------------+
                |            | ``model_id``      | ``string`` | Set the model ID              |
                +------------+-------------------+------------+-------------------------------+
                |            | ``model_type``    | ``string`` | Set the model type            |
                +------------+-------------------+------------+-------------------------------+
                |            | ``functionality`` | ``string`` | Set the feature descriptions  |
                +------------+-------------------+------------+-------------------------------+
                |            | ``vendor_name``   | ``string`` | Set the vendor name           |
                +------------+-------------------+------------+-------------------------------+
                |            | ``model_comment`` | ``string`` | Set the description           |
                +------------+-------------------+------------+-------------------------------+
                |            | ``network_type``  | ``string`` | Set the network type.         |
                +------------+-------------------+------------+-------------------------------+
                |            | ``create_by``     | ``string`` | Set the create_by.            |
                |            |                   |            | - Value definition            |
                |            |                   |            | Self: Self-training models    |
                |            |                   |            | Marketplace: Marketplace      |
                |            |                   |            | purchacing model              |
                +------------+-------------------+------------+-------------------------------+
                |            | ``package_id``    | ``string`` | Set the marketplace package ID|
                +------------+-------------------+------------+-------------------------------+
                |            | ``product_id``    | ``string`` | Set the marketplace product ID|
                +------------+-------------------+------------+-------------------------------+
                |            |``metadata_format_ | ``string`` | Set the metadata_format_id.   |
                |            |id``               |            |                               |
                +------------+-------------------+------------+-------------------------------+
                |            | ``projects``      | ``array``  | Refer :ref:`projects <p2>`    |
                |            |                   |            | for more details              |
                +------------+-------------------+------------+-------------------------------+

                +------------+--------------------+------------+-----------------------------------+
                | projects   | .. _p2:                                                             |
                +------------+--------------------+------------+-----------------------------------+
                | *Level1*   | *Level2*           | *Type*     | *Description*                     |
                +============+====================+============+===================================+
                |``projects``|                    | ``array``  |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_project_    | ``string`` |Set the model project name         |
                |            |name``              |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_project_    | ``string`` |Set the model project id           |
                |            |id``                |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_platform``  |``string``  |Set the model platform             |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_type``      |``string``  |Set the model type                 |
                +------------+--------------------+------------+-----------------------------------+
                |            |``project_type``    |``string``  |Set the project type               |
                +------------+--------------------+------------+-----------------------------------+
                |            |``device_id``       |``string``  |Set the device ID                  |
                +------------+--------------------+------------+-----------------------------------+
                |            |``versions``        |``array``   |Refer :ref:`versions <v2>`         |
                |            |                    |            |for more details                   |
                +------------+--------------------+------------+-----------------------------------+

                +------------+--------------------+------------+-----------------------------------+
                | versions   | .. _v2:                                                             |
                +------------+--------------------+------------+-----------------------------------+
                | *Level1*   | *Level2*           | *Type*     | *Description*                     |
                +============+====================+============+===================================+
                |``versions``|                    | ``array``  |There must be one subordinate      |
                |            |                    |            |element for this API.              |
                +------------+--------------------+------------+-----------------------------------+
                |            |``version_number``  | ``string`` |Set the version number             |
                +------------+--------------------+------------+-----------------------------------+
                |            |``iteration_id``    |``string``  |Set the iteration ID               |
                +------------+--------------------+------------+-----------------------------------+
                |            |``iteration_name``  |``string``  |Set the iteration name             |
                +------------+--------------------+------------+-----------------------------------+
                |            |``accuracy``        |``string``  |Set the accuracy                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_performan   |``object``  |Set the performance information    |
                |            |ces``               |            |of the model.                      |
                +------------+--------------------+------------+-----------------------------------+
                |            |``latest_flg``      |``string``  |Set the latest flag                |
                +------------+--------------------+------------+-----------------------------------+
                |            |``publish_latest    |``string``  |Set the latest published flag      |
                |            |_flg``              |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``version_status``  |``string``  |Set the status                     |
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
                |            |``org_file_name``   |``string``  |Set the preconversion model        |
                |            |                    |            |filename.                          |
                +------------+--------------------+------------+-----------------------------------+
                |            |``org_file_size``   |``integer`` |Set the publish model file size    |
                +------------+--------------------+------------+-----------------------------------+
                |            |``publish_file_     |``string``  |Set the publish model filename     |
                |            |name``              |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``publish_file_     |``integer`` |Set the publish model file size    |
                |            |size``              |            |                                   |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_file_size`` |``integer`` |Set the model file size            |
                +------------+--------------------+------------+-----------------------------------+
                |            |``model_framework`` |``string``  |Set the model framework            |
                +------------+--------------------+------------+-----------------------------------+
                |            |``conv_id``         |``string``  |Set the conversion request ID      |
                +------------+--------------------+------------+-----------------------------------+
                |            |``labels``          |``string[]``|Set the label array                |
                +------------+--------------------+------------+-----------------------------------+
                |            |``stage``           |``string``  |Set the conversion stage           |
                +------------+--------------------+------------+-----------------------------------+
                |            |``kpi``             |``array``   |                                   |
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
                 - The json format is an array of objects. Each object contains the \
                    following values.

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
            metadata_format_id,
        )

    def get_base_model_status(
        self,
        model_id: str,
        latest_type: str = "1",
    ):
        """Get the specified base model information

        Args:
            model_id (str, required) : Model ID.
            latest_type (str, optional) : Latest version type.

                - Value definition

                    - 0: Latest published version
                    - 1: Latest version (latest including model version being \
                    converted/published)

                default: 1

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +-----------------+----------+----------+-----------------------------------------+
                | *Level1*        | *Level2* | *Type*   |*Description*                            |
                +=================+==========+==========+=========================================+
                |``model_id``     |          |``string``|Set the model ID                         |
                +-----------------+----------+----------+-----------------------------------------+
                |``model_type``   |          |``string``|Set the model type                       |
                +-----------------+----------+----------+-----------------------------------------+
                |``functionality``|          |``string``|Set the function                         |
                |                 |          |          |descriptions                             |
                +-----------------+----------+----------+-----------------------------------------+
                |``vendor_name``  |          |``string``|Set the vendor name                      |
                +-----------------+----------+----------+-----------------------------------------+
                |``model_comment``|          |``string``|Set the description                      |
                +-----------------+----------+----------+-----------------------------------------+
                |``network_type`` |          |``string``|Set the network type.                    |
                +-----------------+----------+----------+-----------------------------------------+
                |``create_by``    |          |``string``| Set the create_by.                      |
                |                 |          |          | - Value definition                      |
                |                 |          |          | Self: Self-training models              |
                |                 |          |          | Marketplace: Marketplace purchasing     |
                |                 |          |          | model                                   |
                +-----------------+----------+----------+-----------------------------------------+
                |``package_id``   |          |``string``|Set the marketplace package ID.          |
                +-----------------+----------+----------+-----------------------------------------+
                |``product_id``   |          |``string``|Set the marketplace product ID.          |
                +-----------------+----------+----------+-----------------------------------------+
                |``metadata_format|          |``string``|Set the metadata_format_id               |
                |_id``            |          |          |                                         |
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
                +============+====================+===========+===================================+
                |``versions``|                    | ``array`` |There must be one subordinate      |
                |            |                    |           |element for this API.              |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``version_number``  | ``string``|Set the version number             |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``iteration_id``    |``string`` |Set the iteration ID               |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``iteration_name``  |``string`` |Set the iteration name             |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``accuracy``        |``string`` |Set the accuracy                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``model_            |``object`` |Set the the performance information|
                |            |performance``       |           |of the model.                      |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``latest_flg``      |``string`` |Set the latest flag                |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``publish_latest_   |``string`` |Set the latest published flag      |
                |            |flg``               |           |                                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``version_status``  |``string`` |Set the status                     |
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
                |            |                    |           |'07': Add to configuration         |
                |            |                    |           |complete                           |
                |            |                    |           |                                   |
                |            |                    |           |'11': 'Saving' Model saving        |
                |            |                    |           |status in Model Retrainer case     |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``org_file_name``   |``string`` |Set the preconversion model        |
                |            |                    |           |filename.                          |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``org_file_size``   |``integer``|Set the publish model file size    |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``publish_file_     |``string`` |Set the publish model file name    |
                |            |name``              |           |                                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``publish_file_     |``integer``|Set the publish model file size    |
                |            |size``              |           |                                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``model_file_size`` |``integer``|Set the model file size.           |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``model_framework`` |``string`` |Set up the model framework         |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``conv_id``         |``string`` |Set the conversion request ID      |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``labels``          |``array``  |Set the label array                |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``stage``           |``string`` |Set the conversion stage           |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``result``          |``string`` |Set the conversion result          |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``kpi``             |``object`` |                                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``converter_log``   |``array``  |converter log.                     |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``convert_start_    |``string`` |Set the conversion start date      |
                |            |date``              |           |                                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``convert_end_date``|``string`` |Set the conversion end date        |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``publish_start_    |``string`` |Set the publish start date         |
                |            |date``              |           |                                   |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``publish_end_date``|``string`` |Set the publish end date           |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``version_comment`` |``string`` |Set the description                |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``version_ins_date``|``string`` |Set the created time of the        |
                |            |                    |           |version.                           |
                +------------+--------------------+-----------+-----------------------------------+
                |            |``version_upd_date``|``string`` |Set the created time of the        |
                |            |                    |           |version.                           |
                +------------+--------------------+-----------+-----------------------------------+

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
        """Deletes the base model, device model, and project associated with
        the specified model ID.

        Args:
            model_id (str, required) : Model ID.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                    +------------+------------+-------------------------------+
                    | *Level1*   | *Type*     | *Description*                 |
                    +============+============+===============================+
                    | ``result`` | ``string`` | Set "SUCCESS" fixing.         |
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
        """Provide a function to publish a conversion model. \
        As model publishing takes time, this is performed asynchronously. \
        Check the processing status in the result of the GetBaseModelStatus \
        API or GetDeviceModelStatus API response.\
        If the result is 'Import completed', the process is completed.

        Args:
            model_id (str, required) : Model ID.
            device_id (str, optional) : Device ID. Specify this when the device model is the\
                target. Do not specify this when the base model is the target.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +----------------+------------+-------------------------------+
                | *Level1*       | *Type*     | *Description*                 |
                +================+============+===============================+
                | ``result``     | ``string`` | Set "SUCCESS" fixing          |
                +----------------+------------+-------------------------------+
                | ``import_id``  | ``string`` | Set the conv id               |
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

    def publish_model_wait_response(
        self, model_id: str,
        device_id: str = None,
        callback=None
    ):
        """Publish model and wait for completion

        Args:
            model_id (str, required) : Model ID.
            device_id (str, optional) : Device ID. Specify this when the device model is the\
                target. Do not specify this when the base model is the target.
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
                +===================+============+===============================+
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
