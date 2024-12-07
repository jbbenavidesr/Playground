def challenge_1(list_1: list, list_2: list):
    """Calculate the total distance between the two lists.

    The distance between the lists is calculated as follows:
    - order the lists in ascending order
    - the distance between two elements is the absolute difference between them
    - the total distance is the sum of the distances between the elements
    """

    list_1.sort()
    list_2.sort()

    total_distance = 0
    for a, b in zip(list_1, list_2):
        total_distance += abs(a - b)

    return total_distance


def challenge_2(list_1: list, list_2: list):
    """Calculates the similarity score between the two lists.

    The similarity score is calculated as follows:
    - For each element in list_1, find how many times it appears in list_2
    - Add the given element multiplied by the number of appearances to the total score
    """

    similarity_score = 0
    for a in list_1:
        similarity_score += a * list_2.count(a)

    return similarity_score


def parse_input(raw_input: str) -> tuple[list[int], list[int]]:
    """Parse the input file and return the two lists."""

    list_1 = []
    list_2 = []

    for line in raw_input.splitlines():
        chars = line.split()
        list_1.append(int(chars[0]))
        list_2.append(int(chars[1]))

    return list_1, list_2


def solve(input: tuple[list[int], list[int]]) -> list[str]:

    result_1 = challenge_1(*input)

    result_2 = challenge_2(*input)

    return [f"Total distance: {result_1}", f"Similarity score: {result_2}"]
