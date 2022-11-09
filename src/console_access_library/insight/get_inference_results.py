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


class SchemaGetInferenceresults(Schema):
    """Schema for API to retrieve (saved) inference result metadata list \
       information for a specified device.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : Device ID.
    device_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for device_id"}
    )

    #: str, optional : Filter.
    filter = fields.String(required=False, error_messages={"invalid": "Invalid string for filter"})

    #: int, optional : Number Of Inference Results.
    number_of_inference_results = fields.Integer(
        required=False,
        error_messages={"invalid": "Invalid Integer for number_of_inference_results"},
    )

    #: int, optional : Raw.
    raw = fields.Integer(required=False, error_messages={"invalid": "Invalid Integer for raw"})

    #: str, optional : Time.
    time = fields.String(required=False, error_messages={"invalid": "Invalid string for time"})

    @validates_schema
    def validate(self, data, **kwargs):
        if data["device_id"] == "":
            raise ValidationError("device_id is required")

        if "filter" in data and data["filter"] is None:
            raise ValidationError("number_of_images is required")

        if "number_of_inference_results" in data and data["number_of_inference_results"] is None:
            raise ValidationError("number_of_inference_results is required")

        if "raw" in data and data["raw"] is None:
            raise ValidationError("raw is required")

        if "time" in data and data["time"] is None:
            raise ValidationError("time is required")


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
        self.logger = Logger().set_logger()

    def get_inference_results(
        self,
        device_id: str,
        filter: str = None,
        number_of_inference_results: int = None,
        raw: int = None,
        time: str = None,
    ):
        """Retrieves (saved) inference result metadata list information for a specified device.

        Args:
            device_id (str, required) : The Device ID.
            filter (str, optional) : The Filter. Search filter (same specifications as Cosmos DB UI
                                     on Azure portal except for the following)

                                        - No need to prepend where string
                                        - It is not necessary to add a deviceID.

            number_of_inference_results (int, optional) :Number of acquisitions.
                                                         If not specified: 20

            raw (int, optional) : The Raw. Data format of inference results.
                                    - 1:Append records stored in Cosmos DB.
                                    - 0:Not granted.

                                        If not specified: 0

            time (str, optional) : The Time. Inference result data stored in Cosmos DB.
                                   yyyyMMddHHmmssfff
                                    - yyyy: 4-digit year string
                                    - MM: 2-digit month string
                                    - dd: 2-digit day string
                                    - HH: 2-digit hour string
                                    - mm: 2-digit minute string
                                    - ss: 2-digit seconds string
                                    - fff: 3-digit millisecond string

        Returns:
            dict:
                - **Success Response** : Dictionary with below key and value pairs.

                    - No key name (object) : Inference data

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
                filter =  "__filter__"
                number_of_inferenceresults =  "__number_of_inferenceresults__"
                raw =  "__raw__"
                time =  "__time__"

                # Insight - GetInferenceResults
                response = console_sdk_client_obj.insight.get_inference_results(device_id,
                                                            filter,
                                                            number_of_inferenceresults,
                                                            raw,
                                                            time)
                pprint(response)
        """

        self.logger.info(sys._getframe().f_code.co_name)

        try:
            # delete local argument 'self' form locals() for validation.
            _local_params = locals()
            if "self" in _local_params:
                del _local_params["self"]

            # set default values, if not passed.
            if "filter" in _local_params and _local_params["filter"] is None:
                _local_params["filter"] = ""

            if (
                "number_of_inference_results" in _local_params
                and _local_params["number_of_inference_results"] is None
            ):
                _local_params["number_of_inference_results"] = 20

            if "raw" in _local_params and _local_params["raw"] is None:
                _local_params["raw"] = 0

            if "time" in _local_params and _local_params["time"] is None:
                _local_params["time"] = ""

            # Validate schema
            _local_params = SchemaGetInferenceresults().load(_local_params)

            _path_params = {
                "device_id": _local_params["device_id"],
            }
            _query_params = {
                "filter": _local_params["filter"],
                "NumberOfInferenceresults": _local_params["number_of_inference_results"],
                "raw": _local_params["raw"],
                "time": _local_params["time"],
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
                    _return_get_inferenceresults = insight_api_instance.get_inference_results(
                        path_params=_path_params, query_params=_query_params
                    )
                    return _return_get_inferenceresults.body

                except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                    _return_get_inferenceresults = self.on_key_error_response(__name__, key_err)
                    return _return_get_inferenceresults

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_get_inferenceresults = self.on_type_error_response(__name__, type_err)
                    return _return_get_inferenceresults

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_get_inferenceresults = self.on_value_error_response(__name__, val_err)
                    return _return_get_inferenceresults

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_get_inferenceresults = self.on_attribute_error_response(
                        __name__, attr_err
                    )
                    return _return_get_inferenceresults

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_get_inferenceresults = self.on_generic_error_response(
                        __name__, exception
                    )
                    return _return_get_inferenceresults

        except ValidationError as err:
            _return_get_inferenceresults = self.on_validation_error_response(__name__, err)
            return _return_get_inferenceresults
