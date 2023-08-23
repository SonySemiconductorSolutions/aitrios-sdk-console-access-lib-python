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
# pylint:disable=too-many-locals
# pylint:disable=invalid-name
# pylint:disable=broad-except
# pylint:disable=too-many-branches

import logging
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
from aitrios_console_rest_client_sdk_primitive.apis.tags import manage_devices_api
from marshmallow import Schema, ValidationError, fields, validates_schema

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass

logger = logging.getLogger(__name__)


class SchemaGetDevices(Schema):
    """Schema for GetDevices API.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, optional : Edge AI Device ID
    device_id = fields.String(
        required=False, error_messages={"invalid": "Invalid string for device_id"}, strict=True
    )

    #: str, optional : Edge AI device name
    device_name = fields.String(
        required=False, error_messages={"invalid": "Invalid string for device_name"}, strict=True
    )

    #: str, optional : Connection status.
    connection_state = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for connection_state"},
        strict=True,
    )

    #: str, optional : Affiliated Edge AI device group
    device_group_id = fields.String(
        required=False,
        error_messages={"invalid": "Invalid string for device_group_id"},
        strict=True,
    )

    @validates_schema
    def validate(self, data, **kwargs):
        if "device_id" in data and (
            data["device_id"] is None or str(data["device_id"]).strip() == ""
        ):
            raise ValidationError("device_id is required or can't be empty string")

        if "device_name" in data and (
            data["device_name"] is None or str(data["device_name"]).strip() == ""
        ):
            raise ValidationError("device_name is required or can't be empty string")

        if "connection_state" in data and (
            data["connection_state"] is None or str(data["connection_state"]).strip() == ""
        ):
            raise ValidationError("connection_state is required or can't be empty string")

        if "device_group_id" in data and (
            data["device_group_id"] is None or str(data["device_group_id"]).strip() == ""
        ):
            raise ValidationError("device_group_id is required or can't be empty string")


class GetDevices(ConsoleAccessBaseClass):
    """This class implements GetDevices API.

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for the class GetDevices

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._config = config

    def get_devices(
        self,
        device_id: str = None,
        device_name: str = None,
        connection_state: str = None,
        device_group_id: str = None,
    ):
        """Get device list information.

        Args:
            device_id (str, optional) : Edge AI Device ID. Partial search, case insensitive.\
                Search all device_ids if not specified.
            device_name (str, optional) : Edge AI device name.\
                Partial search, case insensitive.\
                If not specified, search all device_names.
            connection_state (str, optional) : Connection status.\
                For connected state: Connected\
                Disconnected state: Disconnected\
                Exact match search, case insensitive.\
                If not specified, search all connection_states.
            device_group_id (str, optional) : Affiliated Edge AI device group.\
                Exact match search, case insensitive.\
                Search all device_group_id if not specified.

        Returns:
            **Return Type**

            - On Success Response - aitrios_console_rest_client_sdk_primitive.schemas.DynamicSchema
            - On Error Response - dict

            **Success Response Schema**

                +------------+--------------------+-----------+--------------------------------+
                | *Level1*   | *Level2*           |*Type*     | *Description*                  |
                +------------+--------------------+-----------+--------------------------------+
                | ``devices``|                    |``array``  | The subordinate elements are   |
                |            |                    |           | listed in ascending order by   |
                |            |                    |           | device ID                      |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``device_id``      |``string`` | Set the device ID              |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``place``          |``string`` | Set the location               |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``comment``        |``string`` | Set the device description     |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``property``       |``string`` | Set device properties          |
                |            |                    |           | (device_name, etc.)            |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``ins_id``         |``string`` | Set the creator of the device  |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``ins_date``       |``string`` | Set the date and               |
                |            |                    |           | time the device was created.   |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``upd_id``         |``string`` | Set up an updater for          |
                |            |                    |           | your device                    |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``upd_date``       |``string`` | Set the date and time          |
                |            |                    |           | of the device update.          |
                +------------+--------------------+-----------+--------------------------------+
                |            |``connectionState`` |``string`` | Set the connection status      |
                |            |                    |           | of the device.                 |
                +------------+--------------------+-----------+--------------------------------+
                |            |``lastActivityTime``|``string`` | Set the last connection date   |
                |            |                    |           | and time of the device.        |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``device_groups``  |``array``  | Refer :ref:`device_groups <dg>`|
                |            |                    |           | for more details               |
                +------------+--------------------+-----------+--------------------------------+
                |            | ``models``         |``array``  | Refer :ref:`models <model>`    |
                |            |                    |           | for more details               |
                +------------+--------------------+-----------+--------------------------------+

                +-------------------+--------------------+------------+--------------------------+
                | device_groups     | .. _dg:                                                    |
                +-------------------+--------------------+------------+--------------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*            |
                +-------------------+--------------------+------------+--------------------------+
                | ``device_groups`` |                    | ``array``  | The subordinate          |
                |                   |                    |            | elements are listed      |
                |                   |                    |            | in ascending order       |
                |                   |                    |            | by device group ID       |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_group_id`` | ``string`` | Set the device group ID  |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``device_type``     | ``string`` | Set the device type      |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``comment``        |``string``  | Set the device           |
                |                   |                    |            | bdescription             |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``ins_id``         |``string``  | Set the date and time    |
                |                   |                    |            | that the device group    |
                |                   |                    |            | was created.             |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``ins_date``       |``string``  | Set the creator of the   |
                |                   |                    |            | device group.            |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``upd_id``         |``string``  | Set the updater for      |
                |                   |                    |            | the device group         |
                +-------------------+--------------------+------------+--------------------------+
                |                   | ``upd_date``       |``string``  | Set the date and time of |
                |                   |                    |            | the device group update. |
                +-------------------+--------------------+------------+--------------------------+

                +-------------------+--------------------+------------+--------------------------+
                | models            | .. _model:                                                 |
                +-------------------+--------------------+------------+--------------------------+
                | *Level1*          | *Level2*           | *Type*     | *Description*            |
                +-------------------+--------------------+------------+--------------------------+
                | ``models``        |                    | ``array``  | The subordinate          |
                |                   |                    |            | elements are listed      |
                |                   |                    |            | in ascending order       |
                |                   |                    |            | by device group ID       |
                +-------------------+--------------------+------------+--------------------------+
                |                   |``model_version_id``| ``string`` | Set the model version ID |
                |                   |                    |            | Format: ModelID:v1.0001  |
                |                   |                    |            | * If DnnModelVersion does|
                |                   |                    |            | not exist in the DB, the |
                |                   |                    |            | network_id is displayed. |
                |                   |                    |            | Example) 0201020002370200|
                |                   |                    |            | In the above case, 000237|
                |                   |                    |            | (7~12 digits) If it is 16|
                |                   |                    |            | digits,it is displayed   |
                |                   |                    |            | as is.                   |
                +-------------------+--------------------+------------+--------------------------+

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

                # Create Instance for DeviceManagement
                device_management_obj = client_obj.get_device_management()

                # DeviceManagement - GetDevices
                response = device_management_obj.get_devices(
                    device_id,
                    device_name,
                    connection_state,
                    device_group_id
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
            if "device_id" in _local_params and _local_params["device_id"] is None:
                del _local_params["device_id"]

            if "device_name" in _local_params and _local_params["device_name"] is None:
                del _local_params["device_name"]

            if "connection_state" in _local_params and _local_params["connection_state"] is None:
                del _local_params["connection_state"]

            if "device_group_id" in _local_params and _local_params["device_group_id"] is None:
                del _local_params["device_group_id"]

            # Validate schema
            _query_params = SchemaGetDevices().load(_local_params)

            # Update the connectionState in query params with connection_state from _local_params
            if "connection_state" in _local_params and "connection_state" in _query_params:
                del _query_params["connection_state"]
                _query_params["connectionState"] = _local_params["connection_state"]
            logger.info(_query_params)

            # Enter a context with an instance of the API client
            with aitrios_console_rest_client_sdk_primitive.ApiClient(
                self._config.configuration,
                header_name="Authorization",
                header_value=self._config.get_access_token(),
            ) as api_client:
                # Create an instance of the API class
                manage_devices_api_instance = manage_devices_api.ManageDevicesApi(api_client)
                try:
                    _return_get_devices = manage_devices_api_instance.get_devices(_query_params)
                    return _return_get_devices.body

                except aitrios_console_rest_client_sdk_primitive.ApiKeyError as key_err:
                    _return_get_devices = self.on_key_error_response(__name__, key_err)

                except aitrios_console_rest_client_sdk_primitive.ApiTypeError as type_err:
                    _return_get_devices = self.on_type_error_response(__name__, type_err)

                except aitrios_console_rest_client_sdk_primitive.ApiValueError as val_err:
                    _return_get_devices = self.on_value_error_response(__name__, val_err)

                except aitrios_console_rest_client_sdk_primitive.ApiAttributeError as attr_err:
                    _return_get_devices = self.on_attribute_error_response(__name__, attr_err)

                except aitrios_console_rest_client_sdk_primitive.ApiException as exception:
                    _return_get_devices = self.on_http_error_response(__name__, exception)

                except Exception as exception:
                    _return_get_devices = self.on_generic_error_response(__name__, exception)

        except ValidationError as err:
            _return_get_devices = self.on_validation_error_response(__name__, err)

        return _return_get_devices
