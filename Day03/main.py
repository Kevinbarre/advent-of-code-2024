import re


def part1(lines):
    instruction_line = ''.join(lines)
    instructions = parse_instruction_line(instruction_line)
    return sum_instructions(instructions)


def part2(lines):
    return 0


def parse_instruction_line(instruction_line):
    return re.findall(r'mul\(\d+,\d+\)', instruction_line)


def compute_instruction(instruction):
    left, right = instruction.split(',')
    operator, number1 = left.split('(')
    number1 = int(number1)
    number2 = int(right.split(')')[0])
    return number1 * number2


def sum_instructions(instructions):
    return sum(compute_instruction(instruction) for instruction in instructions)


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
