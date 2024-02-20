from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attribution_enum import AttributionEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attribution_response_object_resource_relationships import (
        AttributionResponseObjectResourceRelationships,
    )
    from ..models.object_links import ObjectLinks


T = TypeVar("T", bound="AttributionResponseObjectResource")


@_attrs_define
class AttributionResponseObjectResource:
    """
    Attributes:
        type (AttributionEnum):
        id (str): The ID of the attribution Example: 925e385b52fb405715f3616c337cc65c.
        links (ObjectLinks):
        relationships (Union[Unset, AttributionResponseObjectResourceRelationships]):
    """

    type: AttributionEnum
    id: str
    links: "ObjectLinks"
    relationships: Union[Unset, "AttributionResponseObjectResourceRelationships"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id

        links = self.links.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
                "links": links,
            }
        )
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attribution_response_object_resource_relationships import (
            AttributionResponseObjectResourceRelationships,
        )
        from ..models.object_links import ObjectLinks

        d = src_dict.copy()
        type = AttributionEnum(d.pop("type"))

        id = d.pop("id")

        links = ObjectLinks.from_dict(d.pop("links"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, AttributionResponseObjectResourceRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = AttributionResponseObjectResourceRelationships.from_dict(_relationships)

        attribution_response_object_resource = cls(
            type=type,
            id=id,
            links=links,
            relationships=relationships,
        )

        attribution_response_object_resource.additional_properties = d
        return attribution_response_object_resource

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
