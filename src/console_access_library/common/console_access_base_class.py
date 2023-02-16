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
# pylint:disable=unused-import
# pylint:disable=broad-except

import json
import logging
import sys
import warnings

warnings.filterwarnings("ignore")
sys.path.append(".")

from datetime import datetime

from marshmallow import Schema, ValidationError, fields, validates_schema

from console_access_library.common.error_codes import ErrorCodes

logger = logging.getLogger(__name__)


class SchemaErrorResponse(Schema):
    """Schema for Validating HTTP Error Response

    Args:
        Schema (object): Inherited from Schema class of marshmallow

    """

    #: str, required : Result
    result = fields.String(required=True, error_messages={"invalid": "Invalid string for result"})

    #: str, required : Code
    code = fields.String(required=True, error_messages={"invalid": "Invalid string for code"})

    #: str, required : Message
    message = fields.String(required=True, error_messages={"invalid": "Invalid string for message"})

    #: str, required : Time
    time = fields.String(required=True, error_messages={"invalid": "Invalid string for time"})


class ConsoleAccessBaseClass:
    """ConsoleAccessBaseClass"""

    def __init__(self):
        """Constructor Method for ConsoleAccessBaseClass"""
        self.error_codes = ErrorCodes

    def _error_message(self, message, schema_params):
        """This function return error message for invalid schema

        Args:
            message(str): error message
            schema_params(schema): schema which was invalid

        Returns:
            str: error message
        """
        error_message = f"\n\t{message} schema = {schema_params}"
        return error_message

    def _get_date_time(self):
        """Returns current date time in string format"""
        _current_time = datetime.now()
        return _current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    def on_validation_error_response(self, module_name, error):
        """Prepares response dictionary on schema validation error.

        Args:
            module_name (string): Name of the module in which validation error encountered.
            error (string): Error message.

        Returns:
            dict: Dictionary object
        """

        logger.debug("Validation Error %s", module_name)
        _return_on_validation_error_response = {
            "result": "ERROR",
            "message": str(error.messages),
            "code": self.error_codes.ERROR.phrase,
            "datetime": self._get_date_time(),
        }
        return _return_on_validation_error_response

    def on_generic_error_response(self, module_name, exception=None, message=None):
        """Prepares response dictionary using the on schema generic error.

        Args:
            module_name (str): Name of the module in which generic error encountered.
            exception (object): Error object.
            message (str): Message string from the API.

        Returns:
            dict: Dictionary object
        """

        logger.debug("Generic Error %s", module_name)
        message_data = None
        if message:
            message_data = message

        if exception:
            message_data = str(exception)

        _return_on_generic_error_response = {
            "result": "ERROR",
            "message": str(message_data),
            "code": self.error_codes.GENERIC_ERROR.phrase,
            "datetime": self._get_date_time(),
        }
        return _return_on_generic_error_response

    def on_key_error_response(self, module_name, key_err):
        """Prepares response dictionary on api key error.

        Args:
            module_name (string): Name of the module in which key error encountered.
            key_err (string): Error message.

        Returns:
            dict: Dictionary object
        """

        logger.debug("Key Error %s", module_name)
        _return_on_key_error_response = {
            "result": "ERROR",
            "message": str(key_err.messages),
            "code": self.error_codes.KEY_ERROR.phrase,
            "datetime": self._get_date_time(),
        }
        return _return_on_key_error_response

    def on_type_error_response(self, module_name, type_error):
        """Prepares response dictionary on api type error.

        Args:
            module_name (string): Name of the module in which type error encountered.
            type_error (string): Error message.

        Returns:
            dict: Dictionary object
        """

        logger.debug("Type Error %s", module_name)
        _return_on_type_error_response = {
            "result": "ERROR",
            "message": str(type_error),
            "code": self.error_codes.TYPE_ERROR.phrase,
            "datetime": self._get_date_time(),
        }
        return _return_on_type_error_response

    def on_attribute_error_response(self, module_name, attr_err):
        """Prepares response dictionary on api attribute error.

        Args:
            module_name (string): Name of the module in which attribute error encountered.
            attr_err (string): Error message.

        Returns:
            dict: Dictionary object
        """

        logger.debug("Attribute Error %s", module_name)
        _return_on_attribute_error_response = {
            "result": "ERROR",
            "message": str(attr_err.messages),
            "code": self.error_codes.ATTRIBUTE_ERROR.phrase,
            "datetime": self._get_date_time(),
        }
        return _return_on_attribute_error_response

    def on_value_error_response(self, module_name, val_err):
        """Prepares response dictionary on api value error.

        Args:
            module_name (string): Name of the module in which value error encountered.
            val_err (string): Error message.

        Returns:
            dict: Dictionary object
        """

        logger.debug("Value Error %s", module_name)
        _return_on_value_error_response = {
            "result": "ERROR",
            "message": str(val_err.messages),
            "code": self.error_codes.VALUE_ERROR.phrase,
            "datetime": self._get_date_time(),
        }
        return _return_on_value_error_response

    def on_http_error_response(self, module_name, http_error):
        """Prepares response dictionary on api http error.

        Args:
            module_name (string): Name of the module in which value error encountered.
            http_error (string): Error message.

        Returns:
            dict: Dictionary object
        """

        logger.debug("Http Error %s", module_name)
        try:
            http_error_json = json.loads(http_error.body)
            _return_on_http_error_response = SchemaErrorResponse().load(http_error_json)

        except Exception as ex:
            _return_on_http_error_response = self.on_generic_error_response(
                module_name, exception=ex
            )

        return _return_on_http_error_response
