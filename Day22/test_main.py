import pytest

from main import part1, part2, mix, prune, next_step, generate, parse_initial_secret_numbers, get_buyer_sequences, build_best_prices

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 37327623


def test_part2():
    # Given
    with open("example2.txt") as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 23


def test_parse_initial_secret_numbers():
    # Given
    lines = [
        "1",
        "10",
        "100",
        "2024"
    ]
    # When
    result = parse_initial_secret_numbers(lines)
    # Then
    assert result == [1, 10, 100, 2024]


def test_mix():
    # Given
    secret_number = 42
    value = 15
    # When
    result = mix(secret_number, value)
    # Then
    assert result == 37


def test_prune():
    # Given
    secret_number = 100000000
    # When
    result = prune(secret_number)
    # Then
    assert result == 16113920


@pytest.mark.parametrize("secret_number, expected",
                         [(123, 15887950),
                          (15887950, 16495136),
                          (16495136, 527345),
                          (527345, 704524),
                          (704524, 1553684),
                          (1553684, 12683156),
                          (12683156, 11100544),
                          (11100544, 12249484),
                          (12249484, 7753432),
                          (7753432, 5908254)
                          ])
def test_next_step(secret_number, expected):
    # Given
    # When
    result = next_step(secret_number)
    # Then
    assert result == expected


@pytest.mark.parametrize("secret_number, expected",
                         [(1, 8685429),
                          (10, 4700978),
                          (100, 15273692),
                          (2024, 8667524)
                          ])
def test_generate(secret_number, expected):
    # Given
    # When
    result = generate(secret_number, 2000)
    # Then
    assert result == expected


@pytest.mark.parametrize("secret_number, expected_price",
                         [(1, 7),
                          (2, 7),
                          (2024, 9)
                          ])
def test_get_buyer_sequences_in(secret_number, expected_price):
    # Given
    # When
    result = get_buyer_sequences(secret_number)
    # Then
    assert (-2, 1, -1, 3) in result
    assert result[(-2, 1, -1, 3)] == expected_price


def test_get_buyer_sequences_not_in():
    # Given
    secret_number = 3
    # When
    result = get_buyer_sequences(secret_number)
    # Then
    assert (-2, 1, -1, 3) not in result


def test_build_best_prices():
    # Given
    secret_numbers = [1, 2, 3, 2024]
    # When
    result = build_best_prices(secret_numbers)
    # Then
    assert (-2, 1, -1, 3) in result
    assert result[(-2, 1, -1, 3)] == 23
