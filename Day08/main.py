import itertools
from collections import defaultdict


def part1(lines):
    antennas, city_dimensions = parse_input(lines)
    return count_unique_antinodes(antennas, city_dimensions)


def part2(lines):
    antennas, city_dimensions = parse_input(lines)
    return count_unique_antinodes_with_harmonics(antennas, city_dimensions)


def parse_input(lines):
    antennas = defaultdict(set)
    for j, line in enumerate(lines):
        for i, cell in enumerate(line):
            if cell != '.':
                antennas[cell].add((i, j))
    return antennas, (len(lines[0]), len(lines))


def get_antinodes(first_antenna, second_antenna, city_dimensions):
    antenna_spacing = (first_antenna[0] - second_antenna[0], first_antenna[1] - second_antenna[1])
    first_antinode = (first_antenna[0] + antenna_spacing[0], first_antenna[1] + antenna_spacing[1])
    second_antinode = (second_antenna[0] - antenna_spacing[0], second_antenna[1] - antenna_spacing[1])
    return {antinode for antinode in {first_antinode, second_antinode} if 0 <= antinode[0] < city_dimensions[0] and 0 <= antinode[1] < city_dimensions[1]}


def count_unique_antinodes(antennas, city_dimensions):
    antinodes = set()
    for frequency, positions in antennas.items():
        for first_antenna, second_antenna in itertools.combinations(positions, 2):
            antinodes.update(get_antinodes(first_antenna, second_antenna, city_dimensions))
    return len(antinodes)


def get_antinodes_with_harmonics(first_antenna, second_antenna, city_dimensions):
    antenna_spacing = (first_antenna[0] - second_antenna[0], first_antenna[1] - second_antenna[1])
    antinodes = set()
    #  First direction
    multiplier = 0
    while True:
        antinode = (first_antenna[0] + multiplier * antenna_spacing[0], first_antenna[1] + multiplier * antenna_spacing[1])
        if 0 <= antinode[0] < city_dimensions[0] and 0 <= antinode[1] < city_dimensions[1]:
            antinodes.add(antinode)
            multiplier += 1
        else:
            # Outside the map
            break
    # Second direction
    multiplier = 0
    while True:
        antinode = (first_antenna[0] - multiplier * antenna_spacing[0], first_antenna[1] - multiplier * antenna_spacing[1])
        if 0 <= antinode[0] < city_dimensions[0] and 0 <= antinode[1] < city_dimensions[1]:
            antinodes.add(antinode)
            multiplier += 1
        else:
            # Outside the map
            break
    return antinodes


def count_unique_antinodes_with_harmonics(antennas, city_dimensions):
    antinodes = set()
    for frequency, positions in antennas.items():
        for first_antenna, second_antenna in itertools.combinations(positions, 2):
            antinodes.update(get_antinodes_with_harmonics(first_antenna, second_antenna, city_dimensions))
    return len(antinodes)


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
