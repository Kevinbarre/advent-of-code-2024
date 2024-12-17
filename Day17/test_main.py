import pytest

from main import part1, part2, parse_input, dv, combo_operand, xor, mod8, jump, execute_instruction, execute_program, join_outputs

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == "4,6,3,5,6,3,5,2,1,0"


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
    lines = [
        "Register A: 729",
        "Register B: 0",
        "Register C: 0",
        "",
        "Program: 0,1,5,4,3,0"
    ]
    # When
    a, b, c, instructions = parse_input(lines)
    # Then
    assert a == 729
    assert b == 0
    assert c == 0
    assert instructions == [0, 1, 5, 4, 3, 0]


@pytest.mark.parametrize("operand, expected",
                         [(0, 0),
                          (1, 1),
                          (2, 2),
                          (3, 3),
                          (4, 11),
                          (5, 22),
                          (6, 33),
                          (7, False)
                          ])
def test_combo_operand(operand, expected):
    # Given
    a = 11
    b = 22
    c = 33
    # When
    result = combo_operand(operand, a, b, c)
    # Then
    assert result == expected


def test_dv():
    # Given
    numerator = 11
    operand = 2
    a, b, c = 0, 0, 0
    # When
    result = dv(numerator, operand, a, b, c)
    # Then
    assert result == 2


@pytest.mark.parametrize("left, right, expected",
                         [(5, 3, 6),
                          (2, 10, 8),
                          (22, 4, 18)
                          ])
def test_xor(left, right, expected):
    # Given
    # When
    result = xor(left, right)
    # Then
    assert result == expected


@pytest.mark.parametrize("operand, expected",
                         [(0, 0),
                          (1, 1),
                          (2, 2),
                          (3, 3),
                          (4, 3),
                          (5, 6),
                          (6, 1),
                          ])
def test_mod8(operand, expected):
    # Given
    a = 11
    b = 22
    c = 33
    # When
    result = mod8(operand, a, b, c)
    # Then
    assert result == expected


@pytest.mark.parametrize("a, operand, expected",
                         [(0, 6, None),
                          (1, 6, 6),
                          (1, 0, 0)
                          ])
def test_jump(a, operand, expected):
    # Given
    # When
    result = jump(operand, a)
    # Then
    assert result == expected


@pytest.mark.parametrize("instruction, expected",
                         [(0, (0, 22, 33, 2, None)),
                          (1, (11, 18, 33, 2, None)),
                          (2, (11, 3, 33, 2, None)),
                          (3, (11, 22, 33, 4, None)),
                          (4, (11, 55, 33, 2, None)),
                          (5, (11, 22, 33, 2, 3)),
                          (6, (11, 0, 33, 2, None)),
                          (7, (11, 22, 0, 2, None))
                          ])
def test_execute_instruction(instruction, expected):
    # Given
    operand = 4
    a = 11
    b = 22
    c = 33
    pointer = 0
    # When
    result = execute_instruction(instruction, operand, a, b, c, pointer)
    # Then
    assert result == expected


def test_execute_instruction_jump_to_0():
    # Given
    instruction = 3
    operand = 0
    a = 1
    b = 0
    c = 0
    pointer = 4
    # When
    a, b, c, pointer, output = execute_instruction(instruction, operand, a, b, c, pointer)
    # Then
    assert a == 1
    assert b == 0
    assert c == 0
    assert pointer == 0
    assert output is None


@pytest.mark.parametrize("a, b, c, instructions, expected_a, expected_b, expected_c, expected_outputs",
                         [(0, 0, 9, [2, 6], 0, 1, 9, []),
                          (10, 0, 0, [5, 0, 5, 1, 5, 4], 10, 0, 0, [0, 1, 2]),
                          (2024, 0, 0, [0, 1, 5, 4, 3, 0], 0, 0, 0, [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0]),
                          (0, 29, 0, [1, 7], 0, 26, 0, []),
                          (0, 2024, 43690, [4, 0], 0, 44354, 43690, [])
                          ])
def test_execute_program(a, b, c, instructions, expected_a, expected_b, expected_c, expected_outputs):
    # Given
    # When
    a, b, c, outputs = execute_program(a, b, c, instructions)
    # Then
    assert a == expected_a
    assert b == expected_b
    assert c == expected_c
    assert outputs == expected_outputs


def test_join_outputs():
    # Given
    outputs = [4, 6, 3, 5, 6, 3, 5, 2, 1, 0]
    # When
    result = join_outputs(outputs)
    # Then
    assert result == "4,6,3,5,6,3,5,2,1,0"
