from __future__ import annotations

import csv
from typing import List

from record import Record


def __read_rows(filename: str, encoding='utf-8') -> List[List[str]]:
    with open(filename, encoding=encoding) as file:
        reader = csv.reader(file, delimiter='\t')
        return [row for row in reader][1:]


def read_records(filename: str, encoding='utf-8') -> List[Record]:
    return [Record.from_row(row) for row in __read_rows(filename, encoding)]
