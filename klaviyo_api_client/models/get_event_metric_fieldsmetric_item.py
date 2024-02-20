from enum import Enum


class GetEventMetricFieldsmetricItem(str, Enum):
    CREATED = "created"
    INTEGRATION = "integration"
    NAME = "name"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
