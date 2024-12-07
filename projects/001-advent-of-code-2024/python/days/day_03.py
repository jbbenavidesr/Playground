import re


def product(list_: list) -> int:
    prod = 1
    for i in list_:
        prod *= i

    return prod


def parse_input(raw_input: str) -> list[list[int]]:
    return [
        re.findall(r"\d+", match)
        for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", raw_input)
    ]


def solve(input: list[list[int]]):

    result_1 = sum(product([int(i) for i in match]) for match in input)

    return [f"The result is: {result_1}"]
