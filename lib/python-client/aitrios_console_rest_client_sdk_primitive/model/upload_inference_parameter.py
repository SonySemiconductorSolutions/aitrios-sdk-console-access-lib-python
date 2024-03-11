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


class UploadInferenceParameter(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "StorageNameIR",
            "StorageSubDirectoryPathIR",
        }
        
        class properties:
            StorageNameIR = schemas.StrSchema
            StorageSubDirectoryPathIR = schemas.StrSchema
            UploadMethodIR = schemas.StrSchema
            PPLParameter = schemas.StrSchema
            CropHOffset = schemas.IntSchema
            CropVOffset = schemas.IntSchema
            CropHSize = schemas.IntSchema
            CropVSize = schemas.IntSchema
            NetworkId = schemas.StrSchema
            __annotations__ = {
                "StorageNameIR": StorageNameIR,
                "StorageSubDirectoryPathIR": StorageSubDirectoryPathIR,
                "UploadMethodIR": UploadMethodIR,
                "PPLParameter": PPLParameter,
                "CropHOffset": CropHOffset,
                "CropVOffset": CropVOffset,
                "CropHSize": CropHSize,
                "CropVSize": CropVSize,
                "NetworkId": NetworkId,
            }
    
    StorageNameIR: MetaOapg.properties.StorageNameIR
    StorageSubDirectoryPathIR: MetaOapg.properties.StorageSubDirectoryPathIR
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StorageNameIR"]) -> MetaOapg.properties.StorageNameIR: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StorageSubDirectoryPathIR"]) -> MetaOapg.properties.StorageSubDirectoryPathIR: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UploadMethodIR"]) -> MetaOapg.properties.UploadMethodIR: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PPLParameter"]) -> MetaOapg.properties.PPLParameter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CropHOffset"]) -> MetaOapg.properties.CropHOffset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CropVOffset"]) -> MetaOapg.properties.CropVOffset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CropHSize"]) -> MetaOapg.properties.CropHSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CropVSize"]) -> MetaOapg.properties.CropVSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["NetworkId"]) -> MetaOapg.properties.NetworkId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["StorageNameIR", "StorageSubDirectoryPathIR", "UploadMethodIR", "PPLParameter", "CropHOffset", "CropVOffset", "CropHSize", "CropVSize", "NetworkId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StorageNameIR"]) -> MetaOapg.properties.StorageNameIR: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["StorageSubDirectoryPathIR"]) -> MetaOapg.properties.StorageSubDirectoryPathIR: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UploadMethodIR"]) -> typing.Union[MetaOapg.properties.UploadMethodIR, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PPLParameter"]) -> typing.Union[MetaOapg.properties.PPLParameter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CropHOffset"]) -> typing.Union[MetaOapg.properties.CropHOffset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CropVOffset"]) -> typing.Union[MetaOapg.properties.CropVOffset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CropHSize"]) -> typing.Union[MetaOapg.properties.CropHSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CropVSize"]) -> typing.Union[MetaOapg.properties.CropVSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["NetworkId"]) -> typing.Union[MetaOapg.properties.NetworkId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["StorageNameIR", "StorageSubDirectoryPathIR", "UploadMethodIR", "PPLParameter", "CropHOffset", "CropVOffset", "CropHSize", "CropVSize", "NetworkId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        StorageNameIR: typing.Union[MetaOapg.properties.StorageNameIR, str, ],
        StorageSubDirectoryPathIR: typing.Union[MetaOapg.properties.StorageSubDirectoryPathIR, str, ],
        UploadMethodIR: typing.Union[MetaOapg.properties.UploadMethodIR, str, schemas.Unset] = schemas.unset,
        PPLParameter: typing.Union[MetaOapg.properties.PPLParameter, str, schemas.Unset] = schemas.unset,
        CropHOffset: typing.Union[MetaOapg.properties.CropHOffset, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        CropVOffset: typing.Union[MetaOapg.properties.CropVOffset, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        CropHSize: typing.Union[MetaOapg.properties.CropHSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        CropVSize: typing.Union[MetaOapg.properties.CropVSize, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        NetworkId: typing.Union[MetaOapg.properties.NetworkId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UploadInferenceParameter':
        return super().__new__(
            cls,
            *_args,
            StorageNameIR=StorageNameIR,
            StorageSubDirectoryPathIR=StorageSubDirectoryPathIR,
            UploadMethodIR=UploadMethodIR,
            PPLParameter=PPLParameter,
            CropHOffset=CropHOffset,
            CropVOffset=CropVOffset,
            CropHSize=CropHSize,
            CropVSize=CropVSize,
            NetworkId=NetworkId,
            _configuration=_configuration,
            **kwargs,
        )
