def part1(lines):
    secret_numbers = parse_initial_secret_numbers(lines)
    return sum(generate(secret_number, 2000) for secret_number in secret_numbers)


def part2(lines):
    return 0


def parse_initial_secret_numbers(lines):
    return [int(line) for line in lines]


def mix(secret_number, value):
    return secret_number ^ value


def prune(secret_number):
    return secret_number % 16777216


def next_step(secret_number):
    temp = secret_number * 64
    secret_number = mix(secret_number, temp)
    secret_number = prune(secret_number)
    temp = secret_number // 32
    secret_number = mix(secret_number, temp)
    secret_number = prune(secret_number)
    temp = secret_number * 2048
    secret_number = mix(secret_number, temp)
    secret_number = prune(secret_number)
    return secret_number


def generate(secret_number, iterations):
    for _ in range(iterations):
        secret_number = next_step(secret_number)
    return secret_number


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
