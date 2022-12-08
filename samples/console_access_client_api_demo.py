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
# pylint:disable=wrong-import-position
# pylint:disable=redefined-builtin
# pylint:disable=no-name-in-module

import os
import sys
import warnings
from pprint import pprint

import yaml

from console_access_library.client import set_logger
from console_access_library.client import Client
from console_access_library.common.logger import Logger

warnings.filterwarnings("ignore")
sys.path.append(".")


if __name__ == "__main__":

    # Set Log Level
    set_logger(Logger.INFO)

    # Set path for Console Access Library Setting File.
    SETTING_FILE_PATH = os.path.join(os.getcwd(), "samples", "console_access_settings.yaml")

    # Instantiate Console Access Library Client.
    client_obj = Client(SETTING_FILE_PATH)

    # Set path for Console Access Library Demo Configuration File.
    demo_config_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "demo_config.yaml"
    )

    # Open Demo Configuration in read mode
    with open(demo_config_file_path, "r", encoding="utf-8") as file:
        demo_configuration = yaml.safe_load(file)

    # Read Demo Configuration Values
    device_id = demo_configuration["demo_configuration"]["device_id"]
    sub_directory_name = demo_configuration["demo_configuration"]["sub_directory_name"]
    number_of_images = demo_configuration["demo_configuration"]["number_of_images"]
    skip = demo_configuration["demo_configuration"]["skip"]
    get_images_order_by = demo_configuration["demo_configuration"]["get_images_order_by"]
    filter = demo_configuration["demo_configuration"]["filter"]
    number_of_inferenceresults = demo_configuration["demo_configuration"][
        "number_of_inferenceresults"
    ]
    raw = demo_configuration["demo_configuration"]["raw"]
    time = demo_configuration["demo_configuration"]["time"]

    # Console Access Library provided API Usage.

    # DeviceManagement - GetDevices
    response = client_obj.device_management.get_devices()
    pprint(response)

    # DeviceManagement - StartUploadInferenceResult
    response = client_obj.device_management.start_upload_inference_result(device_id)
    pprint(response)

    # DeviceManagement - StopUploadInferenceResult
    response = client_obj.device_management.stop_upload_inference_result(device_id)
    pprint(response)

    # DeviceManagement - GetCommandParameterFile
    response = client_obj.device_management.get_command_parameter_file()
    pprint(response)

    # Insight - GetImageDirectories
    response = client_obj.insight.get_image_directories(device_id)
    pprint(response)

    # Insight - GetImages
    response = client_obj.insight.get_images(
        device_id,
        sub_directory_name,
    )
    pprint(response)

    # Insight - GetInferenceResults
    response = client_obj.insight.get_inference_results(
        device_id,
        raw=raw
    )
    pprint(response)
