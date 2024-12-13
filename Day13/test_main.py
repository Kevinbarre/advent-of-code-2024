import pytest

from main import part1, part2, parse_input, split_input_line, find_cheapest_solution, get_cheapest_cost, sum_total_tokens, recalibrate_claw_machine

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 480


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 875318608908


@pytest.mark.parametrize("raw_line, expected",
                         [("Button A: X+94, Y+34", (94, 34)),
                          ("Button B: X+22, Y+67", (22, 67)),
                          ("Prize: X=8400, Y=5400", (8400, 5400)),
                          ])
def test_split_input(raw_line, expected):
    # Given
    # When
    result = split_input_line(raw_line)
    # Then
    assert result == expected


def test_parse_input():
    # Given
    lines = [
        "Button A: X+94, Y+34",
        "Button B: X+22, Y+67",
        "Prize: X=8400, Y=5400",
        "",
        "Button A: X+26, Y+66",
        "Button B: X+67, Y+21",
        "Prize: X=12748, Y=12176",
        "",
        "Button A: X+17, Y+86",
        "Button B: X+84, Y+37",
        "Prize: X=7870, Y=6450",
        "",
        "Button A: X+69, Y+23",
        "Button B: X+27, Y+71",
        "Prize: X=18641, Y=10279",
    ]
    # When
    result = parse_input(lines)
    # Then
    assert result == [
        ((94, 34), (22, 67), (8400, 5400)),
        ((26, 66), (67, 21), (12748, 12176)),
        ((17, 86), (84, 37), (7870, 6450)),
        ((69, 23), (27, 71), (18641, 10279))
    ]


@pytest.mark.parametrize("claw_machine, expected",
                         [(((94, 34), (22, 67), (8400, 5400)), (80, 40)),
                          (((26, 66), (67, 21), (12748, 12176)), False),
                          (((17, 86), (84, 37), (7870, 6450)), (38, 86)),
                          (((69, 23), (27, 71), (18641, 10279)), False)
                          ])
def test_find_cheapest_solution(claw_machine, expected):
    # Given
    # When
    result = find_cheapest_solution(claw_machine)
    # Then
    assert result == expected


@pytest.mark.parametrize("solution, expected",
                         [((80, 40), 280),
                          ((38, 86), 200)
                          ])
def test_get_cheapest_cost(solution, expected):
    # Given
    # When
    result = get_cheapest_cost(solution)
    # Then
    assert result == expected


def test_sum_total_tokens():
    # Given
    claw_machines = [
        ((94, 34), (22, 67), (8400, 5400)),
        ((26, 66), (67, 21), (12748, 12176)),
        ((17, 86), (84, 37), (7870, 6450)),
        ((69, 23), (27, 71), (18641, 10279))
    ]
    # When
    result = sum_total_tokens(claw_machines)
    # Then
    assert result == 480


def test_recalibrate_claw_machine():
    # Given
    claw_machine = ((94, 34), (22, 67), (8400, 5400))
    # When
    result = recalibrate_claw_machine(claw_machine)
    # Then
    assert result == ((94, 34), (22, 67), (10000000008400, 10000000005400))


@pytest.mark.parametrize("claw_machine, expected",
                         [(((94, 34), (22, 67), (10000000008400, 10000000005400)), False),
                          (((26, 66), (67, 21), (10000000012748, 10000000012176)), (118679050709, 103199174542)),
                          (((17, 86), (84, 37), (10000000007870, 10000000006450)), False),
                          (((69, 23), (27, 71), (10000000018641, 10000000010279)), (102851800151, 107526881786))
                          ])
def test_find_cheapest_solution_recalibrated(claw_machine, expected):
    # Given
    # When
    result = find_cheapest_solution(claw_machine)
    # Then
    assert result == expected
