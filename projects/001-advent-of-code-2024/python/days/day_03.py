import operator
import re
from functools import reduce
from numbers import Number
from typing import Iterable, Iterator


def extract_multiplications_from_memory(
    computer_memory: str,
) -> Iterator[Iterable[int, int]]:
    """Extract all multiplication pairs from the corrupted memory file.

    Multiplication pairs are all that can be found exactly like "mul(X,Y)"
    """

    multiplication_instruction_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    for match in re.finditer(multiplication_instruction_pattern, computer_memory):
        yield map(int, match.groups())


def multiply(obj: Iterable[Number]) -> Number:
    """Multiply a sequence of numbers"""
    return reduce(operator.mul, obj, 1)


def challenge_1(computer_memory: str) -> int:
    """Get multiplications out of corrupted memory file"""
    return sum(
        multiply(mul_pair)
        for mul_pair in extract_multiplications_from_memory(computer_memory)
    )


def solve(computer_memory: str):

    result_1 = challenge_1(computer_memory)

    return [f"The result is: {result_1}"]
