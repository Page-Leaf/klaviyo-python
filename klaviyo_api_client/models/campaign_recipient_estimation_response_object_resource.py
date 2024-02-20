from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.campaign_recipient_estimation_enum import CampaignRecipientEstimationEnum

if TYPE_CHECKING:
    from ..models.campaign_recipient_estimation_response_object_resource_attributes import (
        CampaignRecipientEstimationResponseObjectResourceAttributes,
    )
    from ..models.object_links import ObjectLinks


T = TypeVar("T", bound="CampaignRecipientEstimationResponseObjectResource")


@_attrs_define
class CampaignRecipientEstimationResponseObjectResource:
    """
    Attributes:
        type (CampaignRecipientEstimationEnum):
        id (str): The ID of the campaign for which to get the estimated number of recipients
        attributes (CampaignRecipientEstimationResponseObjectResourceAttributes):
        links (ObjectLinks):
    """

    type: CampaignRecipientEstimationEnum
    id: str
    attributes: "CampaignRecipientEstimationResponseObjectResourceAttributes"
    links: "ObjectLinks"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id

        attributes = self.attributes.to_dict()

        links = self.links.to_dict()

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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.campaign_recipient_estimation_response_object_resource_attributes import (
            CampaignRecipientEstimationResponseObjectResourceAttributes,
        )
        from ..models.object_links import ObjectLinks

        d = src_dict.copy()
        type = CampaignRecipientEstimationEnum(d.pop("type"))

        id = d.pop("id")

        attributes = CampaignRecipientEstimationResponseObjectResourceAttributes.from_dict(d.pop("attributes"))

        links = ObjectLinks.from_dict(d.pop("links"))

        campaign_recipient_estimation_response_object_resource = cls(
            type=type,
            id=id,
            attributes=attributes,
            links=links,
        )

        campaign_recipient_estimation_response_object_resource.additional_properties = d
        return campaign_recipient_estimation_response_object_resource

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
