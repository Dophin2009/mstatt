from __future__ import annotations

import enum

from mstat.exception import ParseException


class RecordStatus(enum.Enum):
    JOINED = 1
    LEFT = 2

    @classmethod
    def from_str(cls, s: str) -> RecordStatus:
        if s == 'Joined':
            return cls.JOINED
        elif s == 'Left':
            return cls.LEFT
        else:
            raise ParseException()
