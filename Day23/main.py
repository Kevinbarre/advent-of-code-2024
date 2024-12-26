import networkx as nx


def part1(lines):
    graph = parse_edges(lines)
    cliques = find_sets_three_computers(graph)
    t_cliques = find_cliques_with_t(cliques)
    return len(t_cliques)


def part2(lines):
    return 0


def parse_edges(lines):
    graph = nx.Graph()
    for line in lines:
        first, second = line.split('-')
        graph.add_edge(first, second)
    return graph


def find_sets_three_computers(graph):
    return set(frozenset(clique) for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3)


def _start_with_t(clique):
    for node in clique:
        if node[0] == 't':
            return True
    return False


def find_cliques_with_t(cliques):
    return set(clique for clique in cliques if _start_with_t(clique))


if __name__ == '__main__':
    with open("input.txt") as f:
        f_lines = f.read().splitlines()

    print("Part 1 : ", part1(f_lines))
    print("Part 2 : ", part2(f_lines))
