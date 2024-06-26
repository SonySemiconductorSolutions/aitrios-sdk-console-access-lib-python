# ------------------------------------------------------------------------
# Copyright 2022, 2023, 2024 Sony Semiconductor Solutions Corp. All rights reserved.

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
import base64
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

        if read_console_access_settings_obj.application_id is not None:
            # Instantiate Azure Config.
            config_obj = Config(
                console_endpoint=read_console_access_settings_obj.console_endpoint,
                portal_authorization_endpoint=read_console_access_settings_obj.portal_authorization_endpoint,
                client_id=read_console_access_settings_obj.client_id,
                client_secret=read_console_access_settings_obj.client_secret,
                application_id=read_console_access_settings_obj.application_id
            )
            APPLICATION_ID_FLG = True
        else:
            # Instantiate Console Access Library Config.
            config_obj = Config(
                console_endpoint=read_console_access_settings_obj.console_endpoint,
                portal_authorization_endpoint=read_console_access_settings_obj.portal_authorization_endpoint,
                client_id=read_console_access_settings_obj.client_id,
                client_secret=read_console_access_settings_obj.client_secret,
                application_id=None,
            )
    else:
        # Instantiate Console Access Library Config.
        config_obj = Config(
            console_endpoint=None,
            portal_authorization_endpoint=None,
            client_id=None,
            client_secret=None,
            application_id=None,
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
                yaml_content = yaml.safe_load(file)
                if "demo_configuration" in yaml_content:
                    demo_configuration = yaml_content["demo_configuration"]

    except Exception as err:
        logging.error(str(err))
        logging.error("Configuration not loaded!!")
        raise err

    # Read Demo Configuration Values
    device_id = demo_configuration["device_id"]
    model_id = demo_configuration["model_id"]
    model = demo_configuration["model"]
    config_id = demo_configuration["config_id"]
    app_name = demo_configuration["app_name"]
    sub_directory_name = demo_configuration["sub_directory_name"]
    version_number = demo_configuration["version_number"]
    file_content_name = demo_configuration["file_content_name"]
    file_content_path = os.path.join("samples",file_content_name)
    if not os.path.exists(file_content_path):
        logging.error("file_content_name is not exist.")
        sys.exit(1)

    if os.path.islink(file_content_path):
        logging.error("Can't open symbolic link file.")
        sys.exit(1)
    
    with open(file_content_path,"rb") as file:
        file_encode_content = base64.b64encode(file.read())
        file_content = file_encode_content.decode('utf-8')

    if file_content_name.endswith(".aot"):
       compiled_flg = "1"
    elif file_content_name.endswith(".wasm"):
       compiled_flg = "0"
    else :
        logging.error("The extension of file_content_name is not appropriate.")
        sys.exit(1)

    get_model_device_id = demo_configuration.get("get_model_device_id", None)
    publish_model_wait_response_device_id = demo_configuration.get("publish_model_wait_response_device_id", None)
    vendor_name = demo_configuration.get("vendor_name", None)
    converted = demo_configuration.get("converted", None)
    comment = demo_configuration.get("comment", None)
    input_format_param = demo_configuration.get("input_format_param", None)
    network_config = demo_configuration.get("network_config", None)
    network_type = demo_configuration.get("network_type", None)
    metadata_format_id = demo_configuration.get("metadata_format_id", None)
    project_name = demo_configuration.get("projnumber_of_imagesect_name", None)
    model_platform = demo_configuration.get("model_platform", None)
    project_type = demo_configuration.get("project_type", None)
    latest_type = demo_configuration.get("latest_type", None)
    sensor_loader_version_number = demo_configuration.get("sensor_loader_version_number", None)
    sensor_version_number = demo_configuration.get("sensor_version_number", None)
    model_version_number = demo_configuration.get("model_version_number", None)
    ap_fw_version_number = demo_configuration.get("ap_fw_version_number", None)
    device_ids = demo_configuration.get("device_ids", device_id)
    replace_model_id = demo_configuration.get("replace_model_id", None)
    timeout = demo_configuration.get("timeout", None)
    entry_point = demo_configuration.get("entry_point", None)
    schema_info = demo_configuration.get("schema_info", None)
    device_name = demo_configuration.get("device_name", None)
    connection_state = demo_configuration.get("connection_state", None)
    device_group_id = demo_configuration.get("device_group_id", None)
    scope = demo_configuration.get("scope", None)
    number_of_images = demo_configuration.get("number_of_images", None)
    skip = demo_configuration.get("skip", None)
    order_by = demo_configuration.get("order_by", None)
    number_of_inference_results = demo_configuration.get("number_of_inference_results", None)
    filter = demo_configuration.get("filter", None)
    raw = demo_configuration.get("raw", None)
    time = demo_configuration.get("time", None)

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
                logger.info("Add To Configuration")
            elif status == ai_model_obj.publish_status.ADD_TO_CONFIGURATION_FAILED.value:
                logger.info("Add To Configuration Failed")
            elif status == ai_model_obj.publish_status.ADD_TO_CONFIGURATION_COMPLETE.value:
                logger.info("Add To Configuration Complete")
            elif status == ai_model_obj.publish_status.SAVING.value:
                logger.info("Saving")
            else:
                logger.info("Error")
                sys.exit(1)
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
                sys.exit(1)

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
                sys.exit(1)

    # Console Access Library provided API Usage.

    # AIModel - ImportBaseModel
    response = ai_model_obj.import_base_model(
        model_id=model_id,
        model=model,
        converted=converted,
        vendor_name=vendor_name,
        comment=comment,
        input_format_param=input_format_param,
        network_config=network_config,
        network_type=network_type,
        metadata_format_id=metadata_format_id
    )
    print("IMPORT BASE MODEL:", response)

    # AIModel - GetModels
    response = ai_model_obj.get_models(
        model_id=model_id,
        comment=comment,
        project_name=project_name,
        model_platform=model_platform,
        project_type=project_type,
        device_id=get_model_device_id,
        latest_type=latest_type,
    )
    print("GET MODELS:", response)

    # AIModel - GetBaseModelStatus
    response = ai_model_obj.get_base_model_status(
        model_id=model_id,
        latest_type=latest_type,
    )
    print("GET BASE MODEL STATUS:", response)

    # AIModel - PublishModelWaitModel
    response = ai_model_obj.publish_model_wait_response(
        model_id=model_id,
        device_id=publish_model_wait_response_device_id,
        callback=publish_callback
    )
    print("PUBLISH MODEL WAIT RESPONSE:", response)

    # Deployment - CreateDeployConfiguration
    response = deployment_obj.create_deploy_configuration(
        config_id=config_id,
        comment=comment,
        sensor_loader_version_number=sensor_loader_version_number,
        sensor_version_number=sensor_version_number,
        model_id=model_id,
        model_version_number=model_version_number,
        ap_fw_version_number=ap_fw_version_number
    )
    print("CREATE DEPLOY CONFIGURATION", response)

    # Deployment - DeployByConfigurationWaitResponse
    response = deployment_obj.deploy_by_configuration_wait_response(
        config_id=config_id,
        device_ids=device_ids,
        replace_model_id=replace_model_id,
        comment=comment,
        timeout=timeout,
        callback=deploy_callback
    )
    print("DEPLOY BY CONFIGURATION WAIT RESPONSE", response)

    # Deployment - CancelDeployment
    deployment_obj.deploy_by_configuration(
        config_id=config_id,
        device_ids=device_ids,
        replace_model_id=replace_model_id,
        comment=comment,
    )
    response_get_deploy_history = deployment_obj.get_deploy_history(device_id=device_id)
    for i in range(len(response_get_deploy_history["deploys"])):
        if (config_id == response_get_deploy_history["deploys"][i]["config_id"] and
                response_get_deploy_history["deploys"][i]["deploy_status"] == "7"):
            deploy_id = response_get_deploy_history["deploys"][i]["id"]
            break
    response = deployment_obj.cancel_deployment(
        device_id=device_id,
        deploy_id=str(deploy_id)
    )
    print("CANCEL DEPLOYMENT", response)

    # Deployment - GetDeployConfigurations
    response = deployment_obj.get_deploy_configurations()
    print("GET DEPLOY CONFIGURATIONS", response)

    # Deployment - GetDeployHistory
    response = deployment_obj.get_deploy_history(device_id=device_id)
    print("GET DEPLOY HISTORY", response)

    # Deployment - ImportDeviceApp
    response = deployment_obj.import_device_app(
        compiled_flg=compiled_flg,
        app_name=app_name,
        version_number=version_number,
        comment=comment,
        file_name=file_content_name,
        file_content=file_content,
        entry_point=entry_point,
        schema_info=schema_info
    )
    print("IMPORT DEVICE APP:", response)

    # Deployment - DeployDeviceAppWaitResponse
    app_status = "0"
    while app_status != "2": 
        device_apps_response = deployment_obj.get_device_apps()
        for i in range(len(device_apps_response["apps"])):
            if device_apps_response["apps"][i]["name"] == app_name:
                app_status = device_apps_response["apps"][i]["versions"][0]["status"]
                if app_status == "3":
                    logging.error("ImportDeviceApp is failed.")
                    sys.exit(1)
    response = deployment_obj.deploy_device_app_wait_response(
        app_name=app_name,
        version_number=version_number,
        device_ids=device_ids,
        comment=comment,
        callback=deploy_device_app_callback
    )
    print("DEPLOY DEVICE APP WAIT RESPONSE", response)

    # Deployment - GetDeviceApps
    response = deployment_obj.get_device_apps()
    print("GET DEVICE APPS:", response)

    # Deployment - GetDeviceAppDeploys
    response = deployment_obj.get_device_app_deploys(
        app_name=app_name,
        version_number=version_number
    )
    print("GET DEVICE APP DEPLOYS", response)

    # DeviceManagement - GetDevices
    response = device_management_obj.get_devices(
        device_id=device_id,
        device_name=device_name,
        connection_state=connection_state,
        device_group_id=device_group_id,
        device_ids=device_ids,
        scope=scope
    )
    print("GET DEVICES:", response)

    # DeviceManagement - StartUploadInferenceResult
    response = device_management_obj.start_upload_inference_result(device_id=device_id)
    print("START UPLOAD INFERENCE RESULT:", response)

    # DeviceManagement - StopUploadInferenceResult
    response = device_management_obj.stop_upload_inference_result(device_id=device_id)
    print("STOP UPLOAD INFERENCE RESULT:", response)

    # DeviceManagement - GetCommandParameterFile
    response = device_management_obj.get_command_parameter_file()
    print("GET COMMAND PARAMETER FILE:", response)

    # Insight - GetImageDirectories
    response = insight_obj.get_image_directories(device_id=device_id)
    print("GET IMAGE DIRECTORIES:", response)

    # Insight - GetImages
    response = insight_obj.get_images(
        device_id=device_id,
        sub_directory_name=sub_directory_name,
        number_of_images=number_of_images,
        skip=skip,
        order_by=order_by
    )
    print("GET IMAGES:", response)

    # Insight - GetInferenceResults
    response = insight_obj.get_inference_results(
        device_id=device_id,
        filter=filter,
        number_of_inference_results=number_of_inference_results,
        raw=raw,
        time=time
    )
    print("GET INFERENCE RESULTS:", response)

    # Insight - GetImageData
    response = insight_obj.get_image_data(
        device_id,
        sub_directory_name,
        number_of_images=number_of_images,
        skip=skip,
        order_by=order_by
    )
    print("GET IMAGE DATA:", response)

    # Insight - GetLastInferenceData
    response = insight_obj.get_last_inference_data(device_id=device_id)
    print("GET LAST INFERENCE DATA:", response)

    # Insight - GetLastInferenceAndImageData
    response = insight_obj.get_last_inference_and_image_data(
        device_id=device_id,
        sub_directory_name=sub_directory_name
    )
    print("GET LAST INFERENCE AND IMAGE DATA:", response)

    # AIModel - DeleteModel
    response = ai_model_obj.delete_model(model_id=model_id)
    print("DELETE MODEL:", response)

    # Deployment - UndeployDeviceApp
    response = deployment_obj.undeploy_device_app(device_ids=device_ids)
    print("UNDEPLOY DEVICE APP:", response)

    # Deployment - DeleteDeviceApp
    response = deployment_obj.delete_device_app(
        app_name=app_name,
        version_number=version_number
    )
    print("DELETE DEVICE APP:", response)

    # Deployment - DeleteDeployConfiguration
    response = deployment_obj.delete_deploy_configuration(config_id=config_id)
    print("DELETE DEPLOY CONFIGURATION:", response)
