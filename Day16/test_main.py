import pytest

from main import part1, part2, parse_level, RIGHT, LEFT, UP, DOWN, get_possible_moves, get_next_direction_score, dijkstra, dijkstra_all_paths, \
    count_distinct_cells


@pytest.mark.parametrize("filename, expected",
                         [("example.txt", 7036),
                          ("example2.txt", 11048),
                          ("example3.txt", 21148),
                          ("example4.txt", 5078),
                          ("example5.txt", 21110),
                          ("example6.txt", 4013),
                          ])
def test_part1(filename, expected):
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == expected


@pytest.mark.parametrize("filename, expected",
                         [("example.txt", 45),
                          ("example2.txt", 64)
                          ])
def test_part2(filename, expected):
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == expected


def test_parse_level():
    # Given
    lines = [
        "###############",
        "#.......#....E#",
        "#.#.###.#.###.#",
        "#.....#.#...#.#",
        "#.###.#####.#.#",
        "#.#.#.......#.#",
        "#.#.#####.###.#",
        "#...........#.#",
        "###.#.#####.#.#",
        "#...#.....#.#.#",
        "#.#.#.###.#.#.#",
        "#.....#...#.#.#",
        "#.###.#.#.#.#.#",
        "#S..#.....#...#",
        "###############"
    ]
    # When
    level, start, end = parse_level(lines)
    # Then
    assert level == [
        "###############",
        "#.......#.....#",
        "#.#.###.#.###.#",
        "#.....#.#...#.#",
        "#.###.#####.#.#",
        "#.#.#.......#.#",
        "#.#.#####.###.#",
        "#...........#.#",
        "###.#.#####.#.#",
        "#...#.....#.#.#",
        "#.#.#.###.#.#.#",
        "#.....#...#.#.#",
        "#.###.#.#.#.#.#",
        "#...#.....#...#",
        "###############"
    ]
    assert start == (1, 13)
    assert end == (13, 1)


@pytest.mark.parametrize("direction, next_direction, expected",
                         [(UP, UP, 1),
                          (UP, LEFT, 1001),
                          (UP, RIGHT, 1001),
                          (UP, DOWN, 2001),
                          (LEFT, UP, 1001),
                          (LEFT, LEFT, 1),
                          (LEFT, RIGHT, 2001),
                          (LEFT, DOWN, 1001),
                          (RIGHT, UP, 1001),
                          (RIGHT, LEFT, 2001),
                          (RIGHT, RIGHT, 1),
                          (RIGHT, DOWN, 1001),
                          (DOWN, UP, 2001),
                          (DOWN, LEFT, 1001),
                          (DOWN, RIGHT, 1001),
                          (DOWN, DOWN, 1),
                          ])
def test_get_next_direction_score(direction, next_direction, expected):
    # Given
    # When
    result = get_next_direction_score(direction, next_direction)
    # Then
    assert result == expected


def test_get_possible_moves():
    # Given
    level = [
        "#####",
        "##.##",
        "#...#",
        "##.##",
        "#####",
    ]
    position = (2, 2)
    direction = RIGHT
    # When
    result = get_possible_moves(level, position, direction)
    # Then
    assert result == {((3, 2), RIGHT, 1), ((1, 2), LEFT, 2001), ((2, 1), UP, 1001), ((2, 3), DOWN, 1001)}


def test_get_possible_moves_with_wall():
    # Given
    level = [
        "#####",
        "##.##",
        "#...#",
        "#####",
        "#####",
    ]
    position = (2, 2)
    direction = RIGHT
    # When
    result = get_possible_moves(level, position, direction)
    # Then
    assert result == {((3, 2), RIGHT, 1), ((1, 2), LEFT, 2001), ((2, 1), UP, 1001)}


def test_dijkstra():
    # Given
    level = [
        "#####",
        "#...#",
        "#.#.#",
        "#...#",
        "#####",
    ]
    start = (1, 3)
    end = (3, 1)
    # When
    result = dijkstra(level, start, end)
    # Then
    assert result == 1004


def test_dijkstra_example():
    # Given
    level = [
        "###############",
        "#.......#.....#",
        "#.#.###.#.###.#",
        "#.....#.#...#.#",
        "#.###.#####.#.#",
        "#.#.#.......#.#",
        "#.#.#####.###.#",
        "#...........#.#",
        "###.#.#####.#.#",
        "#...#.....#.#.#",
        "#.#.#.###.#.#.#",
        "#.....#...#.#.#",
        "#.###.#.#.#.#.#",
        "#...#.....#...#",
        "###############"
    ]
    start = (1, 13)
    end = (13, 1)
    # When
    result = dijkstra(level, start, end)
    # Then
    assert result == 7036


def test_dijkstra_example6():
    # Given
    level = [
        "##########",
        "#........#",
        "#.##.#####",
        "#..#.....#",
        "##.#####.#",
        "#........#",
        "##########"
    ]
    start = (1, 5)
    end = (8, 1)
    # When
    result = dijkstra(level, start, end)
    # Then
    assert result == 4013


def test_dijkstra_all_paths():
    # Given
    level = [
        "#####",
        "###.#",
        "#...#",
        "#.#.#",
        "#...#",
        "#.###",
        "#####"
    ]
    start = (1, 5)
    end = (3, 1)
    # When
    result = dijkstra_all_paths(level, start, end)
    # Then
    assert result == {
        tuple([(1, 5), (1, 4), (1, 3), (1, 2), (2, 2), (3, 2), (3, 1)]),
        tuple([(1, 5), (1, 4), (2, 4), (3, 4), (3, 3), (3, 2), (3, 1)])
    }


def test_count_distinct_cells():
    # Given
    all_paths = {
        tuple([(1, 5), (1, 4), (1, 3), (1, 2), (2, 2), (3, 2), (3, 1)]),
        tuple([(1, 5), (1, 4), (2, 4), (3, 4), (3, 3), (3, 2), (3, 1)])
    }
    # When
    result = count_distinct_cells(all_paths)
    # Then
    assert result == 10
