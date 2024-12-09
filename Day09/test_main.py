from main import part1, part2, parse_input, reorganize, calculate_checksum, reorganize_whole_files, search_next_empty_space

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
    assert result == 2858


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


def test_reorganize_whole_files():
    # Given
    disk_map = [
        "0", "0", ".", ".", ".", "1", "1", "1", ".", ".", ".", "2", ".", ".", ".", "3", "3", "3", ".", "4", "4", ".", "5", "5", "5", "5", ".", "6", "6", "6",
        "6", ".", "7", "7", "7", ".", "8", "8", "8", "8", "9", "9"
    ]
    # When
    result = reorganize_whole_files(disk_map)
    # Then
    assert result == [
        "0", "0", "9", "9", "2", "1", "1", "1", "7", "7", "7", ".", "4", "4", ".", "3", "3", "3", ".", ".", ".", ".", "5", "5", "5", "5", ".", "6", "6", "6",
        "6", ".", ".", ".", ".", ".", "8", "8", "8", "8", ".", "."
    ]


def test_search_next_empty_space():
    # Given
    disk_map = ["0", "0", ".", "1", ".", ".", ".", "2", "3"]
    # When
    result = search_next_empty_space(disk_map, 3, -1)
    # Then
    assert result == 4


def test_search_next_empty_space_at_end():
    # Given
    disk_map = ["0", "0", ".", "1", ".", ".", ".", ".", "."]
    # When
    result = search_next_empty_space(disk_map, 5, -1)
    # Then
    assert result == 4


def test_search_next_empty_space_none_found():
    # Given
    disk_map = ["0", "0", ".", "1", ".", ".", ".", "2", "3"]
    # When
    result = search_next_empty_space(disk_map, 4, -1)
    # Then
    assert result == False


def test_search_next_empty_space_after_j():
    # Given
    disk_map = ["0", "0", ".", "1", ".", ".", ".", ".", "."]
    # When
    result = search_next_empty_space(disk_map, 5, -6)
    # Then
    assert result == False


def test_calculate_checksum_with_spaces():
    # Given
    disk_map = [
        "0", "0", "9", "9", "2", "1", "1", "1", "7", "7", "7", ".", "4", "4", ".", "3", "3", "3", ".", ".", ".", ".", "5", "5", "5", "5", ".", "6", "6", "6",
        "6", ".", ".", ".", ".", ".", "8", "8", "8", "8", ".", "."
    ]
    # When
    result = calculate_checksum(disk_map)
    # Then
    assert result == 2858
