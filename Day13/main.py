def part1(lines):
    claw_machines = parse_input(lines)
    return sum_total_tokens(claw_machines)


def part2(lines):
    return 0


def split_input_line(raw_line):
    _, right = raw_line.split(':')
    raw_x, raw_y = right.split()
    x = int(raw_x[2:-1])
    y = int(raw_y[2:])
    return x, y


def parse_input(lines):
    line_groups = []
    current_group = []
    for line in lines:
        if line != "":
            current_group.append(line)
        else:
            line_groups.append(current_group)
            current_group = []
    # Append last group
    line_groups.append(current_group)

    claw_machines = []
    for raw_button_a, raw_button_b, raw_prize in line_groups:
        a = split_input_line(raw_button_a)
        b = split_input_line(raw_button_b)
        prize = split_input_line(raw_prize)
        claw_machines.append((a, b, prize))
    return claw_machines


def find_cheapest_solution(claw_machine):
    """
    x = number of press on A
    y = number of press on B
    Solution solves:
    - x*a_x + y*b_x = prize_x
    - y*a_y + y*b_y = prize_y
    Which is: (https://fr.wikipedia.org/wiki/R%C3%A8gle_de_Cramer)
    - x = (prize_x * b_y - prize_y * b_x) / (a_x * b_y - a_y * b_x)
    - y = (a_x * prize_y - a_y * prize_x) / (a_x * b_y - a_y * b_x)
    """
    a, b, prize = claw_machine
    a_x, a_y = a
    b_x, b_y = b
    prize_x, prize_y = prize
    x = (prize_x * b_y - prize_y * b_x) / (a_x * b_y - a_y * b_x)
    y = (a_x * prize_y - a_y * prize_x) / (a_x * b_y - a_y * b_x)
    if x.is_integer() and y.is_integer():
        return int(x), int(y)
    else:
        return False


def get_cheapest_cost(solution):
    x, y = solution
    return 3 * x + y


def sum_total_tokens(claw_machines):
    total = 0
    for claw_machine in claw_machines:
        solution = find_cheapest_solution(claw_machine)
        if solution:
            total += get_cheapest_cost(solution)
    return total


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
