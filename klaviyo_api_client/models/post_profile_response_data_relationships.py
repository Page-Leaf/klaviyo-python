from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_profile_response_data_relationships_lists import PostProfileResponseDataRelationshipsLists
    from ..models.post_profile_response_data_relationships_segments import PostProfileResponseDataRelationshipsSegments


T = TypeVar("T", bound="PostProfileResponseDataRelationships")


@_attrs_define
class PostProfileResponseDataRelationships:
    """
    Attributes:
        lists (Union[Unset, PostProfileResponseDataRelationshipsLists]):
        segments (Union[Unset, PostProfileResponseDataRelationshipsSegments]):
    """

    lists: Union[Unset, "PostProfileResponseDataRelationshipsLists"] = UNSET
    segments: Union[Unset, "PostProfileResponseDataRelationshipsSegments"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lists: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lists, Unset):
            lists = self.lists.to_dict()

        segments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.segments, Unset):
            segments = self.segments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lists is not UNSET:
            field_dict["lists"] = lists
        if segments is not UNSET:
            field_dict["segments"] = segments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_profile_response_data_relationships_lists import PostProfileResponseDataRelationshipsLists
        from ..models.post_profile_response_data_relationships_segments import (
            PostProfileResponseDataRelationshipsSegments,
        )

        d = src_dict.copy()
        _lists = d.pop("lists", UNSET)
        lists: Union[Unset, PostProfileResponseDataRelationshipsLists]
        if isinstance(_lists, Unset):
            lists = UNSET
        else:
            lists = PostProfileResponseDataRelationshipsLists.from_dict(_lists)

        _segments = d.pop("segments", UNSET)
        segments: Union[Unset, PostProfileResponseDataRelationshipsSegments]
        if isinstance(_segments, Unset):
            segments = UNSET
        else:
            segments = PostProfileResponseDataRelationshipsSegments.from_dict(_segments)

        post_profile_response_data_relationships = cls(
            lists=lists,
            segments=segments,
        )

        post_profile_response_data_relationships.additional_properties = d
        return post_profile_response_data_relationships

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
