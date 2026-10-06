import heapq

def dijkstra(graph, start):
    # Set the distance of all nodes to infinity
    distances = {node: float('infinity') for node in graph}
    
    # Distance from the starting node to itself is 0
    distances[start] = 0
    
    # Priority queue stores (distance, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip if this is not the shortest known distance
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Update if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


# City map graph (cities and travel distance)
city_map = {
    'Dhaka': {'Chittagong': 250, 'Sylhet': 240},
    'Chittagong': {'Dhaka': 250, 'Coxs_Bazar': 150},
    'Sylhet': {'Dhaka': 240, 'Chittagong': 300},
    'Coxs_Bazar': {'Chittagong': 150}
}

shortest_distances = dijkstra(city_map, 'Dhaka')

print("Shortest distances from Dhaka:", shortest_distances)
