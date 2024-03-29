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


class InferenceResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            DeviceID = schemas.StrSchema
            ModelID = schemas.StrSchema
            Image = schemas.BoolSchema
            
            
            class Inferences(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Inference']:
                        return Inference
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Inference'], typing.List['Inference']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Inferences':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Inference':
                    return super().__getitem__(i)
            id = schemas.StrSchema
            ttl = schemas.IntSchema
            _rid = schemas.StrSchema
            _self = schemas.StrSchema
            _etag = schemas.StrSchema
            _attachments = schemas.StrSchema
            _ts = schemas.IntSchema
            __annotations__ = {
                "DeviceID": DeviceID,
                "ModelID": ModelID,
                "Image": Image,
                "Inferences": Inferences,
                "id": id,
                "ttl": ttl,
                "_rid": _rid,
                "_self": _self,
                "_etag": _etag,
                "_attachments": _attachments,
                "_ts": _ts,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DeviceID"]) -> MetaOapg.properties.DeviceID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ModelID"]) -> MetaOapg.properties.ModelID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Image"]) -> MetaOapg.properties.Image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Inferences"]) -> MetaOapg.properties.Inferences: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ttl"]) -> MetaOapg.properties.ttl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_rid"]) -> MetaOapg.properties._rid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_self"]) -> MetaOapg.properties._self: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_etag"]) -> MetaOapg.properties._etag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_attachments"]) -> MetaOapg.properties._attachments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_ts"]) -> MetaOapg.properties._ts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["DeviceID", "ModelID", "Image", "Inferences", "id", "ttl", "_rid", "_self", "_etag", "_attachments", "_ts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DeviceID"]) -> typing.Union[MetaOapg.properties.DeviceID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ModelID"]) -> typing.Union[MetaOapg.properties.ModelID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Image"]) -> typing.Union[MetaOapg.properties.Image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Inferences"]) -> typing.Union[MetaOapg.properties.Inferences, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ttl"]) -> typing.Union[MetaOapg.properties.ttl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_rid"]) -> typing.Union[MetaOapg.properties._rid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_self"]) -> typing.Union[MetaOapg.properties._self, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_etag"]) -> typing.Union[MetaOapg.properties._etag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_attachments"]) -> typing.Union[MetaOapg.properties._attachments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_ts"]) -> typing.Union[MetaOapg.properties._ts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["DeviceID", "ModelID", "Image", "Inferences", "id", "ttl", "_rid", "_self", "_etag", "_attachments", "_ts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        DeviceID: typing.Union[MetaOapg.properties.DeviceID, str, schemas.Unset] = schemas.unset,
        ModelID: typing.Union[MetaOapg.properties.ModelID, str, schemas.Unset] = schemas.unset,
        Image: typing.Union[MetaOapg.properties.Image, bool, schemas.Unset] = schemas.unset,
        Inferences: typing.Union[MetaOapg.properties.Inferences, list, tuple, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        ttl: typing.Union[MetaOapg.properties.ttl, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _rid: typing.Union[MetaOapg.properties._rid, str, schemas.Unset] = schemas.unset,
        _self: typing.Union[MetaOapg.properties._self, str, schemas.Unset] = schemas.unset,
        _etag: typing.Union[MetaOapg.properties._etag, str, schemas.Unset] = schemas.unset,
        _attachments: typing.Union[MetaOapg.properties._attachments, str, schemas.Unset] = schemas.unset,
        _ts: typing.Union[MetaOapg.properties._ts, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InferenceResult':
        return super().__new__(
            cls,
            *_args,
            DeviceID=DeviceID,
            ModelID=ModelID,
            Image=Image,
            Inferences=Inferences,
            id=id,
            ttl=ttl,
            _rid=_rid,
            _self=_self,
            _etag=_etag,
            _attachments=_attachments,
            _ts=_ts,
            _configuration=_configuration,
            **kwargs,
        )

from aitrios_console_rest_client_sdk_primitive.model.inference import Inference
