from enum import Enum


class FlowSeriesRequestDTOResourceObjectAttributesInterval(str, Enum):
    DAILY = "daily"
    HOURLY = "hourly"
    MONTHLY = "monthly"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
