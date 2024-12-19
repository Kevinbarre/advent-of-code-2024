import pytest

from main import part1, part2, parse_towels, check_design, count_possible_designs

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 6


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 0


def test_parse_towels():
    # Given
    lines = [
        "r, wr, b, g, bwu, rb, gb, br",
        "",
        "brwrr",
        "bggr",
        "gbbr",
        "rrbgbr",
        "ubwu",
        "bwurrg",
        "brgr",
        "bbrgwb"
    ]
    # When
    towels, designs = parse_towels(lines)
    # Then
    assert towels == {"r", "wr", "b", "g", "bwu", "rb", "gb", "br"}
    assert designs == [
        "brwrr",
        "bggr",
        "gbbr",
        "rrbgbr",
        "ubwu",
        "bwurrg",
        "brgr",
        "bbrgwb"
    ]


@pytest.mark.parametrize("design, expected",
                         [("brwrr", ["br", "wr", "r"]),
                          ("bggr", ["b", "g", "g", "r"]),
                          ("gbbr", ["gb", "br"]),
                          ("rrbgbr", ["r", "rb", "gb", "r"]),  # ["r", "rb", "g", "br"]), # Other possible design, but not the one found
                          ("ubwu", False),
                          ("bwurrg", ["bwu", "r", "r", "g"]),
                          ("brgr", ["br", "g", "r"]),
                          ("bbrgwb", False)
                          ]
                         )
def test_check_design(design, expected):
    # Given
    towels = {"r", "wr", "b", "g", "bwu", "rb", "gb", "br"}
    # When
    result = check_design(design, towels)
    # Then
    assert result == expected


def test_count_possible_designs():
    # Given
    towels = {"r", "wr", "b", "g", "bwu", "rb", "gb", "br"}
    designs = [
        "brwrr",
        "bggr",
        "gbbr",
        "rrbgbr",
        "ubwu",
        "bwurrg",
        "brgr",
        "bbrgwb"
    ]
    # When
    result = count_possible_designs(designs, towels)
    # Then
    assert result == 6
