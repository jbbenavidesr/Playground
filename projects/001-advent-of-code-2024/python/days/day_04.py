from typing import Iterable

WordSearch = Iterable[str]

LOOKUP_WORD = "XMAS"

DIRECTIONS = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
]


def extract_words(
    starting_position: tuple[int, int], word_search: WordSearch, length: int
) -> list[str]:
    """Get all the words of length that can be extracted starting on given position

    Parameters:
    -----------
    starting_position: the tuple with the postion for starting the word lookup
    word_search: the word search where the words should be extracted from
    length: the length of words that will be extracted
    """

    words = []

    for direction in DIRECTIONS:
        word = ""
        x, y = starting_position
        for _ in range(length):
            if x < 0 or y < 0:
                break

            try:
                word += word_search[y][x]
            except IndexError:
                break

            x, y = (
                x + direction[0],
                y + direction[1],
            )

        if len(word) == length:
            words.append(word)

    return words


def challenge_1(word_search: WordSearch) -> int:
    """Count the number of times the word shows up in the word search"""

    count = 0

    for y, line in enumerate(word_search):
        for x in range(len(line)):
            if word_search[y][x] != LOOKUP_WORD[0]:
                continue

            words = extract_words(
                starting_position=(x, y),
                word_search=word_search,
                length=len(LOOKUP_WORD),
            )

            count += words.count(LOOKUP_WORD)

    return count


def parse_input(input_string: str) -> WordSearch:
    """Turn the input file into a 2D array of letters"""
    return input_string.split("\n")


def solve(word_search: WordSearch) -> list[str]:

    result_1 = challenge_1(word_search)

    return [f"The word {LOOKUP_WORD} show's up {result_1} times."]
