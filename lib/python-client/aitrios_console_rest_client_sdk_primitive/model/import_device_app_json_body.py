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


class ImportDeviceAppJsonBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    ImportDeviceApp Json Body
    """


    class MetaOapg:
        required = {
            "app_name",
            "file_content",
            "compiled_flg",
            "file_name",
            "version_number",
        }
        
        class properties:
            compiled_flg = schemas.StrSchema
            app_name = schemas.StrSchema
            version_number = schemas.StrSchema
            file_name = schemas.StrSchema
            file_content = schemas.StrSchema
            entry_point = schemas.StrSchema
            comment = schemas.StrSchema
            
            
            class schema_info(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class interfaces(
                            schemas.DictSchema
                        ):
                        
                        
                            class MetaOapg:
                                
                                class properties:
                                    
                                    
                                    class _in(
                                        schemas.ListSchema
                                    ):
                                    
                                    
                                        class MetaOapg:
                                            
                                            
                                            class items(
                                                schemas.DictSchema
                                            ):
                                            
                                            
                                                class MetaOapg:
                                                    
                                                    class properties:
                                                        metadataFormatId = schemas.StrSchema
                                                        __annotations__ = {
                                                            "metadataFormatId": metadataFormatId,
                                                        }
                                                
                                                @typing.overload
                                                def __getitem__(self, name: typing_extensions.Literal["metadataFormatId"]) -> MetaOapg.properties.metadataFormatId: ...
                                                
                                                @typing.overload
                                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                                
                                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["metadataFormatId", ], str]):
                                                    # dict_instance[name] accessor
                                                    return super().__getitem__(name)
                                                
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: typing_extensions.Literal["metadataFormatId"]) -> typing.Union[MetaOapg.properties.metadataFormatId, schemas.Unset]: ...
                                                
                                                @typing.overload
                                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                                
                                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["metadataFormatId", ], str]):
                                                    return super().get_item_oapg(name)
                                                
                                            
                                                def __new__(
                                                    cls,
                                                    *_args: typing.Union[dict, frozendict.frozendict, ],
                                                    metadataFormatId: typing.Union[MetaOapg.properties.metadataFormatId, str, schemas.Unset] = schemas.unset,
                                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                                ) -> 'items':
                                                    return super().__new__(
                                                        cls,
                                                        *_args,
                                                        metadataFormatId=metadataFormatId,
                                                        _configuration=_configuration,
                                                        **kwargs,
                                                    )
                                    
                                        def __new__(
                                            cls,
                                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                                            _configuration: typing.Optional[schemas.Configuration] = None,
                                        ) -> '_in':
                                            return super().__new__(
                                                cls,
                                                _arg,
                                                _configuration=_configuration,
                                            )
                                    
                                        def __getitem__(self, i: int) -> MetaOapg.items:
                                            return super().__getitem__(i)
                                    __annotations__ = {
                                        "in": _in,
                                    }
                            
                            @typing.overload
                            def __getitem__(self, name: typing_extensions.Literal["in"]) -> MetaOapg.properties._in: ...
                            
                            @typing.overload
                            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                            
                            def __getitem__(self, name: typing.Union[typing_extensions.Literal["in", ], str]):
                                # dict_instance[name] accessor
                                return super().__getitem__(name)
                            
                            
                            @typing.overload
                            def get_item_oapg(self, name: typing_extensions.Literal["in"]) -> typing.Union[MetaOapg.properties._in, schemas.Unset]: ...
                            
                            @typing.overload
                            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                            
                            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["in", ], str]):
                                return super().get_item_oapg(name)
                            
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'interfaces':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        __annotations__ = {
                            "interfaces": interfaces,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["interfaces"]) -> MetaOapg.properties.interfaces: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["interfaces", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["interfaces"]) -> typing.Union[MetaOapg.properties.interfaces, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["interfaces", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    interfaces: typing.Union[MetaOapg.properties.interfaces, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'schema_info':
                    return super().__new__(
                        cls,
                        *_args,
                        interfaces=interfaces,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "compiled_flg": compiled_flg,
                "app_name": app_name,
                "version_number": version_number,
                "file_name": file_name,
                "file_content": file_content,
                "entry_point": entry_point,
                "comment": comment,
                "schema_info": schema_info,
            }
    
    app_name: MetaOapg.properties.app_name
    file_content: MetaOapg.properties.file_content
    compiled_flg: MetaOapg.properties.compiled_flg
    file_name: MetaOapg.properties.file_name
    version_number: MetaOapg.properties.version_number
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compiled_flg"]) -> MetaOapg.properties.compiled_flg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["app_name"]) -> MetaOapg.properties.app_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_number"]) -> MetaOapg.properties.version_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_content"]) -> MetaOapg.properties.file_content: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entry_point"]) -> MetaOapg.properties.entry_point: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schema_info"]) -> MetaOapg.properties.schema_info: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["compiled_flg", "app_name", "version_number", "file_name", "file_content", "entry_point", "comment", "schema_info", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compiled_flg"]) -> MetaOapg.properties.compiled_flg: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["app_name"]) -> MetaOapg.properties.app_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_number"]) -> MetaOapg.properties.version_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_name"]) -> MetaOapg.properties.file_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_content"]) -> MetaOapg.properties.file_content: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entry_point"]) -> typing.Union[MetaOapg.properties.entry_point, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schema_info"]) -> typing.Union[MetaOapg.properties.schema_info, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["compiled_flg", "app_name", "version_number", "file_name", "file_content", "entry_point", "comment", "schema_info", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        app_name: typing.Union[MetaOapg.properties.app_name, str, ],
        file_content: typing.Union[MetaOapg.properties.file_content, str, ],
        compiled_flg: typing.Union[MetaOapg.properties.compiled_flg, str, ],
        file_name: typing.Union[MetaOapg.properties.file_name, str, ],
        version_number: typing.Union[MetaOapg.properties.version_number, str, ],
        entry_point: typing.Union[MetaOapg.properties.entry_point, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        schema_info: typing.Union[MetaOapg.properties.schema_info, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ImportDeviceAppJsonBody':
        return super().__new__(
            cls,
            *_args,
            app_name=app_name,
            file_content=file_content,
            compiled_flg=compiled_flg,
            file_name=file_name,
            version_number=version_number,
            entry_point=entry_point,
            comment=comment,
            schema_info=schema_info,
            _configuration=_configuration,
            **kwargs,
        )
