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
# pylint:disable=too-many-instance-attributes
# pylint:disable=too-many-public-methods
# pylint:disable=duplicate-code

from console_access_library.common.console_access_base_class import ConsoleAccessBaseClass
from console_access_library.device_management.get_command_parameter_file import GetCommandParameterFile
from console_access_library.device_management.get_devices import GetDevices
from console_access_library.device_management.start_upload_inference_result import (
    StartUploadInferenceResult,
)
from console_access_library.device_management.stop_upload_inference_result import (
    StopUploadInferenceResult,
)


class DeviceManagement(ConsoleAccessBaseClass):
    """Abstract class to access Console Access Library DeviceManagement component
    APIs from devicemanagement component

    Args:
        ConsoleAccessBaseClass (object): Inherited from \
            :class:`~console_access_library.common.ConsoleAccessBaseClass`.
    """

    def __init__(self, config):
        """Constructor Method for DeviceManagement Abstract class

        Args:
            config (object): Object of Configuration Class
        """
        super().__init__()
        self._get_devices_obj = GetDevices(config)
        self._start_upload_inference_result_obj = StartUploadInferenceResult(config)
        self._stop_upload_inference_result_obj = StopUploadInferenceResult(config)
        self._get_command_parameter_file_obj = GetCommandParameterFile(config)

    def get_devices(self, query_params: dict = None):
        """Abstract function call to ``get_devices`` API

        Args:
            query_params (dict, optional): Dictionary of parameters to be passed. Defaults to None

        Returns:
            dict: Dictionary object returned by ``get_devices`` API
        """

        return self._get_devices_obj.get_devices(query_params=query_params)

    def start_upload_inference_result(self, device_id: str):
        """Abstract function call to ``start_upload_inference_result`` API

        Args:
            device_id (str, required): Device ID. No more than 100 characters.

        Returns:
            dict: Dictionary object returned by ``start_upload_inference_result`` API
        """

        return self._start_upload_inference_result_obj.start_upload_inference_result(
            device_id=device_id
        )

    def stop_upload_inference_result(self, device_id: str):
        """Abstract function call to ``stop_upload_inference_result`` API

        Args:
            device_id (str, required): Device ID. No more than 100 characters.

        Returns:
            dict: Dictionary object returned by ``stop_upload_inference_result`` API
        """

        return self._stop_upload_inference_result_obj.stop_upload_inference_result(
            device_id=device_id
        )

    def get_command_parameter_file(self):
        """Abstract function call to ``get_command_parameter_file`` API

        Returns:
            dict: Dictionary object returned by ``get_command_parameter_file`` API
        """

        return self._get_command_parameter_file_obj.get_command_parameter_file()
