from typing import Iterator


def get_row_index(rows: int) -> Iterator[int]:
    current = 0
    step = 1
    while True:
        yield current
        current += step
        if current == 0 or current == rows - 1:
            step = -step


def zigzag(s: str, rows: int) -> str:
    if rows == 1:
        return s
    char_rows = [[] for _ in range(rows)]
    for i, row_index in zip(range(len(s)), get_row_index(rows)):
        char_rows[row_index].append(s[i])

    return "".join([char for row in char_rows for char in row])


print(zigzag("ABCDEF", 2))
