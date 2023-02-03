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

from enum import IntEnum


class ErrorCodes(IntEnum):
    """Class to check error status code

    Args:
        IntEnum(object): Inherited from class enum
    """

    def __new__(cls, value, phrase, description=""):
        obj = int.__new__(cls, value)
        obj._value_ = value

        obj.phrase = phrase
        obj.description = description
        return obj

    SUCCESS = (0, "Success")
    ERROR = (1, "E001")
    GENERIC_ERROR = (2, "Generic Error")
    KEY_ERROR = (3, "Key Error")
    TYPE_ERROR = (4, "Type Error")
    ATTRIBUTE_ERROR = (5, "Attribute Error")
    VALUE_ERROR = (6, "Value Error")
