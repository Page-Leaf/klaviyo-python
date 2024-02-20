from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.profile_enum import ProfileEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_member_response_object_resource_attributes import ListMemberResponseObjectResourceAttributes
    from ..models.object_links import ObjectLinks


T = TypeVar("T", bound="ListMemberResponseObjectResource")


@_attrs_define
class ListMemberResponseObjectResource:
    """
    Attributes:
        type (ProfileEnum):
        attributes (ListMemberResponseObjectResourceAttributes):
        links (ObjectLinks):
        id (Union[Unset, str]): Primary key that uniquely identifies this profile. Generated by Klaviyo. Example:
            01GDDKASAP8TKDDA2GRZDSVP4H.
    """

    type: ProfileEnum
    attributes: "ListMemberResponseObjectResourceAttributes"
    links: "ObjectLinks"
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        attributes = self.attributes.to_dict()

        links = self.links.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "attributes": attributes,
                "links": links,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_member_response_object_resource_attributes import ListMemberResponseObjectResourceAttributes
        from ..models.object_links import ObjectLinks

        d = src_dict.copy()
        type = ProfileEnum(d.pop("type"))

        attributes = ListMemberResponseObjectResourceAttributes.from_dict(d.pop("attributes"))

        links = ObjectLinks.from_dict(d.pop("links"))

        id = d.pop("id", UNSET)

        list_member_response_object_resource = cls(
            type=type,
            attributes=attributes,
            links=links,
            id=id,
        )

        list_member_response_object_resource.additional_properties = d
        return list_member_response_object_resource

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