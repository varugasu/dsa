from dijkstra import dijkstra


def test_dijkstra():
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"C": 3, "D": 2, "E": 3},
        "C": {"B": 1, "D": 4, "E": 5},
        "D": {},
        "E": {},
    }
    start_node = "A"

    assert dijkstra(graph, start_node) == {"A": 0, "B": 3, "C": 2, "D": 5, "E": 6}
