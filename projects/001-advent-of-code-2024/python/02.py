from pathlib import Path
from argparse import ArgumentParser


def verify_step(
    step: int, direction: int, max_step: int = 3, min_step: int = 1
) -> bool:

    return step * direction < 0 or abs(step) < min_step or abs(step) > max_step


def is_report_safe(report: list[int]) -> bool:
    """Check if a report is safe.

    A report is considered safe if it is gradually increasing or decreasing. That is:
    - The levels are either all increasing or all decreasing
    - The difference between two consecutive levels is at least 1 and at most 3
    """

    direction = report[1] - report[0]

    for i in range(len(report) - 1):
        step = report[i + 1] - report[i]

        if verify_step(step, direction):
            return False

    return True


def challenge_1(reports: list[list[int]]):
    """Count the number of reports which are safe"""

    return sum(is_report_safe(report) for report in reports)


def challenge_2(reports: list[list[int]]):
    return None


def parse_input(input_file: Path) -> list[list[int]]:
    """Parse the input file."""

    with input_file.open() as file:
        return [[int(level) for level in line.split()] for line in file]


def main():

    parser = ArgumentParser()
    parser.add_argument("input_file", type=Path)
    args = parser.parse_args()
    input_file = args.input_file

    if not input_file.exists():
        print(f"File {input_file} does not exist.")
        return

    reports = parse_input(input_file)
    result = challenge_1(reports)

    print(f"Safe Reports: {result}")

    result = challenge_2(reports)

    print(f"Safe Reports with Dampner: {result}")


if __name__ == "__main__":
    main()
