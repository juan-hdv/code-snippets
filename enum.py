from enum import Enum


class IndexingCategories(Enum):
    """Placement Aggregates indexig categories"""
    VETTINGS = 1
    REQUIREMENTS = 2
    PROMOTIONS = 3

    @staticmethod
    def alla(self):
        return {cat.value for cat in self}


print(IndexingCategories.alla())
