from __future__ import annotations

import csv
from typing import List

from .record import Record
from .record import User


def __read_rows(filename: str, encoding='utf-8') -> List[List[str]]:
    with open(filename, encoding=encoding) as file:
        reader = csv.reader(file, delimiter='\t')
        return [row for row in reader][1:]


def read_records(filename: str, encoding='utf-8') -> List[Record]:
    return [Record.from_row(row) for row in __read_rows(filename, encoding)]


def read_users(filename: str, encoding='utf-8') -> List[User]:
    return User.from_multiple_record_list(read_records(filename, encoding))
