import heapq
import math
from typing import NamedTuple


def part1(lines):
    level, start, end = parse_level(lines)
    return dijkstra(level, start, end)


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
    start = (0, 0)
    end = (0, 0)
    for j, row in enumerate(lines):
        for i, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            if cell == 'E':
                end = (i, j)
    level = [line.replace('S', '.').replace('E', '.') for line in lines]
    return level, start, end


def get_next_direction_score(direction, next_direction):
    if direction == next_direction:
        return 1
    elif direction[0] == -1 * next_direction[0] and direction[1] == -1 * next_direction[1]:
        return 2001
    else:
        return 1001


def get_possible_moves(level, position, direction):
    possible_moves = set()
    for next_direction in [UP, DOWN, LEFT, RIGHT]:
        next_position = (position[0] + next_direction[0], position[1] + next_direction[1])
        if level[next_position[1]][next_position[0]] == '.':
            possible_moves.add((next_position, next_direction, get_next_direction_score(direction, next_direction)))
    return possible_moves


def dijkstra(level, start, end):
    scores = {(start, RIGHT): 0}
    next_cells = [(0, start, RIGHT, [start])]
    while next_cells:
        cell_score, cell_position, cell_direction, path = heapq.heappop(next_cells)
        if cell_position == end:
            # End reached, can return
            return cell_score
        possible_moves = get_possible_moves(level, cell_position, cell_direction)
        for next_position, next_direction, next_score in possible_moves:
            updated_score = cell_score + next_score
            if updated_score < scores.get((next_position, next_direction), math.inf):
                # Update scores with the new one to next position with next direction if it's lower than existing one
                scores[(next_position, next_direction)] = updated_score
                # Add next position to next cells with its current direction and path used to reach it
                new_path = path + [next_position]
                heapq.heappush(next_cells, (updated_score, next_position, next_direction, new_path))


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
