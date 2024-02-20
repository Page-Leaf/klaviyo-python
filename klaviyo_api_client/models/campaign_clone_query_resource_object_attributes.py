from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CampaignCloneQueryResourceObjectAttributes")


@_attrs_define
class CampaignCloneQueryResourceObjectAttributes:
    """
    Attributes:
        new_name (Union[Unset, str]): The name for the new cloned campaign Example: My cloned campaign's new name.
    """

    new_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_name = self.new_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_name is not UNSET:
            field_dict["new_name"] = new_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_name = d.pop("new_name", UNSET)

        campaign_clone_query_resource_object_attributes = cls(
            new_name=new_name,
        )

        campaign_clone_query_resource_object_attributes.additional_properties = d
        return campaign_clone_query_resource_object_attributes

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
