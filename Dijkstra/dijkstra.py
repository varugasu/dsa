import heapq


def dijkstra(graph: dict[str, dict[str, int]], start: str) -> dict[str, float]:
    pq = []
    heapq.heappush(pq, (0, start))
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
