import pytest

from main import part1, part2, LEFT, UP, RIGHT, DOWN, parse_level, map_instruction, move, find_first_empty_space, move_sequence, get_box_positions, \
    sum_gps_coordinates


@pytest.mark.parametrize("filename, expected",
                         [("example.txt", 10092),
                          ("example2.txt", 2028)
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
                         [("example.txt", 0),
                          ("example2.txt", 0)
                          ])
def test_part2(filename, expected):
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 0


@pytest.mark.parametrize("instruction, expected",
                         [('^', UP),
                          ('v', DOWN),
                          ('<', LEFT),
                          ('>', RIGHT)
                          ])
def test_map_instruction(instruction, expected):
    # Given
    # When
    result = map_instruction(instruction)
    # Then
    assert result == expected


def test_parse_level():
    # Given
    lines = [
        "########",
        "#..O.O.#",
        "##@.O..#",
        "#...O..#",
        "#.#.O..#",
        "#...O..#",
        "#......#",
        "########",
        "",
        "<^^>>>vv<v",
        ">>v<<"
    ]
    # When
    level, movements, starting_position = parse_level(lines)
    # Then
    assert level == [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', 'O', '.', 'O', '.', '#'],
        ['#', '#', '@', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    assert movements == [LEFT, UP, UP, RIGHT, RIGHT, RIGHT, DOWN, DOWN, LEFT, DOWN,
                         RIGHT, RIGHT, DOWN, LEFT, LEFT]
    assert starting_position == (2, 2)


def test_move_no_obstacle():
    # Given
    level = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', 'O', '.', 'O', '.', '#'],
        ['#', '#', '@', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    position = (2, 2)
    movement = UP
    # When
    next_level, next_position = move(level, position, movement)
    # Then
    assert next_level == [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '@', 'O', '.', 'O', '.', '#'],
        ['#', '#', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    assert next_position == (2, 1)


def test_move_direct_obstacle():
    level = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', 'O', '.', 'O', '.', '#'],
        ['#', '#', '@', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    position = (2, 2)
    movement = LEFT
    # When
    next_level, next_position = move(level, position, movement)
    # Then
    assert next_level == [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', 'O', '.', 'O', '.', '#'],
        ['#', '#', '@', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    assert next_position == (2, 2)


def test_move_single_box():
    level = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '@', 'O', '.', 'O', '.', '#'],
        ['#', '#', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    position = (2, 1)
    movement = RIGHT
    # When
    next_level, next_position = move(level, position, movement)
    # Then
    assert next_level == [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '@', 'O', 'O', '.', '#'],
        ['#', '#', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    assert next_position == (3, 1)


def test_find_first_empty_space_single_box():
    # Given
    level = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '@', 'O', '.', 'O', '.', '#'],
        ['#', '#', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    first_box_position = (3, 1)
    movement = RIGHT
    # When
    result = find_first_empty_space(level, first_box_position, movement)
    # Then
    assert result == (4, 1)


def test_find_first_empty_space_box_against_wall():
    # Given
    level = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '@', 'O', '.', 'O', '.', '#'],
        ['#', '#', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    first_box_position = (3, 1)
    movement = UP
    # When
    result = find_first_empty_space(level, first_box_position, movement)
    # Then
    assert result == False


def test_find_first_empty_space_multiple_boxes():
    # Given
    level = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '@', 'O', '.', 'O', '.', '#'],
        ['#', '#', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    first_box_position = (4, 2)
    movement = DOWN
    # When
    result = find_first_empty_space(level, first_box_position, movement)
    # Then
    assert result == (4, 6)


def test_move_multiple_boxes():
    level = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '@', 'O', 'O', '.', '#'],
        ['#', '#', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    position = (3, 1)
    movement = RIGHT
    # When
    next_level, next_position = move(level, position, movement)
    # Then
    assert next_level == [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '@', 'O', 'O', '#'],
        ['#', '#', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    assert next_position == (4, 1)


def test_move_multiple_boxes_against_wall():
    level = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '@', 'O', 'O', '#'],
        ['#', '#', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    position = (4, 1)
    movement = RIGHT
    # When
    next_level, next_position = move(level, position, movement)
    # Then
    assert next_level == [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '@', 'O', 'O', '#'],
        ['#', '#', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    assert next_position == (4, 1)


def test_move_sequence():
    # Given
    level = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', 'O', '.', 'O', '.', '#'],
        ['#', '#', '@', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '#', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    movements = [LEFT, UP, UP, RIGHT, RIGHT, RIGHT, DOWN, DOWN, LEFT, DOWN,
                 RIGHT, RIGHT, DOWN, LEFT, LEFT]
    starting_position = (2, 2)
    # When
    level, end_position = move_sequence(level, starting_position, movements)
    # Then
    assert level == [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', 'O', 'O', '#'],
        ['#', '#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', 'O', '#'],
        ['#', '.', '#', 'O', '@', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    assert end_position == (4, 4)


def test_get_box_positions():
    # Given
    level = [
        ['#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', 'O', 'O', '#'],
        ['#', '#', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', 'O', '#'],
        ['#', '.', '#', 'O', '@', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '.', '.', '.', 'O', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#'],
    ]
    # When
    result = get_box_positions(level)
    # Then
    assert result == {(5, 1), (6, 1), (6, 3), (3, 4), (4, 5), (4, 6)}


def test_sum_gps_coordinates():
    # Given
    box_positions = {(5, 1), (6, 1), (6, 3), (3, 4), (4, 5), (4, 6)}
    # When
    result = sum_gps_coordinates(box_positions)
    # Then
    assert result == 2028
