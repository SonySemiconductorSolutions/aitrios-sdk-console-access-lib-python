# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from aitrios_console_rest_client_sdk_primitive.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from aitrios_console_rest_client_sdk_primitive.model.aws import AWS
from aitrios_console_rest_client_sdk_primitive.model.azure import Azure
from aitrios_console_rest_client_sdk_primitive.model.bind_command_parameter_file_to_device_json_body import BindCommandParameterFileToDeviceJsonBody
from aitrios_console_rest_client_sdk_primitive.model.change_password_json_body import ChangePasswordJsonBody
from aitrios_console_rest_client_sdk_primitive.model.create_firmware_json_body import CreateFirmwareJsonBody
from aitrios_console_rest_client_sdk_primitive.model.create_project_image_regions_json_body import CreateProjectImageRegionsJsonBody
from aitrios_console_rest_client_sdk_primitive.model.delete_images_json_body import DeleteImagesJsonBody
from aitrios_console_rest_client_sdk_primitive.model.deploy_configuration import DeployConfiguration
from aitrios_console_rest_client_sdk_primitive.model.deploy_device_app_json_body import DeployDeviceAppJsonBody
from aitrios_console_rest_client_sdk_primitive.model.deploy_history import DeployHistory
from aitrios_console_rest_client_sdk_primitive.model.device import Device
from aitrios_console_rest_client_sdk_primitive.model.device_app import DeviceApp
from aitrios_console_rest_client_sdk_primitive.model.device_app_deploy_history import DeviceAppDeployHistory
from aitrios_console_rest_client_sdk_primitive.model.device_certificate import DeviceCertificate
from aitrios_console_rest_client_sdk_primitive.model.device_group import DeviceGroup
from aitrios_console_rest_client_sdk_primitive.model.devices import Devices
from aitrios_console_rest_client_sdk_primitive.model.enroll_device_json_body import EnrollDeviceJsonBody
from aitrios_console_rest_client_sdk_primitive.model.error_response import ErrorResponse
from aitrios_console_rest_client_sdk_primitive.model.event_log import EventLog
from aitrios_console_rest_client_sdk_primitive.model.fw_operation import FWOperation
from aitrios_console_rest_client_sdk_primitive.model.file_id import FileId
from aitrios_console_rest_client_sdk_primitive.model.firmware import Firmware
from aitrios_console_rest_client_sdk_primitive.model.image import Image
from aitrios_console_rest_client_sdk_primitive.model.import_base_model_json_body import ImportBaseModelJsonBody
from aitrios_console_rest_client_sdk_primitive.model.import_device_app_json_body import ImportDeviceAppJsonBody
from aitrios_console_rest_client_sdk_primitive.model.import_images_from_files_json_body import ImportImagesFromFilesJsonBody
from aitrios_console_rest_client_sdk_primitive.model.import_images_from_scblob_json_body import ImportImagesFromScblobJsonBody
from aitrios_console_rest_client_sdk_primitive.model.inference import Inference
from aitrios_console_rest_client_sdk_primitive.model.inference_result import InferenceResult
from aitrios_console_rest_client_sdk_primitive.model.model import Model
from aitrios_console_rest_client_sdk_primitive.model.model_info import ModelInfo
from aitrios_console_rest_client_sdk_primitive.model.model_project import ModelProject
from aitrios_console_rest_client_sdk_primitive.model.model_project_info import ModelProjectInfo
from aitrios_console_rest_client_sdk_primitive.model.model_project_of_model import ModelProjectOfModel
from aitrios_console_rest_client_sdk_primitive.model.model_project_of_model_info import ModelProjectOfModelInfo
from aitrios_console_rest_client_sdk_primitive.model.model_version import ModelVersion
from aitrios_console_rest_client_sdk_primitive.model.model_version_info import ModelVersionInfo
from aitrios_console_rest_client_sdk_primitive.model.model_version_json_body import ModelVersionJsonBody
from aitrios_console_rest_client_sdk_primitive.model.primary_interval import PrimaryInterval
from aitrios_console_rest_client_sdk_primitive.model.region import Region
from aitrios_console_rest_client_sdk_primitive.model.regist_command_parameter_file_body import RegistCommandParameterFileBody
from aitrios_console_rest_client_sdk_primitive.model.secondary_interval import SecondaryInterval
from aitrios_console_rest_client_sdk_primitive.model.set_device_app_log_json_body import SetDeviceAppLogJsonBody
from aitrios_console_rest_client_sdk_primitive.model.set_device_configuration_json_body import SetDeviceConfigurationJsonBody
from aitrios_console_rest_client_sdk_primitive.model.set_image_configuration_json_body import SetImageConfigurationJsonBody
from aitrios_console_rest_client_sdk_primitive.model.success_response import SuccessResponse
from aitrios_console_rest_client_sdk_primitive.model.tag import Tag
from aitrios_console_rest_client_sdk_primitive.model.training_kit import TrainingKit
from aitrios_console_rest_client_sdk_primitive.model.unbind_command_parameter_file_json_body import UnbindCommandParameterFileJsonBody
from aitrios_console_rest_client_sdk_primitive.model.update_base_model_version_json_body import UpdateBaseModelVersionJsonBody
from aitrios_console_rest_client_sdk_primitive.model.update_command_parameter_file_body import UpdateCommandParameterFileBody
from aitrios_console_rest_client_sdk_primitive.model.update_device_certificate_json_body import UpdateDeviceCertificateJsonBody
from aitrios_console_rest_client_sdk_primitive.model.update_device_model_version_json_body import UpdateDeviceModelVersionJsonBody
from aitrios_console_rest_client_sdk_primitive.model.update_ir_hub_connector_json_body import UpdateIRHubConnectorJsonBody
from aitrios_console_rest_client_sdk_primitive.model.update_project_image_regions_json_body import UpdateProjectImageRegionsJsonBody
from aitrios_console_rest_client_sdk_primitive.model.update_project_tag_json_body import UpdateProjectTagJsonBody
from aitrios_console_rest_client_sdk_primitive.model.upload_inference_parameter import UploadInferenceParameter
from aitrios_console_rest_client_sdk_primitive.model.vafe_log import VafeLog
