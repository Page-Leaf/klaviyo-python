from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.profile_enum import ProfileEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.onsite_profile_create_query_resource_object_attributes import (
        OnsiteProfileCreateQueryResourceObjectAttributes,
    )
    from ..models.onsite_profile_meta import OnsiteProfileMeta


T = TypeVar("T", bound="OnsiteProfileCreateQueryResourceObject")


@_attrs_define
class OnsiteProfileCreateQueryResourceObject:
    """
    Attributes:
        type (ProfileEnum):
        attributes (OnsiteProfileCreateQueryResourceObjectAttributes):
        id (Union[Unset, str]): Primary key that uniquely identifies this profile. Generated by Klaviyo. Example:
            01GDDKASAP8TKDDA2GRZDSVP4H.
        meta (Union[Unset, OnsiteProfileMeta]):
    """

    type: ProfileEnum
    attributes: "OnsiteProfileCreateQueryResourceObjectAttributes"
    id: Union[Unset, str] = UNSET
    meta: Union[Unset, "OnsiteProfileMeta"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        attributes = self.attributes.to_dict()

        id = self.id

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "attributes": attributes,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.onsite_profile_create_query_resource_object_attributes import (
            OnsiteProfileCreateQueryResourceObjectAttributes,
        )
        from ..models.onsite_profile_meta import OnsiteProfileMeta

        d = src_dict.copy()
        type = ProfileEnum(d.pop("type"))

        attributes = OnsiteProfileCreateQueryResourceObjectAttributes.from_dict(d.pop("attributes"))

        id = d.pop("id", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, OnsiteProfileMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = OnsiteProfileMeta.from_dict(_meta)

        onsite_profile_create_query_resource_object = cls(
            type=type,
            attributes=attributes,
            id=id,
            meta=meta,
        )

        onsite_profile_create_query_resource_object.additional_properties = d
        return onsite_profile_create_query_resource_object

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
