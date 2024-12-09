def part1(lines):
    disk_map = parse_input(lines)
    disk_map = reorganize(disk_map)
    return calculate_checksum(disk_map)


def part2(lines):
    disk_map = parse_input(lines)
    disk_map = reorganize_whole_files(disk_map)
    return calculate_checksum(disk_map)


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
            # Reached an empty space
            continue
        checksum += i * int(file_id)
    return checksum


def search_next_empty_space(disk_map, file_size, j):
    i = 0
    # Search for next empty space
    while i < len(disk_map) + j:
        if disk_map[i] != '.':
            i += 1
            continue
        # Empty space found, count number of consecutive spaces
        k = i
        while k < len(disk_map) and disk_map[k] == '.':
            k += 1
        if k - i >= file_size:
            # Empty space large enough found, return index of first block
            return i
        else:  # Restarting from k current value
            i = k
    # Outside the disk_map
    return False


def reorganize_whole_files(disk_map):
    j = -1
    while True:
        # Search for next occupied space
        while j >= -len(disk_map) and disk_map[j] == '.':
            j -= 1
        if j < -len(disk_map):
            # Outside the disk_map, nothing left to do
            return disk_map
        # Occupied space found, check file size
        file_id = disk_map[j]
        k = j
        while k >= -len(disk_map) and disk_map[k] == file_id:
            k -= 1
        if k < -len(disk_map):
            # Outside of disk_map, nothing left to do
            return disk_map
        file_size = j - k
        # Search for next empty space starting from beginning that could fit the file, but not after j
        i = search_next_empty_space(disk_map, file_size, j)
        if i:
            # Swap blocks
            for m in range(file_size):
                # Swap blocks
                disk_map[i + m] = disk_map[j - m]
                disk_map[j - m] = '.'
            # Restarting from k
            j = k
        else:
            # No space large enough found, skipping current file by restarting from k
            j = k


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
