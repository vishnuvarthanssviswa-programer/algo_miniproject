import heapq

graph = {
    'A': [('B',4), ('C',2)],
    'B': [('A',4), ('C',1), ('D',5)],
    'C': [('A',2), ('B',1), ('D',8)],
    'D': [('B',5), ('C',8)]
}

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist

print(dijkstra(graph, 'A'))
