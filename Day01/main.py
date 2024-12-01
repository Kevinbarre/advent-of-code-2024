from collections import Counter


def part1(lines):
    first_list, second_list = create_lists(lines)
    return sum_distances(first_list, second_list)


def part2(lines):
    first_list_counter, second_list_counter = (Counter(created_list) for created_list in create_lists(lines))
    return sum_similarity_scores(first_list_counter, second_list_counter)


def split_ids(line):
    first, second = (int(number) for number in line.split())
    return first, second


def create_lists(lines):
    first_list = []
    second_list = []
    for line in lines:
        first, second = split_ids(line)
        first_list.append(first)
        second_list.append(second)
    first_list.sort()
    second_list.sort()
    return first_list, second_list


def get_distance(first, second):
    return abs(first - second)


def sum_distances(first_list, second_list):
    total = 0
    for first, second in zip(first_list, second_list):
        total += get_distance(first, second)
    return total


def get_similarity_score(first, second_list_counter):
    return second_list_counter[first] * first


def sum_similarity_scores(first_list_counter, second_list_counter):
    total = 0
    for first, count in first_list_counter.items():
        total += get_similarity_score(first, second_list_counter) * count
    return total


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
