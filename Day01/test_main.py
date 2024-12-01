from collections import Counter

import pytest

from main import part1, part2, split_ids, create_lists, get_distance, sum_distances, get_similarity_score, \
    sum_similarity_scores

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 11


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 31


def test_split_ids():
    # Given
    line = "3   4"
    # When
    first, second = split_ids(line)
    # Then
    assert first == 3
    assert second == 4


def test_create_lists():
    # Given
    lines = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ]
    # When
    first_list, second_list = create_lists(lines)
    # Then
    assert first_list == [1, 2, 3, 3, 3, 4]
    assert second_list == [3, 3, 3, 4, 5, 9]


@pytest.mark.parametrize("first, second, expected",
                         [(3, 7, 4),
                          (9, 3, 6)
                          ])
def test_get_distance(first, second, expected):
    # Given
    # When
    result = get_distance(first, second)
    # Then
    assert result == expected


def test_sum_distances():
    # Given
    first_list = [1, 2, 3, 3, 3, 4]
    second_list = [3, 3, 3, 4, 5, 9]
    # When
    result = sum_distances(first_list, second_list)
    # Then
    assert result == 11


@pytest.mark.parametrize("first, expected",
                         [(1, 0),
                          (2, 0),
                          (3, 9),
                          (4, 4)
                          ])
def test_get_similarity_score(first, expected):
    # Given
    second_list_counter = Counter([3, 3, 3, 4, 5, 9])
    # When
    result = get_similarity_score(first, second_list_counter)
    # Then
    assert result == expected


def test_sum_similarity_scores():
    # Given
    first_list_counter = Counter([1, 2, 3, 3, 3, 4])
    second_list_counter = Counter([3, 3, 3, 4, 5, 9])
    # When
    result = sum_similarity_scores(first_list_counter, second_list_counter)
    # Then
    assert result == 31
