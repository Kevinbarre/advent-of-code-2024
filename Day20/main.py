from collections import Counter
from typing import NamedTuple


def part1(lines):
    racetrack, start, end = parse_racetrack(lines)
    path = find_path(racetrack, start, end)
    possible_cheats = find_possible_cheats(racetrack)
    time_saved = find_time_saved(path, possible_cheats)
    return count_cheats_saving_at_least(time_saved, 100)


def part2(lines):
    return 0


class Direction(NamedTuple):
    x: int
    y: int


UP = Direction(0, -1)
DOWN = Direction(0, 1)
LEFT = Direction(-1, 0)
RIGHT = Direction(1, 0)


def parse_racetrack(lines):
    start = (0, 0)
    end = (0, 0)
    for j, line in enumerate(lines):
        for i, cell in enumerate(line):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)

    racetrack = [line.replace('S', '.').replace('E', '.') for line in lines]
    return racetrack, start, end


def get_neighbours(racetrack, position):
    neighbours = set()
    for direction in [UP, DOWN, LEFT, RIGHT]:
        neighbour = (position[0] + direction[0], position[1] + direction[1])
        if racetrack[neighbour[1]][neighbour[0]] == '.':
            neighbours.add(neighbour)
    return neighbours


def find_path(racetrack, start, end):
    position = start
    time = 0
    path = {}
    while position != end:
        path[position] = time
        time += 1
        for neighbour in get_neighbours(racetrack, position):
            if neighbour not in path:
                position = neighbour
                break
    # Account for end position
    path[position] = time
    return path


def is_possible_cheat(racetrack, position):
    empty_adjacent_positions = {}
    height = len(racetrack)
    width = len(racetrack[0])
    if position[0] in (0, width - 1) or position[1] in (0, height - 1):
        return set()
    for direction in [UP, DOWN, LEFT, RIGHT]:
        adjacent_position = (position[0] + direction[0], position[1] + direction[1])
        if racetrack[adjacent_position[1]][adjacent_position[0]] == '.':
            empty_adjacent_positions[direction] = adjacent_position
    if UP in empty_adjacent_positions and DOWN in empty_adjacent_positions:
        return {empty_adjacent_positions[UP], empty_adjacent_positions[DOWN]}
    elif LEFT in empty_adjacent_positions and RIGHT in empty_adjacent_positions:
        return {empty_adjacent_positions[LEFT], empty_adjacent_positions[RIGHT]}
    else:
        return set()


def find_possible_cheats(racetrack):
    possible_cheats = {}
    for j, row in enumerate(racetrack):
        for i, cell in enumerate(row):
            if cell == '#':
                position = (i, j)
                possible_cheat = is_possible_cheat(racetrack, position)
                if possible_cheat:
                    possible_cheats[position] = possible_cheat
    return possible_cheats


def find_time_saved(path, possible_cheats):
    time_saved = {}
    for cheat_position, (cheat_start, cheat_end) in possible_cheats.items():
        time_saved[cheat_position] = abs(path[cheat_start] - path[cheat_end]) - 2
    return time_saved


def count_cheats_saving_at_least(time_saved, time):
    counter = Counter(time_saved.values())
    return sum(number_cheats for time_value, number_cheats in counter.items() if time_value >= time)


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
