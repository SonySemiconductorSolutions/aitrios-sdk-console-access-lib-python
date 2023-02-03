import typing_extensions

from aitrios_console_rest_client_sdk_primitive.paths import PathValues
from aitrios_console_rest_client_sdk_primitive.apis.paths.devices import Devices
from aitrios_console_rest_client_sdk_primitive.apis.paths.command_parameter_files import CommandParameterFiles
from aitrios_console_rest_client_sdk_primitive.apis.paths.command_parameter_files_file_name import CommandParameterFilesFileName
from aitrios_console_rest_client_sdk_primitive.apis.paths.devices_configuration_command_parameter_files_file_name import DevicesConfigurationCommandParameterFilesFileName
from aitrios_console_rest_client_sdk_primitive.apis.paths.deployconfigurations import Deployconfigurations
from aitrios_console_rest_client_sdk_primitive.apis.paths.deployconfigurations_config_id import DeployconfigurationsConfigId
from aitrios_console_rest_client_sdk_primitive.apis.paths.devices_device_id_deploys_deploy_id import DevicesDeviceIdDeploysDeployId
from aitrios_console_rest_client_sdk_primitive.apis.paths.devices_device_id_deploys import DevicesDeviceIdDeploys
from aitrios_console_rest_client_sdk_primitive.apis.paths.device_apps import DeviceApps
from aitrios_console_rest_client_sdk_primitive.apis.paths.device_apps_app_name_version_number import DeviceAppsAppNameVersionNumber
from aitrios_console_rest_client_sdk_primitive.apis.paths.device_apps_deploys import DeviceAppsDeploys
from aitrios_console_rest_client_sdk_primitive.apis.paths.device_apps_app_name_version_number_deploys import DeviceAppsAppNameVersionNumberDeploys
from aitrios_console_rest_client_sdk_primitive.apis.paths.devices_device_id_inferenceresults_collectstart import DevicesDeviceIdInferenceresultsCollectstart
from aitrios_console_rest_client_sdk_primitive.apis.paths.devices_device_id_inferenceresults_collectstop import DevicesDeviceIdInferenceresultsCollectstop
from aitrios_console_rest_client_sdk_primitive.apis.paths.devices_images_export import DevicesImagesExport
from aitrios_console_rest_client_sdk_primitive.apis.paths.devices_images_directories import DevicesImagesDirectories
from aitrios_console_rest_client_sdk_primitive.apis.paths.devices_device_id_images_directories_sub_directory_name import DevicesDeviceIdImagesDirectoriesSubDirectoryName
from aitrios_console_rest_client_sdk_primitive.apis.paths.devices_device_id_inferenceresults import DevicesDeviceIdInferenceresults
from aitrios_console_rest_client_sdk_primitive.apis.paths.models_model_id import ModelsModelId
from aitrios_console_rest_client_sdk_primitive.apis.paths.models_model_id_base import ModelsModelIdBase
from aitrios_console_rest_client_sdk_primitive.apis.paths.models import Models

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DEVICES: Devices,
        PathValues.COMMAND_PARAMETER_FILES: CommandParameterFiles,
        PathValues.COMMAND_PARAMETER_FILES_FILE_NAME: CommandParameterFilesFileName,
        PathValues.DEVICES_CONFIGURATION_COMMAND_PARAMETER_FILES_FILE_NAME: DevicesConfigurationCommandParameterFilesFileName,
        PathValues.DEPLOYCONFIGURATIONS: Deployconfigurations,
        PathValues.DEPLOYCONFIGURATIONS_CONFIG_ID: DeployconfigurationsConfigId,
        PathValues.DEVICES_DEVICE_ID_DEPLOYS_DEPLOY_ID: DevicesDeviceIdDeploysDeployId,
        PathValues.DEVICES_DEVICE_ID_DEPLOYS: DevicesDeviceIdDeploys,
        PathValues.DEVICE_APPS: DeviceApps,
        PathValues.DEVICE_APPS_APP_NAME_VERSION_NUMBER: DeviceAppsAppNameVersionNumber,
        PathValues.DEVICE_APPS_DEPLOYS: DeviceAppsDeploys,
        PathValues.DEVICE_APPS_APP_NAME_VERSION_NUMBER_DEPLOYS: DeviceAppsAppNameVersionNumberDeploys,
        PathValues.DEVICES_DEVICE_ID_INFERENCERESULTS_COLLECTSTART: DevicesDeviceIdInferenceresultsCollectstart,
        PathValues.DEVICES_DEVICE_ID_INFERENCERESULTS_COLLECTSTOP: DevicesDeviceIdInferenceresultsCollectstop,
        PathValues.DEVICES_IMAGES_EXPORT: DevicesImagesExport,
        PathValues.DEVICES_IMAGES_DIRECTORIES: DevicesImagesDirectories,
        PathValues.DEVICES_DEVICE_ID_IMAGES_DIRECTORIES_SUB_DIRECTORY_NAME: DevicesDeviceIdImagesDirectoriesSubDirectoryName,
        PathValues.DEVICES_DEVICE_ID_INFERENCERESULTS: DevicesDeviceIdInferenceresults,
        PathValues.MODELS_MODEL_ID: ModelsModelId,
        PathValues.MODELS_MODEL_ID_BASE: ModelsModelIdBase,
        PathValues.MODELS: Models,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DEVICES: Devices,
        PathValues.COMMAND_PARAMETER_FILES: CommandParameterFiles,
        PathValues.COMMAND_PARAMETER_FILES_FILE_NAME: CommandParameterFilesFileName,
        PathValues.DEVICES_CONFIGURATION_COMMAND_PARAMETER_FILES_FILE_NAME: DevicesConfigurationCommandParameterFilesFileName,
        PathValues.DEPLOYCONFIGURATIONS: Deployconfigurations,
        PathValues.DEPLOYCONFIGURATIONS_CONFIG_ID: DeployconfigurationsConfigId,
        PathValues.DEVICES_DEVICE_ID_DEPLOYS_DEPLOY_ID: DevicesDeviceIdDeploysDeployId,
        PathValues.DEVICES_DEVICE_ID_DEPLOYS: DevicesDeviceIdDeploys,
        PathValues.DEVICE_APPS: DeviceApps,
        PathValues.DEVICE_APPS_APP_NAME_VERSION_NUMBER: DeviceAppsAppNameVersionNumber,
        PathValues.DEVICE_APPS_DEPLOYS: DeviceAppsDeploys,
        PathValues.DEVICE_APPS_APP_NAME_VERSION_NUMBER_DEPLOYS: DeviceAppsAppNameVersionNumberDeploys,
        PathValues.DEVICES_DEVICE_ID_INFERENCERESULTS_COLLECTSTART: DevicesDeviceIdInferenceresultsCollectstart,
        PathValues.DEVICES_DEVICE_ID_INFERENCERESULTS_COLLECTSTOP: DevicesDeviceIdInferenceresultsCollectstop,
        PathValues.DEVICES_IMAGES_EXPORT: DevicesImagesExport,
        PathValues.DEVICES_IMAGES_DIRECTORIES: DevicesImagesDirectories,
        PathValues.DEVICES_DEVICE_ID_IMAGES_DIRECTORIES_SUB_DIRECTORY_NAME: DevicesDeviceIdImagesDirectoriesSubDirectoryName,
        PathValues.DEVICES_DEVICE_ID_INFERENCERESULTS: DevicesDeviceIdInferenceresults,
        PathValues.MODELS_MODEL_ID: ModelsModelId,
        PathValues.MODELS_MODEL_ID_BASE: ModelsModelIdBase,
        PathValues.MODELS: Models,
    }
)
