def part1(lines):
    disk_map = parse_input(lines)
    disk_map = reorganize(disk_map)
    return calculate_checksum(disk_map)


def part2(lines):
    return 0


def parse_input(lines):
    line = lines[0]
    disk_map = []
    file_id = 0
    for i, digit in enumerate(line):
        if i % 2 == 0:
            # File
            disk_map.extend(str(file_id) for _ in range(int(digit)))
            file_id += 1
        else:
            # Free space
            disk_map.extend('.' for _ in range(int(digit)))
    return disk_map


def reorganize(disk_map):
    i = 0
    j = -1
    while True:
        # Search for next empty space
        while i < len(disk_map) and disk_map[i] != '.':
            i += 1
        # Search for next occupied space
        while j >= -len(disk_map) and disk_map[j] == '.':
            j -= 1
        if i >= len(disk_map) or j < -len(disk_map) or i > len(disk_map) + j:
            # Outside the disk_map, nothing left to do
            return disk_map
        else:
            # Swap blocks
            disk_map[i] = disk_map[j]
            disk_map[j] = '.'


def calculate_checksum(disk_map):
    checksum = 0
    for i, file_id in enumerate(disk_map):
        if file_id == '.':
            # Reached the empty spaces
            break
        checksum += i * int(file_id)
    return checksum


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
