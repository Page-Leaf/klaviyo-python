from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.campaign_recipient_estimation_job_enum import CampaignRecipientEstimationJobEnum

if TYPE_CHECKING:
    from ..models.object_links import ObjectLinks
    from ..models.post_campaign_recipient_estimation_job_response_data_attributes import (
        PostCampaignRecipientEstimationJobResponseDataAttributes,
    )


T = TypeVar("T", bound="PostCampaignRecipientEstimationJobResponseData")


@_attrs_define
class PostCampaignRecipientEstimationJobResponseData:
    """
    Attributes:
        type (CampaignRecipientEstimationJobEnum):
        id (str): The ID of the campaign used for estimating recipients Example: 01GMRWDSA0ARTAKE1SFX8JGXAY.
        attributes (PostCampaignRecipientEstimationJobResponseDataAttributes):
        links (ObjectLinks):
    """

    type: CampaignRecipientEstimationJobEnum
    id: str
    attributes: "PostCampaignRecipientEstimationJobResponseDataAttributes"
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
        from ..models.object_links import ObjectLinks
        from ..models.post_campaign_recipient_estimation_job_response_data_attributes import (
            PostCampaignRecipientEstimationJobResponseDataAttributes,
        )

        d = src_dict.copy()
        type = CampaignRecipientEstimationJobEnum(d.pop("type"))

        id = d.pop("id")

        attributes = PostCampaignRecipientEstimationJobResponseDataAttributes.from_dict(d.pop("attributes"))

        links = ObjectLinks.from_dict(d.pop("links"))

        post_campaign_recipient_estimation_job_response_data = cls(
            type=type,
            id=id,
            attributes=attributes,
            links=links,
        )

        post_campaign_recipient_estimation_job_response_data.additional_properties = d
        return post_campaign_recipient_estimation_job_response_data

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
