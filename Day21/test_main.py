import pytest

from main import part1, part2, get_shortest_sequence_length, get_complexity

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 126384


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 0


@pytest.mark.parametrize("code, expected",
                         [("029A", 68),
                          ("980A", 60),
                          ("179A", 68),
                          ("456A", 64),
                          ("379A", 64)
                          ])
def test_get_shortest_sequence_length(code, expected):
    # Given
    depth = 3
    # When
    result = get_shortest_sequence_length(code, depth)
    # Then
    assert result == expected


@pytest.mark.parametrize("code, expected",
                         [("029A", 68 * 29),
                          ("980A", 60 * 980),
                          ("179A", 68 * 179),
                          ("456A", 64 * 456),
                          ("379A", 64 * 379)
                          ])
def test_get_complexity(code, expected):
    # Given
    depth = 3
    # When
    result = get_complexity(code, depth)
    # Then
    assert result == expected
