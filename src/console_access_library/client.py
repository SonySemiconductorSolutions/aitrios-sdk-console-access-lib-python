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

import pickle
import sys
import warnings

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.common.logger import Logger
from console_access_library.common.config import Config
from console_access_library.common.error_codes import ErrorCodes
from console_access_library.device_management.device_management import DeviceManagement
from console_access_library.insight.insight import Insight


class Client:
    """Abstract class for Console Access Library"""

    def __init__(self, settings_file_path):
        """Constructor Method for Client Abstract class

        Args:
            settings_file_path (file path): File path for configuration
        """
        config = Config(settings_file_path)
        result = config.read_settings_file()

        if result == ErrorCodes.SUCCESS:
            self.device_management = DeviceManagement(config)
            self.insight = Insight(config)


def set_logger(level=Logger.WARNING):
    """Set log level"""
    log_level = {"CONSOLE_LOG_LEVEL": str(level)}

    with open("log_level.pickle", "wb") as handle:
        pickle.dump(log_level, handle, protocol=pickle.HIGHEST_PROTOCOL)
