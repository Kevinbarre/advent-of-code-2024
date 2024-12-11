from collections import defaultdict, Counter


def part1(lines):
    arrangement = parse_arrangement(lines)
    arrangement = multiple_steps(arrangement, 25)
    return count_stones(arrangement)


def part2(lines):
    arrangement = parse_arrangement(lines)
    arrangement = multiple_steps(arrangement, 75)
    return count_stones(arrangement)


def parse_arrangement(lines):
    line = lines[0]
    return Counter(int(number) for number in line.split())


def blink(stone):
    stone_as_string = str(stone)
    if stone == 0:
        return [1]
    elif len(stone_as_string) % 2 == 0:
        left, right = int(stone_as_string[:len(stone_as_string) // 2]), int(stone_as_string[len(stone_as_string) // 2:])
        return [left, right]
    else:
        return [stone * 2024]


def step(arrangement):
    next_arrangement = defaultdict(lambda: 0)
    for stone, count in arrangement.items():
        new_stones = blink(stone)
        for new_stone in new_stones:
            next_arrangement[new_stone] += count
    return next_arrangement


def multiple_steps(arrangement, number_steps):
    for _ in range(number_steps):
        arrangement = step(arrangement)
    return arrangement


def count_stones(arrangement):
    return sum(value for value in arrangement.values())


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
