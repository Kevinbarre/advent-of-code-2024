from collections import defaultdict


def part1(lines):
    secret_numbers = parse_initial_secret_numbers(lines)
    return sum(generate(secret_number, 2000) for secret_number in secret_numbers)


def part2(lines):
    secret_numbers = parse_initial_secret_numbers(lines)
    best_prices = build_best_prices(secret_numbers)
    return max(best_prices.values())


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


def get_buyer_sequences(secret_number):
    # Execute the 4 first changes
    buyer_sequences = {}
    first_value = secret_number % 10
    secret_number = next_step(secret_number)
    second_value = secret_number % 10
    first = second_value - first_value
    secret_number = next_step(secret_number)
    third_value = secret_number % 10
    second = third_value - second_value
    secret_number = next_step(secret_number)
    previous_value = secret_number % 10
    third = previous_value - third_value
    secret_number = next_step(secret_number)
    new_value = secret_number % 10
    fourth = new_value - previous_value
    buyer_sequences[(first, second, third, fourth)] = new_value
    # Iterate for the remaining ones
    for _ in range(1996):
        secret_number = next_step(secret_number)
        previous_value = new_value
        new_value = secret_number % 10
        first = second
        second = third
        third = fourth
        fourth = new_value - previous_value
        key = (first, second, third, fourth)
        if key not in buyer_sequences:
            buyer_sequences[key] = new_value
    return buyer_sequences


def build_best_prices(secret_numbers):
    best_prices = defaultdict(lambda: 0)
    for secret_number in secret_numbers:
        buyer_sequences = get_buyer_sequences(secret_number)
        for sequence, price in buyer_sequences.items():
            best_prices[sequence] += price
    return best_prices


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
