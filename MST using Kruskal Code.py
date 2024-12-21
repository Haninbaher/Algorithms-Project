class DisjointSet:
    def _init_(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Find with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Union by rank."""
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(edges, n):
    """Finds the MST using Kruskal's algorithm."""
    # Sort edges by weight
    edges.sort(key=lambda edge: edge[2])
    ds = DisjointSet(n)
    mst = []
    mst_weight = 0

    for u, v, w in edges:
        # If u and v belong to different sets, add the edge to MST
        if ds.find(u) != ds.find(v):
            mst.append((u, v, w))
            mst_weight += w
            ds.union(u, v)

    return mst, mst_weight

# Example Usage
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
n = 4  # Number of vertices

mst, total_weight = kruskal(edges, n)
print("Edges in MST:", mst)
print("Total weight of MST:", total_weight)