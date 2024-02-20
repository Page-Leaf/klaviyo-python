from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.campaign_values_request_dto_resource_object_attributes_statistics_item import (
    CampaignValuesRequestDTOResourceObjectAttributesStatisticsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_timeframe import CustomTimeframe
    from ..models.timeframe import Timeframe


T = TypeVar("T", bound="CampaignValuesRequestDTOResourceObjectAttributes")


@_attrs_define
class CampaignValuesRequestDTOResourceObjectAttributes:
    """
    Attributes:
        statistics (List[CampaignValuesRequestDTOResourceObjectAttributesStatisticsItem]): List of statistics to query
            for. All rate statistics will be returned in fractional form [0.0, 1.0] Example: ['opens', 'open_rate'].
        timeframe (Union['CustomTimeframe', 'Timeframe']): The timeframe to query for data within. The max length a
            timeframe can be is 1 year
        conversion_metric_id (str): ID of the metric to be used for conversion statistics Example: RESQ6t.
        filter_ (Union[Unset, str]): API filter string used to filter the query.
            Allowed filters are send_channel, campaign_id.
            Allowed operators are equals, contains-any.
            Only one filter can be used per attribute, only AND can be used as a combination operator.
            Max of 100 messages per ANY filter. Example: and(equals(campaign_id,"abc123"),contains-
            any(send_channel,["email","sms"])).
    """

    statistics: List[CampaignValuesRequestDTOResourceObjectAttributesStatisticsItem]
    timeframe: Union["CustomTimeframe", "Timeframe"]
    conversion_metric_id: str
    filter_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.timeframe import Timeframe

        statistics = []
        for statistics_item_data in self.statistics:
            statistics_item = statistics_item_data.value
            statistics.append(statistics_item)

        timeframe: Dict[str, Any]
        if isinstance(self.timeframe, Timeframe):
            timeframe = self.timeframe.to_dict()
        else:
            timeframe = self.timeframe.to_dict()

        conversion_metric_id = self.conversion_metric_id

        filter_ = self.filter_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statistics": statistics,
                "timeframe": timeframe,
                "conversion_metric_id": conversion_metric_id,
            }
        )
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_timeframe import CustomTimeframe
        from ..models.timeframe import Timeframe

        d = src_dict.copy()
        statistics = []
        _statistics = d.pop("statistics")
        for statistics_item_data in _statistics:
            statistics_item = CampaignValuesRequestDTOResourceObjectAttributesStatisticsItem(statistics_item_data)

            statistics.append(statistics_item)

        def _parse_timeframe(data: object) -> Union["CustomTimeframe", "Timeframe"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                timeframe_type_0 = Timeframe.from_dict(data)

                return timeframe_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            timeframe_type_1 = CustomTimeframe.from_dict(data)

            return timeframe_type_1

        timeframe = _parse_timeframe(d.pop("timeframe"))

        conversion_metric_id = d.pop("conversion_metric_id")

        filter_ = d.pop("filter", UNSET)

        campaign_values_request_dto_resource_object_attributes = cls(
            statistics=statistics,
            timeframe=timeframe,
            conversion_metric_id=conversion_metric_id,
            filter_=filter_,
        )

        campaign_values_request_dto_resource_object_attributes.additional_properties = d
        return campaign_values_request_dto_resource_object_attributes

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
