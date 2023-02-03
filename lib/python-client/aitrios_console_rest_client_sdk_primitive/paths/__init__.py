# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from aitrios_console_rest_client_sdk_primitive.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    DEVICES = "/devices"
    COMMAND_PARAMETER_FILES = "/command_parameter_files"
    COMMAND_PARAMETER_FILES_FILE_NAME = "/command_parameter_files/{file_name}"
    DEVICES_CONFIGURATION_COMMAND_PARAMETER_FILES_FILE_NAME = "/devices/configuration/command_parameter_files/{file_name}"
    DEPLOYCONFIGURATIONS = "/deployconfigurations"
    DEPLOYCONFIGURATIONS_CONFIG_ID = "/deployconfigurations/{config_id}"
    DEVICES_DEVICE_ID_DEPLOYS_DEPLOY_ID = "/devices/{device_id}/deploys/{deploy_id}"
    DEVICES_DEVICE_ID_DEPLOYS = "/devices/{device_id}/deploys"
    DEVICE_APPS = "/device_apps"
    DEVICE_APPS_APP_NAME_VERSION_NUMBER = "/device_apps/{app_name}/{version_number}"
    DEVICE_APPS_DEPLOYS = "/device_apps_deploys"
    DEVICE_APPS_APP_NAME_VERSION_NUMBER_DEPLOYS = "/device_apps/{app_name}/{version_number}/deploys"
    DEVICES_DEVICE_ID_INFERENCERESULTS_COLLECTSTART = "/devices/{device_id}/inferenceresults/collectstart"
    DEVICES_DEVICE_ID_INFERENCERESULTS_COLLECTSTOP = "/devices/{device_id}/inferenceresults/collectstop"
    DEVICES_IMAGES_EXPORT = "/devices/images/export"
    DEVICES_IMAGES_DIRECTORIES = "/devices/images/directories"
    DEVICES_DEVICE_ID_IMAGES_DIRECTORIES_SUB_DIRECTORY_NAME = "/devices/{device_id}/images/directories/{sub_directory_name}"
    DEVICES_DEVICE_ID_INFERENCERESULTS = "/devices/{device_id}/inferenceresults"
    MODELS_MODEL_ID = "/models/{model_id}"
    MODELS_MODEL_ID_BASE = "/models/{model_id}/base"
    MODELS = "/models"
