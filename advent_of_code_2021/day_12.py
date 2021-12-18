import os
from typing import Dict, List


def get_graph(connections: List[str]) -> Dict[str, List[str]]:
    graph = {}

    for connection in connections:
        a, b = connection.split("-")
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]

    return graph


def dijkstra(
    current_node: str,
    graph: Dict[str, List[str]],
    visited: List[str],
    paths: List[List[str]],
    is_extra_small: bool,
):
    visited.append(current_node)

    if current_node == "end":
        paths.append(visited)

    for neighbouring_node in graph[current_node]:
        extra = None
        if is_extra_small:
            extra = (
                neighbouring_node not in ["start", "end"]
                and neighbouring_node.islower()
                and not any(
                    [
                        visited_node.islower()
                        and visited.count(visited_node) > 1
                        for visited_node in visited
                    ]
                )
            )

        if neighbouring_node not in visited or (
            neighbouring_node in visited
            and (neighbouring_node.isupper() or (is_extra_small and extra))
        ):
            dijkstra(
                neighbouring_node, graph, visited.copy(), paths, is_extra_small
            )

    return paths


def solve_first(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]
    graph = get_graph(data)
    paths = dijkstra("start", graph, [], [], False)

    return len(paths)


def solve_second(file_name: str) -> int:
    with open(
        f"{os.path.dirname(os.path.realpath(__file__))}/{file_name}", "r"
    ) as f:
        data = [x.strip() for x in f.readlines()]
    graph = get_graph(data)
    paths = dijkstra("start", graph, [], [], True)

    return len(paths)
