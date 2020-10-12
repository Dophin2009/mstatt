from __future__ import annotations

import csv
from typing import List

from record import Record
from record import User


def read_rows(filename: str, encoding='utf-16') -> List[List[str]]:
    with open(filename, encoding=encoding) as file:
        reader = csv.reader(file, delimiter='\t')
        return [row for row in reader][1:]


def read_records(filename: str, encoding='utf-16') -> List[Record]:
    return [Record.from_row(row) for row in read_rows(filename, encoding)]


records = read_records('2020-09-29.csv')
for u in User.from_multiple_record_list(records):
    print(u)
