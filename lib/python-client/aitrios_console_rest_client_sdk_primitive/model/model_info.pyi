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


class ModelInfo(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            model_id = schemas.StrSchema
            model_type = schemas.StrSchema
            functionality = schemas.StrSchema
            vendor_name = schemas.StrSchema
            model_comment = schemas.StrSchema
            network_type = schemas.StrSchema
            create_by = schemas.StrSchema
            package_id = schemas.StrSchema
            product_id = schemas.StrSchema
            metadata_format_id = schemas.StrSchema
            
            
            class projects(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ModelProjectOfModelInfo']:
                        return ModelProjectOfModelInfo
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ModelProjectOfModelInfo'], typing.List['ModelProjectOfModelInfo']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'projects':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ModelProjectOfModelInfo':
                    return super().__getitem__(i)
            __annotations__ = {
                "model_id": model_id,
                "model_type": model_type,
                "functionality": functionality,
                "vendor_name": vendor_name,
                "model_comment": model_comment,
                "network_type": network_type,
                "create_by": create_by,
                "package_id": package_id,
                "product_id": product_id,
                "metadata_format_id": metadata_format_id,
                "projects": projects,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_id"]) -> MetaOapg.properties.model_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_type"]) -> MetaOapg.properties.model_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functionality"]) -> MetaOapg.properties.functionality: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendor_name"]) -> MetaOapg.properties.vendor_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_comment"]) -> MetaOapg.properties.model_comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network_type"]) -> MetaOapg.properties.network_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_by"]) -> MetaOapg.properties.create_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["package_id"]) -> MetaOapg.properties.package_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["product_id"]) -> MetaOapg.properties.product_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata_format_id"]) -> MetaOapg.properties.metadata_format_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projects"]) -> MetaOapg.properties.projects: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["model_id", "model_type", "functionality", "vendor_name", "model_comment", "network_type", "create_by", "package_id", "product_id", "metadata_format_id", "projects", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_id"]) -> typing.Union[MetaOapg.properties.model_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_type"]) -> typing.Union[MetaOapg.properties.model_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functionality"]) -> typing.Union[MetaOapg.properties.functionality, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendor_name"]) -> typing.Union[MetaOapg.properties.vendor_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_comment"]) -> typing.Union[MetaOapg.properties.model_comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network_type"]) -> typing.Union[MetaOapg.properties.network_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_by"]) -> typing.Union[MetaOapg.properties.create_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["package_id"]) -> typing.Union[MetaOapg.properties.package_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["product_id"]) -> typing.Union[MetaOapg.properties.product_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata_format_id"]) -> typing.Union[MetaOapg.properties.metadata_format_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projects"]) -> typing.Union[MetaOapg.properties.projects, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["model_id", "model_type", "functionality", "vendor_name", "model_comment", "network_type", "create_by", "package_id", "product_id", "metadata_format_id", "projects", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        model_id: typing.Union[MetaOapg.properties.model_id, str, schemas.Unset] = schemas.unset,
        model_type: typing.Union[MetaOapg.properties.model_type, str, schemas.Unset] = schemas.unset,
        functionality: typing.Union[MetaOapg.properties.functionality, str, schemas.Unset] = schemas.unset,
        vendor_name: typing.Union[MetaOapg.properties.vendor_name, str, schemas.Unset] = schemas.unset,
        model_comment: typing.Union[MetaOapg.properties.model_comment, str, schemas.Unset] = schemas.unset,
        network_type: typing.Union[MetaOapg.properties.network_type, str, schemas.Unset] = schemas.unset,
        create_by: typing.Union[MetaOapg.properties.create_by, str, schemas.Unset] = schemas.unset,
        package_id: typing.Union[MetaOapg.properties.package_id, str, schemas.Unset] = schemas.unset,
        product_id: typing.Union[MetaOapg.properties.product_id, str, schemas.Unset] = schemas.unset,
        metadata_format_id: typing.Union[MetaOapg.properties.metadata_format_id, str, schemas.Unset] = schemas.unset,
        projects: typing.Union[MetaOapg.properties.projects, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ModelInfo':
        return super().__new__(
            cls,
            *_args,
            model_id=model_id,
            model_type=model_type,
            functionality=functionality,
            vendor_name=vendor_name,
            model_comment=model_comment,
            network_type=network_type,
            create_by=create_by,
            package_id=package_id,
            product_id=product_id,
            metadata_format_id=metadata_format_id,
            projects=projects,
            _configuration=_configuration,
            **kwargs,
        )

from aitrios_console_rest_client_sdk_primitive.model.model_project_of_model_info import ModelProjectOfModelInfo
