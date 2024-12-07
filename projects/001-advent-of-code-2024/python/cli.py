import sys
from pathlib import Path
from typing import Callable
from argparse import ArgumentParser
import importlib


def import_day_module(day: int):
    """
    Dynamically import the module for the specified day.

    :param day: Day number

    :return: Imported module
    """
    try:
        return importlib.import_module(f"days.day_{day:02d}")
    except ImportError:
        print(f"Error: No solution found for Day {day}")
        sys.exit(1)


def read_input[T](input_file: Path, parser: Callable[[str], T] = lambda x: x) -> T:
    """
    Read the input file and return the necessary data parsed according to the parser
    function. If no parser function is passed, just return the file content as a string.

    :param input_path: Path to the input file
    :param parser: Function for parsing the content of the file

    :return: Contents of the input file as a string
    """

    try:
        with input_file.open("r") as file:
            return parser(file.read())
    except FileNotFoundError:
        print(
            f"Error: file {input_file} was not found, check that the path is correct."
        )
        sys.exit(1)


def run_challenge(day: int, input_file: Path) -> list[str]:
    """Run challenges for a specific day.


    :param day: Day number
    :param input_path: Path to input file

    :returns list with formatted solutions to the challenges
    """

    challenge_module = import_day_module(day)

    input = read_input(input_file, challenge_module.parse_input)

    return challenge_module.solve(input)


def show_solutions(solutions: list[str]) -> None:
    """Display the solutions in the desired format"""
    for solution in solutions:
        print(solution)


def main():

    parser = ArgumentParser(
        description=(
            "A CLI application for running the challenges of the Advent Of Code 2024"
        )
    )
    parser.add_argument("day", type=int, help="Day of the challenge")
    parser.add_argument("input_file", type=Path, help="Path to the input file")
    args = parser.parse_args()

    solutions = run_challenge(args.day, args.input_file)

    show_solutions(solutions)


if __name__ == "__main__":
    main()
