import typing_extensions

from aitrios_console_rest_client_sdk_primitive.apis.tags import TagValues
from aitrios_console_rest_client_sdk_primitive.apis.tags.command_parameter_file_api import CommandParameterFileApi
from aitrios_console_rest_client_sdk_primitive.apis.tags.deploy_api import DeployApi
from aitrios_console_rest_client_sdk_primitive.apis.tags.device_app_api import DeviceAppApi
from aitrios_console_rest_client_sdk_primitive.apis.tags.device_command_api import DeviceCommandApi
from aitrios_console_rest_client_sdk_primitive.apis.tags.insight_api import InsightApi
from aitrios_console_rest_client_sdk_primitive.apis.tags.manage_devices_api import ManageDevicesApi
from aitrios_console_rest_client_sdk_primitive.apis.tags.train_model_api import TrainModelApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.COMMAND_PARAMETER_FILE: CommandParameterFileApi,
        TagValues.DEPLOY: DeployApi,
        TagValues.DEVICE_APP: DeviceAppApi,
        TagValues.DEVICE_COMMAND: DeviceCommandApi,
        TagValues.INSIGHT: InsightApi,
        TagValues.MANAGE_DEVICES: ManageDevicesApi,
        TagValues.TRAIN_MODEL: TrainModelApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.COMMAND_PARAMETER_FILE: CommandParameterFileApi,
        TagValues.DEPLOY: DeployApi,
        TagValues.DEVICE_APP: DeviceAppApi,
        TagValues.DEVICE_COMMAND: DeviceCommandApi,
        TagValues.INSIGHT: InsightApi,
        TagValues.MANAGE_DEVICES: ManageDevicesApi,
        TagValues.TRAIN_MODEL: TrainModelApi,
    }
)
