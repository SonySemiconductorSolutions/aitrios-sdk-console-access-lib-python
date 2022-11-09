# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from aitrios_console_rest_client_sdk_primitive.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    COMMAND_PARAMETER_FILE = "Command Parameter File"
    DEPLOY = "Deploy"
    DEVICE_APP = "Device App"
    DEVICE_COMMAND = "Device Command"
    INSIGHT = "Insight"
    MANAGE_DEVICES = "Manage Devices"
    TRAIN_MODEL = "Train Model"
