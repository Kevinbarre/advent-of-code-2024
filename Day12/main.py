from typing import NamedTuple


def part1(lines):
    regions_by_plot = find_regions_by_plot(lines)
    regions = get_distinct_regions(regions_by_plot)
    return get_total_price(regions)


def part2(lines):
    regions_by_plot = find_regions_by_plot(lines)
    regions = get_distinct_regions(regions_by_plot)
    return get_total_price_with_discount(regions)


class Direction(NamedTuple):
    x: int
    y: int


UP = Direction(0, -1)
DOWN = Direction(0, 1)
LEFT = Direction(-1, 0)
RIGHT = Direction(1, 0)


class Region:
    def __init__(self, letter: chr, members: set, perimeter: int, sides: int):
        self.letter = letter
        self.members = members
        self.perimeter = perimeter
        self.sides = sides

    def __eq__(self, other):
        return self.letter == other.letter and self.members == other.members and self.perimeter == other.perimeter and self.sides == other.sides

    def __hash__(self):
        return hash((self.letter, tuple(self.members), self.perimeter, self.sides))

    def __repr__(self):
        return "Region('{}', {}, {}, {})".format(self.letter, self.members, self.perimeter, self.sides)

    def add_member(self, plot, perimeter, sides):
        self.members.add(plot)
        self.perimeter += perimeter
        self.sides += sides

    def merge(self, region, regions_by_plot):
        # Do not merge with self
        if region == self:
            return
        self.members.update(region.members)
        self.perimeter += region.perimeter
        self.sides += region.sides
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
    side_contributions = count_corners(plot, garden)
    # First create a region for the current plot
    current_region = Region(current_letter, {plot}, perimeter_contribution, side_contributions)
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


def count_corners(plot, garden):
    total = 0
    x, y = plot
    height = len(garden)
    width = len(garden[0])
    current_letter = garden[y][x]
    above_letter = garden[y - 1][x] if y - 1 >= 0 else None
    below_letter = garden[y + 1][x] if y + 1 < height else None
    left_letter = garden[y][x - 1] if x - 1 >= 0 else None
    right_letter = garden[y][x + 1] if x + 1 < width else None
    diagonal_top_left_letter = garden[y - 1][x - 1] if x - 1 >= 0 and y - 1 >= 0 else None
    diagonal_top_right_letter = garden[y - 1][x + 1] if x + 1 < width and y - 1 >= 0 else None
    diagonal_bottom_left_letter = garden[y + 1][x - 1] if x - 1 >= 0 and y + 1 < height else None
    diagonal_bottom_right_letter = garden[y + 1][x + 1] if x + 1 < width and y + 1 < height else None
    # Top-left corner
    if current_letter != above_letter and current_letter != left_letter:
        # Case when there is no continuous letter
        total += 1
    if current_letter == above_letter == left_letter and current_letter != diagonal_top_left_letter:
        # Case when there is an angle
        total += 1
    # Top-right corner
    if current_letter != above_letter and current_letter != right_letter:
        # Case when there is no continuous letter
        total += 1
    if current_letter == above_letter == right_letter and current_letter != diagonal_top_right_letter:
        # Case when there is an angle
        total += 1
    # Bottom-left corner
    if current_letter != below_letter and current_letter != left_letter:
        # Case when there is no continuous letter
        total += 1
    if current_letter == below_letter == left_letter and current_letter != diagonal_bottom_left_letter:
        # Case when there is an angle
        total += 1
    # Bottom-right corner
    if current_letter != below_letter and current_letter != right_letter:
        # Case when there is no continuous letter
        total += 1
    if current_letter == below_letter == right_letter and current_letter != diagonal_bottom_right_letter:
        # Case when there is an angle
        total += 1
    return total


def get_total_price_with_discount(regions):
    return sum(region.area * region.sides for region in regions)


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
