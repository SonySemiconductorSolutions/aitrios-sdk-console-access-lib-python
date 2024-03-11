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


class DeviceCertificate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            device_id = schemas.StrSchema
            internal_device_id = schemas.StrSchema
            device_name = schemas.StrSchema
            credentials_id_object = schemas.StrSchema
            credentials_type = schemas.StrSchema
            expiration_date = schemas.StrSchema
            created_time = schemas.StrSchema
            __annotations__ = {
                "device_id": device_id,
                "internal_device_id": internal_device_id,
                "device_name": device_name,
                "credentials_id_object": credentials_id_object,
                "credentials_type": credentials_type,
                "expiration_date": expiration_date,
                "created_time": created_time,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internal_device_id"]) -> MetaOapg.properties.internal_device_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_name"]) -> MetaOapg.properties.device_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credentials_id_object"]) -> MetaOapg.properties.credentials_id_object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credentials_type"]) -> MetaOapg.properties.credentials_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiration_date"]) -> MetaOapg.properties.expiration_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_time"]) -> MetaOapg.properties.created_time: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_id", "internal_device_id", "device_name", "credentials_id_object", "credentials_type", "expiration_date", "created_time", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> typing.Union[MetaOapg.properties.device_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internal_device_id"]) -> typing.Union[MetaOapg.properties.internal_device_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_name"]) -> typing.Union[MetaOapg.properties.device_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credentials_id_object"]) -> typing.Union[MetaOapg.properties.credentials_id_object, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credentials_type"]) -> typing.Union[MetaOapg.properties.credentials_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiration_date"]) -> typing.Union[MetaOapg.properties.expiration_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_time"]) -> typing.Union[MetaOapg.properties.created_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_id", "internal_device_id", "device_name", "credentials_id_object", "credentials_type", "expiration_date", "created_time", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        device_id: typing.Union[MetaOapg.properties.device_id, str, schemas.Unset] = schemas.unset,
        internal_device_id: typing.Union[MetaOapg.properties.internal_device_id, str, schemas.Unset] = schemas.unset,
        device_name: typing.Union[MetaOapg.properties.device_name, str, schemas.Unset] = schemas.unset,
        credentials_id_object: typing.Union[MetaOapg.properties.credentials_id_object, str, schemas.Unset] = schemas.unset,
        credentials_type: typing.Union[MetaOapg.properties.credentials_type, str, schemas.Unset] = schemas.unset,
        expiration_date: typing.Union[MetaOapg.properties.expiration_date, str, schemas.Unset] = schemas.unset,
        created_time: typing.Union[MetaOapg.properties.created_time, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeviceCertificate':
        return super().__new__(
            cls,
            *_args,
            device_id=device_id,
            internal_device_id=internal_device_id,
            device_name=device_name,
            credentials_id_object=credentials_id_object,
            credentials_type=credentials_type,
            expiration_date=expiration_date,
            created_time=created_time,
            _configuration=_configuration,
            **kwargs,
        )
