from collections import deque


def part1(lines):
    topographic_map = parse_input(lines)
    return get_sum_trailhead_scores(topographic_map)


def part2(lines):
    return 0


def parse_input(lines):
    return [[int(cell) for cell in line] for line in lines]


def find_trailheads(topographic_map):
    return {(x, y) for y, row in enumerate(topographic_map) for x, cell in enumerate(row) if cell == 0}


def get_neighbours(trailhead, topographic_map):
    x, y = trailhead
    height = len(topographic_map)
    width = len(topographic_map[0])
    return {(x + i, y + j) for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)] if 0 <= x + i < width and 0 <= y + j < height}


def find_hiking_trails(trailhead, topographic_map):
    pending_trails = deque()
    pending_trails.append([trailhead])
    hiking_trails = set()
    while pending_trails:
        current_trail = pending_trails.pop()
        last_cell = current_trail[-1]
        last_cell_value = topographic_map[last_cell[1]][last_cell[0]]
        neighbours = get_neighbours(last_cell, topographic_map)
        for neighbour in neighbours:
            neighbour_value = topographic_map[neighbour[1]][neighbour[0]]
            if neighbour_value == last_cell_value + 1:
                new_trail = current_trail.copy()
                new_trail.append(neighbour)
                if neighbour_value == 9:
                    # End of the hiking trail
                    hiking_trails.add(tuple(new_trail))
                else:
                    # Keep walking on this trail
                    pending_trails.append(new_trail)
    return hiking_trails


def get_trailhead_score(trailhead, topographic_map):
    hiking_trails = find_hiking_trails(trailhead, topographic_map)
    destinations = {hiking_trail[-1] for hiking_trail in hiking_trails}
    return len(destinations)


def get_sum_trailhead_scores(topographic_map):
    trailheads = find_trailheads(topographic_map)
    return sum(get_trailhead_score(trailhead, topographic_map) for trailhead in trailheads)


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
