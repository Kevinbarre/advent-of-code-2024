import pytest

from main import part1, part2, parse_racetrack, get_neighbours, find_path, find_possible_cheats, is_possible_cheat, find_time_saved, \
    count_cheats_saving_at_least, find_possible_cheats_max_time

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 0


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 0


def test_parse_racetrack():
    # Given
    lines = [
        "###############",
        "#...#...#.....#",
        "#.#.#.#.#.###.#",
        "#S#...#.#.#...#",
        "#######.#.#.###",
        "#######.#.#...#",
        "#######.#.###.#",
        "###..E#...#...#",
        "###.#######.###",
        "#...###...#...#",
        "#.#####.#.###.#",
        "#.#...#.#.#...#",
        "#.#.#.#.#.#.###",
        "#...#...#...###",
        "###############"
    ]
    # When
    racetrack, start, end = parse_racetrack(lines)
    # Then
    assert racetrack == [
        "###############",
        "#...#...#.....#",
        "#.#.#.#.#.###.#",
        "#.#...#.#.#...#",
        "#######.#.#.###",
        "#######.#.#...#",
        "#######.#.###.#",
        "###...#...#...#",
        "###.#######.###",
        "#...###...#...#",
        "#.#####.#.###.#",
        "#.#...#.#.#...#",
        "#.#.#.#.#.#.###",
        "#...#...#...###",
        "###############"
    ]
    assert start == (1, 3)
    assert end == (5, 7)


def test_get_neighbours():
    # Given
    racetrack = [
        "###############",
        "#...#...#.....#",
        "#.#.#.#.#.###.#",
        "#.#...#.#.#...#",
        "#######.#.#.###",
        "#######.#.#...#",
        "#######.#.###.#",
        "###...#...#...#",
        "###.#######.###",
        "#...###...#...#",
        "#.#####.#.###.#",
        "#.#...#.#.#...#",
        "#.#.#.#.#.#.###",
        "#...#...#...###",
        "###############"
    ]
    position = (1, 3)
    # When
    result = get_neighbours(racetrack, position)
    # Then
    assert result == {(1, 2)}


def test_find_path():
    # Given
    racetrack = [
        "###############",
        "#...#...#.....#",
        "#.#.#.#.#.###.#",
        "#.#...#.#.#...#",
        "#######.#.#.###",
        "#######.#.#...#",
        "#######.#.###.#",
        "###...#...#...#",
        "###.#######.###",
        "#...###...#...#",
        "#.#####.#.###.#",
        "#.#...#.#.#...#",
        "#.#.#.#.#.#.###",
        "#...#...#...###",
        "###############"
    ]
    start = (1, 3)
    end = (5, 7)
    # When
    result = find_path(racetrack, start, end)
    # Then
    assert result == {(1, 3): 0, (1, 2): 1, (1, 1): 2, (2, 1): 3, (3, 1): 4, (3, 2): 5, (3, 3): 6, (4, 3): 7, (5, 3): 8, (5, 2): 9, (5, 1): 10, (6, 1): 11,
                      (7, 1): 12, (7, 2): 13, (7, 3): 14, (7, 4): 15, (7, 5): 16, (7, 6): 17, (7, 7): 18, (8, 7): 19, (9, 7): 20, (9, 6): 21, (9, 5): 22,
                      (9, 4): 23, (9, 3): 24, (9, 2): 25, (9, 1): 26, (10, 1): 27, (11, 1): 28, (12, 1): 29, (13, 1): 30, (13, 2): 31, (13, 3): 32, (12, 3): 33,
                      (11, 3): 34, (11, 4): 35, (11, 5): 36, (12, 5): 37, (13, 5): 38, (13, 6): 39, (13, 7): 40, (12, 7): 41, (11, 7): 42, (11, 8): 43,
                      (11, 9): 44, (12, 9): 45, (13, 9): 46, (13, 10): 47, (13, 11): 48, (12, 11): 49, (11, 11): 50, (11, 12): 51, (11, 13): 52, (10, 13): 53,
                      (9, 13): 54, (9, 12): 55, (9, 11): 56, (9, 10): 57, (9, 9): 58, (8, 9): 59, (7, 9): 60, (7, 10): 61, (7, 11): 62, (7, 12): 63,
                      (7, 13): 64, (6, 13): 65, (5, 13): 66, (5, 12): 67, (5, 11): 68, (4, 11): 69, (3, 11): 70, (3, 12): 71, (3, 13): 72, (2, 13): 73,
                      (1, 13): 74, (1, 12): 75, (1, 11): 76, (1, 10): 77, (1, 9): 78, (2, 9): 79, (3, 9): 80, (3, 8): 81, (3, 7): 82, (4, 7): 83, (5, 7): 84}


@pytest.mark.parametrize("position, expected",
                         [((2, 3), {(1, 3), (3, 3)}),
                          ((2, 10), set()),
                          ((0, 0), set()),
                          ((14, 14), set())
                          ])
def test_is_possible_cheat(position, expected):
    # Given
    racetrack = [
        "###############",
        "#...#...#.....#",
        "#.#.#.#.#.###.#",
        "#.#...#.#.#...#",
        "#######.#.#.###",
        "#######.#.#...#",
        "#######.#.###.#",
        "###...#...#...#",
        "###.#######.###",
        "#...###...#...#",
        "#.#####.#.###.#",
        "#.#...#.#.#...#",
        "#.#.#.#.#.#.###",
        "#...#...#...###",
        "###############"
    ]
    # When
    result = is_possible_cheat(racetrack, position)
    # Then
    assert result == expected


def test_find_possible_cheats():
    # Given
    racetrack = [
        "###############",
        "#...#...#.....#",
        "#.#.#.#.#.###.#",
        "#.#...#.#.#...#",
        "#######.#.#.###",
        "#######.#.#...#",
        "#######.#.###.#",
        "###...#...#...#",
        "###.#######.###",
        "#...###...#...#",
        "#.#####.#.###.#",
        "#.#...#.#.#...#",
        "#.#.#.#.#.#.###",
        "#...#...#...###",
        "###############"
    ]
    # When
    result = find_possible_cheats(racetrack)
    # Then
    assert result == {
        (2, 3): {(1, 3), (3, 3)},
        (2, 2): {(1, 2), (3, 2)},
        (4, 1): {(3, 1), (5, 1)},
        (4, 2): {(3, 2), (5, 2)},
        (6, 3): {(5, 3), (7, 3)},
        (6, 2): {(5, 2), (7, 2)},
        (8, 1): {(7, 1), (9, 1)},
        (8, 2): {(7, 2), (9, 2)},
        (8, 3): {(7, 3), (9, 3)},
        (8, 4): {(7, 4), (9, 4)},
        (8, 5): {(7, 5), (9, 5)},
        (8, 6): {(7, 6), (9, 6)},
        (6, 7): {(5, 7), (7, 7)},
        (7, 8): {(7, 7), (7, 9)},
        (8, 8): {(8, 7), (8, 9)},
        (9, 8): {(9, 7), (9, 9)},
        (10, 7): {(9, 7), (11, 7)},
        (10, 5): {(9, 5), (11, 5)},
        (10, 4): {(9, 4), (11, 4)},
        (10, 3): {(9, 3), (11, 3)},
        (11, 2): {(11, 1), (11, 3)},
        (12, 2): {(12, 1), (12, 3)},
        (13, 4): {(13, 3), (13, 5)},
        (12, 4): {(12, 3), (12, 5)},
        (11, 6): {(11, 5), (11, 7)},
        (12, 6): {(12, 5), (12, 7)},
        (13, 8): {(13, 7), (13, 9)},
        (12, 8): {(12, 7), (12, 9)},
        (10, 9): {(9, 9), (11, 9)},
        (11, 10): {(11, 9), (11, 11)},
        (12, 10): {(12, 9), (12, 11)},
        (10, 11): {(9, 11), (11, 11)},
        (10, 12): {(9, 12), (11, 12)},
        (8, 13): {(7, 13), (9, 13)},
        (8, 12): {(7, 12), (9, 12)},
        (8, 11): {(7, 11), (9, 11)},
        (8, 10): {(7, 10), (9, 10)},
        (6, 11): {(5, 11), (7, 11)},
        (6, 12): {(5, 12), (7, 12)},
        (4, 13): {(3, 13), (5, 13)},
        (4, 12): {(3, 12), (5, 12)},
        (3, 10): {(3, 9), (3, 11)},
        (2, 11): {(1, 11), (3, 11)},
        (2, 12): {(1, 12), (3, 12)}
    }


def test_find_time_saved():
    # Given
    path = {(1, 3): 0, (1, 2): 1, (1, 1): 2, (2, 1): 3, (3, 1): 4, (3, 2): 5, (3, 3): 6, (4, 3): 7, (5, 3): 8, (5, 2): 9, (5, 1): 10, (6, 1): 11,
            (7, 1): 12, (7, 2): 13, (7, 3): 14, (7, 4): 15, (7, 5): 16, (7, 6): 17, (7, 7): 18, (8, 7): 19, (9, 7): 20, (9, 6): 21, (9, 5): 22,
            (9, 4): 23, (9, 3): 24, (9, 2): 25, (9, 1): 26, (10, 1): 27, (11, 1): 28, (12, 1): 29, (13, 1): 30, (13, 2): 31, (13, 3): 32, (12, 3): 33,
            (11, 3): 34, (11, 4): 35, (11, 5): 36, (12, 5): 37, (13, 5): 38, (13, 6): 39, (13, 7): 40, (12, 7): 41, (11, 7): 42, (11, 8): 43,
            (11, 9): 44, (12, 9): 45, (13, 9): 46, (13, 10): 47, (13, 11): 48, (12, 11): 49, (11, 11): 50, (11, 12): 51, (11, 13): 52, (10, 13): 53,
            (9, 13): 54, (9, 12): 55, (9, 11): 56, (9, 10): 57, (9, 9): 58, (8, 9): 59, (7, 9): 60, (7, 10): 61, (7, 11): 62, (7, 12): 63,
            (7, 13): 64, (6, 13): 65, (5, 13): 66, (5, 12): 67, (5, 11): 68, (4, 11): 69, (3, 11): 70, (3, 12): 71, (3, 13): 72, (2, 13): 73,
            (1, 13): 74, (1, 12): 75, (1, 11): 76, (1, 10): 77, (1, 9): 78, (2, 9): 79, (3, 9): 80, (3, 8): 81, (3, 7): 82, (4, 7): 83, (5, 7): 84}
    possible_cheats = {
        (2, 3): {(1, 3), (3, 3)},
        (2, 2): {(1, 2), (3, 2)},
        (4, 1): {(3, 1), (5, 1)},
        (4, 2): {(3, 2), (5, 2)},
        (6, 3): {(5, 3), (7, 3)},
        (6, 2): {(5, 2), (7, 2)},
        (8, 1): {(7, 1), (9, 1)},
        (8, 2): {(7, 2), (9, 2)},
        (8, 3): {(7, 3), (9, 3)},
        (8, 4): {(7, 4), (9, 4)},
        (8, 5): {(7, 5), (9, 5)},
        (8, 6): {(7, 6), (9, 6)},
        (6, 7): {(5, 7), (7, 7)},
        (7, 8): {(7, 7), (7, 9)},
        (8, 8): {(8, 7), (8, 9)},
        (9, 8): {(9, 7), (9, 9)},
        (10, 7): {(9, 7), (11, 7)},
        (10, 5): {(9, 5), (11, 5)},
        (10, 4): {(9, 4), (11, 4)},
        (10, 3): {(9, 3), (11, 3)},
        (11, 2): {(11, 1), (11, 3)},
        (12, 2): {(12, 1), (12, 3)},
        (13, 4): {(13, 3), (13, 5)},
        (12, 4): {(12, 3), (12, 5)},
        (11, 6): {(11, 5), (11, 7)},
        (12, 6): {(12, 5), (12, 7)},
        (13, 8): {(13, 7), (13, 9)},
        (12, 8): {(12, 7), (12, 9)},
        (10, 9): {(9, 9), (11, 9)},
        (11, 10): {(11, 9), (11, 11)},
        (12, 10): {(12, 9), (12, 11)},
        (10, 11): {(9, 11), (11, 11)},
        (10, 12): {(9, 12), (11, 12)},
        (8, 13): {(7, 13), (9, 13)},
        (8, 12): {(7, 12), (9, 12)},
        (8, 11): {(7, 11), (9, 11)},
        (8, 10): {(7, 10), (9, 10)},
        (6, 11): {(5, 11), (7, 11)},
        (6, 12): {(5, 12), (7, 12)},
        (4, 13): {(3, 13), (5, 13)},
        (4, 12): {(3, 12), (5, 12)},
        (3, 10): {(3, 9), (3, 11)},
        (2, 11): {(1, 11), (3, 11)},
        (2, 12): {(1, 12), (3, 12)}
    }
    # When
    result = find_time_saved(path, possible_cheats)
    # Then
    assert result == {
        (2, 3): 4,
        (2, 2): 2,
        (4, 1): 4,
        (4, 2): 2,
        (6, 3): 4,
        (6, 2): 2,
        (8, 1): 12,
        (8, 2): 10,
        (8, 3): 8,
        (8, 4): 6,
        (8, 5): 4,
        (8, 6): 2,
        (6, 7): 64,
        (7, 8): 40,
        (8, 8): 38,
        (9, 8): 36,
        (10, 7): 20,
        (10, 5): 12,
        (10, 4): 10,
        (10, 3): 8,
        (11, 2): 4,
        (12, 2): 2,
        (13, 4): 4,
        (12, 4): 2,
        (11, 6): 4,
        (12, 6): 2,
        (13, 8): 4,
        (12, 8): 2,
        (10, 9): 12,
        (11, 10): 4,
        (12, 10): 2,
        (10, 11): 4,
        (10, 12): 2,
        (8, 13): 8,
        (8, 12): 6,
        (8, 11): 4,
        (8, 10): 2,
        (6, 11): 4,
        (6, 12): 2,
        (4, 13): 4,
        (4, 12): 2,
        (3, 10): 8,
        (2, 11): 4,
        (2, 12): 2
    }


@pytest.mark.parametrize("time, expected",
                         [(100, 0),
                          (12, 8),
                          (2, 44)
                          ])
def test_count_cheats_saving_at_least(time, expected):
    # Given
    time_saved = {
        (2, 3): 4,
        (2, 2): 2,
        (4, 1): 4,
        (4, 2): 2,
        (6, 3): 4,
        (6, 2): 2,
        (8, 1): 12,
        (8, 2): 10,
        (8, 3): 8,
        (8, 4): 6,
        (8, 5): 4,
        (8, 6): 2,
        (6, 7): 64,
        (7, 8): 40,
        (8, 8): 38,
        (9, 8): 36,
        (10, 7): 20,
        (10, 5): 12,
        (10, 4): 10,
        (10, 3): 8,
        (11, 2): 4,
        (12, 2): 2,
        (13, 4): 4,
        (12, 4): 2,
        (11, 6): 4,
        (12, 6): 2,
        (13, 8): 4,
        (12, 8): 2,
        (10, 9): 12,
        (11, 10): 4,
        (12, 10): 2,
        (10, 11): 4,
        (10, 12): 2,
        (8, 13): 8,
        (8, 12): 6,
        (8, 11): 4,
        (8, 10): 2,
        (6, 11): 4,
        (6, 12): 2,
        (4, 13): 4,
        (4, 12): 2,
        (3, 10): 8,
        (2, 11): 4,
        (2, 12): 2
    }
    # When
    result = count_cheats_saving_at_least(time_saved, time)
    # Then
    assert result == expected


def test_find_possible_cheats_max_time():
    # Given
    path = {(1, 3): 0, (1, 2): 1, (1, 1): 2, (2, 1): 3, (3, 1): 4, (3, 2): 5, (3, 3): 6, (4, 3): 7, (5, 3): 8, (5, 2): 9, (5, 1): 10, (6, 1): 11,
            (7, 1): 12, (7, 2): 13, (7, 3): 14, (7, 4): 15, (7, 5): 16, (7, 6): 17, (7, 7): 18, (8, 7): 19, (9, 7): 20, (9, 6): 21, (9, 5): 22,
            (9, 4): 23, (9, 3): 24, (9, 2): 25, (9, 1): 26, (10, 1): 27, (11, 1): 28, (12, 1): 29, (13, 1): 30, (13, 2): 31, (13, 3): 32, (12, 3): 33,
            (11, 3): 34, (11, 4): 35, (11, 5): 36, (12, 5): 37, (13, 5): 38, (13, 6): 39, (13, 7): 40, (12, 7): 41, (11, 7): 42, (11, 8): 43,
            (11, 9): 44, (12, 9): 45, (13, 9): 46, (13, 10): 47, (13, 11): 48, (12, 11): 49, (11, 11): 50, (11, 12): 51, (11, 13): 52, (10, 13): 53,
            (9, 13): 54, (9, 12): 55, (9, 11): 56, (9, 10): 57, (9, 9): 58, (8, 9): 59, (7, 9): 60, (7, 10): 61, (7, 11): 62, (7, 12): 63,
            (7, 13): 64, (6, 13): 65, (5, 13): 66, (5, 12): 67, (5, 11): 68, (4, 11): 69, (3, 11): 70, (3, 12): 71, (3, 13): 72, (2, 13): 73,
            (1, 13): 74, (1, 12): 75, (1, 11): 76, (1, 10): 77, (1, 9): 78, (2, 9): 79, (3, 9): 80, (3, 8): 81, (3, 7): 82, (4, 7): 83, (5, 7): 84}
    max_time = 2
    # When
    result = find_possible_cheats_max_time(path, max_time)
    # Then
    assert result == {
        ((1, 3), (3, 3)): 4,
        ((1, 2), (3, 2)): 2,
        ((3, 1), (5, 1)): 4,
        ((3, 2), (5, 2)): 2,
        ((5, 3), (7, 3)): 4,
        ((5, 2), (7, 2)): 2,
        ((7, 1), (9, 1)): 12,
        ((7, 2), (9, 2)): 10,
        ((7, 3), (9, 3)): 8,
        ((7, 4), (9, 4)): 6,
        ((7, 5), (9, 5)): 4,
        ((7, 6), (9, 6)): 2,
        ((7, 7), (5, 7)): 64,
        ((7, 7), (7, 9)): 40,
        ((8, 7), (8, 9)): 38,
        ((9, 7), (9, 9)): 36,
        ((9, 7), (11, 7)): 20,
        ((9, 5), (11, 5)): 12,
        ((9, 4), (11, 4)): 10,
        ((9, 3), (11, 3)): 8,
        ((11, 1), (11, 3)): 4,
        ((12, 1), (12, 3)): 2,
        ((13, 3), (13, 5)): 4,
        ((12, 3), (12, 5)): 2,
        ((11, 5), (11, 7)): 4,
        ((12, 5), (12, 7)): 2,
        ((13, 7), (13, 9)): 4,
        ((12, 7), (12, 9)): 2,
        ((11, 9), (9, 9)): 12,
        ((11, 9), (11, 11)): 4,
        ((12, 9), (12, 11)): 2,
        ((11, 11), (9, 11)): 4,
        ((11, 12), (9, 12)): 2,
        ((9, 13), (7, 13)): 8,
        ((9, 12), (7, 12)): 6,
        ((9, 11), (7, 11)): 4,
        ((9, 10), (7, 10)): 2,
        ((7, 11), (5, 11)): 4,
        ((7, 12), (5, 12)): 2,
        ((5, 13), (3, 13)): 4,
        ((5, 12), (3, 12)): 2,
        ((3, 11), (3, 9)): 8,
        ((3, 11), (1, 11)): 4,
        ((3, 12), (1, 12)): 2
    }
