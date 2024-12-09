import pytest

from main import part1, part2, parse_input, evaluate, Operators, get_possible_operators, get_total_calibration_result, get_possible_operators2, Operators2, \
    evaluate2, concat, get_total_calibration_result2

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 3749


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 11387


def test_parse_input():
    # Given
    lines = [
        "190: 10 19",
        "3267: 81 40 27",
        "83: 17 5",
        "156: 15 6",
        "7290: 6 8 6 15",
        "161011: 16 10 13",
        "192: 17 8 14",
        "21037: 9 7 18 13",
        "292: 11 6 16 20",
    ]
    # When
    result = parse_input(lines)
    # Then
    assert result == [
        (190, [10, 19]),
        (3267, [81, 40, 27]),
        (83, [17, 5]),
        (156, [15, 6]),
        (7290, [6, 8, 6, 15]),
        (161011, [16, 10, 13]),
        (192, [17, 8, 14]),
        (21037, [9, 7, 18, 13]),
        (292, [11, 6, 16, 20]),
    ]


def test_get_possible_operators():
    # Given
    length = 3
    # When
    result = get_possible_operators(length)
    # Then
    assert result == {
        (Operators.ADD, Operators.ADD, Operators.ADD),
        (Operators.ADD, Operators.ADD, Operators.MULT),
        (Operators.ADD, Operators.MULT, Operators.ADD),
        (Operators.MULT, Operators.ADD, Operators.ADD),
        (Operators.ADD, Operators.MULT, Operators.MULT),
        (Operators.MULT, Operators.ADD, Operators.MULT),
        (Operators.MULT, Operators.MULT, Operators.ADD),
        (Operators.MULT, Operators.MULT, Operators.MULT),
    }


@pytest.mark.parametrize("equation, expected",
                         [((190, [10, 19]), True),
                          ((3267, [81, 40, 27]), True),
                          ((83, [17, 5]), False),
                          ((156, [15, 6]), False),
                          ((7290, [6, 8, 6, 15]), False),
                          ((161011, [16, 10, 13]), False),
                          ((192, [17, 8, 14]), False),
                          ((21037, [9, 7, 18, 13]), False),
                          ((292, [11, 6, 16, 20]), True)
                          ])
def test_evaluate(equation, expected):
    # Given
    # When
    result = evaluate(equation)
    # Then
    assert result == expected


def test_get_total_calibration_result():
    # Given
    equations = [
        (190, [10, 19]),
        (3267, [81, 40, 27]),
        (83, [17, 5]),
        (156, [15, 6]),
        (7290, [6, 8, 6, 15]),
        (161011, [16, 10, 13]),
        (192, [17, 8, 14]),
        (21037, [9, 7, 18, 13]),
        (292, [11, 6, 16, 20]),
    ]
    # When
    result = get_total_calibration_result(equations)
    # Then
    assert result == 3749


def test_get_possible_operators2():
    # Given
    length = 3
    # When
    result = get_possible_operators2(length)
    # Then
    assert result == {
        (Operators2.ADD, Operators2.ADD, Operators2.CONCAT),
        (Operators2.ADD, Operators2.CONCAT, Operators2.ADD),
        (Operators2.CONCAT, Operators2.ADD, Operators2.ADD),
        (Operators2.ADD, Operators2.CONCAT, Operators2.CONCAT),
        (Operators2.CONCAT, Operators2.ADD, Operators2.CONCAT),
        (Operators2.CONCAT, Operators2.CONCAT, Operators2.ADD),
        (Operators2.CONCAT, Operators2.CONCAT, Operators2.CONCAT),
        (Operators2.ADD, Operators2.CONCAT, Operators2.MULT),
        (Operators2.CONCAT, Operators2.ADD, Operators2.MULT),
        (Operators2.CONCAT, Operators2.CONCAT, Operators2.MULT),
        (Operators2.ADD, Operators2.MULT, Operators2.CONCAT),
        (Operators2.CONCAT, Operators2.MULT, Operators2.ADD),
        (Operators2.CONCAT, Operators2.MULT, Operators2.CONCAT),
        (Operators2.MULT, Operators2.ADD, Operators2.CONCAT),
        (Operators2.MULT, Operators2.CONCAT, Operators2.ADD),
        (Operators2.MULT, Operators2.CONCAT, Operators2.CONCAT),
        (Operators2.CONCAT, Operators2.MULT, Operators2.MULT),
        (Operators2.MULT, Operators2.CONCAT, Operators2.MULT),
        (Operators2.MULT, Operators2.MULT, Operators2.CONCAT)
    }


def test_concat():
    # Given
    left = 123
    right = 456
    # When
    result = concat(left, right)
    # Then
    assert result == 123456


@pytest.mark.parametrize("equation, expected",
                         [((190, [10, 19]), True),
                          ((3267, [81, 40, 27]), True),
                          ((83, [17, 5]), False),
                          ((156, [15, 6]), True),
                          ((7290, [6, 8, 6, 15]), True),
                          ((161011, [16, 10, 13]), False),
                          ((192, [17, 8, 14]), True),
                          ((21037, [9, 7, 18, 13]), False),
                          ((292, [11, 6, 16, 20]), True)
                          ])
def test_evaluate2(equation, expected):
    # Given
    # When
    result = evaluate2(equation)
    # Then
    assert result == expected


def test_get_total_calibration_result2():
    # Given
    equations = [
        (190, [10, 19]),
        (3267, [81, 40, 27]),
        (83, [17, 5]),
        (156, [15, 6]),
        (7290, [6, 8, 6, 15]),
        (161011, [16, 10, 13]),
        (192, [17, 8, 14]),
        (21037, [9, 7, 18, 13]),
        (292, [11, 6, 16, 20]),
    ]
    # When
    result = get_total_calibration_result2(equations)
    # Then
    assert result == 11387
