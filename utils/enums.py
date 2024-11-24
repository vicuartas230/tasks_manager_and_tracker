from enum import Enum, auto

priority_map = {
        1: "High",
        2: "Medium",
        3: "Low"
    }

status_map = {
    1: "Pending",
    2: "In-progress",
    3: "Completed"
}


class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

    @classmethod
    def parse_priority(cls, value):
        mapping = {
            "High": cls.HIGH,
            "Medium": cls.MEDIUM,
            "Low": cls.LOW
        }

        return mapping[value]


class Status(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()

    @classmethod
    def parse_status(cls, value):
        mapping = {
            "Pending": cls.PENDING,
            "In-progress": cls.IN_PROGRESS,
            "Completed": cls.COMPLETED
        }

        return mapping[value]
