from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_campaign_recipient_estimation_job_response_data_attributes_status import (
    PostCampaignRecipientEstimationJobResponseDataAttributesStatus,
)

T = TypeVar("T", bound="PostCampaignRecipientEstimationJobResponseDataAttributes")


@_attrs_define
class PostCampaignRecipientEstimationJobResponseDataAttributes:
    """
    Attributes:
        status (PostCampaignRecipientEstimationJobResponseDataAttributesStatus): The status of the recipient estimation
            job
    """

    status: PostCampaignRecipientEstimationJobResponseDataAttributesStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        status = PostCampaignRecipientEstimationJobResponseDataAttributesStatus(d.pop("status"))

        post_campaign_recipient_estimation_job_response_data_attributes = cls(
            status=status,
        )

        post_campaign_recipient_estimation_job_response_data_attributes.additional_properties = d
        return post_campaign_recipient_estimation_job_response_data_attributes

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