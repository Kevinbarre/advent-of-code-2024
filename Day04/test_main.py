import pytest

from main import part1, part2, count_horizontal, rotate, count_vertical, count_diagonal_bottom_right, count_all_diagonal, count_xmas, is_x_mas, count_x_mas

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 18


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 9


def test_count_horizontal():
    # Given
    word_search = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]
    # When
    result = count_horizontal(word_search)
    # Then
    assert result == 5


def test_rotate():
    # Given
    word_search = [
        "..X..",
        "..M..",
        "..A..",
        "..S..",
        "....."
    ]
    # When
    result = rotate(word_search)
    # Then
    assert result == [
        ".....",
        ".....",
        ".SAMX",
        ".....",
        ".....",
    ]


def test_count_vertical():
    # Given
    word_search = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]
    # When
    result = count_vertical(word_search)
    # Then
    assert result == 3


def test_count_diagonal_bottom_right():
    # Given
    word_search = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]
    # When
    result = count_diagonal_bottom_right(word_search)
    # Then
    assert result == 1


def test_count_all_diagonal():
    # Given
    word_search = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]
    # When
    result = count_all_diagonal(word_search)
    # Then
    assert result == 10


def test_count_xmas():
    # Given
    word_search = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]
    # When
    result = count_xmas(word_search)
    # Then
    assert result == 18


@pytest.mark.parametrize("word_search, expected",
                         [(["M.S",
                            ".A.",
                            "M.S"], True),
                          (["S.S",
                            ".A.",
                            "M.M"], True),
                          (["M.M",
                            ".A.",
                            "S.S"], True),
                          (["S.M",
                            ".A.",
                            "S.M"], True),
                          ([".M.",
                            "MAS",
                            ".S."], False),
                          (["S.M",
                            ".A.",
                            "M.S"], False),
                          (["M..",
                            ".A.",
                            "..S"], False),
                          ])
def test_is_mas(word_search, expected):
    # Given
    word_search = [
        "M.S",
        ".A.",
        "M.S"
    ]
    # When
    result = is_x_mas(word_search, 1, 1)
    # Then
    assert result == True


def test_count_x_mas():
    # Given
    word_search = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
    ]
    # When
    result = count_x_mas(word_search)
    # Then
    assert result == 9
