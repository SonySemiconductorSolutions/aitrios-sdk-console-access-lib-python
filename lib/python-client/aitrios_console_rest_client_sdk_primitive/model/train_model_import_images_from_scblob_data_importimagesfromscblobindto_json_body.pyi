# coding: utf-8

"""
    AITRIOS | Console

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.1.0
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


class TrainModelImportImagesFromScblobDataImportimagesfromscblobindtoJsonBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ImportImagesFromScblob API json_body class.

Attributes:
----------
tags_name(list): tag name list.
container_url(str): container url.
    """


    class MetaOapg:
        required = {
            "container_url",
        }
        
        class properties:
            container_url = schemas.StrSchema
            
            
            class tags_name(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tags_name':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "container_url": container_url,
                "tags_name": tags_name,
            }
    
    container_url: MetaOapg.properties.container_url
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["container_url"]) -> MetaOapg.properties.container_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags_name"]) -> MetaOapg.properties.tags_name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["container_url", "tags_name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["container_url"]) -> MetaOapg.properties.container_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags_name"]) -> typing.Union[MetaOapg.properties.tags_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["container_url", "tags_name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        container_url: typing.Union[MetaOapg.properties.container_url, str, ],
        tags_name: typing.Union[MetaOapg.properties.tags_name, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TrainModelImportImagesFromScblobDataImportimagesfromscblobindtoJsonBody':
        return super().__new__(
            cls,
            *args,
            container_url=container_url,
            tags_name=tags_name,
            _configuration=_configuration,
            **kwargs,
        )
