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

# pylint:disable=wrong-import-position
# pylint:disable=duplicate-code
# pylint:disable=too-few-public-methods
# pylint:disable=missing-module-docstring
# pylint:disable=import-error
# pylint:disable=missing-function-docstring
# pylint:disable=wrong-import-order
# pylint:disable=raise-missing-from

import logging
import sys
import warnings
from pathlib import Path

import yaml
from marshmallow import Schema, ValidationError, fields

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.error_codes import ErrorCodes

logger = logging.getLogger(__name__)


class SchemaAppConfiguration(Schema):
    """Schema for AppConfiguration

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: string, required : Console access URL
    console_endpoint = fields.String(required=False, missing=None)

    #: string, required : Access token issuance URL required for Console access
    portal_authorization_endpoint = fields.String(required=False, missing=None)

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


class ReadConsoleAccessSettings:
    """This class obtains the configuration details needed for APIs from user."""

    def __init__(self, settings_file_path):
        """Constructor method for config class

        Args:
            settings_file_path (str, required): Path for the app configuration file.
        """
        self._console_endpoint = None
        self._portal_authorization_endpoint = None
        self._client_secret = None
        self._client_id = None
        self._read_settings_file(settings_file_path)

    def _read_settings_file(self, settings_file_path):
        """Read App configuration file for configurations details needed for APIs.

        Returns:
            - "Success" - On Success
            - "Throw exception on event of error occur" - On Error
        """

        _return_value = ErrorCodes.SUCCESS
        _settings = None

        try:
            # Check if file path is symbolic link
            symbolic_link = Path(settings_file_path).is_symlink()
            if symbolic_link is True:
                sys.exit("The path to configuration file is a symbolic link")
            else:
                # Read the Configuration File
                with open(settings_file_path, "r", encoding="utf-8") as file:
                    _yaml_data = yaml.safe_load(file)

                # Validate schema of demo configuration file
                _settings = SchemaAppConfig().load(_yaml_data)
                logger.info("App Configuration loaded successfully!!")

        except ValidationError as err:
            logger.error(str(err.messages))
            logger.error("Configuration not loaded!!")
            raise err

        try:
            if _settings is not None:
                # Read yaml configuration
                self._console_endpoint = _settings["console_access_settings"]["console_endpoint"]
                self._portal_authorization_endpoint = _settings["console_access_settings"][
                    "portal_authorization_endpoint"
                ]
                self._client_secret = _settings["console_access_settings"]["client_secret"]
                self._client_id = _settings["console_access_settings"]["client_id"]

        except KeyError as err:
            logger.error(str(err))
            raise err

        return _return_value

    @property
    def console_endpoint(self):
        return self._console_endpoint

    @property
    def portal_authorization_endpoint(self):
        return self._portal_authorization_endpoint

    @property
    def client_secret(self):
        return self._client_secret

    @property
    def client_id(self):
        return self._client_id
