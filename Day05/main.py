def part1(lines):
    page_ordering_rules, page_updates = parse_input(lines)
    return sum_correctly_updated_pages(page_updates, page_ordering_rules)


def part2(lines):
    page_ordering_rules, page_updates = parse_input(lines)
    return sum_reordered_page_updates(page_updates, page_ordering_rules)


def parse_input(lines):
    index = lines.index("")
    raw_page_ordering_rules, raw_page_updates = lines[:index], lines[index + 1:]

    page_ordering_rules = {}
    for raw_page_ordering_rule in raw_page_ordering_rules:
        key, value = (int(elem) for elem in raw_page_ordering_rule.split('|'))
        try:
            page_ordering_rules[key].add(value)
        except KeyError:
            page_ordering_rules[key] = {value}

    page_updates = [[int(elem) for elem in raw_page_update.split(',')] for raw_page_update in raw_page_updates]

    return page_ordering_rules, page_updates


def is_correctly_placed(number, page_update, page_ordering_rules):
    # Get position of the number we're checking
    index = page_update.index(number)
    # Iterate over the remaining list on its right
    for next_number in page_update[index + 1:]:
        # Next number is not part of the ordering, no constraints on it so we ignore it
        if next_number not in page_ordering_rules:
            continue
        # If number should be after one of the remaining number, then pages are not in the right order
        if number in page_ordering_rules[next_number]:
            return False
    return True


def is_in_order(page_update, page_ordering_rules):
    for number in page_update:
        if not is_correctly_placed(number, page_update, page_ordering_rules):
            return False
    return True


def get_middle_page_number(page_update):
    return page_update[len(page_update) // 2]


def sum_correctly_updated_pages(page_updates, page_ordering_rules):
    return sum(get_middle_page_number(page_update) for page_update in page_updates if is_in_order(page_update, page_ordering_rules))


def reorder(page_update, page_ordering_rules):
    # Case when the list is empty
    if not page_update:
        return page_update
    first = page_update[0]
    if is_correctly_placed(first, page_update, page_ordering_rules):
        # First number is correctly placed, keep it here and reorder the remaining elements in the list
        return [first] + reorder(page_update[1:], page_ordering_rules)
    else:
        # First number is not correctly placed, shift it and the end, and try to reorder again
        return reorder(page_update[1:] + [first], page_ordering_rules)


def get_reordered_page_updates(page_updates, page_ordering_rules):
    reordered_page_updates = []
    for page_update in page_updates:
        if not is_in_order(page_update, page_ordering_rules):
            reordered_page_updates.append(reorder(page_update, page_ordering_rules))
    return reordered_page_updates


def sum_reordered_page_updates(page_updates, page_ordering_rules):
    return sum(get_middle_page_number(page_update) for page_update in get_reordered_page_updates(page_updates, page_ordering_rules))


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
