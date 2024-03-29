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


class Tag(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            tag_id = schemas.StrSchema
            tag_name = schemas.StrSchema
            tag_description = schemas.StrSchema
            tag_type = schemas.NumberSchema
            image_count = schemas.NumberSchema
            __annotations__ = {
                "tag_id": tag_id,
                "tag_name": tag_name,
                "tag_description": tag_description,
                "tag_type": tag_type,
                "image_count": image_count,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_id"]) -> MetaOapg.properties.tag_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_name"]) -> MetaOapg.properties.tag_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_description"]) -> MetaOapg.properties.tag_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag_type"]) -> MetaOapg.properties.tag_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image_count"]) -> MetaOapg.properties.image_count: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tag_id", "tag_name", "tag_description", "tag_type", "image_count", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_id"]) -> typing.Union[MetaOapg.properties.tag_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_name"]) -> typing.Union[MetaOapg.properties.tag_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_description"]) -> typing.Union[MetaOapg.properties.tag_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag_type"]) -> typing.Union[MetaOapg.properties.tag_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image_count"]) -> typing.Union[MetaOapg.properties.image_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tag_id", "tag_name", "tag_description", "tag_type", "image_count", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tag_id: typing.Union[MetaOapg.properties.tag_id, str, schemas.Unset] = schemas.unset,
        tag_name: typing.Union[MetaOapg.properties.tag_name, str, schemas.Unset] = schemas.unset,
        tag_description: typing.Union[MetaOapg.properties.tag_description, str, schemas.Unset] = schemas.unset,
        tag_type: typing.Union[MetaOapg.properties.tag_type, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        image_count: typing.Union[MetaOapg.properties.image_count, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Tag':
        return super().__new__(
            cls,
            *_args,
            tag_id=tag_id,
            tag_name=tag_name,
            tag_description=tag_description,
            tag_type=tag_type,
            image_count=image_count,
            _configuration=_configuration,
            **kwargs,
        )
