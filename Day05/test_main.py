import pytest

from main import part1, part2, parse_input, is_correctly_placed, is_in_order, get_middle_page_number, sum_correctly_updated_pages

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 143


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 0


def test_parse_input():
    # Given
    lines = [
        "47 | 53",
        "97 | 13",
        "97 | 61",
        "97 | 47",
        "75 | 29",
        "61 | 13",
        "75 | 53",
        "29 | 13",
        "97 | 29",
        "53 | 29",
        "61 | 53",
        "97 | 53",
        "61 | 29",
        "47 | 13",
        "75 | 47",
        "97 | 75",
        "47 | 61",
        "75 | 61",
        "47 | 29",
        "75 | 13",
        "53 | 13",
        "",
        "75, 47, 61, 53, 29",
        "97, 61, 53, 29, 13",
        "75, 29, 13",
        "75, 97, 47, 61, 53",
        "61, 13, 29",
        "97, 13, 75, 29, 47"
    ]
    # When
    page_ordering_rules, page_updates = parse_input(lines)
    # Then
    assert page_ordering_rules == {
        47: {53, 13, 61, 29},
        97: {13, 61, 47, 29, 53, 75},
        75: {29, 53, 47, 61, 13},
        61: {13, 53, 29},
        29: {13},
        53: {29, 13},
    }
    assert page_updates == [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47]
    ]


@pytest.mark.parametrize("number, expected",
                         [(1, True),
                          (2, False)
                          ])
def test_is_correctly_placed(number, expected):
    # Given
    page_ordering_rules = {
        1: {2, 3},
        3: {2}
    }
    page_update = [1, 2, 3]
    # When
    result = is_correctly_placed(number, page_update, page_ordering_rules)
    # Then
    assert result == expected


@pytest.mark.parametrize("page_update, expected",
                         [([75, 47, 61, 53, 29], True),
                          ([97, 61, 53, 29, 13], True),
                          ([75, 29, 13], True),
                          ([75, 97, 47, 61, 53], False),
                          ([61, 13, 29], False),
                          ([97, 13, 75, 29, 47], False)
                          ])
def test_is_in_order(page_update, expected):
    # Given
    page_ordering_rules = {
        47: {53, 13, 61, 29},
        97: {13, 61, 47, 29, 53, 75},
        75: {29, 53, 47, 61, 13},
        61: {13, 53, 29},
        29: {13},
        53: {29, 13},
    }
    # When
    result = is_in_order(page_update, page_ordering_rules)
    # Then
    assert result == expected


@pytest.mark.parametrize("page_update, expected",
                         [([75, 47, 61, 53, 29], 61),
                          ([97, 61, 53, 29, 13], 53),
                          ([75, 29, 13], 29),
                          ])
def test_get_middle_page_number(page_update, expected):
    # Given
    # When
    result = get_middle_page_number(page_update)
    # Then
    assert result == expected


def test_sum_correctly_updated_pages():
    # Given
    page_ordering_rules = {
        47: {53, 13, 61, 29},
        97: {13, 61, 47, 29, 53, 75},
        75: {29, 53, 47, 61, 13},
        61: {13, 53, 29},
        29: {13},
        53: {29, 13},
    }
    page_updates = [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47]
    ]
    # When
    result = sum_correctly_updated_pages(page_updates, page_ordering_rules)
    # Then
    assert result == 143
