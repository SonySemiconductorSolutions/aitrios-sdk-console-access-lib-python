# coding: utf-8

"""
    AITRIOS | Console

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.4.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from aitrios_console_rest_client_sdk_primitive import schemas  # noqa: F401


class CreateFirmwareJsonBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    CreateFirmware API model
    """


    class MetaOapg:
        required = {
            "file_content",
            "file_name",
            "version_number",
            "firmware_type",
        }
        
        class properties:
            firmware_type = schemas.StrSchema
            version_number = schemas.StrSchema
            file_name = schemas.StrSchema
            file_content = schemas.StrSchema
            comment = schemas.StrSchema
            __annotations__ = {
                "firmware_type": firmware_type,
                "version_number": version_number,
                "file_name": file_name,
                "file_content": file_content,
                "comment": comment,
            }
    
    file_content: MetaOapg.properties.file_content
    file_name: MetaOapg.properties.file_name
    version_number: MetaOapg.properties.version_number
    firmware_type: MetaOapg.properties.firmware_type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firmware_type"]) -> MetaOapg.properties.firmware_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_number"]) -> MetaOapg.properties.version_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_content"]) -> MetaOapg.properties.file_content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["firmware_type", "version_number", "file_name", "file_content", "comment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firmware_type"]) -> MetaOapg.properties.firmware_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_number"]) -> MetaOapg.properties.version_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_content"]) -> MetaOapg.properties.file_content: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["firmware_type", "version_number", "file_name", "file_content", "comment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        file_content: typing.Union[MetaOapg.properties.file_content, str, ],
        file_name: typing.Union[MetaOapg.properties.file_name, str, ],
        version_number: typing.Union[MetaOapg.properties.version_number, str, ],
        firmware_type: typing.Union[MetaOapg.properties.firmware_type, str, ],
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateFirmwareJsonBody':
        return super().__new__(
            cls,
            *_args,
            file_content=file_content,
            file_name=file_name,
            version_number=version_number,
            firmware_type=firmware_type,
            comment=comment,
            _configuration=_configuration,
            **kwargs,
        )
