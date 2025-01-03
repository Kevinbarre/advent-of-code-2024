import pytest

from main import part1, part2, parse_instruction_line, compute_instruction, sum_instructions, \
    parse_instruction_line_with_conditions

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 161


def test_part2():
    # Given
    with open("example2.txt") as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 48


def test_parse_instruction_line():
    # Given
    instruction_line = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    # When
    result = parse_instruction_line(instruction_line)
    # Then
    assert result == ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]


def test_compute_instruction():
    # Given
    instruction = "mul(2,4)"
    # When
    result = compute_instruction(instruction)
    # Then
    assert result == 8


def test_sum_instructions():
    # Given
    instructions = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
    # When
    result = sum_instructions(instructions)
    # Then
    assert result == 161


@pytest.mark.parametrize("instruction_line, expected",
                         [("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", ["mul(2,4)", "mul(8,5)"]),
                          ("xmul(2,4)&mul[3,7]!^do()_mul(5,5)+mul(32,64](mul(11,8)undon't()?mul(8,5))", ["mul(2,4)", "mul(5,5)", "mul(11,8)"])
                          ])
def test_parse_instruction_line_with_conditions(instruction_line, expected):
    # Given
    # When
    result = parse_instruction_line_with_conditions(instruction_line)
    # Then
    assert result == expected
