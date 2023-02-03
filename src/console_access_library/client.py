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

import sys
import warnings

warnings.filterwarnings("ignore")
sys.path.append(".")

from console_access_library.ai_model.ai_model import AIModel
from console_access_library.deployment.deployment import Deployment
from console_access_library.device_management.device_management import DeviceManagement
from console_access_library.insight.insight import Insight


class Client:
    """Abstract class for Console Access Library"""

    def __init__(self, config):
        """Constructor Method for Client Abstract class

        Args:
            config (object): Object of Configuration Class
        """
        self.device_management = DeviceManagement(config)
        self.insight = Insight(config)
        self.deployment = Deployment(config)
        self.ai_model = AIModel(config)

    def get_device_management(self):
        """Get Instance that provides DeviceManagement API

        Returns:
            object: Instance that provides the DeviceManagement API
        """
        return self.device_management

    def get_ai_model(self):
        """Get Instance that provides AIModel API

        Returns:
            object: Instance that provides the AIModel API
        """
        return self.ai_model

    def get_deployment(self):
        """Get Instance that provides Deployment API

        Returns:
            object: Instance that provides the Deployment API
        """
        return self.deployment

    def get_insight(self):
        """Get Instance that provides Insight API

        Returns:
            object: Instance that provides the Insight API
        """
        return self.insight
