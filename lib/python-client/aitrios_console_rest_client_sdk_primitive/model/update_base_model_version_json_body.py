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


class UpdateBaseModelVersionJsonBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    UpdateBaseModelVersion JsonBody.
    """


    class MetaOapg:
        
        class properties:
            comment = schemas.StrSchema
            input_format_param = schemas.StrSchema
            network_config = schemas.StrSchema
            __annotations__ = {
                "comment": comment,
                "input_format_param": input_format_param,
                "network_config": network_config,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input_format_param"]) -> MetaOapg.properties.input_format_param: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network_config"]) -> MetaOapg.properties.network_config: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["comment", "input_format_param", "network_config", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input_format_param"]) -> typing.Union[MetaOapg.properties.input_format_param, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network_config"]) -> typing.Union[MetaOapg.properties.network_config, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["comment", "input_format_param", "network_config", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        input_format_param: typing.Union[MetaOapg.properties.input_format_param, str, schemas.Unset] = schemas.unset,
        network_config: typing.Union[MetaOapg.properties.network_config, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateBaseModelVersionJsonBody':
        return super().__new__(
            cls,
            *_args,
            comment=comment,
            input_format_param=input_format_param,
            network_config=network_config,
            _configuration=_configuration,
            **kwargs,
        )