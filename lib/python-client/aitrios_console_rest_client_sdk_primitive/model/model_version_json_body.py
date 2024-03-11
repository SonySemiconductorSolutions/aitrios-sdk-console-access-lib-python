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


class ModelVersionJsonBody(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            version_number = schemas.StrSchema
            iteration_id = schemas.StrSchema
            iteration_name = schemas.StrSchema
            accuracy = schemas.StrSchema
            model_performances = schemas.DictSchema
            latest_flg = schemas.StrSchema
            publish_latest_flg = schemas.StrSchema
            version_status = schemas.StrSchema
            org_file_name = schemas.StrSchema
            org_file_size = schemas.IntSchema
            publish_file_name = schemas.StrSchema
            publish_file_size = schemas.IntSchema
            model_file_size = schemas.IntSchema
            model_framework = schemas.StrSchema
            conv_id = schemas.StrSchema
            
            
            class labels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'labels':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            stage = schemas.StrSchema
            result = schemas.StrSchema
            kpi = schemas.DictSchema
            
            
            class converter_log(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.DictSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'converter_log':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            convert_start_date = schemas.StrSchema
            convert_end_date = schemas.StrSchema
            publish_start_date = schemas.StrSchema
            publish_end_date = schemas.StrSchema
            version_comment = schemas.StrSchema
            version_ins_date = schemas.StrSchema
            version_upd_date = schemas.StrSchema
            __annotations__ = {
                "version_number": version_number,
                "iteration_id": iteration_id,
                "iteration_name": iteration_name,
                "accuracy": accuracy,
                "model_performances": model_performances,
                "latest_flg": latest_flg,
                "publish_latest_flg": publish_latest_flg,
                "version_status": version_status,
                "org_file_name": org_file_name,
                "org_file_size": org_file_size,
                "publish_file_name": publish_file_name,
                "publish_file_size": publish_file_size,
                "model_file_size": model_file_size,
                "model_framework": model_framework,
                "conv_id": conv_id,
                "labels": labels,
                "stage": stage,
                "result": result,
                "kpi": kpi,
                "converter_log": converter_log,
                "convert_start_date": convert_start_date,
                "convert_end_date": convert_end_date,
                "publish_start_date": publish_start_date,
                "publish_end_date": publish_end_date,
                "version_comment": version_comment,
                "version_ins_date": version_ins_date,
                "version_upd_date": version_upd_date,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_number"]) -> MetaOapg.properties.version_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iteration_id"]) -> MetaOapg.properties.iteration_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iteration_name"]) -> MetaOapg.properties.iteration_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accuracy"]) -> MetaOapg.properties.accuracy: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_performances"]) -> MetaOapg.properties.model_performances: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latest_flg"]) -> MetaOapg.properties.latest_flg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publish_latest_flg"]) -> MetaOapg.properties.publish_latest_flg: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_status"]) -> MetaOapg.properties.version_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_file_name"]) -> MetaOapg.properties.org_file_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_file_size"]) -> MetaOapg.properties.org_file_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publish_file_name"]) -> MetaOapg.properties.publish_file_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publish_file_size"]) -> MetaOapg.properties.publish_file_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_file_size"]) -> MetaOapg.properties.model_file_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_framework"]) -> MetaOapg.properties.model_framework: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conv_id"]) -> MetaOapg.properties.conv_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> MetaOapg.properties.labels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stage"]) -> MetaOapg.properties.stage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kpi"]) -> MetaOapg.properties.kpi: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["converter_log"]) -> MetaOapg.properties.converter_log: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["convert_start_date"]) -> MetaOapg.properties.convert_start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["convert_end_date"]) -> MetaOapg.properties.convert_end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publish_start_date"]) -> MetaOapg.properties.publish_start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publish_end_date"]) -> MetaOapg.properties.publish_end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_comment"]) -> MetaOapg.properties.version_comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_ins_date"]) -> MetaOapg.properties.version_ins_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_upd_date"]) -> MetaOapg.properties.version_upd_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version_number", "iteration_id", "iteration_name", "accuracy", "model_performances", "latest_flg", "publish_latest_flg", "version_status", "org_file_name", "org_file_size", "publish_file_name", "publish_file_size", "model_file_size", "model_framework", "conv_id", "labels", "stage", "result", "kpi", "converter_log", "convert_start_date", "convert_end_date", "publish_start_date", "publish_end_date", "version_comment", "version_ins_date", "version_upd_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_number"]) -> typing.Union[MetaOapg.properties.version_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iteration_id"]) -> typing.Union[MetaOapg.properties.iteration_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iteration_name"]) -> typing.Union[MetaOapg.properties.iteration_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accuracy"]) -> typing.Union[MetaOapg.properties.accuracy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_performances"]) -> typing.Union[MetaOapg.properties.model_performances, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latest_flg"]) -> typing.Union[MetaOapg.properties.latest_flg, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publish_latest_flg"]) -> typing.Union[MetaOapg.properties.publish_latest_flg, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_status"]) -> typing.Union[MetaOapg.properties.version_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_file_name"]) -> typing.Union[MetaOapg.properties.org_file_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_file_size"]) -> typing.Union[MetaOapg.properties.org_file_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publish_file_name"]) -> typing.Union[MetaOapg.properties.publish_file_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publish_file_size"]) -> typing.Union[MetaOapg.properties.publish_file_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_file_size"]) -> typing.Union[MetaOapg.properties.model_file_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_framework"]) -> typing.Union[MetaOapg.properties.model_framework, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conv_id"]) -> typing.Union[MetaOapg.properties.conv_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> typing.Union[MetaOapg.properties.labels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stage"]) -> typing.Union[MetaOapg.properties.stage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> typing.Union[MetaOapg.properties.result, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kpi"]) -> typing.Union[MetaOapg.properties.kpi, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["converter_log"]) -> typing.Union[MetaOapg.properties.converter_log, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["convert_start_date"]) -> typing.Union[MetaOapg.properties.convert_start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["convert_end_date"]) -> typing.Union[MetaOapg.properties.convert_end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publish_start_date"]) -> typing.Union[MetaOapg.properties.publish_start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publish_end_date"]) -> typing.Union[MetaOapg.properties.publish_end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_comment"]) -> typing.Union[MetaOapg.properties.version_comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_ins_date"]) -> typing.Union[MetaOapg.properties.version_ins_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_upd_date"]) -> typing.Union[MetaOapg.properties.version_upd_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version_number", "iteration_id", "iteration_name", "accuracy", "model_performances", "latest_flg", "publish_latest_flg", "version_status", "org_file_name", "org_file_size", "publish_file_name", "publish_file_size", "model_file_size", "model_framework", "conv_id", "labels", "stage", "result", "kpi", "converter_log", "convert_start_date", "convert_end_date", "publish_start_date", "publish_end_date", "version_comment", "version_ins_date", "version_upd_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        version_number: typing.Union[MetaOapg.properties.version_number, str, schemas.Unset] = schemas.unset,
        iteration_id: typing.Union[MetaOapg.properties.iteration_id, str, schemas.Unset] = schemas.unset,
        iteration_name: typing.Union[MetaOapg.properties.iteration_name, str, schemas.Unset] = schemas.unset,
        accuracy: typing.Union[MetaOapg.properties.accuracy, str, schemas.Unset] = schemas.unset,
        model_performances: typing.Union[MetaOapg.properties.model_performances, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        latest_flg: typing.Union[MetaOapg.properties.latest_flg, str, schemas.Unset] = schemas.unset,
        publish_latest_flg: typing.Union[MetaOapg.properties.publish_latest_flg, str, schemas.Unset] = schemas.unset,
        version_status: typing.Union[MetaOapg.properties.version_status, str, schemas.Unset] = schemas.unset,
        org_file_name: typing.Union[MetaOapg.properties.org_file_name, str, schemas.Unset] = schemas.unset,
        org_file_size: typing.Union[MetaOapg.properties.org_file_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        publish_file_name: typing.Union[MetaOapg.properties.publish_file_name, str, schemas.Unset] = schemas.unset,
        publish_file_size: typing.Union[MetaOapg.properties.publish_file_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        model_file_size: typing.Union[MetaOapg.properties.model_file_size, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        model_framework: typing.Union[MetaOapg.properties.model_framework, str, schemas.Unset] = schemas.unset,
        conv_id: typing.Union[MetaOapg.properties.conv_id, str, schemas.Unset] = schemas.unset,
        labels: typing.Union[MetaOapg.properties.labels, list, tuple, schemas.Unset] = schemas.unset,
        stage: typing.Union[MetaOapg.properties.stage, str, schemas.Unset] = schemas.unset,
        result: typing.Union[MetaOapg.properties.result, str, schemas.Unset] = schemas.unset,
        kpi: typing.Union[MetaOapg.properties.kpi, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        converter_log: typing.Union[MetaOapg.properties.converter_log, list, tuple, schemas.Unset] = schemas.unset,
        convert_start_date: typing.Union[MetaOapg.properties.convert_start_date, str, schemas.Unset] = schemas.unset,
        convert_end_date: typing.Union[MetaOapg.properties.convert_end_date, str, schemas.Unset] = schemas.unset,
        publish_start_date: typing.Union[MetaOapg.properties.publish_start_date, str, schemas.Unset] = schemas.unset,
        publish_end_date: typing.Union[MetaOapg.properties.publish_end_date, str, schemas.Unset] = schemas.unset,
        version_comment: typing.Union[MetaOapg.properties.version_comment, str, schemas.Unset] = schemas.unset,
        version_ins_date: typing.Union[MetaOapg.properties.version_ins_date, str, schemas.Unset] = schemas.unset,
        version_upd_date: typing.Union[MetaOapg.properties.version_upd_date, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelVersionJsonBody':
        return super().__new__(
            cls,
            *_args,
            version_number=version_number,
            iteration_id=iteration_id,
            iteration_name=iteration_name,
            accuracy=accuracy,
            model_performances=model_performances,
            latest_flg=latest_flg,
            publish_latest_flg=publish_latest_flg,
            version_status=version_status,
            org_file_name=org_file_name,
            org_file_size=org_file_size,
            publish_file_name=publish_file_name,
            publish_file_size=publish_file_size,
            model_file_size=model_file_size,
            model_framework=model_framework,
            conv_id=conv_id,
            labels=labels,
            stage=stage,
            result=result,
            kpi=kpi,
            converter_log=converter_log,
            convert_start_date=convert_start_date,
            convert_end_date=convert_end_date,
            publish_start_date=publish_start_date,
            publish_end_date=publish_end_date,
            version_comment=version_comment,
            version_ins_date=version_ins_date,
            version_upd_date=version_upd_date,
            _configuration=_configuration,
            **kwargs,
        )
