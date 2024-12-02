import pytest

from main import part1, part2, read_reports, is_safe, count_safe_reports

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 2


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 0


def test_read_reports():
    # Given
    lines = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9"
    ]
    # When
    reports = read_reports(lines)
    # Then
    assert reports == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]
    ]


@pytest.mark.parametrize("report, expected",
                         [([7, 6, 4, 2, 1], True),
                          ([1, 2, 7, 8, 9], False),
                          ([9, 7, 6, 2, 1], False),
                          ([1, 3, 2, 4, 5], False),
                          ([8, 6, 4, 4, 1], False),
                          ([1, 3, 6, 7, 9], True)
                          ])
def test_is_safe(report, expected):
    # Given
    # When
    result = is_safe(report)
    # Then
    assert result == expected


def test_count_safe_reports():
    # Given
    reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]
    ]
    # When
    result = count_safe_reports(reports)
    # Then
    assert result == 2
