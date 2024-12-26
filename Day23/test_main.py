from main import part1, part2, parse_edges, find_sets_three_computers, find_cliques_with_t

filename = "example.txt"


def test_part1():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part1(lines)
    # Then
    assert result == 7


def test_part2():
    # Given
    with open(filename) as f:
        lines = f.read().splitlines()
    # When
    result = part2(lines)
    # Then
    assert result == 0


def test_parse_edges():
    # Given
    lines = [
        "kh-tc",
        "qp-kh",
        "de-cg",
        "ka-co",
        "yn-aq",
        "qp-ub",
        "cg-tb",
        "vc-aq",
        "tb-ka",
        "wh-tc",
        "yn-cg",
        "kh-ub",
        "ta-co",
        "de-co",
        "tc-td",
        "tb-wq",
        "wh-td",
        "ta-ka",
        "td-qp",
        "aq-cg",
        "wq-ub",
        "ub-vc",
        "de-ta",
        "wq-aq",
        "wq-vc",
        "wh-yn",
        "ka-de",
        "kh-ta",
        "co-tc",
        "wh-qp",
        "tb-vc",
        "td-yn"
    ]
    # When
    result = parse_edges(lines)
    # Then
    assert set(result.nodes) == {"aq", "cg", "co", "de", "ka", "kh", "qp", "ta", "tb", "tc", "td", "ub", "vc", "wh", "wq", "yn"}
    assert len(result.edges) == 32


def test_find_sets_three_computers():
    # Given
    lines = [
        "kh-tc",
        "qp-kh",
        "de-cg",
        "ka-co",
        "yn-aq",
        "qp-ub",
        "cg-tb",
        "vc-aq",
        "tb-ka",
        "wh-tc",
        "yn-cg",
        "kh-ub",
        "ta-co",
        "de-co",
        "tc-td",
        "tb-wq",
        "wh-td",
        "ta-ka",
        "td-qp",
        "aq-cg",
        "wq-ub",
        "ub-vc",
        "de-ta",
        "wq-aq",
        "wq-vc",
        "wh-yn",
        "ka-de",
        "kh-ta",
        "co-tc",
        "wh-qp",
        "tb-vc",
        "td-yn"
    ]
    graph = parse_edges(lines)
    # When
    result = find_sets_three_computers(graph)
    # Then
    assert result == {
        frozenset({"aq", "cg", "yn"}),
        frozenset({"aq", "vc", "wq"}),
        frozenset({"co", "de", "ka"}),
        frozenset({"co", "de", "ta"}),
        frozenset({"co", "ka", "ta"}),
        frozenset({"de", "ka", "ta"}),
        frozenset({"kh", "qp", "ub"}),
        frozenset({"qp", "td", "wh"}),
        frozenset({"tb", "vc", "wq"}),
        frozenset({"tc", "td", "wh"}),
        frozenset({"td", "wh", "yn"}),
        frozenset({"ub", "vc", "wq"})
    }


def test_find_cliques_with_t():
    # Given
    cliques = {
        frozenset({"aq", "cg", "yn"}),
        frozenset({"aq", "vc", "wq"}),
        frozenset({"co", "de", "ka"}),
        frozenset({"co", "de", "ta"}),
        frozenset({"co", "ka", "ta"}),
        frozenset({"de", "ka", "ta"}),
        frozenset({"kh", "qp", "ub"}),
        frozenset({"qp", "td", "wh"}),
        frozenset({"tb", "vc", "wq"}),
        frozenset({"tc", "td", "wh"}),
        frozenset({"td", "wh", "yn"}),
        frozenset({"ub", "vc", "wq"})
    }
    # When
    result = find_cliques_with_t(cliques)
    # Then
    assert result == {
        frozenset({"co", "de", "ta"}),
        frozenset({"co", "ka", "ta"}),
        frozenset({"de", "ka", "ta"}),
        frozenset({"qp", "td", "wh"}),
        frozenset({"tb", "vc", "wq"}),
        frozenset({"tc", "td", "wh"}),
        frozenset({"td", "wh", "yn"})
    }
