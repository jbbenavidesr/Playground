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


def is_report_safe_with_dampener(report: list[int]) -> bool:

    if is_report_safe(report):
        return True

    for i in range(len(report)):
        if is_report_safe(report[:i] + report[i + 1 :]):
            return True

    return False


def challenge_2(reports: list[list[int]]):
    """Count the number of safe reports after applying the Problem Dampener"""
    return sum(is_report_safe_with_dampener(report) for report in reports)


def parse_input(raw_input: str) -> list[list[int]]:
    """Parse the input file."""

    return [[int(level) for level in line.split()] for line in raw_input]


def solve(reports: list[list[int]]):

    result_1 = challenge_1(reports)
    result_2 = challenge_2(reports)

    return [
        f"Safe Reports: {result_1}",
        f"Safe Reports with Problem Dampener: {result_2}",
    ]
