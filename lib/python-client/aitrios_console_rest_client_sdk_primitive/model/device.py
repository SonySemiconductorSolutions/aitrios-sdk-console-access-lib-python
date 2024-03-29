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


class Device(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "ins_date",
            "upd_id",
            "device_id",
            "upd_date",
            "connectionState",
            "ins_id",
            "lastActivityTime",
        }
        
        class properties:
            device_id = schemas.StrSchema
            ins_id = schemas.StrSchema
            ins_date = schemas.StrSchema
            upd_id = schemas.StrSchema
            upd_date = schemas.StrSchema
            connectionState = schemas.StrSchema
            lastActivityTime = schemas.StrSchema
            place = schemas.StrSchema
            comment = schemas.StrSchema
            
            
            class _property(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "device_name",
                        "internal_device_id",
                    }
                    
                    class properties:
                        device_name = schemas.StrSchema
                        internal_device_id = schemas.StrSchema
                        __annotations__ = {
                            "device_name": device_name,
                            "internal_device_id": internal_device_id,
                        }
                
                device_name: MetaOapg.properties.device_name
                internal_device_id: MetaOapg.properties.internal_device_id
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["device_name"]) -> MetaOapg.properties.device_name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["internal_device_id"]) -> MetaOapg.properties.internal_device_id: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_name", "internal_device_id", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["device_name"]) -> MetaOapg.properties.device_name: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["internal_device_id"]) -> MetaOapg.properties.internal_device_id: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_name", "internal_device_id", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    device_name: typing.Union[MetaOapg.properties.device_name, str, ],
                    internal_device_id: typing.Union[MetaOapg.properties.internal_device_id, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> '_property':
                    return super().__new__(
                        cls,
                        *_args,
                        device_name=device_name,
                        internal_device_id=internal_device_id,
                        _configuration=_configuration,
                        **kwargs,
                    )
            device_type = schemas.StrSchema
            display_device_type = schemas.StrSchema
            
            
            class models(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                model_version_id = schemas.StrSchema
                                __annotations__ = {
                                    "model_version_id": model_version_id,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["model_version_id"]) -> MetaOapg.properties.model_version_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["model_version_id", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["model_version_id"]) -> typing.Union[MetaOapg.properties.model_version_id, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["model_version_id", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            model_version_id: typing.Union[MetaOapg.properties.model_version_id, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                model_version_id=model_version_id,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'models':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class device_groups(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            required = {
                                "ins_date",
                                "upd_id",
                                "device_group_id",
                                "upd_date",
                                "device_type",
                                "ins_id",
                            }
                            
                            class properties:
                                device_group_id = schemas.StrSchema
                                device_type = schemas.StrSchema
                                comment = schemas.StrSchema
                                ins_id = schemas.StrSchema
                                ins_date = schemas.StrSchema
                                upd_id = schemas.StrSchema
                                upd_date = schemas.StrSchema
                                __annotations__ = {
                                    "device_group_id": device_group_id,
                                    "device_type": device_type,
                                    "comment": comment,
                                    "ins_id": ins_id,
                                    "ins_date": ins_date,
                                    "upd_id": upd_id,
                                    "upd_date": upd_date,
                                }
                        
                        ins_date: MetaOapg.properties.ins_date
                        upd_id: MetaOapg.properties.upd_id
                        device_group_id: MetaOapg.properties.device_group_id
                        upd_date: MetaOapg.properties.upd_date
                        device_type: MetaOapg.properties.device_type
                        ins_id: MetaOapg.properties.ins_id
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["device_group_id"]) -> MetaOapg.properties.device_group_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["device_type"]) -> MetaOapg.properties.device_type: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ins_id"]) -> MetaOapg.properties.ins_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["ins_date"]) -> MetaOapg.properties.ins_date: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["upd_id"]) -> MetaOapg.properties.upd_id: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["upd_date"]) -> MetaOapg.properties.upd_date: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_group_id", "device_type", "comment", "ins_id", "ins_date", "upd_id", "upd_date", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["device_group_id"]) -> MetaOapg.properties.device_group_id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["device_type"]) -> MetaOapg.properties.device_type: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ins_id"]) -> MetaOapg.properties.ins_id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["ins_date"]) -> MetaOapg.properties.ins_date: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["upd_id"]) -> MetaOapg.properties.upd_id: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["upd_date"]) -> MetaOapg.properties.upd_date: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_group_id", "device_type", "comment", "ins_id", "ins_date", "upd_id", "upd_date", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            ins_date: typing.Union[MetaOapg.properties.ins_date, str, ],
                            upd_id: typing.Union[MetaOapg.properties.upd_id, str, ],
                            device_group_id: typing.Union[MetaOapg.properties.device_group_id, str, ],
                            upd_date: typing.Union[MetaOapg.properties.upd_date, str, ],
                            device_type: typing.Union[MetaOapg.properties.device_type, str, ],
                            ins_id: typing.Union[MetaOapg.properties.ins_id, str, ],
                            comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                ins_date=ins_date,
                                upd_id=upd_id,
                                device_group_id=device_group_id,
                                upd_date=upd_date,
                                device_type=device_type,
                                ins_id=ins_id,
                                comment=comment,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'device_groups':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            configuration = schemas.DictSchema
            state = schemas.DictSchema
            
            
            class command_results(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                command_name = schemas.StrSchema
                                result = schemas.StrSchema
                                execute_time = schemas.StrSchema
                                __annotations__ = {
                                    "command_name": command_name,
                                    "result": result,
                                    "execute_time": execute_time,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["command_name"]) -> MetaOapg.properties.command_name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["execute_time"]) -> MetaOapg.properties.execute_time: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["command_name", "result", "execute_time", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["command_name"]) -> typing.Union[MetaOapg.properties.command_name, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> typing.Union[MetaOapg.properties.result, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["execute_time"]) -> typing.Union[MetaOapg.properties.execute_time, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["command_name", "result", "execute_time", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            command_name: typing.Union[MetaOapg.properties.command_name, str, schemas.Unset] = schemas.unset,
                            result: typing.Union[MetaOapg.properties.result, str, schemas.Unset] = schemas.unset,
                            execute_time: typing.Union[MetaOapg.properties.execute_time, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                command_name=command_name,
                                result=result,
                                execute_time=execute_time,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'command_results':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class apps(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                name = schemas.StrSchema
                                version = schemas.StrSchema
                                comment = schemas.StrSchema
                                __annotations__ = {
                                    "name": name,
                                    "version": version,
                                    "comment": comment,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "version", "comment", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "version", "comment", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                            version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
                            comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                name=name,
                                version=version,
                                comment=comment,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'apps':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "device_id": device_id,
                "ins_id": ins_id,
                "ins_date": ins_date,
                "upd_id": upd_id,
                "upd_date": upd_date,
                "connectionState": connectionState,
                "lastActivityTime": lastActivityTime,
                "place": place,
                "comment": comment,
                "property": _property,
                "device_type": device_type,
                "display_device_type": display_device_type,
                "models": models,
                "device_groups": device_groups,
                "configuration": configuration,
                "state": state,
                "command_results": command_results,
                "apps": apps,
            }
    
    ins_date: MetaOapg.properties.ins_date
    upd_id: MetaOapg.properties.upd_id
    device_id: MetaOapg.properties.device_id
    upd_date: MetaOapg.properties.upd_date
    connectionState: MetaOapg.properties.connectionState
    ins_id: MetaOapg.properties.ins_id
    lastActivityTime: MetaOapg.properties.lastActivityTime
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ins_id"]) -> MetaOapg.properties.ins_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ins_date"]) -> MetaOapg.properties.ins_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upd_id"]) -> MetaOapg.properties.upd_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upd_date"]) -> MetaOapg.properties.upd_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionState"]) -> MetaOapg.properties.connectionState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastActivityTime"]) -> MetaOapg.properties.lastActivityTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["place"]) -> MetaOapg.properties.place: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["property"]) -> MetaOapg.properties._property: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_type"]) -> MetaOapg.properties.device_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_device_type"]) -> MetaOapg.properties.display_device_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["models"]) -> MetaOapg.properties.models: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_groups"]) -> MetaOapg.properties.device_groups: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> MetaOapg.properties.configuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["command_results"]) -> MetaOapg.properties.command_results: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apps"]) -> MetaOapg.properties.apps: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["device_id", "ins_id", "ins_date", "upd_id", "upd_date", "connectionState", "lastActivityTime", "place", "comment", "property", "device_type", "display_device_type", "models", "device_groups", "configuration", "state", "command_results", "apps", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_id"]) -> MetaOapg.properties.device_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ins_id"]) -> MetaOapg.properties.ins_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ins_date"]) -> MetaOapg.properties.ins_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upd_id"]) -> MetaOapg.properties.upd_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upd_date"]) -> MetaOapg.properties.upd_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionState"]) -> MetaOapg.properties.connectionState: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastActivityTime"]) -> MetaOapg.properties.lastActivityTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["place"]) -> typing.Union[MetaOapg.properties.place, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["property"]) -> typing.Union[MetaOapg.properties._property, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_type"]) -> typing.Union[MetaOapg.properties.device_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_device_type"]) -> typing.Union[MetaOapg.properties.display_device_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["models"]) -> typing.Union[MetaOapg.properties.models, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_groups"]) -> typing.Union[MetaOapg.properties.device_groups, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union[MetaOapg.properties.configuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["command_results"]) -> typing.Union[MetaOapg.properties.command_results, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apps"]) -> typing.Union[MetaOapg.properties.apps, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["device_id", "ins_id", "ins_date", "upd_id", "upd_date", "connectionState", "lastActivityTime", "place", "comment", "property", "device_type", "display_device_type", "models", "device_groups", "configuration", "state", "command_results", "apps", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ins_date: typing.Union[MetaOapg.properties.ins_date, str, ],
        upd_id: typing.Union[MetaOapg.properties.upd_id, str, ],
        device_id: typing.Union[MetaOapg.properties.device_id, str, ],
        upd_date: typing.Union[MetaOapg.properties.upd_date, str, ],
        connectionState: typing.Union[MetaOapg.properties.connectionState, str, ],
        ins_id: typing.Union[MetaOapg.properties.ins_id, str, ],
        lastActivityTime: typing.Union[MetaOapg.properties.lastActivityTime, str, ],
        place: typing.Union[MetaOapg.properties.place, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        device_type: typing.Union[MetaOapg.properties.device_type, str, schemas.Unset] = schemas.unset,
        display_device_type: typing.Union[MetaOapg.properties.display_device_type, str, schemas.Unset] = schemas.unset,
        models: typing.Union[MetaOapg.properties.models, list, tuple, schemas.Unset] = schemas.unset,
        device_groups: typing.Union[MetaOapg.properties.device_groups, list, tuple, schemas.Unset] = schemas.unset,
        configuration: typing.Union[MetaOapg.properties.configuration, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        command_results: typing.Union[MetaOapg.properties.command_results, list, tuple, schemas.Unset] = schemas.unset,
        apps: typing.Union[MetaOapg.properties.apps, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Device':
        return super().__new__(
            cls,
            *_args,
            ins_date=ins_date,
            upd_id=upd_id,
            device_id=device_id,
            upd_date=upd_date,
            connectionState=connectionState,
            ins_id=ins_id,
            lastActivityTime=lastActivityTime,
            place=place,
            comment=comment,
            device_type=device_type,
            display_device_type=display_device_type,
            models=models,
            device_groups=device_groups,
            configuration=configuration,
            state=state,
            command_results=command_results,
            apps=apps,
            _configuration=_configuration,
            **kwargs,
        )
