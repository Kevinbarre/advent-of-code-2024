import math


def part1(lines, width, height):
    robots = parse_robots(lines)
    positions = move_robots(robots, 100, width, height)
    number_robots = count_quadrants(positions, width, height)
    return safety_factor(number_robots)


def part2(lines):
    return 0


class Robot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def position_at(self, time, width, height):
        return (self.px + time * self.vx) % width, (self.py + time * self.vy) % height

    def __eq__(self, other):
        return other and self.px == other.px and self.py == other.py and self.vx == other.vx and self.vy == other.vy

    def __repr__(self):
        return "Robot(px={}, py={}, vx={}, vy={})".format(self.px, self.py, self.vx, self.vy)


def parse_robots(lines):
    robots = []
    for line in lines:
        raw_p, raw_v = line.split()
        raw_px, raw_py = raw_p.split(',')
        raw_vx, raw_vy = raw_v.split(',')
        robots.append(Robot(int(raw_px[2:]), int(raw_py), int(raw_vx[2:]), int(raw_vy)))
    return robots


def move_robots(robots, time, width, height):
    return [robot.position_at(time, width, height) for robot in robots]


def count_quadrants(positions, width, height):
    top_left = 0
    top_right = 0
    bottom_left = 0
    bottom_right = 0
    half_width = width // 2
    half_height = height // 2
    for x, y in positions:
        if x < half_width and y < half_height:
            top_left += 1
        elif x > half_width and y < half_height:
            top_right += 1
        elif x < half_width and y > half_height:
            bottom_left += 1
        elif x > half_width and y > half_height:
            bottom_right += 1
    return top_left, top_right, bottom_left, bottom_right


def safety_factor(number_robots):
    return math.prod(number_robots)


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()
    WIDTH = 101
    HEIGHT = 103

    print("Part 1 : ", part1(f_lines, WIDTH, HEIGHT))
    print("Part 2 : ", part2(f_lines))
