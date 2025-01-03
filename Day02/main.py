def part1(lines):
    reports = read_reports(lines)
    return count_safe_reports(reports)


def part2(lines):
    reports = read_reports(lines)
    return count_safe_reports_with_dampener(reports)


def read_reports(lines):
    return [[int(number) for number in line.split()] for line in lines]


def is_safe(report):
    ascending = report[1] - report[0] > 0
    if ascending:
        return all(0 < report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    else:  # descending
        return all(0 < report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))


def count_safe_reports(reports):
    return sum(1 for report in reports if is_safe(report))


def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        new_report = [level for index, level in enumerate(report) if index != i]
        if is_safe(new_report):
            return True
    return False


def count_safe_reports_with_dampener(reports):
    return sum(1 for report in reports if is_safe_with_dampener(report))


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
