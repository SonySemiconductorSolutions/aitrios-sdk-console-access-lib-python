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

# pylint:disable=missing-module-docstring
# pylint:disable=import-error
# pylint:disable=too-many-instance-attributes
# pylint:disable=too-many-public-methods
# pylint:disable=duplicate-code
# pylint:disable=wrong-import-position
# pylint:disable=redefined-builtin
# pylint:disable=no-name-in-module
# pylint:disable=global-statement
# pylint:disable=superfluous-parens

import logging
import os
import sys
import warnings
from pathlib import Path

import yaml

warnings.filterwarnings("ignore")
sys.path.append(".")
import console_access_library
from console_access_library.client import Client
from console_access_library.common.config import Config
from console_access_library.common.read_console_access_settings import ReadConsoleAccessSettings

logger = logging.getLogger(console_access_library.LIBRARY_NAME)

PREV_PUBLISH_CALLBACK_STATUS = None

if __name__ == "__main__":
    # Set log label as info
    console_access_library.set_logger(logging.INFO)

    # Set path for Console Access Library Setting File.
    SETTING_FILE_PATH = os.path.join(os.getcwd(), "samples", "console_access_settings.yaml")
    if os.path.exists(SETTING_FILE_PATH):
        # Instantiate Console Access Library ReadConsoleAccessSettings.
        read_console_access_settings_obj = ReadConsoleAccessSettings(SETTING_FILE_PATH)

        # Instantiate Console Access Library Config.
        config_obj = Config(
            read_console_access_settings_obj.console_endpoint,
            read_console_access_settings_obj.portal_authorization_endpoint,
            read_console_access_settings_obj.client_id,
            read_console_access_settings_obj.client_secret,
        )
    else:
        # Instantiate Console Access Library Config.
        config_obj = Config(
            console_endpoint=None,
            portal_authorization_endpoint=None,
            client_id=None,
            client_secret=None,
        )

    # Instantiate Console Access Library Client.
    client_obj = Client(config_obj)

    # Create Instance for DeviceManagement
    device_management_obj = client_obj.get_device_management()

    # Create Instance for AIModel
    ai_model_obj = client_obj.get_ai_model()

    # Create Instance for Deployment
    deployment_obj = client_obj.get_deployment()

    # Create Instance for Insight
    insight_obj = client_obj.get_insight()

    # Set path for Console Access Library Demo Configuration File.
    demo_config_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "demo_config.yaml"
    )

    try:
        # Check if file path is symbolic link
        symbolic_link = Path(demo_config_file_path).is_symlink()
        if symbolic_link is True:
            sys.exit("The path to configuration file is a symbolic link")
        else:
            # Open Demo Configuration in read mode
            with open(demo_config_file_path, "r", encoding="utf-8") as file:
                demo_configuration = yaml.safe_load(file)

    except Exception as err:
        logging.error(str(err))
        logging.error("Configuration not loaded!!")
        raise err

    # Read Demo Configuration Values
    device_id = demo_configuration["demo_configuration"]["device_id"]
    sub_directory_name = demo_configuration["demo_configuration"]["sub_directory_name"]
    number_of_images = demo_configuration["demo_configuration"]["number_of_images"]
    skip = demo_configuration["demo_configuration"]["skip"]
    get_images_order_by = demo_configuration["demo_configuration"]["get_images_order_by"]
    filter = demo_configuration["demo_configuration"]["filter"]
    number_of_inference_results = demo_configuration["demo_configuration"][
        "number_of_inference_results"
    ]
    raw = demo_configuration["demo_configuration"]["raw"]
    time = demo_configuration["demo_configuration"]["time"]
    model_id = demo_configuration["demo_configuration"]["model_id"]
    key = demo_configuration["demo_configuration"]["key"]
    app_name = demo_configuration["demo_configuration"]["app_name"]
    version_number = demo_configuration["demo_configuration"]["version_number"]

    model = demo_configuration["demo_configuration"]["model"]
    compiled_flg = demo_configuration["demo_configuration"]["compiled_flg"]
    file_name = demo_configuration["demo_configuration"]["file_name"]
    get_last_inference_and_image_data_order_by = demo_configuration["demo_configuration"][
        "get_last_inference_and_image_data_order_by"
    ]

    config_id = demo_configuration["demo_configuration"]["config_id"]
    sensor_loader_version_number = demo_configuration["demo_configuration"][
        "sensor_loader_version_number"
    ]
    sensor_version_number = demo_configuration["demo_configuration"]["sensor_version_number"]
    model_version_number = demo_configuration["demo_configuration"]["model_version_number"]
    ap_fw_version_number = demo_configuration["demo_configuration"]["ap_fw_version_number"]

    device_ids = demo_configuration["demo_configuration"]["device_ids"]
    deploy_parameter = demo_configuration["demo_configuration"]["deploy_parameter"]
    comment = demo_configuration["demo_configuration"]["comment"]

    replace_model_id = demo_configuration["demo_configuration"]["replace_model_id"]

    timeout = demo_configuration["demo_configuration"]["timeout"]
    file_content_path = os.path.join(os.getcwd(), "samples", "device_application_file_content.txt")

    def publish_callback(status):
        """Callback for publish model status"""
        global PREV_PUBLISH_CALLBACK_STATUS
        if status != PREV_PUBLISH_CALLBACK_STATUS:
            if status == ai_model_obj.publish_status.BEFORE_CONVERSION.value:
                logger.info("Before Conversion")
            elif status == ai_model_obj.publish_status.CONVERTING.value:
                logger.info("Converting")
            elif status == ai_model_obj.publish_status.CONVERSION_FAILED.value:
                logger.info("Conversion Failed")
            elif status == ai_model_obj.publish_status.CONVERSION_COMPLETE.value:
                logger.info("Conversion Completed")
            elif status == ai_model_obj.publish_status.ADDING_TO_CONFIGURATION.value:
                logger.info("Add To Comfiguration")
            elif status == ai_model_obj.publish_status.ADD_TO_CONFIGURATION_FAILED.value:
                logger.info("Add To Configuration Failed")
            elif status == ai_model_obj.publish_status.ADD_TO_CONFIGURATION_COMPLETE.value:
                logger.info("Add To Configuration Complete")
            elif status == ai_model_obj.publish_status.SAVING.value:
                logger.info("Saving")
            else:
                logger.info("Error")
            PREV_PUBLISH_CALLBACK_STATUS = status
        else:
            print(".", end="", flush=True)

    def deploy_callback(deploy_status_array):
        """Callback for Deploy model status"""

        for _, devices_array in enumerate(deploy_status_array):
            deploy_device_id = list(devices_array.keys())[0]
            status = devices_array[deploy_device_id]["status"]
            if status == deployment_obj.deploy_by_configuration_status_obj.DEPLOYING.value:
                logger.info("Deployment In Progress - %s", deploy_device_id)
            elif status == (deployment_obj.deploy_by_configuration_status_obj.SUCCESSFUL.value):
                logger.info("Deployment Completed - %s", deploy_device_id)
            elif status == (deployment_obj.deploy_by_configuration_status_obj.FAILED.value):
                logger.info("Deployment Failed - %s", deploy_device_id)
            elif status == (deployment_obj.deploy_by_configuration_status_obj.CANCELED.value):
                logger.info("Deployment Canceled - %s", deploy_device_id)
            elif status == (
                deployment_obj.deploy_by_configuration_status_obj.DEVICEAPP_UNDEPLOY.value
            ):
                logger.info("Deployment Undeployed - %s", deploy_device_id)
            else:
                logger.info("Error - %s", deploy_device_id)

    def deploy_device_app_callback(deploy_status_array):
        """Callback for Deploy Device App status"""
        for _, devices_array in enumerate(deploy_status_array):
            deploy_device_id = list(devices_array.keys())[0]
            status = devices_array[deploy_device_id]["status"]
            if status == deployment_obj.deploy_device_app_status_obj.DEPLOYING.value:
                logger.info("Deployment In Progress - %s", deploy_device_id)
            elif status == (deployment_obj.deploy_device_app_status_obj.DEPLOYMENT_DONE.value):
                logger.info("Deployment Completed - %s", deploy_device_id)
            elif status == (deployment_obj.deploy_device_app_status_obj.DEPLOYMENT_FAILED.value):
                logger.info("Deployment Failed - %s", deploy_device_id)
            elif status == (deployment_obj.deploy_device_app_status_obj.DEPLOYMENT_CANCELED.value):
                logger.info("Deployment Canceled - %s", deploy_device_id)
            else:
                logger.info("Error - %s", deploy_device_id)

    # Console Access Library provided API Usage.

    # AIModel - ImportBaseModel
    response = ai_model_obj.import_base_model(model_id, model)
    print("IMPORT BASE MODEL:", response)

    # AIModel - GetModels
    response = ai_model_obj.get_models()
    print("GET MODELS:", response)

    # AIModel - GetBaseModelStatus
    response = ai_model_obj.get_base_model_status(model_id)
    print("GET BASE MODEL STATUS:", response)

    # AIModel - PublishModelWaitModel
    response = ai_model_obj.publish_model_wait_response(model_id, callback=publish_callback)
    print("PUBLISH MODEL WAIT RESPONSE:", response)

    # Deployment - CreateDeployConfiguration
    response = deployment_obj.create_deploy_configuration(
        config_id, model_id=model_id
    )
    print("CREATE DEPLOY CONFIGURATION", response)

    # Deployment - DeployByConfigurationWaitResponse
    response = deployment_obj.deploy_by_configuration_wait_response(
        config_id, device_ids, replace_model_id, callback=deploy_callback
    )
    print("DEPLOY BY CONFIGURATION WAIT RESPONSE", response)

    # Deployment - GetDeployConfigurations
    response = deployment_obj.get_deploy_configurations()
    print("GET DEPLOY CONFIGURATIONS", response)

    # Deployment - GetDeployHistory
    response = deployment_obj.get_deploy_history(device_id)
    print("GET DEPLOY HISTORY", response)

    # Deployment - ImportDeviceApp
    if os.path.exists(file_content_path):
        with open(file_content_path, "r", encoding="utf-8") as file:
            file_content = file.read()
        response = deployment_obj.import_device_app(
            compiled_flg=compiled_flg,
            app_name=app_name,
            version_number=version_number,
            file_name=file_name,
            file_content=file_content,
        )
        print("IMPORT DEVICE APP:", response)

        # Deployment - DeployDeviceAppWaitResponse
        response = deployment_obj.deploy_device_app_wait_response(
            app_name, version_number, device_ids, callback=deploy_device_app_callback
        )
        print("DEPLOY DEVICE APP WAIT RESPONSE", response)

    else:
        print("Please upload the file device_application_file_content.txt")

    # Deployment - GetDeviceApps
    response = deployment_obj.get_device_apps()
    print("GET DEVICE APPS:", response)

    # Deployment - GetDeviceAppDeploys
    response = deployment_obj.get_device_app_deploys(app_name, version_number)
    print("GET DEVICE APP DEPLOYS", response)

    # Deployment - CancelDeployment
    response_get_deploy_history = deployment_obj.get_deploy_history(device_id)
    for i in range(len(response_get_deploy_history["deploys"])):
        if config_id == response_get_deploy_history["deploys"][i]["config_id"]:
            deploy_id = response_get_deploy_history["deploys"][i]["id"]
            break
    response = deployment_obj.cancel_deployment(device_id, str(deploy_id))
    print("CANCEL DEPLOYMENT", response)

    # DeviceManagement - GetDevices
    response = device_management_obj.get_devices()
    print("GET DEVICES:", response)

    # DeviceManagement - StartUploadInferenceResult
    response = device_management_obj.start_upload_inference_result(device_id)
    print("START UPLOAD INFERENCE RESULT:", response)

    # DeviceManagement - StopUploadInferenceResult
    response = device_management_obj.stop_upload_inference_result(device_id)
    print("STOP UPLOAD INFERENCE RESULT:", response)

    # DeviceManagement - GetCommandParameterFile
    response = device_management_obj.get_command_parameter_file()
    print("GET COMMAND PARAMETER FILE:", response)

    # Insight - GetImageDirectories
    response = insight_obj.get_image_directories(device_id)
    print("GET IMAGE DIRECTORIES:", response)

    # Insight - GetImages
    response = insight_obj.get_images(
        device_id,
        sub_directory_name,
    )
    print("GET IMAGES:", response)

    # Insight - GetInferenceResults
    response = insight_obj.get_inference_results(device_id, raw=raw)
    print("GET INFERENCE RESULTS:", response)

    # Insight - GetImageData
    response = insight_obj.get_image_data(
        device_id, sub_directory_name, number_of_images=number_of_images, skip=skip
    )
    print("GET IMAGE DATA:", response)

    # Insight - GetLastInferenceData
    response = insight_obj.get_last_inference_data(device_id)
    print("GET LAST INFERENCE DATA:", response)

    # Insight - GetLastInferenceAndImageData
    response = insight_obj.get_last_inference_and_image_data(device_id, sub_directory_name)
    print("GET LAST INFERENCE AND IMAGE DATA:", response)

    # AIModel - DeleteModel
    response = ai_model_obj.delete_model(model_id)
    print("DELETE MODEL:", response)

    # Deployment - UndeployDeviceApp
    response = deployment_obj.undeploy_device_app(device_ids)
    print("UNDEPLOY DEVICE APP:", response)

    # Deployment - DeleteDeviceApp
    response = deployment_obj.delete_device_app(app_name, version_number)
    print("DELETE DEVICE APP:", response)

    # Deployment - DeleteDeployConfiguration
    response = deployment_obj.delete_deploy_configuration(config_id)
    print("DELETE DEPLOY CONFIGURATION:", response)
