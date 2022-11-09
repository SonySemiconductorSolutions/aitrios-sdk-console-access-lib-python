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
# pylint:disable=unused-import

import sys
import warnings

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.error_codes import ErrorCodes


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

    def on_validation_error_response(self, module_name, error):
        """Prepares response dictionary on schema validation error.

        Args:
            module_name (string): Name of the module in which validation error encountered.
            error (string): Error message.

        Returns:
            dict: Dictionary object
        """

        _return_on_validation_error_response = {
            "message": (
                f"{module_name}: {self.error_codes.ERROR.phrase} :{str(str(error.messages))}"
            ),
            "error_code": self.error_codes.ERROR.phrase,
        }
        return _return_on_validation_error_response

    def on_generic_error_response(self, module_name, exception):
        """Prepares response dictionary using the on schema generic error.

        Args:
            module_name (string): Name of the module in which generic error encountered.
            exception (object): Error object.

        Returns:
            dict: Dictionary object
        """

        _return_on_generic_error_response = {
            "message": (
                f"{module_name}: {self.error_codes.GENERIC_ERROR.phrase} :{str(exception.body)}"
            ),
            "error_code": self.error_codes.GENERIC_ERROR.phrase,
        }
        return _return_on_generic_error_response

    def on_key_error_response(self, module_name, key_err):
        """Prepares response dictionary on api key error.

        Args:
            module_name (string): Name of the module in which key error encountered.
            error (string): Error message.

        Returns:
            dict: Dictionary object
        """

        _return_on_key_error_response = {
            "message": f"{module_name}: {self.error_codes.KEY_ERROR.phrase} :{str(key_err)}",
            "error_code": self.error_codes.KEY_ERROR.phrase,
        }
        return _return_on_key_error_response

    def on_type_error_response(self, module_name, type_error):
        """Prepares response dictionary on api type error.

        Args:
            module_name (string): Name of the module in which type error encountered.
            error (string): Error message.

        Returns:
            dict: Dictionary object
        """

        _return_on_type_error_response = {
            "message": f"{module_name}: {self.error_codes.TYPE_ERROR.phrase} :{str(type_error)}",
            "error_code": self.error_codes.TYPE_ERROR.phrase,
        }
        return _return_on_type_error_response

    def on_attribute_error_response(self, module_name, attr_err):
        """Prepares response dictionary on api attribute error.

        Args:
            module_name (string): Name of the module in which attribute error encountered.
            error (string): Error message.

        Returns:
            dict: Dictionary object
        """

        _return_on_attribute_error_response = {
            "message": f"{module_name}: {self.error_codes.ATTRIBUTE_ERROR.phrase} :{str(attr_err)}",
            "error_code": self.error_codes.ATTRIBUTE_ERROR.phrase,
        }
        return _return_on_attribute_error_response

    def on_value_error_response(self, module_name, val_err):
        """Prepares response dictionary on api value error.

        Args:
            module_name (string): Name of the module in which value error encountered.
            error (string): Error message.

        Returns:
            dict: Dictionary object
        """

        _return_on_value_error_response = {
            "message": f"{module_name}: {self.error_codes.VALUE_ERROR.phrase} :{str(val_err)}",
            "error_code": self.error_codes.VALUE_ERROR.phrase,
        }
        return _return_on_value_error_response
