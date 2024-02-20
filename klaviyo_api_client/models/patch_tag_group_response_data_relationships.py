from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_tag_group_response_data_relationships_tags import PatchTagGroupResponseDataRelationshipsTags


T = TypeVar("T", bound="PatchTagGroupResponseDataRelationships")


@_attrs_define
class PatchTagGroupResponseDataRelationships:
    """
    Attributes:
        tags (Union[Unset, PatchTagGroupResponseDataRelationshipsTags]):
    """

    tags: Union[Unset, "PatchTagGroupResponseDataRelationshipsTags"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_tag_group_response_data_relationships_tags import PatchTagGroupResponseDataRelationshipsTags

        d = src_dict.copy()
        _tags = d.pop("tags", UNSET)
        tags: Union[Unset, PatchTagGroupResponseDataRelationshipsTags]
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = PatchTagGroupResponseDataRelationshipsTags.from_dict(_tags)

        patch_tag_group_response_data_relationships = cls(
            tags=tags,
        )

        patch_tag_group_response_data_relationships.additional_properties = d
        return patch_tag_group_response_data_relationships

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
