from enum import Enum


class GetCouponCodesFieldscouponCodeItem(str, Enum):
    EXPIRES_AT = "expires_at"
    STATUS = "status"
    UNIQUE_CODE = "unique_code"

    def __str__(self) -> str:
        return str(self.value)
