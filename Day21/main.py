import functools


def part1(lines):
    return sum(get_complexity(code, 3) for code in lines)


def part2(lines):
    return sum(get_complexity(code, 26) for code in lines)


# Taken from reddit: The best path has this priority : < first, then ^ or v , and then >
SHORTEST_PATHS_NUMERIC_KEYPAD = {
    ('A', 'A'): "A",
    ('A', '0'): "<A",
    ('A', '1'): "^<<A",
    ('A', '2'): "<^A",
    ('A', '3'): "^A",
    ('A', '4'): "^^<<A",
    ('A', '5'): "<^^A",
    ('A', '6'): "^^A",
    ('A', '7'): "^^^<<A",
    ('A', '8'): "<^^^A",
    ('A', '9'): "^^^A",
    ('0', 'A'): ">A",
    ('0', '0'): "A",
    ('0', '1'): "^<A",
    ('0', '2'): "^A",
    ('0', '3'): "^>A",
    ('0', '4'): "^^<A",
    ('0', '5'): "^^A",
    ('0', '6'): "^^>A",
    ('0', '7'): "^^^<A",
    ('0', '8'): "^^^A",
    ('0', '9'): "^^^>A",
    ('1', 'A'): ">>vA",
    ('1', '0'): ">vA",
    ('1', '1'): "A",
    ('1', '2'): ">A",
    ('1', '3'): ">>A",
    ('1', '4'): "^A",
    ('1', '5'): "^>A",
    ('1', '6'): "^>>A",
    ('1', '7'): "^^A",
    ('1', '8'): "^^>A",
    ('1', '9'): "^^>>A",
    ('2', 'A'): "v>A",
    ('2', '0'): "vA",
    ('2', '1'): "<A",
    ('2', '2'): "A",
    ('2', '3'): ">A",
    ('2', '4'): "<^A",
    ('2', '5'): "^A",
    ('2', '6'): "^>A",
    ('2', '7'): "<^^A",
    ('2', '8'): "^^A",
    ('2', '9'): "^^>A",
    ('3', 'A'): "vA",
    ('3', '0'): "<vA",
    ('3', '1'): "<<A",
    ('3', '2'): "<A",
    ('3', '3'): "A",
    ('3', '4'): "<<^A",
    ('3', '5'): "<^A",
    ('3', '6'): "^A",
    ('3', '7'): "<<^^A",
    ('3', '8'): "<^^A",
    ('3', '9'): "^^A",
    ('4', 'A'): ">>vvA",
    ('4', '0'): ">vvA",
    ('4', '1'): "vA",
    ('4', '2'): "v>A",
    ('4', '3'): "v>>A",
    ('4', '4'): "A",
    ('4', '5'): ">A",
    ('4', '6'): ">>A",
    ('4', '7'): "^A",
    ('4', '8'): "^>A",
    ('4', '9'): "^>>A",
    ('5', 'A'): "vv>A",
    ('5', '0'): "vvA",
    ('5', '1'): "<vA",
    ('5', '2'): "vA",
    ('5', '3'): "v>A",
    ('5', '4'): "<A",
    ('5', '5'): "A",
    ('5', '6'): ">A",
    ('5', '7'): "<^A",
    ('5', '8'): "^A",
    ('5', '9'): "^>A",
    ('6', 'A'): "vvA",
    ('6', '0'): "<vvA",
    ('6', '1'): "<<vA",
    ('6', '2'): "<vA",
    ('6', '3'): "vA",
    ('6', '4'): "<<A",
    ('6', '5'): "<A",
    ('6', '6'): "A",
    ('6', '7'): "<<^A",
    ('6', '8'): "<^A",
    ('6', '9'): "^A",
    ('7', 'A'): ">>vvvA",
    ('7', '0'): ">vvvA",
    ('7', '1'): "vvA",
    ('7', '2'): "vv>A",
    ('7', '3'): "vv>>A",
    ('7', '4'): "vA",
    ('7', '5'): "v>A",
    ('7', '6'): "v>>A",
    ('7', '7'): "A",
    ('7', '8'): ">A",
    ('7', '9'): ">>A",
    ('8', 'A'): "vvv>A",
    ('8', '0'): "vvvA",
    ('8', '1'): "<vvA",
    ('8', '2'): "vvA",
    ('8', '3'): "vv>A",
    ('8', '4'): "<vA",
    ('8', '5'): "vA",
    ('8', '6'): "v>A",
    ('8', '7'): "<A",
    ('8', '8'): "A",
    ('8', '9'): ">A",
    ('9', 'A'): "vvvA",
    ('9', '0'): "<vvvA",
    ('9', '1'): "<<vvA",
    ('9', '2'): "<vvA",
    ('9', '3'): "vvA",
    ('9', '4'): "<<vA",
    ('9', '5'): "<vA",
    ('9', '6'): "vA",
    ('9', '7'): "<<A",
    ('9', '8'): "<A",
    ('9', '9'): "A",
}

SHORTEST_PATHS_DIRECTIONAL_KEYPAD = {
    ('A', 'A'): "A",
    ('A', '^'): "<A",
    ('A', '>'): "vA",
    ('A', 'v'): "<vA",
    ('A', '<'): "v<<A",
    ('^', 'A'): ">A",
    ('^', '^'): "A",
    ('^', '>'): "v>A",
    ('^', 'v'): "vA",
    ('^', '<'): "v<A",
    ('>', 'A'): "^A",
    ('>', '^'): "<^A",
    ('>', '>'): "A",
    ('>', 'v'): "<A",
    ('>', '<'): "<<A",
    ('v', 'A'): "^>A",
    ('v', '^'): "^A",
    ('v', '>'): ">A",
    ('v', 'v'): "A",
    ('v', '<'): "<A",
    ('<', 'A'): ">>^A",
    ('<', '^'): ">^A",
    ('<', '>'): ">>A",
    ('<', 'v'): ">A",
    ('<', '<'): "A",
}


@functools.cache
def _get_shortest_sequence_directional(sequence, depth):
    if depth == 0:
        return len(sequence)
    else:
        total = 0
        for start, end in zip('A' + sequence, sequence):
            sub_sequence = SHORTEST_PATHS_DIRECTIONAL_KEYPAD[(start, end)]
            total += _get_shortest_sequence_directional(sub_sequence, depth - 1)
        return total


def get_shortest_sequence_length(code, depth):
    total = 0
    for start, end in zip('A' + code, code):
        sequence = SHORTEST_PATHS_NUMERIC_KEYPAD[(start, end)]
        total += _get_shortest_sequence_directional(sequence, depth - 1)
    return total


def get_complexity(code, depth):
    shortest_sequence_length = get_shortest_sequence_length(code, depth)
    numeric_part = int(code[:-1])
    return numeric_part * shortest_sequence_length


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))