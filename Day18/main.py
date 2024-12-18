import heapq
import math
from typing import NamedTuple


def part1(lines, grid_size, number_bytes):
    coordinates = parse_coordinates(lines)
    grid, start, end = generate_grid(grid_size)
    grid = simulate_fall(grid, coordinates, number_bytes)
    return dijkstra(grid, start, end)


def part2(lines):
    return 0


class Direction(NamedTuple):
    x: int
    y: int


UP = Direction(0, -1)
DOWN = Direction(0, 1)
LEFT = Direction(-1, 0)
RIGHT = Direction(1, 0)


def parse_coordinates(lines):
    coordinates = []
    for line in lines:
        x, y = line.split(',')
        coordinates.append((int(x), int(y)))
    return coordinates


def generate_grid(grid_size):
    border = [['#'] * (grid_size + 3)]
    grid = border + [['#'] + ['.' for _ in range(grid_size + 1)] + ['#'] for _ in range(grid_size + 1)] + border
    start = (1, 1)
    end = (grid_size + 1, grid_size + 1)
    return grid, start, end


def simulate_fall(grid, coordinates, number_bytes):
    for x, y in coordinates[:number_bytes]:
        grid[y + 1][x + 1] = '#'
    return grid


def get_possible_moves(grid, position):
    possible_moves = set()
    for next_direction in [UP, DOWN, LEFT, RIGHT]:
        next_position = (position[0] + next_direction[0], position[1] + next_direction[1])
        if grid[next_position[1]][next_position[0]] == '.':
            possible_moves.add(next_position)
    return possible_moves


def dijkstra(grid, start, end):
    scores = {start: 0}
    next_cells = [(0, start, [start])]
    while next_cells:
        cell_score, cell_position, path = heapq.heappop(next_cells)
        if cell_position == end:
            # End reached, can return
            return cell_score
        possible_moves = get_possible_moves(grid, cell_position)
        for next_position in possible_moves:
            updated_score = cell_score + 1
            if updated_score < scores.get(next_position, math.inf):
                # Update scores with the new one to next position if it's lower than existing one
                scores[next_position] = updated_score
                # Add next position to next cells with its current direction and path used to reach it
                new_path = path + [next_position]
                heapq.heappush(next_cells, (updated_score, next_position, new_path))


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines, 70, 1024))
    print("Part 2 : ", part2(f_lines))
