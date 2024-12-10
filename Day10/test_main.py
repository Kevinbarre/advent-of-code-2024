import pytest

from main import part1, part2, parse_input, find_trailheads, get_trailhead_score, get_neighbours, find_hiking_trails, get_sum_trailhead_scores, \
    get_trailhead_rating, get_sum_trailhead_ratings

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 36


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 81


def test_parse_input():
    # Given
    lines = [
        "89010123",
        "78121874",
        "87430965",
        "96549874",
        "45678903",
        "32019012",
        "01329801",
        "10456732"
    ]
    # When
    result = parse_input(lines)
    # Then
    assert result == [
        [8, 9, 0, 1, 0, 1, 2, 3],
        [7, 8, 1, 2, 1, 8, 7, 4],
        [8, 7, 4, 3, 0, 9, 6, 5],
        [9, 6, 5, 4, 9, 8, 7, 4],
        [4, 5, 6, 7, 8, 9, 0, 3],
        [3, 2, 0, 1, 9, 0, 1, 2],
        [0, 1, 3, 2, 9, 8, 0, 1],
        [1, 0, 4, 5, 6, 7, 3, 2]
    ]


def test_find_trailheads():
    # Given
    topographic_map = [
        [8, 9, 0, 1, 0, 1, 2, 3],
        [7, 8, 1, 2, 1, 8, 7, 4],
        [8, 7, 4, 3, 0, 9, 6, 5],
        [9, 6, 5, 4, 9, 8, 7, 4],
        [4, 5, 6, 7, 8, 9, 0, 3],
        [3, 2, 0, 1, 9, 0, 1, 2],
        [0, 1, 3, 2, 9, 8, 0, 1],
        [1, 0, 4, 5, 6, 7, 3, 2]
    ]
    # When
    result = find_trailheads(topographic_map)
    # Then
    assert result == {(2, 0), (4, 0), (4, 2), (6, 4), (2, 5), (5, 5), (0, 6), (6, 6), (1, 7)}


@pytest.mark.parametrize("trailhead, expected",
                         [((2, 0), {(1, 0), (3, 0), (2, 1)}),
                          ((0, 7), {(1, 7), (0, 6)})
                          ])
def test_get_neighbours(trailhead, expected):
    # Given
    topographic_map = [
        [8, 9, 0, 1, 0, 1, 2, 3],
        [7, 8, 1, 2, 1, 8, 7, 4],
        [8, 7, 4, 3, 0, 9, 6, 5],
        [9, 6, 5, 4, 9, 8, 7, 4],
        [4, 5, 6, 7, 8, 9, 0, 3],
        [3, 2, 0, 1, 9, 0, 1, 2],
        [0, 1, 3, 2, 9, 8, 0, 1],
        [1, 0, 4, 5, 6, 7, 3, 2]
    ]
    # When
    result = get_neighbours(trailhead, topographic_map)
    # Then
    assert result == expected


def test_find_hiking_trails():
    # Given
    trailhead = (2, 0)
    topographic_map = [
        [8, 9, 0, 1, 0, 1, 2, 3],
        [7, 8, 1, 2, 1, 8, 7, 4],
        [8, 7, 4, 3, 0, 9, 6, 5],
        [9, 6, 5, 4, 9, 8, 7, 4],
        [4, 5, 6, 7, 8, 9, 0, 3],
        [3, 2, 0, 1, 9, 0, 1, 2],
        [0, 1, 3, 2, 9, 8, 0, 1],
        [1, 0, 4, 5, 6, 7, 3, 2]
    ]
    # When
    result = find_hiking_trails(trailhead, topographic_map)
    # Then
    assert result == {
        # Paths to first 9
        ((2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (1, 2), (1, 1), (1, 0)),
        ((2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (1, 0)),
        ((2, 0), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (1, 2), (1, 1), (1, 0)),
        ((2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (1, 0)),
        # Paths to second 9
        ((2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (1, 2), (0, 2), (0, 3)),
        ((2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (0, 2), (0, 3)),
        ((2, 0), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (1, 2), (0, 2), (0, 3)),
        ((2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (0, 2), (0, 3)),
        # Paths to third 9
        ((2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 3)),
        ((2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (2, 4), (3, 4), (4, 4), (4, 3)),
        ((2, 0), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 3)),
        ((2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (2, 4), (3, 4), (4, 4), (4, 3)),
        # Paths to fourth 9
        ((2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (5, 4)),
        ((2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (2, 4), (3, 4), (4, 4), (5, 4)),
        ((2, 0), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (5, 4)),
        ((2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (2, 4), (3, 4), (4, 4), (5, 4)),
        # Paths to fifth 9
        ((2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5)),
        ((2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5)),
        ((2, 0), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5)),
        ((2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5)),
    }


def test_get_trailhead_score():
    # Given
    trailhead = (2, 0)
    topographic_map = [
        [8, 9, 0, 1, 0, 1, 2, 3],
        [7, 8, 1, 2, 1, 8, 7, 4],
        [8, 7, 4, 3, 0, 9, 6, 5],
        [9, 6, 5, 4, 9, 8, 7, 4],
        [4, 5, 6, 7, 8, 9, 0, 3],
        [3, 2, 0, 1, 9, 0, 1, 2],
        [0, 1, 3, 2, 9, 8, 0, 1],
        [1, 0, 4, 5, 6, 7, 3, 2]
    ]
    # When
    result = get_trailhead_score(trailhead, topographic_map)
    # Then
    assert result == 5


def test_get_sum_trailhead_scores():
    # Given
    topographic_map = [
        [8, 9, 0, 1, 0, 1, 2, 3],
        [7, 8, 1, 2, 1, 8, 7, 4],
        [8, 7, 4, 3, 0, 9, 6, 5],
        [9, 6, 5, 4, 9, 8, 7, 4],
        [4, 5, 6, 7, 8, 9, 0, 3],
        [3, 2, 0, 1, 9, 0, 1, 2],
        [0, 1, 3, 2, 9, 8, 0, 1],
        [1, 0, 4, 5, 6, 7, 3, 2]
    ]
    # When
    result = get_sum_trailhead_scores(topographic_map)
    # Then
    assert result == 36


def test_get_trailhead_rating():
    # Given
    trailhead = (2, 0)
    topographic_map = [
        [8, 9, 0, 1, 0, 1, 2, 3],
        [7, 8, 1, 2, 1, 8, 7, 4],
        [8, 7, 4, 3, 0, 9, 6, 5],
        [9, 6, 5, 4, 9, 8, 7, 4],
        [4, 5, 6, 7, 8, 9, 0, 3],
        [3, 2, 0, 1, 9, 0, 1, 2],
        [0, 1, 3, 2, 9, 8, 0, 1],
        [1, 0, 4, 5, 6, 7, 3, 2]
    ]
    # When
    result = get_trailhead_rating(trailhead, topographic_map)
    # Then
    assert result == 20


def test_get_sum_trailhead_ratings():
    # Given
    topographic_map = [
        [8, 9, 0, 1, 0, 1, 2, 3],
        [7, 8, 1, 2, 1, 8, 7, 4],
        [8, 7, 4, 3, 0, 9, 6, 5],
        [9, 6, 5, 4, 9, 8, 7, 4],
        [4, 5, 6, 7, 8, 9, 0, 3],
        [3, 2, 0, 1, 9, 0, 1, 2],
        [0, 1, 3, 2, 9, 8, 0, 1],
        [1, 0, 4, 5, 6, 7, 3, 2]
    ]
    # When
    result = get_sum_trailhead_ratings(topographic_map)
    # Then
    assert result == 81
