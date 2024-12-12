from typing import NamedTuple


def part1(lines):
    regions_by_plot = find_regions_by_plot(lines)
    regions = get_distinct_regions(regions_by_plot)
    return get_total_price(regions)


def part2(lines):
    return 0


class Direction(NamedTuple):
    x: int
    y: int


UP = Direction(0, -1)
DOWN = Direction(0, 1)
LEFT = Direction(-1, 0)
RIGHT = Direction(1, 0)


class Region:
    def __init__(self, letter: chr, members: set, perimeter: int):
        self.letter = letter
        self.members = members
        self.perimeter = perimeter

    def __eq__(self, other):
        return self.letter == other.letter and self.members == other.members and self.perimeter == other.perimeter

    def __hash__(self):
        return hash((self.letter, tuple(self.members), self.perimeter))

    def __repr__(self):
        return "Region('{}', {}, {})".format(self.letter, self.members, self.perimeter)

    def add_member(self, plot, perimeter):
        self.members.add(plot)
        self.perimeter += perimeter

    def merge(self, region, regions_by_plot):
        # Do not merge with self
        if region == self:
            return
        self.members.update(region.members)
        self.perimeter += region.perimeter
        for member in region.members:
            regions_by_plot[member] = self

    @property
    def area(self):
        return len(self.members)


def get_neighbours(plot, garden):
    x, y = plot
    height = len(garden)
    width = len(garden[0])
    neighbours = {}
    for direction in [UP, DOWN, LEFT, RIGHT]:
        i, j = direction
        neighbour_x = x + i
        neighbour_y = y + j
        if 0 <= neighbour_x < width and 0 <= neighbour_y < height:
            neighbours[direction] = (neighbour_x, neighbour_y, garden[neighbour_y][neighbour_x])
    return neighbours


def check_plot(plot, garden, regions_by_plot: dict[tuple, Region]):
    x, y = plot
    current_letter = garden[y][x]
    neighbours = get_neighbours(plot, garden)
    perimeter_contribution = 4 - sum(1 for _, _, letter in neighbours.values() if letter == current_letter)
    # First create a region for the current plot
    current_region = Region(current_letter, {plot}, perimeter_contribution)
    regions_by_plot[plot] = current_region
    if LEFT in neighbours:
        left_neighbour_x, left_neighbour_y, left_neighbour_letter = neighbours[LEFT]
        if left_neighbour_letter == current_letter:
            # Merge current region with the left one
            left_region = regions_by_plot[(left_neighbour_x, left_neighbour_y)]
            left_region.merge(current_region, regions_by_plot)
            # Update current region in case we need to merge it again
            current_region = left_region
    if UP in neighbours:
        up_neighbour_x, up_neighbour_y, up_neighbour_letter = neighbours[UP]
        if up_neighbour_letter == current_letter:
            ## Merge current region with the up one
            up_region = regions_by_plot[(up_neighbour_x, up_neighbour_y)]
            up_region.merge(current_region, regions_by_plot)


def find_regions_by_plot(garden):
    regions_by_plot = {}
    for j in range(len(garden)):
        for i in range(len(garden[j])):
            check_plot((i, j), garden, regions_by_plot)
    return regions_by_plot


def get_distinct_regions(regions_by_plot):
    return set(regions_by_plot.values())


def get_total_price(regions):
    return sum(region.area * region.perimeter for region in regions)


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
