import itertools
from enum import Enum


def part1(lines):
    equations = parse_input(lines)
    return get_total_calibration_result(equations)


def part2(lines):
    equations = parse_input(lines)
    # return get_total_calibration_result2(equations)
    return get_total_calibration_result_right_to_left(equations)


class Operators(Enum):
    ADD = '+',
    MULT = '*'


class Operators2(Enum):
    ADD = '+',
    MULT = '*',
    CONCAT = '||'


def parse_input(lines):
    equations = []
    for line in lines:
        test_value, numbers = line.split(':')
        test_value = int(test_value)
        numbers = [int(number) for number in numbers.split()]
        equations.append((test_value, numbers))
    return equations


def get_possible_operators(length):
    return {elem for elem in itertools.product(Operators, repeat=length)}


def evaluate(equation):
    test_value, numbers = equation
    possible_operators = get_possible_operators(len(numbers) - 1)
    for possible_operator in possible_operators:
        total = numbers[0]
        for number, operator in zip(numbers[1:], possible_operator):
            if operator == Operators.ADD:
                total += number
            else:  # operator == Operators.MULT
                total *= number
        if total == test_value:
            # Found a working way of combining operators
            return True
    return False


def get_total_calibration_result(equations):
    total = 0
    for equation in equations:
        if evaluate(equation):
            total += equation[0]
    return total


def get_possible_operators2(length):
    exclusion = {elem for elem in itertools.product((Operators2.ADD, Operators2.MULT), repeat=length)}
    return {elem for elem in itertools.product(Operators2, repeat=length)} - exclusion


def concat(left, right):
    return int(str(left) + str(right))


def evaluate2(equation):
    # First check if only using ADD and MULT it works:
    if evaluate(equation):
        return True
    # Otherwise try also using the combinations with concat
    test_value, numbers = equation
    possible_operators = get_possible_operators2(len(numbers) - 1)
    for possible_operator in possible_operators:
        total = numbers[0]
        for number, operator in zip(numbers[1:], possible_operator):
            if operator == Operators2.ADD:
                total += number
            elif operator == Operators2.MULT:
                total *= number
            else:  # operator == Operators2.CONCAT
                total = concat(total, number)
        if total == test_value:
            # Found a working way of combining operators
            return True
    return False


def get_total_calibration_result2(equations):
    total = 0
    for equation in equations:
        if evaluate2(equation):
            total += equation[0]
    return total


def get_possible_operators_right_to_left(length):
    return {elem for elem in itertools.product(Operators2, repeat=length)}


def unconcat(left, right):
    return int(str(left).removesuffix(str(right)))


def evaluate_right_to_left(equation):
    test_value, numbers = equation
    target = numbers[0]
    possible_operators = get_possible_operators_right_to_left(len(numbers) - 1)
    for possible_operator in possible_operators:
        current_value = test_value
        premature_exit = False
        for number, operator in zip(reversed(numbers[1:]), possible_operator):
            if operator == Operators2.ADD:
                current_value -= number
                if current_value < target:
                    # Going below target, can stop processing this iteration
                    premature_exit = True
                    break
            elif operator == Operators2.MULT:
                if current_value % number == 0:
                    current_value //= number
                else:
                    # Not divisible, can stop processing this iteration
                    premature_exit = True
                    break
            else:  # operator == Operators2.CONCAT
                if str(current_value).endswith(str(number)) and current_value != number:
                    current_value = unconcat(current_value, number)
                else:
                    # Not ending with the number, can stop processing this iteration
                    premature_exit = True
                    break
        if not premature_exit and current_value == target:
            # Found a working way of combining operators
            return True
    return False


def get_total_calibration_result_right_to_left(equations):
    total = 0
    for equation in equations:
        if evaluate_right_to_left(equation):
            total += equation[0]
    return total


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
