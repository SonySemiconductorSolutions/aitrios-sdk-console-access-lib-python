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
# pylint:disable=too-many-arguments
# pylint:disable=broad-except
# pylint:disable=unused-argument
# pylint:disable=broad-exception-raised


import logging
import os
import sys
import time
import warnings
from enum import Enum

import aitrios_console_rest_client_sdk_primitive
import jwt
import requests
from marshmallow import Schema, ValidationError, fields, validates_schema
from urllib3 import util
from urllib.parse import urlparse

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.error_codes import ErrorCodes
from console_access_library.third_party.ocsp_checker import ocspchecker

logger = logging.getLogger(__name__)


class SchemaConsoleAccessSettingsConfiguration(Schema):
    """Schema for ConsoleAccessSettingsConfiguration.

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: string, required : Console access URL
    console_endpoint = fields.String(
        required=True,
        error_messages={"invalid": "Invalid string for console_endpoint"},
        strict=True,
    )

    #: string, required : Access token issuance URL required for Console access
    portal_authorization_endpoint = fields.String(
        required=True,
        error_messages={"invalid": "Invalid string for portal_authorization_endpoint"},
        strict=True,
    )

    #: string, required : Client ID required to issue an access token
    client_secret = fields.String(
        required=True, error_messages={"invalid": "Invalid string for client_secret"}, strict=True
    )

    #: string, required : Client Secret required to issue an access token
    client_id = fields.String(
        required=True, error_messages={"invalid": "Invalid string for client_id"}, strict=True
    )

    @validates_schema
    def validate(self, data, **_):
        if str(data["console_endpoint"]).strip() == "":
            raise ValidationError("console_endpoint is required")

        if str(data["portal_authorization_endpoint"]).strip() == "":
            raise ValidationError("portal_authorization_endpoint is required")

        if str(data["client_secret"]).strip() == "":
            raise ValidationError("client_secret is required")

        if str(data["client_id"]).strip() == "":
            raise ValidationError("client_id is required")


class TokenValidationEnum(Enum):
    """Access Token Validation Status Enum Value"""

    VALID_TOKEN = "00"
    TOKEN_EXPIRED = "01"
    INVALID_TOKEN = "02"
    EMPTY_TOKEN = "03"


class Config:
    """This class obtains the configuration details needed for APIs from user."""

    def __init__(
        self,
        console_endpoint: str = None,
        portal_authorization_endpoint: str = None,
        client_id: str = None,
        client_secret: str = None,
    ):
        """Constructor method for config class

        Args:
            console_endpoint (str, optional): Console access URL.
            If not specified, read from environment variables.

            portal_authorization_endpoint (str, optional): Access token issuance URL
            required for console access.
            If not specified, read from environment variables.

            client_id (str, optional): Client ID required to issue an access token.
            If not specified, read from environment variables.

            client_secret (str, optional): Client Secret required to issue an access token.
            If not specified, read from environment variables.
        """
        self._console_endpoint = console_endpoint
        self._portal_authorization_endpoint = portal_authorization_endpoint
        self._client_secret = client_secret
        self._client_id = client_id
        self._save_last_access_token = None
        self._proxy = None

        #  If not specified, read from environment variables.
        if self._console_endpoint is None:
            self._console_endpoint = os.environ.get("CONSOLE_ENDPOINT")

        if self._portal_authorization_endpoint is None:
            self._portal_authorization_endpoint = os.environ.get("PORTAL_AUTHORIZATION_ENDPOINT")

        if self._client_secret is None:
            self._client_secret = os.environ.get("CLIENT_SECRET")

        if self._client_id is None:
            self._client_id = os.environ.get("CLIENT_ID")

        # Validate Console Access Setting Configuration Parameters
        self.validate_config_parameters(
            self._console_endpoint,
            self._portal_authorization_endpoint,
            self._client_secret,
            self._client_id,
        )

        # Read Proxy from environment
        self._proxy = self.get_https_proxy()

        # Set configuration parameters.
        self.configuration = aitrios_console_rest_client_sdk_primitive.Configuration(
            host=self._console_endpoint, 
            proxy=self._proxy,
            proxy_headers=self.get_proxy_auth_header(self._proxy)
        )

    def validate_config_parameters(
        self,
        console_endpoint: str,
        portal_authorization_endpoint: str,
        client_id: str,
        client_secret: str,
    ):
        """
        Validation for Console Access Setting Configuration Parameters.

        Returns:
            - "Throw exception on event of error occur" - On Error
        """

        try:
            # delete local argument 'self' form locals() for validation.
            _local_params = locals()
            if "self" in _local_params:
                del _local_params["self"]

            # Validate schema
            SchemaConsoleAccessSettingsConfiguration().load(_local_params)

        except Exception as ex:
            logger.error(str(ex))
            raise ex

    def get_https_proxy(self):
        """
        Get proxy setting from environment variable

        Returns:
            - "__proxy_str__" - Proxy string
        """

        proxy_env_var = "https_proxy"
        return os.environ.get(proxy_env_var) or os.environ.get(proxy_env_var.upper())

    def get_proxy_auth_header(self, proxy=None):
        """Get proxy headers for authorization

        Args:
            - Proxy string
        Returns:
            - Proxy headers for proxy_basic_auth
        """
        if proxy is None:
            return None

        parsed_proxy = urlparse(proxy)
        if parsed_proxy.username and parsed_proxy.password is not None:
            return util.make_headers(
                proxy_basic_auth=f"{parsed_proxy.username}:{parsed_proxy.password}")
        return None

    def validate_access_token(self, access_token: str):
        """Function to Validate Access Token

        Args:
            access_token (str): Access Token for Authentication

        Returns:
            str : Enum value

                - "00" for Valid Token
                - "01" for Token expired
                - "02" for Invalid token.
                - "03" for Empty token.
        """
        # Check if access token is Empty
        if access_token is not None:
            try:
                access_token = access_token.split(" ")[1]
                decoded_access_token = jwt.decode(access_token, options={"verify_signature": False})
                exp = decoded_access_token.get("exp")
                if exp - round(time.time()) <= 180 or exp < time.time():
                    logger.debug("Less than 3 mins for Token Expiry or Token Already expired")
                    return TokenValidationEnum.TOKEN_EXPIRED.value
            except Exception as ex:
                logger.debug("Invalid AccessToken %s", ex)
                return TokenValidationEnum.INVALID_TOKEN.value
        else:
            return TokenValidationEnum.EMPTY_TOKEN.value

        return TokenValidationEnum.VALID_TOKEN.value

    def _get_ocsp_status(self, host_url):
        """Get OCSP status for the host_url"""
        retval = False
        try:
            result = ocspchecker.get_ocsp_status(host=host_url, proxy=self.get_https_proxy())
            if result[2] == "OCSP Status: GOOD":
                retval = True
        except Exception as ex:
            logger.error(str(ex))
        return retval

    def _get_access_token(
        self,
    ):
        """Get Access Token from Token Server needed for API.

        Returns:
            - "__access_token_str__" - On Success
            - "Throw exception on event of error occur" - On Error
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
                url=self._portal_authorization_endpoint, headers=_headers, data=_data, timeout=180
            )
            _response_json = _response.json()
            _return_value = "bearer " + _response_json["access_token"]

        except Exception as ex:
            logger.error(str(ex))
            raise ex

        return _return_value

    def get_access_token(
        self,
    ):
        """Check if access token is available or not, and check its validity.

        Returns:
            - "__access_token_str__" - On Success
            - "Generic Error" - If an error occurs when obtaining an access token

            - Throws error if OCSP status "is not good" for any of the URLs(console_endpoint or \
                    portal_authorization_endpoint)
        """

        _validation_code = self.validate_access_token(self._save_last_access_token)
        # If the Access token variable has a token, check the validity of the token,
        # if expired or invalid or empty token found generate new access token
        if _validation_code in [
            TokenValidationEnum.TOKEN_EXPIRED.value,
            TokenValidationEnum.INVALID_TOKEN.value,
            TokenValidationEnum.EMPTY_TOKEN.value

        ]:
            # To avoid multiple OCSP request, check OCSP status for _console_endpoint
            # and _portal_authorization_endpoint when requesting for access token
            # verify revocation of certificate before urllib3 request,
            _console_endpoint_ocsp_status = self._get_ocsp_status(self._console_endpoint)
            _portal_authorization_endpoint_ocsp_status = self._get_ocsp_status(
                self._portal_authorization_endpoint
            )
            if not _console_endpoint_ocsp_status:
                raise Exception(f"OCSP Status of URL {self._console_endpoint} is not good")

            if not _portal_authorization_endpoint_ocsp_status:
                raise Exception(
                    f"OCSP Status of URL {self._portal_authorization_endpoint} is not good")

            self._save_last_access_token = self._get_access_token()

        # Return the access token stored the Access token variable
        return self._save_last_access_token
