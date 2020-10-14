from __future__ import annotations

import csv
from typing import List
from typing import TextIO

from mstat.record import Record
from mstat.record import User


def __read_rows(file: TextIO) -> List[List[str]]:
    reader = csv.reader(file, delimiter='\t')
    return [row for row in reader][1:]


def read_records(file: TextIO) -> List[Record]:
    return [Record.from_row(row) for row in __read_rows(file)]


def read_users(file: TextIO) -> List[User]:
    return User.from_multiple_record_list(read_records(file))
