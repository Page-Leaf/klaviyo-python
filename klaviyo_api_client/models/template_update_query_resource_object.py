from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_enum import TemplateEnum

if TYPE_CHECKING:
    from ..models.template_update_query_resource_object_attributes import TemplateUpdateQueryResourceObjectAttributes


T = TypeVar("T", bound="TemplateUpdateQueryResourceObject")


@_attrs_define
class TemplateUpdateQueryResourceObject:
    """
    Attributes:
        type (TemplateEnum):
        id (str): The ID of template
        attributes (TemplateUpdateQueryResourceObjectAttributes):
    """

    type: TemplateEnum
    id: str
    attributes: "TemplateUpdateQueryResourceObjectAttributes"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id

        attributes = self.attributes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.template_update_query_resource_object_attributes import (
            TemplateUpdateQueryResourceObjectAttributes,
        )

        d = src_dict.copy()
        type = TemplateEnum(d.pop("type"))

        id = d.pop("id")

        attributes = TemplateUpdateQueryResourceObjectAttributes.from_dict(d.pop("attributes"))

        template_update_query_resource_object = cls(
            type=type,
            id=id,
            attributes=attributes,
        )

        template_update_query_resource_object.additional_properties = d
        return template_update_query_resource_object

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
