import heapq

def prims_algorithm(graph, start_node):
    mst = []
    visited = set([start_node])

    # Store edges in the heap as (cost, from_node, to_node)
    edges = [(cost, start_node, to)
             for to, cost in graph[start_node].items()]

    heapq.heapify(edges)

    total_cost = 0

    while edges:
        cost, frm, to = heapq.heappop(edges)

        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            total_cost += cost

            for next_node, next_cost in graph[to].items():
                if next_node not in visited:
                    heapq.heappush(
                        edges,
                        (next_cost, to, next_node)
                    )

    return mst, total_cost


# Graph representation (houses and cable costs)
housing_society = {
    'House_A': {'House_B': 4, 'House_C': 3},
    'House_B': {'House_A': 4, 'House_C': 1, 'House_D': 2},
    'House_C': {'House_A': 3, 'House_B': 1, 'House_D': 4},
    'House_D': {'House_B': 2, 'House_C': 4}
}

mst_routes, min_cable = prims_algorithm(
    housing_society,
    'House_A'
)

print("Minimum Cable Routes:", mst_routes)
print("Minimum Total Cable Cost:", min_cable)
