from enum import Enum


class GetFlowActionMessagesFieldsflowMessageItem(str, Enum):
    CHANNEL = "channel"
    CONTENT = "content"
    CREATED = "created"
    NAME = "name"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
