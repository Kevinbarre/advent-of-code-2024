from typing import NamedTuple


def part1(lines):
    level, movements, starting_position = parse_level(lines)
    level, _ = move_sequence(level, starting_position, movements)
    box_positions = get_box_positions(level)
    return sum_gps_coordinates(box_positions)


def part2(lines):
    return 0


class Direction(NamedTuple):
    x: int
    y: int


UP = Direction(0, -1)
DOWN = Direction(0, 1)
LEFT = Direction(-1, 0)
RIGHT = Direction(1, 0)


def map_instruction(raw_instruction):
    if raw_instruction == '^':
        return UP
    elif raw_instruction == 'v':
        return DOWN
    elif raw_instruction == '<':
        return LEFT
    else:  # raw_instruction == '>'
        return RIGHT


def parse_level(lines):
    level = []
    instructions_index = 0
    for i, line in enumerate(lines):
        if line != "":
            level.append([cell for cell in line])
        else:
            instructions_index = i
            break
    raw_instructions = lines[instructions_index + 1:]
    instructions = [map_instruction(raw_instruction) for raw_instruction in ''.join(raw_instructions)]
    starting_position = (0, 0)
    for j, row in enumerate(level):
        for i, cell in enumerate(row):
            if cell == '@':
                starting_position = (i, j)
                break
    return level, instructions, starting_position


def find_first_empty_space(level, first_box_position, movement):
    i = 0
    next_cell = 'O'
    next_cell_position = first_box_position
    while next_cell == 'O':
        i += 1
        next_cell_position = (first_box_position[0] + i * movement[0], first_box_position[1] + i * movement[1])
        next_cell = level[next_cell_position[1]][next_cell_position[0]]
    if next_cell == '.':
        return next_cell_position
    else:
        return False


def move(level, position, movement):
    next_position = (position[0] + movement[0], position[1] + movement[1])
    next_cell = level[next_position[1]][next_position[0]]
    if next_cell == '#':
        # Move to obstacle, movement not possible
        return level, position
    elif next_cell == '.':
        # Move to empty space
        # Current position becomes an empty space
        level[position[1]][position[0]] = '.'
        # Robot occupies next position
        level[next_position[1]][next_position[0]] = '@'
    else:  # next_cell == 'O'
        first_empty_space = find_first_empty_space(level, next_position, movement)
        if not first_empty_space:
            # Box blocked by obstacle, movement not possible
            return level, position
        if first_empty_space:
            # Move boxes
            # The boxes are shifting, equivalent to first box teleporting on first empty space
            level[first_empty_space[1]][first_empty_space[0]] = 'O'
            # Current position becomes an empty space
            level[position[1]][position[0]] = '.'
            # Robot occupies next position
            level[next_position[1]][next_position[0]] = '@'
    return level, next_position


def move_sequence(level, starting_position, movements):
    position = starting_position
    for movement in movements:
        level, position = move(level, position, movement)
    return level, position


def get_box_positions(level):
    return {(i, j) for j, row in enumerate(level) for i, cell in enumerate(row) if cell == 'O'}


def sum_gps_coordinates(box_positions):
    return sum(100 * j + i for i, j in box_positions)


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
