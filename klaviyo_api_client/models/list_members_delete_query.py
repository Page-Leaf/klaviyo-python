from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_members_delete_query_data_item import ListMembersDeleteQueryDataItem


T = TypeVar("T", bound="ListMembersDeleteQuery")


@_attrs_define
class ListMembersDeleteQuery:
    """
    Attributes:
        data (List['ListMembersDeleteQueryDataItem']):
    """

    data: List["ListMembersDeleteQueryDataItem"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

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
        from ..models.list_members_delete_query_data_item import ListMembersDeleteQueryDataItem

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ListMembersDeleteQueryDataItem.from_dict(data_item_data)

            data.append(data_item)

        list_members_delete_query = cls(
            data=data,
        )

        list_members_delete_query.additional_properties = d
        return list_members_delete_query

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
