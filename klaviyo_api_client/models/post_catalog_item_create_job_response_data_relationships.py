from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_catalog_item_create_job_response_data_relationships_items import (
        PostCatalogItemCreateJobResponseDataRelationshipsItems,
    )


T = TypeVar("T", bound="PostCatalogItemCreateJobResponseDataRelationships")


@_attrs_define
class PostCatalogItemCreateJobResponseDataRelationships:
    """
    Attributes:
        items (Union[Unset, PostCatalogItemCreateJobResponseDataRelationshipsItems]):
    """

    items: Union[Unset, "PostCatalogItemCreateJobResponseDataRelationshipsItems"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.items, Unset):
            items = self.items.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_catalog_item_create_job_response_data_relationships_items import (
            PostCatalogItemCreateJobResponseDataRelationshipsItems,
        )

        d = src_dict.copy()
        _items = d.pop("items", UNSET)
        items: Union[Unset, PostCatalogItemCreateJobResponseDataRelationshipsItems]
        if isinstance(_items, Unset):
            items = UNSET
        else:
            items = PostCatalogItemCreateJobResponseDataRelationshipsItems.from_dict(_items)

        post_catalog_item_create_job_response_data_relationships = cls(
            items=items,
        )

        post_catalog_item_create_job_response_data_relationships.additional_properties = d
        return post_catalog_item_create_job_response_data_relationships

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
