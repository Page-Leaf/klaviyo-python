from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_category_bulk_update_job_enum import CatalogCategoryBulkUpdateJobEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_category_update_job_response_object_resource_attributes import (
        CatalogCategoryUpdateJobResponseObjectResourceAttributes,
    )
    from ..models.get_catalog_category_update_job_response_compound_document_data_relationships import (
        GetCatalogCategoryUpdateJobResponseCompoundDocumentDataRelationships,
    )
    from ..models.object_links import ObjectLinks


T = TypeVar("T", bound="GetCatalogCategoryUpdateJobResponseCompoundDocumentData")


@_attrs_define
class GetCatalogCategoryUpdateJobResponseCompoundDocumentData:
    """
    Attributes:
        type (CatalogCategoryBulkUpdateJobEnum):
        id (str): Unique identifier for retrieving the job. Generated by Klaviyo.
        attributes (CatalogCategoryUpdateJobResponseObjectResourceAttributes):
        links (ObjectLinks):
        relationships (Union[Unset, GetCatalogCategoryUpdateJobResponseCompoundDocumentDataRelationships]):
    """

    type: CatalogCategoryBulkUpdateJobEnum
    id: str
    attributes: "CatalogCategoryUpdateJobResponseObjectResourceAttributes"
    links: "ObjectLinks"
    relationships: Union[Unset, "GetCatalogCategoryUpdateJobResponseCompoundDocumentDataRelationships"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id

        attributes = self.attributes.to_dict()

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
                "attributes": attributes,
                "links": links,
            }
        )
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_category_update_job_response_object_resource_attributes import (
            CatalogCategoryUpdateJobResponseObjectResourceAttributes,
        )
        from ..models.get_catalog_category_update_job_response_compound_document_data_relationships import (
            GetCatalogCategoryUpdateJobResponseCompoundDocumentDataRelationships,
        )
        from ..models.object_links import ObjectLinks

        d = src_dict.copy()
        type = CatalogCategoryBulkUpdateJobEnum(d.pop("type"))

        id = d.pop("id")

        attributes = CatalogCategoryUpdateJobResponseObjectResourceAttributes.from_dict(d.pop("attributes"))

        links = ObjectLinks.from_dict(d.pop("links"))

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[Unset, GetCatalogCategoryUpdateJobResponseCompoundDocumentDataRelationships]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = GetCatalogCategoryUpdateJobResponseCompoundDocumentDataRelationships.from_dict(
                _relationships
            )

        get_catalog_category_update_job_response_compound_document_data = cls(
            type=type,
            id=id,
            attributes=attributes,
            links=links,
            relationships=relationships,
        )

        get_catalog_category_update_job_response_compound_document_data.additional_properties = d
        return get_catalog_category_update_job_response_compound_document_data

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
