# coding: utf-8

"""
    AITRIOS | Console

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""

from aitrios_console_rest_client_sdk_primitive.paths.devices_configuration_command_parameter_files_file_name.put import ApplyCommandParameterFileToDevice
from aitrios_console_rest_client_sdk_primitive.paths.devices_configuration_command_parameter_files_file_name.delete import CancelCommandParameterFile
from aitrios_console_rest_client_sdk_primitive.paths.command_parameter_files.get import GetCommandParameter
from aitrios_console_rest_client_sdk_primitive.paths.command_parameter_files.post import RegistCommandParameterFile
from aitrios_console_rest_client_sdk_primitive.paths.command_parameter_files_file_name.patch import UpdateCommandParameterFile


class CommandParameterFileApi(
    ApplyCommandParameterFileToDevice,
    CancelCommandParameterFile,
    GetCommandParameter,
    RegistCommandParameterFile,
    UpdateCommandParameterFile,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
