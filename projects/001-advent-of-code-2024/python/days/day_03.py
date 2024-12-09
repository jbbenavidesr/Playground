import operator
import re
from functools import reduce
from numbers import Number
from typing import Iterable, Iterator


def extract_operations_from_memory(
    computer_memory: str,
) -> Iterator[re.Match]:
    """Extract all multiplication pairs from the corrupted memory file.

    Multiplication pairs are all that can be found exactly like "mul(X,Y)"
    """

    multiplication_instruction_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    return re.finditer(multiplication_instruction_pattern, computer_memory)


def get_multiplication_pair_from_operation(operation: re.Match) -> tuple[int, int]:
    """Get the numbers that need to be multiplied from an extracted operation"""
    return tuple(map(int, operation.groups()))


def multiply(obj: Iterable[Number]) -> Number:
    """Multiply a sequence of numbers"""
    return reduce(operator.mul, obj, 1)


def challenge_1(computer_memory: str) -> int:
    """Get multiplications out of corrupted memory file"""
    return sum(
        multiply(get_multiplication_pair_from_operation(operation))
        for operation in extract_operations_from_memory(computer_memory)
    )


def challenge_2(computer_memory: str) -> int:
    """Get multiplications out of corrupted memory file, taking into account conditional
    operations that enable or disable processing.
    """

    conditional_pattern = r"(don't\(\)|do\(\))"

    split = re.split(conditional_pattern, computer_memory)

    enabled = True
    total = 0
    for fragment in split:
        if fragment == "do()":
            enabled = True
        elif fragment == "don't()":
            enabled = False
        elif enabled:
            total += challenge_1(fragment)

    return total


def solve(computer_memory: str):

    result_1 = challenge_1(computer_memory)

    result_2 = challenge_2(computer_memory)

    return [f"The result is: {result_1}", f"Result with conditionals is: {result_2}"]
