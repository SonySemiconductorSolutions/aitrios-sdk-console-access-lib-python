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
# pylint:disable=too-many-return-statements
# pylint:disable=protected-access
# pylint:disable=too-many-branches
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


class SchemaGetInferenceresults(Schema):
    """Schema for API to Get a list of (saved) inference results metadata.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : Device ID
    device_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for device_id"}, strict=True
    )

    #: str, optional : Search filter. \
    #:                 The specifications are the same except for those of Cosmos DB UI
    #:                 of the Azure portal and those listed below.
    #:
    #:                 - A where string does not need to be added to the heading.
    #:                 - deviceID does not need to be added.
    #:
    #:                 Filter Example:
    #:
    #:                     * ModelID: string  match filter
    #:                         eg. "c.ModelID=\"0300000001590100\""
    #:                     * Image: boolean  match filter eg. "c.Image=true"
    #:                     * T: string  match or more filter
    #:                         eg. "c.Inferences[0].T>=\"20230412140050618\""
    #:                     * T: string  range filter
    #:                         eg. "EXISTS(SELECT VALUE i FROM i IN c.Inferences \
    #:                             WHERE i.T >= \"20230412140023098\" AND \
    #:                             i.T <= \"20230412140029728\")"
    #:                     * _ts: number  match filter
    #:                         eg. "c._ts=1681308028"
    #:
    #:                 Default = ''
    filter = fields.String(
        required=False, error_messages={"invalid": "Invalid string for filter"}, strict=True
    )

    #: int, optional : Number of cases to get.
    #:                 Return the latest record of the specified number of cases.
    #:                 Maximum value: 10000.
    #:                 default: 20
    number_of_inference_results = fields.Integer(
        required=False,
        error_messages={"invalid": "Invalid Integer for number_of_inference_results"},
        strict=True,
    )

    #: int, optional : If 1 is specified, add a record stored to Cosmos DB and return it.
    #:                 Default:1
    #:
    #:                 - Value definition
    #:
    #:                  - 0: Do not add
    #:                  - 1: Add
    raw = fields.Integer(
        required=False, error_messages={"invalid": "Invalid Integer for raw"}, strict=True
    )

    #: str, optional : When this value is specified, extract the inference result \
    #:                 metadata within the following range. Default:""
    #:
    #:                 - Extraction range:
    #:                   (time - threshold) <= T
    #:
    #:                   Time in inference result metadata < (time + threshold)
    #:
    #:                     - Value definition
    #:
    #:                         - yyyy: 4-digit year string
    #:                         - MM: 2-digit month string
    #:                         - dd: 2-digit day string
    #:                         - HH: 2-digit hour string
    #:                         - mm: 2-digit minute string
    #:                         - ss: 2-digit seconds string
    #:                         - fff: 3-digit millisecond string
    time = fields.String(
        required=False, error_messages={"invalid": "Invalid string for time"}, strict=True
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if str(data["device_id"]).strip() == "":
            raise ValidationError("device_id is required or can't be empty string")

        if "filter" in data and (data["filter"] is None or str(data["filter"]).strip() == ""):
            raise ValidationError("filter is required or can't be empty string")

        if "number_of_inference_results" in data and (
            data["number_of_inference_results"] is None
            or isinstance(data["number_of_inference_results"], int) is False
            or data["number_of_inference_results"] < 0
        ):
            raise ValidationError(
                "number_of_inference_results is required or number_of_inference_results must be"
                " integer or can't be negative"
            )

        if "raw" in data and (
            data["raw"] is None or isinstance(data["raw"], int) is False or data["raw"] < 0
        ):
            raise ValidationError("raw is required or raw must be integer or can't be negative")

        date_format = "%Y%m%d%H%M%S%f"
        if "time" in data and data["time"] is not None and str(data["time"]).strip() != "":
            try:
                datetime.strptime(data["time"], date_format)
            except Exception as ex:
                logger.error(str(ex))
                raise ValidationError("Invalid time format") from ex
        elif "time" in data and (data["time"] is None or str(data["time"]).strip() == ""):
            raise ValidationError("time is required or can't be empty string")


class GetInferenceresults(ConsoleAccessBaseClass):
    """This class implements API to get inference results.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class GetInferenceresults

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

    def get_inference_results(
        self,
        device_id: str,
        filter: str = None,
        number_of_inference_results: int = 20,
        raw: int = 1,
        time: str = None,
    ):
        """Get the (saved) inference result metadata list information for a specified device.

        Args:
            device_id (str, required) : Device ID
            filter (str, optional) : Search filter.
                The specifications are the same except for those of Cosmos DB UI \
                    of the Azure portal and those listed below.

                - A where string does not need to be added to the heading.
                - deviceID does not need to be added.

                        Filter Example:

                            * ModelID: string  match filter
                                eg. "c.ModelID=\"0300000001590100\""
                            * Image: boolean  match filter eg. "c.Image=true"
                            * T: string  match or more filter
                                eg. "c.Inferences[0].T>=\"20230412140050618\""
                            * T: string  range filter
                                eg. "EXISTS(SELECT VALUE i FROM i IN c.Inferences \
                                    WHERE i.T >= \"20230412140023098\" AND \
                                    i.T <= \"20230412140029728\")"
                            * _ts: number  match filter
                                eg. "c._ts=1681308028"

                Default = ''

            number_of_inference_results (int, optional) :Number of cases to get.
                Return the latest record of the specified number of cases. Maximum value: 10000.
                default: 20

            raw (int, optional) : If 1 is specified, add a record stored to Cosmos DB and return it.

                - Value definitions

                    - 0: Do not add
                    - 1: Add

                default: 1

            time (str, optional) : When this value is specified,\
                    extract the inference result metadata within the following range. \
                    Default:""

                    - Extraction range:
                      (time - threshold) <= T

                      Time in inference result metadata < (time + threshold)

                    - Value definition

                        - yyyy: 4-digit year string
                        - MM: 2-digit month string
                        - dd: 2-digit day string
                        - HH: 2-digit hour string
                        - mm: 2-digit minute string
                        - ss: 2-digit seconds string
                        - fff: 3-digit millisecond string

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------------+-------------+-----------+------------------------------------+
                | *Level1*         | *Level2*    | *Type*    | *Description*                      |
                +==================+============+============+====================================+
                | ``No_item_name`` |             |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``id``       | ``string``| Inference result metadata ID.      |
                |                  |             |           | =GUID generated automatically by   |
                |                  |             |           | CosmosDB                           |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``device_id``| ``string``| Device ID.                         |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model_id`` | ``string``| Model ID.                          |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``version    | ``string``| Version number.                    |
                |                  |_number``    |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model      |``string`` | Model version ID.                  |
                |                  |_version_id``|           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``model      |``string`` | Model type                         |
                |                  |_type``      |           |                                    |
                |                  |             |           | 00: Image category                 |
                |                  |             |           |                                    |
                |                  |             |           | 01: Object detection               |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``training   |``string`` |                                    |
                |                  |_kit_name``  |           |                                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``_ts``      |``integer``| Timestamp.                         |
                |                  |             |           | =_ts of CosmosDB                   |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``inference  |           |Refer :ref:`inference_result <ifr2>`|
                |                  |_result``    |           |for more details                    |
                +------------------+-------------+-----------+------------------------------------+
                |                  |``inferenc   |``array``  |Refer :ref:`inferences <if2>`       |
                |                  |es``         |           |for more details                    |
                +------------------+-------------+-----------+------------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inference_result   | .. _ifr2:                                                 |
                +--------------------+--------------+------------+-------------------------------+
                | *Level1*           | *Level2*     | *Type*     | *Description*                 |
                +====================+==============+============+===============================+
                |``inference_result``|              |            |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``DeviceID``  | ``string`` |Device ID                      |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``ModelID``   |``string``  |DnnModelVersion                |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``Image``     |``boolean`` |Synchronized to the            |
                |                    |              |            |InputTensor output.            |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``Inferences``|``array``   |Refer :ref:`inferences <if2>`  |
                |                    |              |            |for more details               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``id``        |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``ttl``       |``integer`` |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_rid``      |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_self``     |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_etag``     |``string``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_attachm    |``string``  |                               |
                |                    |ents``        |            |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``_ts``       |``integer`` |                               |
                +--------------------+--------------+------------+-------------------------------+

                +--------------------+--------------+------------+-------------------------------+
                | inferences         | .. _if2:                                                  |
                +--------------------+--------------+------------+-------------------------------+
                | *Level1*           | *Level2*     | *Type*     | *Description*                 |
                +====================+==============+============+===============================+
                |``inferences``      |              | ``array``  |                               |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``T``         | ``string`` |Time when retrieving           |
                |                    |              |            |data from the sensor.          |
                +--------------------+--------------+------------+-------------------------------+
                |                    |``O``         |``string``  |Output tensor (Encoding format)|
                +--------------------+--------------+------------+-------------------------------+

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
                    if any input non integer parameter found OR
                    if any input time format is invalid.
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
                device_id =  "__device_id__"
                filter =  "__filter__"
                number_of_inference_results =  "__number_of_inference_results__"
                raw =  "__raw__"
                time =  "__time__"

                # Insight - GetInferenceResults
                response = insight_obj.get_inference_results(device_id,
                                                            filter,
                                                            number_of_inference_results,
                                                            raw,
                                                            time)
                pprint(response)
        """

        logger.info(sys._getframe().f_code.co_name)

        try:
            _local_params = locals()
            # delete local argument 'self' form locals() for validation.
            if "self" in _local_params:
                del _local_params["self"]

            # set default values, if not passed.
            if "filter" in _local_params and _local_params["filter"] is None:
                del _local_params["filter"]

            if (
                "number_of_inference_results" in _local_params
                and _local_params["number_of_inference_results"] is None
            ):
                _local_params["number_of_inference_results"] = 20

            if "raw" in _local_params and _local_params["raw"] is None:
                _local_params["raw"] = 1

            if "time" in _local_params and _local_params["time"] is None:
                del _local_params["time"]

            # Validate schema
            _local_params = SchemaGetInferenceresults().load(_local_params)

            _path_params = {
                "device_id": _local_params["device_id"],
            }
            _query_params = {
                "NumberOfInferenceresults": _local_params["number_of_inference_results"],
                "raw": _local_params["raw"],
            }

            if "filter" in _local_params:
                filter_dict = {"filter": _local_params["filter"]}
                _query_params.update(filter_dict)

            if "time" in _local_params:
                time_dict = {"time": _local_params["time"]}
                _query_params.update(time_dict)

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
                    _return_get_inference_results = insight_api_instance.get_inference_results(
                        path_params=_path_params, query_params=_query_params
                    )
                    return _return_get_inference_results.body

                except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                    _return_get_inference_results = self.on_key_error_response(__name__, key_err)

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_get_inference_results = self.on_type_error_response(__name__, type_err)

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_get_inference_results = self.on_value_error_response(__name__, val_err)

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_get_inference_results = self.on_attribute_error_response(
                        __name__, attr_err
                    )

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_get_inference_results = self.on_http_error_response(__name__, exception)

                except Exception as exception:
                    _return_get_inference_results = self.on_generic_error_response(
                        __name__, exception
                    )

        except ValidationError as err:
            _return_get_inference_results = self.on_validation_error_response(__name__, err)

        return _return_get_inference_results
