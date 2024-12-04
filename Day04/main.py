def part1(lines):
    return count_xmas(lines)


def part2(lines):
    return count_x_mas(lines)


def count_horizontal(word_search):
    total = sum(row.count('XMAS') for row in word_search)
    total += sum(row.count('SAMX') for row in word_search)
    return total


def rotate(word_search):
    return ["".join(row) for row in zip(*reversed(word_search))]


def count_vertical(word_search):
    rotated_word_search = rotate(word_search)
    return count_horizontal(rotated_word_search)


def count_diagonal_bottom_right(word_search):
    total = 0
    for j in range(len(word_search) - 3):
        for i in range(len(word_search[j]) - 3):
            if word_search[j][i] == 'X' and word_search[j + 1][i + 1] == 'M' and word_search[j + 2][i + 2] == 'A' and word_search[j + 3][i + 3] == 'S':
                total += 1
    return total


def count_all_diagonal(word_search):
    total = count_diagonal_bottom_right(word_search)
    rotated_word_search = word_search
    for i in range(3):
        rotated_word_search = rotate(rotated_word_search)
        count = count_diagonal_bottom_right(rotated_word_search)
        total += count_diagonal_bottom_right(rotated_word_search)
    return total


def count_xmas(word_search):
    return count_horizontal(word_search) + count_vertical(word_search) + count_all_diagonal(word_search)


def is_x_mas(word_search, x, y):
    """
    Search for an X-MAS, in the two diagonals directions, assuming (x,y) are the coordinates of an A, always at the center of the cross

    :param word_search: Grid to search for
    :param x: X coordinate (column)
    :param y: Y coordinate (row)
    :return: True if an X-MAS is found, False otherwise
    """
    count_mas = 0
    # Top-left to bottom-right diagonal
    if word_search[y - 1][x - 1] == 'M' and word_search[y + 1][x + 1] == 'S' or word_search[y - 1][x - 1] == 'S' and word_search[y + 1][x + 1] == 'M':
        count_mas += 1
    # Top-right to bottom-left diagonal
    if word_search[y - 1][x + 1] == 'M' and word_search[y + 1][x - 1] == 'S' or word_search[y - 1][x + 1] == 'S' and word_search[y + 1][x - 1] == 'M':
        count_mas += 1
    return count_mas == 2


def count_x_mas(word_search):
    total = 0
    for y in range(1, len(word_search) - 1):
        for x in range(1, len(word_search[y]) - 1):
            if word_search[y][x] == 'A' and is_x_mas(word_search, x, y):
                total += 1
    return total


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
