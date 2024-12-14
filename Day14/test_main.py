import pytest

from main import part1, part2, parse_robots, Robot, count_quadrants, safety_factor, move_robots, get_robots_picture

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    width = 11
    height = 7
    # When
    result = part1(lines, width, height)
    # Then
    assert result == 12


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    width = 11
    height = 7
    # When
    result = part2(lines, width, height)
    # Then
    assert result == 0


def test_parse_robots():
    # Given
    lines = [
        "p=0,4 v=3,-3",
        "p=6,3 v=-1,-3",
        "p=10,3 v=-1,2",
        "p=2,0 v=2,-1",
        "p=0,0 v=1,3",
        "p=3,0 v=-2,-2",
        "p=7,6 v=-1,-3",
        "p=3,0 v=-1,-2",
        "p=9,3 v=2,3",
        "p=7,3 v=-1,2",
        "p=2,4 v=2,-3",
        "p=9,5 v=-3,-3",
    ]
    # When
    result = parse_robots(lines)
    # Then
    assert result == [
        Robot(0, 4, 3, -3),
        Robot(6, 3, -1, -3),
        Robot(10, 3, -1, 2),
        Robot(2, 0, 2, -1),
        Robot(0, 0, 1, 3),
        Robot(3, 0, -2, -2),
        Robot(7, 6, -1, -3),
        Robot(3, 0, -1, -2),
        Robot(9, 3, 2, 3),
        Robot(7, 3, -1, 2),
        Robot(2, 4, 2, -3),
        Robot(9, 5, -3, -3)
    ]


@pytest.mark.parametrize("time, expected",
                         [(0, (2, 4)),
                          (1, (4, 1)),
                          (2, (6, 5)),
                          (3, (8, 2)),
                          (4, (10, 6)),
                          (5, (1, 3)),
                          ])
def test_robot_position_at(time, expected):
    # Given
    robot = Robot(2, 4, 2, -3)
    width = 11
    height = 7
    # When
    result = robot.position_at(time, width, height)
    # Then
    assert result == expected


def test_move_robots():
    # Given
    robots = [
        Robot(0, 4, 3, -3),
        Robot(6, 3, -1, -3),
        Robot(10, 3, -1, 2),
        Robot(2, 0, 2, -1),
        Robot(0, 0, 1, 3),
        Robot(3, 0, -2, -2),
        Robot(7, 6, -1, -3),
        Robot(3, 0, -1, -2),
        Robot(9, 3, 2, 3),
        Robot(7, 3, -1, 2),
        Robot(2, 4, 2, -3),
        Robot(9, 5, -3, -3)
    ]
    time = 100
    width = 11
    height = 7
    # When
    result = move_robots(robots, time, width, height)
    # Then
    assert result == [
        (3, 5),
        (5, 4),
        (9, 0),
        (4, 5),
        (1, 6),
        (1, 3),
        (6, 0),
        (2, 3),
        (0, 2),
        (6, 0),
        (4, 5),
        (6, 6)
    ]


def test_count_quadrants():
    # Given
    positions = [
        (3, 5),
        (5, 4),
        (9, 0),
        (4, 5),
        (1, 6),
        (1, 3),
        (6, 0),
        (2, 3),
        (0, 2),
        (6, 0),
        (4, 5),
        (6, 6)
    ]
    width = 11
    height = 7
    # When
    result = count_quadrants(positions, width, height)
    # Then
    assert result == (1, 3, 4, 1)


def test_safety_factor():
    # Given
    number_robots = (1, 3, 4, 1)
    # When
    result = safety_factor(number_robots)
    # Then
    assert result == 12


def test_get_robots_picture():
    # Given
    positions = [
        (3, 5),
        (5, 4),
        (9, 0),
        (4, 5),
        (1, 6),
        (1, 3),
        (6, 0),
        (2, 3),
        (0, 2),
        (6, 0),
        (4, 5),
        (6, 6)
    ]
    width = 11
    height = 7
    # When
    result = get_robots_picture(positions, width, height)
    # Then
    assert result == [
        "......2..1.",
        "...........",
        "1..........",
        ".11........",
        ".....1.....",
        "...12......",
        ".1....1....",
    ]
