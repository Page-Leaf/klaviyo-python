from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.profile_enum import ProfileEnum

T = TypeVar("T", bound="GetEventResponseCompoundDocumentDataRelationshipsProfileData")


@_attrs_define
class GetEventResponseCompoundDocumentDataRelationshipsProfileData:
    """
    Attributes:
        type (ProfileEnum):
        id (str): Profile ID of the associated profile, if available
    """

    type: ProfileEnum
    id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ProfileEnum(d.pop("type"))

        id = d.pop("id")

        get_event_response_compound_document_data_relationships_profile_data = cls(
            type=type,
            id=id,
        )

        get_event_response_compound_document_data_relationships_profile_data.additional_properties = d
        return get_event_response_compound_document_data_relationships_profile_data

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
