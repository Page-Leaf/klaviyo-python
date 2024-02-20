from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.patch_list_partial_update_response_data import PatchListPartialUpdateResponseData


T = TypeVar("T", bound="PatchListPartialUpdateResponse")


@_attrs_define
class PatchListPartialUpdateResponse:
    """
    Attributes:
        data (PatchListPartialUpdateResponseData):
    """

    data: "PatchListPartialUpdateResponseData"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patch_list_partial_update_response_data import PatchListPartialUpdateResponseData

        d = src_dict.copy()
        data = PatchListPartialUpdateResponseData.from_dict(d.pop("data"))

        patch_list_partial_update_response = cls(
            data=data,
        )

        patch_list_partial_update_response.additional_properties = d
        return patch_list_partial_update_response

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
