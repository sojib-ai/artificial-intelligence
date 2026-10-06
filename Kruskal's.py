class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        
    def find(self, item):
        if self.parent[item] == item:
            return item
        return self.parent[self.find(self.parent[item])]
        
    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2


def kruskals_algorithm(vertices, edges):
    mst = []
    ds = DisjointSet(vertices)
    
    # Sort edges from smallest to largest cost
    sorted_edges = sorted(edges, key=lambda item: item[2])
    
    total_cost = 0
    
    for u, v, weight in sorted_edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight
            
    return mst, total_cost


# Power grid information (city 1, city 2, grid line cost)
cities = ['Grid_A', 'Grid_B', 'Grid_C', 'Grid_D']

power_lines = [
    ('Grid_A', 'Grid_B', 10),
    ('Grid_A', 'Grid_C', 6),
    ('Grid_A', 'Grid_D', 5),
    ('Grid_B', 'Grid_D', 15),
    ('Grid_C', 'Grid_D', 4)
]


mst_grid, min_grid_cost = kruskals_algorithm(cities, power_lines)

print("Power Grid Connections:", mst_grid)
print("Minimum Total Grid Cost:", min_grid_cost)
