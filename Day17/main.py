def part1(lines):
    a, b, c, instructions = parse_input(lines)
    a, b, c, outputs = execute_program(a, b, c, instructions)
    return join_outputs(outputs)


def part2(lines):
    _, b, c, instructions = parse_input(lines)
    return find_a(b, c, instructions)


def parse_input(lines):
    a, b, c = (int(line.split()[-1]) for line in lines[:3])
    raw_instructions = lines[4].split()[1].split(',')
    instructions = [int(instruction) for instruction in raw_instructions]
    return a, b, c, instructions


def combo_operand(operand, a, b, c):
    if operand in range(0, 4):
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:  # 7, will not appear in valid programs
        return False


def dv(numerator, operand, a, b, c):
    return numerator // (2 ** combo_operand(operand, a, b, c))


def xor(left, right):
    return left ^ right


def mod8(operand, a, b, c):
    return combo_operand(operand, a, b, c) % 8


def jump(operand, a):
    if a == 0:
        return None
    else:
        return operand


def execute_instruction(instruction, operand, a, b, c, pointer):
    pointer += 2
    output = None
    if instruction == 0:  # adv
        a = dv(a, operand, a, b, c)
    elif instruction == 1:  # bxl
        b = xor(b, operand)
    elif instruction == 2:  # bst
        b = mod8(operand, a, b, c)
    elif instruction == 3:  # jnz
        jmp = jump(operand, a)
        if jmp is not None:
            pointer = jmp
    elif instruction == 4:  # bxc
        b = xor(b, c)
    elif instruction == 5:  # out
        output = mod8(operand, a, b, c)
    elif instruction == 6:  # bdv
        b = dv(a, operand, a, b, c)
    else:  # instruction == 7: # cdv
        c = dv(a, operand, a, b, c)
    return a, b, c, pointer, output


def execute_program(a, b, c, instructions):
    pointer = 0
    outputs = []
    while pointer < len(instructions) - 1:
        instruction = instructions[pointer]
        operand = instructions[pointer + 1]
        a, b, c, pointer, output = execute_instruction(instruction, operand, a, b, c, pointer)
        if output is not None:
            outputs.append(output)
    return a, b, c, outputs


def join_outputs(outputs):
    return ','.join(str(output) for output in outputs)


def build_octal(a_octal_digits):
    power = len(a_octal_digits) - 1
    return sum(digit * (8 ** (power - i)) for i, digit in enumerate(a_octal_digits))


def find_a(b, c, instructions):
    power = len(instructions) - 1
    i = 0
    a_octal_digits = [0] * len(instructions)
    a_octal_digits[0] = 1
    while power >= 0:
        sublist = instructions[power:]
        a = build_octal(a_octal_digits)
        _, _, _, outputs = execute_program(a, b, c, instructions)
        if outputs[power:] == sublist:
            # Correct 'a' found for this power, move on to the next index
            i += 1
            power -= 1
        else:
            # Increment digit for current index
            a_octal_digits[i] += 1
            while a_octal_digits[i] == 8:
                # No solution found, need to go back to the previous digit
                a_octal_digits[i] = 0
                i -= 1
                a_octal_digits[i] += 1
                power += 1
    return build_octal(a_octal_digits)


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
