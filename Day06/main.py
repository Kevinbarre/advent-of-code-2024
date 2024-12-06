from typing import NamedTuple


def part1(lines):
    starting_position, level = parse_level(lines)
    _, final_level, _ = run_through_level(starting_position, level)
    return count_x(final_level)


def part2(lines):
    return 0


class Direction(NamedTuple):
    x: int
    y: int


UP = Direction(0, -1)
DOWN = Direction(0, 1)
LEFT = Direction(-1, 0)
RIGHT = Direction(1, 0)


def parse_level(lines):
    # Find starting position
    x = y = 0
    for j, line in enumerate(lines):
        if '^' in line:
            y = j
            for i, cell in enumerate(line):
                if cell == '^':
                    x = i
                    break
    level = [['Z'] + [cell if cell != '^' else 'X' for cell in line] + ['Z'] for line in lines]
    border = ['Z' for i in range(len(level[0]))]
    level.insert(0, border)
    level.append(border)
    # Account for top and left border in starting position
    return (x + 1, y + 1), level


def move(position, level, direction):
    new_position = (position[0] + direction[0], position[1] + direction[1])
    future_cell = level[new_position[1]][new_position[0]]
    if future_cell in ('.', 'X'):
        # Walkable cell, let's proceed
        level[new_position[1]][new_position[0]] = 'X'
        return new_position, level, direction, False
    elif future_cell == '#':
        # Obstacle, turn right
        if direction == UP:
            new_direction = RIGHT
        elif direction == RIGHT:
            new_direction = DOWN
        elif direction == DOWN:
            new_direction = LEFT
        else:  # Direction == LEFT:
            new_direction = UP
        return position, level, new_direction, False
    else:
        # End of level reached
        return position, level, direction, True


def run_through_level(starting_position, input_level):
    position = starting_position
    level = input_level
    direction = UP
    done = False
    while not done:
        position, level, direction, done = move(position, level, direction)
    return position, level, direction


def count_x(level):
    return sum(1 for row in level for cell in row if cell == 'X')


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
