import pytest

from main import part1, part2, blink, step, multiple_steps, parse_arrangement, count_stones

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 55312


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 65601038650482


def test_parse_arrangement():
    # Given
    lines = ["125 17"]
    # When
    result = parse_arrangement(lines)
    # Then
    assert result == {125: 1, 17: 1}


def test_blink_zero():
    # Given
    stone = 0
    # When
    result = blink(stone)
    # Then
    assert result == [1]


@pytest.mark.parametrize("stone, expected",
                         [(89, [8, 9]),
                          (1000, [10, 0])
                          ])
def test_blink_even_digits(stone, expected):
    # Given
    # When
    result = blink(stone)
    # Then
    assert result == expected


@pytest.mark.parametrize("stone, expected",
                         [(1, [2024]),
                          (999, [2021976])
                          ])
def test_blink_others(stone, expected):
    # Given
    # When
    result = blink(stone)
    # Then
    assert result == expected


@pytest.mark.parametrize("arrangement, expected",
                         [({125: 1, 17: 1}, {253000: 1, 1: 1, 7: 1}),
                          ({253000: 1, 1: 1, 7: 1}, {0: 1, 253: 1, 2024: 1, 14168: 1}),
                          ({0: 1, 253: 1, 2024: 1, 14168: 1}, {512072: 1, 1: 1, 20: 1, 24: 1, 28676032: 1}),
                          ({512072: 1, 1: 1, 20: 1, 24: 1, 28676032: 1}, {512: 1, 72: 1, 2024: 1, 2: 2, 0: 1, 4: 1, 2867: 1, 6032: 1}),
                          ({512: 1, 72: 1, 2024: 1, 2: 2, 0: 1, 4: 1, 2867: 1, 6032: 1},
                           {1036288: 1, 7: 1, 2: 1, 20: 1, 24: 1, 4048: 2, 1: 1, 8096: 1, 28: 1, 67: 1, 60: 1, 32: 1}),
                          ({1036288: 1, 7: 1, 2: 1, 20: 1, 24: 1, 4048: 2, 1: 1, 8096: 1, 28: 1, 67: 1, 60: 1, 32: 1},
                           {2097446912: 1, 14168: 1, 4048: 1, 2: 4, 0: 2, 4: 1, 40: 2, 48: 2, 2024: 1, 80: 1, 96: 1, 8: 1, 6: 2, 7: 1, 3: 1}),
                          ])
def test_step(arrangement, expected):
    # Given
    # When
    result = step(arrangement)
    # Then
    assert result == expected


def test_multiple_steps():
    # Given
    arrangement = {125: 1, 17: 1}
    # When
    result = multiple_steps(arrangement, 6)
    # Then
    assert result == {2097446912: 1, 14168: 1, 4048: 1, 2: 4, 0: 2, 4: 1, 40: 2, 48: 2, 2024: 1, 80: 1, 96: 1, 8: 1, 6: 2, 7: 1, 3: 1}


def test_count_stones():
    # Given
    arrangement = {2097446912: 1, 14168: 1, 4048: 1, 2: 4, 0: 2, 4: 1, 40: 2, 48: 2, 2024: 1, 80: 1, 96: 1, 8: 1, 6: 2, 7: 1, 3: 1}
    # When
    result = count_stones(arrangement)
    # Then
    assert result == 22
