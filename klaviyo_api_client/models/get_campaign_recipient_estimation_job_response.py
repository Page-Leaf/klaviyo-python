from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.campaign_recipient_estimation_job_response_object_resource import (
        CampaignRecipientEstimationJobResponseObjectResource,
    )


T = TypeVar("T", bound="GetCampaignRecipientEstimationJobResponse")


@_attrs_define
class GetCampaignRecipientEstimationJobResponse:
    """
    Attributes:
        data (CampaignRecipientEstimationJobResponseObjectResource):
    """

    data: "CampaignRecipientEstimationJobResponseObjectResource"
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
        from ..models.campaign_recipient_estimation_job_response_object_resource import (
            CampaignRecipientEstimationJobResponseObjectResource,
        )

        d = src_dict.copy()
        data = CampaignRecipientEstimationJobResponseObjectResource.from_dict(d.pop("data"))

        get_campaign_recipient_estimation_job_response = cls(
            data=data,
        )

        get_campaign_recipient_estimation_job_response.additional_properties = d
        return get_campaign_recipient_estimation_job_response

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
