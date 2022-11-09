# coding: utf-8

"""
    Console API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.0.2
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


class RegistCommandParameterBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    RegistCommandParameter Json Body
    """


    class MetaOapg:
        required = {
            "file_name",
            "parameter",
        }
        
        class properties:
            file_name = schemas.StrSchema
            parameter = schemas.StrSchema
            comment = schemas.StrSchema
            __annotations__ = {
                "file_name": file_name,
                "parameter": parameter,
                "comment": comment,
            }
    
    file_name: MetaOapg.properties.file_name
    parameter: MetaOapg.properties.parameter
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parameter"]) -> MetaOapg.properties.parameter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["file_name", "parameter", "comment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parameter"]) -> MetaOapg.properties.parameter: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["file_name", "parameter", "comment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        file_name: typing.Union[MetaOapg.properties.file_name, str, ],
        parameter: typing.Union[MetaOapg.properties.parameter, str, ],
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RegistCommandParameterBody':
        return super().__new__(
            cls,
            *args,
            file_name=file_name,
            parameter=parameter,
            comment=comment,
            _configuration=_configuration,
            **kwargs,
        )
