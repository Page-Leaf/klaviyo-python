from enum import Enum


class GetCatalogItemCategoriesFieldscatalogCategoryItem(str, Enum):
    EXTERNAL_ID = "external_id"
    NAME = "name"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
