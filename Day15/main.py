from typing import NamedTuple


def part1(lines):
    level, movements, starting_position = parse_level(lines)
    level, _ = move_sequence(level, starting_position, movements)
    box_positions = get_box_positions(level)
    return sum_gps_coordinates(box_positions)


def part2(lines):
    level, movements, _ = parse_level(lines)
    level, starting_position = expand_level(level)
    level, _ = move2_sequence(level, starting_position, movements)
    box_positions = get_big_box_positions(level)
    return sum_gps_coordinates(box_positions)


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


def expand_level(level):
    expanded_level = []
    for row in level:
        expanded_row = []
        for cell in row:
            if cell == '#':
                expanded_row.extend(['#', '#'])
            elif cell == 'O':
                expanded_row.extend(['[', ']'])
            elif cell == '.':
                expanded_row.extend(['.', '.'])
            else:  # cell == '@'
                expanded_row.extend(['@', '.'])
        expanded_level.append(expanded_row)
    starting_position = (0, 0)
    for j, row in enumerate(expanded_level):
        for i, cell in enumerate(row):
            if cell == '@':
                starting_position = (i, j)
                break
    return expanded_level, starting_position


def find_distance_first_horizontal_empty_space(level, next_position, movement):
    distance_first_horizontal_empty_space = 0
    next_cell = level[next_position[1]][next_position[0]]
    while next_cell in ('[', ']'):
        distance_first_horizontal_empty_space += 1
        next_cell_position = (next_position[0] + distance_first_horizontal_empty_space * movement[0], next_position[1])
        next_cell = level[next_cell_position[1]][next_cell_position[0]]
    if next_cell == '.':
        return distance_first_horizontal_empty_space + 1
    else:
        return 0


def find_chained_boxes(level, first_box_position, movement):
    boxes_to_check = {first_box_position}
    chained_boxes = set()
    while boxes_to_check:
        box_to_check = boxes_to_check.pop()
        chained_boxes.add(box_to_check)
        next_left = level[box_to_check[1] + movement[1]][box_to_check[0]]
        next_right = level[box_to_check[1] + movement[1]][box_to_check[0] + 1]
        if next_left == next_right == '.':
            # Path is clear, the box will be able to move
            continue
        elif next_left == '#' or next_right == '#':
            # Obstacle on the way, we won't be able to move the boxes
            return set()
        else:
            if next_left == '[':
                # Aligned box, add it to the boxes to check
                boxes_to_check.add((box_to_check[0], box_to_check[1] + movement[1]))
            if next_left == ']':
                # Shifted box on the left, add it to the boxes to check
                boxes_to_check.add((box_to_check[0] - 1, box_to_check[1] + movement[1]))
            if next_right == '[':
                # Shifted box on the right, add it to the boxes to check
                boxes_to_check.add((box_to_check[0] + 1, box_to_check[1] + movement[1]))
    return chained_boxes


def move2(level, position, movement):
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
    else:  # next_cell in ('[',']')
        if movement in (LEFT, RIGHT):
            distance_first_empty_space = find_distance_first_horizontal_empty_space(level, next_position, movement)
            if distance_first_empty_space == 0:
                # Box blocked by obstacle, movement not possible
                return level, position
            else:
                # Move boxes
                # The boxes are shifting
                for i in reversed(range(1, distance_first_empty_space)):
                    level[next_position[1]][next_position[0] + i * movement[0]] = level[next_position[1]][next_position[0] + (i - 1) * movement[0]]
                # Current position becomes an empty space
                level[position[1]][position[0]] = '.'
                # Robot occupies next position
                level[next_position[1]][next_position[0]] = '@'
        else:  # movement in (UP, DOWN):
            if next_cell == '[':
                # Left part of the box, box_position is next_position
                box_position = next_position
            else:  # next_cell == ']'
                # Right part of the box, box_position is on the left
                box_position = (next_position[0] - 1, next_position[1])
            # Find all boxes chained to the one we want to push
            chained_boxes = find_chained_boxes(level, box_position, movement)
            if not chained_boxes:
                # Can't move, one of the box is blocked by an obstacle
                return level, position
            else:
                for chained_box in chained_boxes:
                    # Clear previous box position
                    level[chained_box[1]][chained_box[0]] = '.'
                    level[chained_box[1]][chained_box[0] + 1] = '.'
                for chained_box in chained_boxes:
                    # Redraw left part of the box according to movement
                    level[chained_box[1] + movement[1]][chained_box[0]] = '['
                    # Redraw right part of the box according to movement
                    level[chained_box[1] + movement[1]][chained_box[0] + 1] = ']'
                # Current position becomes an empty space
                level[position[1]][position[0]] = '.'
                # Robot occupies next position
                level[next_position[1]][next_position[0]] = '@'
    return level, next_position


def move2_sequence(level, starting_position, movements):
    position = starting_position
    for movement in movements:
        level, position = move2(level, position, movement)
    return level, position


def get_big_box_positions(level):
    return {(i, j) for j, row in enumerate(level) for i, cell in enumerate(row) if cell == '['}


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
