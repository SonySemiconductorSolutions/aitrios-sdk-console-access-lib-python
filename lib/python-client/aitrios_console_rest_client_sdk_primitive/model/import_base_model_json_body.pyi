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


class ImportBaseModelJsonBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "model",
            "model_id",
        }
        
        class properties:
            model = schemas.StrSchema
            model_id = schemas.StrSchema
            input_format_param = schemas.StrSchema
            network_config = schemas.StrSchema
            converted = schemas.BoolSchema
            vendor_name = schemas.StrSchema
            comment = schemas.StrSchema
            network_type = schemas.StrSchema
            metadata_format_id = schemas.StrSchema
            __annotations__ = {
                "model": model,
                "model_id": model_id,
                "input_format_param": input_format_param,
                "network_config": network_config,
                "converted": converted,
                "vendor_name": vendor_name,
                "comment": comment,
                "network_type": network_type,
                "metadata_format_id": metadata_format_id,
            }
    
    model: MetaOapg.properties.model
    model_id: MetaOapg.properties.model_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_id"]) -> MetaOapg.properties.model_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input_format_param"]) -> MetaOapg.properties.input_format_param: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network_config"]) -> MetaOapg.properties.network_config: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["converted"]) -> MetaOapg.properties.converted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendor_name"]) -> MetaOapg.properties.vendor_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network_type"]) -> MetaOapg.properties.network_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata_format_id"]) -> MetaOapg.properties.metadata_format_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["model", "model_id", "input_format_param", "network_config", "converted", "vendor_name", "comment", "network_type", "metadata_format_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model"]) -> MetaOapg.properties.model: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_id"]) -> MetaOapg.properties.model_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input_format_param"]) -> typing.Union[MetaOapg.properties.input_format_param, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network_config"]) -> typing.Union[MetaOapg.properties.network_config, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["converted"]) -> typing.Union[MetaOapg.properties.converted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendor_name"]) -> typing.Union[MetaOapg.properties.vendor_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network_type"]) -> typing.Union[MetaOapg.properties.network_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata_format_id"]) -> typing.Union[MetaOapg.properties.metadata_format_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["model", "model_id", "input_format_param", "network_config", "converted", "vendor_name", "comment", "network_type", "metadata_format_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        model: typing.Union[MetaOapg.properties.model, str, ],
        model_id: typing.Union[MetaOapg.properties.model_id, str, ],
        input_format_param: typing.Union[MetaOapg.properties.input_format_param, str, schemas.Unset] = schemas.unset,
        network_config: typing.Union[MetaOapg.properties.network_config, str, schemas.Unset] = schemas.unset,
        converted: typing.Union[MetaOapg.properties.converted, bool, schemas.Unset] = schemas.unset,
        vendor_name: typing.Union[MetaOapg.properties.vendor_name, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        network_type: typing.Union[MetaOapg.properties.network_type, str, schemas.Unset] = schemas.unset,
        metadata_format_id: typing.Union[MetaOapg.properties.metadata_format_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ImportBaseModelJsonBody':
        return super().__new__(
            cls,
            *_args,
            model=model,
            model_id=model_id,
            input_format_param=input_format_param,
            network_config=network_config,
            converted=converted,
            vendor_name=vendor_name,
            comment=comment,
            network_type=network_type,
            metadata_format_id=metadata_format_id,
            _configuration=_configuration,
            **kwargs,
        )
