def part1(lines):
    towels, designs = parse_towels(lines)
    return count_possible_designs(designs, towels)


def part2(lines):
    return 0


def parse_towels(lines):
    towels = {towel for towel in lines[0].split(", ")}
    return towels, lines[2:]


def check_design(design, towels):
    if design in towels:
        return [design]
    else:
        for i in reversed(range(len(design))):
            sub_design = design[:i]
            if sub_design in towels:
                remaining = check_design(design[i:], towels)
                if remaining:
                    return [sub_design] + remaining
    return False


def count_possible_designs(designs, towels):
    return sum(1 for design in designs if check_design(design, towels))


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
