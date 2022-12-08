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

# pylint:disable=wrong-import-position
# pylint:disable=duplicate-code
# pylint:disable=too-few-public-methods
# pylint:disable=missing-module-docstring
# pylint:disable=import-error
# pylint:disable=missing-function-docstring
# pylint:disable=wrong-import-order

import json
import os
import sys
import warnings

import aitrios_console_rest_client_sdk_primitive
import requests
import yaml
from marshmallow import Schema, ValidationError, fields

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.error_codes import ErrorCodes
from console_access_library.common.logger import Logger


class SchemaAppConfiguration(Schema):
    """Schema for AppConfiguration

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: string, required : Console access URL
    base_url = fields.String(required=False, missing=None)

    #: string, required : Access token issuance URL required for Console access
    token_url = fields.String(required=False, missing=None)

    #: string, required : Client ID required to issue an access token
    client_secret = fields.String(required=False, missing=None)

    #: string, required : Client Secret required to issue an access token
    client_id = fields.String(required=False, missing=None)


class SchemaAppConfig(Schema):
    """Schema for AppConfiguration

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: app_configuration : Nested AppConfiguration schema
    console_access_settings = fields.Nested(SchemaAppConfiguration())


class Config:
    """This class obtains the configuration details needed for APIs from user."""

    def __init__(self, settings_file_path):
        """Constructor method for config class

        Args:
            settings_file_path (str, required): Path for the app configuration file.
        """
        self.base_url = None
        self.configuration = None

        self._token_url = None
        self._client_secret = None
        self._client_id = None
        self._settings_file_path = settings_file_path
        self.logger = Logger().set_logger()

    def read_settings_file(self):
        """Read App configuration file for configurations details needed for APIs.

        Returns:
            - "Success" - On Success
            - "Generic Error" - If an error occurs when reading the configuration file
        """

        _return_value = ErrorCodes.SUCCESS
        _settings = None

        try:
            # Read the Configuration File
            with open(self._settings_file_path, "r", encoding="utf-8") as file:
                _yaml_data = yaml.safe_load(file)

                # Validate schema of demo configuration file
                _settings = SchemaAppConfig().load(_yaml_data)
                self.logger.info("App Configuration loaded successfully!!")

        except ValidationError as err:
            self.logger.error(str(err.messages))
            self.logger.error("Configuration not loaded!!")
            _return_value = ErrorCodes.GENERIC_ERROR

        try:
            if _settings is not None:

                # Store yaml configuration
                self.base_url = _settings["console_access_settings"]["base_url"]
                if self.base_url is None:
                    self.base_url = os.environ.get("BASE_URL")

                self._token_url = _settings["console_access_settings"]["token_url"]
                if self._token_url is None:
                    self._token_url = os.environ.get("TOKEN_URL")

                self._client_secret = _settings["console_access_settings"]["client_secret"]
                if self._client_secret is None:
                    self._client_secret = os.environ.get("CLIENT_SECRET")

                self._client_id = _settings["console_access_settings"]["client_id"]
                if self._client_id is None:
                    self._client_id = os.environ.get("CLIENT_ID")

                # Set configuration parameters.
                self.configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
                    host=self.base_url
                )

        except KeyError as err:
            self.logger.error(str(err))
            _return_value = ErrorCodes.GENERIC_ERROR

        return _return_value

    def get_access_token(self):
        """Get Access Token from Token Server needed for API.

        Returns:
            - "__access_token_str__" - On Success
            - "Generic Error" - If an error occurs when obtaining an access token
        """

        _return_value = ErrorCodes.SUCCESS

        try:
            # Set headers
            _headers = {
                "Content-Type": "application/x-www-form-urlencoded",
            }

            # Set payload
            _data = {
                "grant_type": "client_credentials",
                "client_secret": self._client_secret,
                "scope": "system",
                "client_id": self._client_id,
            }

            # Create an instance of the API class
            _response = requests.post(
                url=self._token_url, headers=_headers, data=_data, timeout=180
            )
            _response_json = _response.json()
            _return_value = "bearer " + _response_json["access_token"]

        except requests.exceptions.HTTPError as ex:
            self.logger.error(str(ex.response.text))
            _return_value = ErrorCodes.GENERIC_ERROR

        return _return_value

    def _get_access_token(self):
        _access_token = None
        _headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        _data = {
            "grant_type": "client_credentials",
            "client_secret": self._client_secret,
            "scope": "system",
            "client_id": self._client_id,
        }
        print(_headers)
        print(_data)
        print(self._token_url)

        with aitrios_console_rest_client_sdk_primitive.ApiClient() as _api_client:
            # Create an instance of the API class
            _response = _api_client.rest_client.request(
                url=self._token_url, method="POST", headers=_headers, body=_data
            )
            _response_json = json.loads(_response.data)
            print(_response_json)
            _access_token = "bearer " + _response_json["access_token"]

        return _access_token
