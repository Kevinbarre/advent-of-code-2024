from main import part1, part2, parse_input, reorganize, calculate_checksum

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 1928


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 0


def test_parse_input():
    # Given
    lines = ["2333133121414131402"]
    # When
    result = parse_input(lines)
    # Then
    assert result == [
        "0", "0", ".", ".", ".", "1", "1", "1", ".", ".", ".", "2", ".", ".", ".", "3", "3", "3", ".", "4", "4", ".", "5", "5", "5", "5", ".", "6", "6", "6",
        "6", ".", "7", "7", "7", ".", "8", "8", "8", "8", "9", "9"
    ]


def test_reorganize():
    # Given
    disk_map = [
        "0", "0", ".", ".", ".", "1", "1", "1", ".", ".", ".", "2", ".", ".", ".", "3", "3", "3", ".", "4", "4", ".", "5", "5", "5", "5", ".", "6", "6", "6",
        "6", ".", "7", "7", "7", ".", "8", "8", "8", "8", "9", "9"
    ]
    # When
    result = reorganize(disk_map)
    # Then
    assert result == [
        "0", "0", "9", "9", "8", "1", "1", "1", "8", "8", "8", "2", "7", "7", "7", "3", "3", "3", "6", "4", "4", "6", "5", "5", "5", "5", "6", "6", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."
    ]


def test_calculate_checksum():
    # Given
    disk_map = [
        "0", "0", "9", "9", "8", "1", "1", "1", "8", "8", "8", "2", "7", "7", "7", "3", "3", "3", "6", "4", "4", "6", "5", "5", "5", "5", "6", "6", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."
    ]
    # When
    result = calculate_checksum(disk_map)
    # Then
    assert result == 1928
