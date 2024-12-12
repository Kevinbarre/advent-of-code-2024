import pytest

from main import part1, part2, get_neighbours, RIGHT, DOWN, LEFT, UP, Region, check_plot, find_regions_by_plot, get_distinct_regions, get_total_price

filename = "example.txt"


@pytest.mark.parametrize("file_name, expected",
                         [(filename, 140),
                          ("example2.txt", 772),
                          ("example3.txt", 1930)
                          ])
def test_part1(file_name, expected):
    # Given
    with open(file_name) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == expected


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 0


@pytest.mark.parametrize("plot, expected",
                         [((0, 0), {RIGHT: (1, 0, 'A'), DOWN: (0, 1, 'B')}),
                          ((1, 0), {LEFT: (0, 0, 'A'), RIGHT: (2, 0, 'A'), DOWN: (1, 1, 'B')}),
                          ((2, 1), {UP: (2, 0, 'A'), DOWN: (2, 2, 'C'), LEFT: (1, 1, 'B'), RIGHT: (3, 1, 'D')})
                          ])
def test_get_neighbours(plot, expected):
    # Given
    garden = [
        "AAAA",
        "BBCD",
        "BBCC",
        "EEEC"
    ]
    # When
    result = get_neighbours(plot, garden)
    # Then
    assert result == expected


def test_check_plot_create_region():
    # Given
    garden = [
        "AAAA",
        "BBCD",
        "BBCC",
        "EEEC"
    ]
    plot = (0, 0)
    regions_by_plot = {}
    # When
    check_plot(plot, garden, regions_by_plot)
    # Then
    assert regions_by_plot == {
        (0, 0): Region('A', {(0, 0)}, 3)
    }


def test_check_plot_add_to_left_region():
    # Given
    garden = [
        "AAAA",
        "BBCD",
        "BBCC",
        "EEEC"
    ]
    plot = (1, 0)
    regions_by_plot = {
        (0, 0): Region('A', {(0, 0)}, 3)
    }
    # When
    check_plot(plot, garden, regions_by_plot)
    # Then
    assert regions_by_plot == {
        (0, 0): Region('A', {(0, 0), (1, 0)}, 5),
        (1, 0): Region('A', {(0, 0), (1, 0)}, 5)
    }


def test_check_plot_add_to_top_region():
    # Given
    garden = [
        "AAAA",
        "BBCD",
        "BBCC",
        "EEEC"
    ]
    plot = (0, 2)
    region_a = Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10)
    region_b = Region('B', {(0, 1), (1, 1)}, 4)
    region_c = Region('C', {(2, 1)}, 3)
    region_d = Region('D', {(3, 1)}, 4)
    regions_by_plot = {
        (0, 0): region_a,
        (1, 0): region_a,
        (2, 0): region_a,
        (3, 0): region_a,
        (0, 1): region_b,
        (1, 1): region_b,
        (2, 1): region_c,
        (3, 1): region_d,
    }
    # When
    check_plot(plot, garden, regions_by_plot)
    # Then
    assert regions_by_plot == {
        (0, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (1, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (2, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (3, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (0, 1): Region('B', {(0, 1), (1, 1), (0, 2)}, 6),
        (1, 1): Region('B', {(0, 1), (1, 1), (0, 2)}, 6),
        (2, 1): Region('C', {(2, 1)}, 3),
        (3, 1): Region('D', {(3, 1)}, 4),
        (0, 2): Region('B', {(0, 1), (1, 1), (0, 2)}, 6),
    }


def test_check_plot_add_to_left_and_up_region():
    # Given
    garden = [
        "AAAA",
        "BBCD",
        "BBCC",
        "EEEC"
    ]
    plot = (1, 2)
    region_a = Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10)
    region_b = Region('B', {(0, 1), (1, 1), (0, 2)}, 6)
    region_c = Region('C', {(2, 1)}, 3)
    region_d = Region('D', {(3, 1)}, 4)
    regions_by_plot = {
        (0, 0): region_a,
        (1, 0): region_a,
        (2, 0): region_a,
        (3, 0): region_a,
        (0, 1): region_b,
        (1, 1): region_b,
        (2, 1): region_c,
        (3, 1): region_d,
        (0, 2): region_b
    }
    # When
    check_plot(plot, garden, regions_by_plot)
    # Then
    assert regions_by_plot == {
        (0, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (1, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (2, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (3, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (0, 1): Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        (1, 1): Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        (2, 1): Region('C', {(2, 1)}, 3),
        (3, 1): Region('D', {(3, 1)}, 4),
        (0, 2): Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        (1, 2): Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8)
    }


def test_check_plot_merge_left_and_up_region():
    # Given
    garden = [
        "AB",
        "BB"
    ]
    plot = (1, 1)
    region_a = Region('A', {(0, 0)}, 4)
    region_b1 = Region('B', {(1, 0)}, 3)
    region_b2 = Region('B', {(0, 1)}, 3)
    regions_by_plot = {
        (0, 0): region_a,
        (1, 0): region_b1,
        (0, 1): region_b2,
    }
    # When
    check_plot(plot, garden, regions_by_plot)
    # Then
    assert regions_by_plot == {
        (0, 0): Region('A', {(0, 0)}, 4),
        (1, 0): Region('B', {(1, 0), (0, 1), (1, 1)}, 8),
        (0, 1): Region('B', {(1, 0), (0, 1), (1, 1)}, 8),
        (1, 1): Region('B', {(1, 0), (0, 1), (1, 1)}, 8)
    }


def test_find_regions_by_plot():
    # Given
    garden = [
        "AAAA",
        "BBCD",
        "BBCC",
        "EEEC"
    ]
    # When
    result = find_regions_by_plot(garden)
    # Then
    assert result == {
        (0, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (1, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (2, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (3, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (0, 1): Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        (1, 1): Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        (2, 1): Region('C', {(2, 1), (2, 2), (3, 2), (3, 3)}, 10),
        (3, 1): Region('D', {(3, 1)}, 4),
        (0, 2): Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        (1, 2): Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        (2, 2): Region('C', {(2, 1), (2, 2), (3, 2), (3, 3)}, 10),
        (3, 2): Region('C', {(2, 1), (2, 2), (3, 2), (3, 3)}, 10),
        (0, 3): Region('E', {(0, 3), (1, 3), (2, 3)}, 8),
        (1, 3): Region('E', {(0, 3), (1, 3), (2, 3)}, 8),
        (2, 3): Region('E', {(0, 3), (1, 3), (2, 3)}, 8),
        (3, 3): Region('C', {(2, 1), (2, 2), (3, 2), (3, 3)}, 10)
    }


def test_get_distinct_regions():
    # Given
    regions_by_plot = {
        (0, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (1, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (2, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (3, 0): Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        (0, 1): Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        (1, 1): Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        (2, 1): Region('C', {(2, 1), (2, 2), (3, 2), (3, 3)}, 10),
        (3, 1): Region('D', {(3, 1)}, 4),
        (0, 2): Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        (1, 2): Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        (2, 2): Region('C', {(2, 1), (2, 2), (3, 2), (3, 3)}, 10),
        (3, 2): Region('C', {(2, 1), (2, 2), (3, 2), (3, 3)}, 10),
        (0, 3): Region('E', {(0, 3), (1, 3), (2, 3)}, 8),
        (1, 3): Region('E', {(0, 3), (1, 3), (2, 3)}, 8),
        (2, 3): Region('E', {(0, 3), (1, 3), (2, 3)}, 8),
        (3, 3): Region('C', {(2, 1), (2, 2), (3, 2), (3, 3)}, 10)
    }
    # When
    result = get_distinct_regions(regions_by_plot)
    # Then
    assert result == {
        Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        Region('C', {(2, 1), (2, 2), (3, 2), (3, 3)}, 10),
        Region('D', {(3, 1)}, 4),
        Region('E', {(0, 3), (1, 3), (2, 3)}, 8),
    }


def test_get_total_price():
    # Given
    regions = {
        Region('A', {(0, 0), (1, 0), (2, 0), (3, 0)}, 10),
        Region('B', {(0, 1), (1, 1), (0, 2), (1, 2)}, 8),
        Region('C', {(2, 1), (2, 2), (3, 2), (3, 3)}, 10),
        Region('D', {(3, 1)}, 4),
        Region('E', {(0, 3), (1, 3), (2, 3)}, 8),
    }
    # When
    result = get_total_price(regions)
    # Then
    assert result == 140
