import pytest

from main import part1, part2, parse_input, get_antinodes, count_unique_antinodes

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 14


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 0


def test_parse_input():
    # Given
    lines = [
        "............",
        "........0...",
        ".....0......",
        ".......0....",
        "....0.......",
        "......A.....",
        "............",
        "............",
        "........A...",
        ".........A..",
        "............",
        "............",
    ]
    # When
    antennas, city_dimensions = parse_input(lines)
    # Then
    assert antennas == {
        '0': {(8, 1), (5, 2), (7, 3), (4, 4)},
        'A': {(6, 5), (8, 8), (9, 9)}
    }
    assert city_dimensions == (12, 12)


@pytest.mark.parametrize("first_antenna, second_antenna, expected",
                         [((8, 1), (5, 2), {(11, 0), (2, 3)}),
                          ((8, 1), (7, 3), {(6, 5)}),
                          ((8, 1), (4, 4), {(0, 7)}),
                          ((5, 2), (7, 3), {(3, 1), (9, 4)}),
                          ((5, 2), (4, 4), {(6, 0), (3, 6)}),
                          ((7, 3), (4, 4), {(10, 2), (1, 5)}),
                          ((6, 5), (8, 8), {(4, 2), (10, 11)}),
                          ((6, 5), (9, 9), {(3, 1)}),
                          ((8, 8), (9, 9), {(7, 7), (10, 10)}),
                          ])
def test_get_antinodes(first_antenna, second_antenna, expected):
    # Given
    city_dimensions = (12, 12)
    # When
    result = get_antinodes(first_antenna, second_antenna, city_dimensions)
    # Then
    assert result == expected


def test_count_unique_antinodes():
    # Given
    antennas = {
        '0': {(8, 1), (5, 2), (7, 3), (4, 4)},
        'A': {(6, 5), (8, 8), (9, 9)}
    }
    city_dimensions = (12, 12)
    # When
    result = count_unique_antinodes(antennas, city_dimensions)
    # Then
    assert result == 14
