from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_catalog_category_delete_job_response_data_relationships_categories import (
        PostCatalogCategoryDeleteJobResponseDataRelationshipsCategories,
    )


T = TypeVar("T", bound="PostCatalogCategoryDeleteJobResponseDataRelationships")


@_attrs_define
class PostCatalogCategoryDeleteJobResponseDataRelationships:
    """
    Attributes:
        categories (Union[Unset, PostCatalogCategoryDeleteJobResponseDataRelationshipsCategories]):
    """

    categories: Union[Unset, "PostCatalogCategoryDeleteJobResponseDataRelationshipsCategories"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        categories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_catalog_category_delete_job_response_data_relationships_categories import (
            PostCatalogCategoryDeleteJobResponseDataRelationshipsCategories,
        )

        d = src_dict.copy()
        _categories = d.pop("categories", UNSET)
        categories: Union[Unset, PostCatalogCategoryDeleteJobResponseDataRelationshipsCategories]
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = PostCatalogCategoryDeleteJobResponseDataRelationshipsCategories.from_dict(_categories)

        post_catalog_category_delete_job_response_data_relationships = cls(
            categories=categories,
        )

        post_catalog_category_delete_job_response_data_relationships.additional_properties = d
        return post_catalog_category_delete_job_response_data_relationships

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