class UnionFind:
    def __init__(self, nodes):
        self.nodes = nodes
        self.roots = [i for i in range(nodes)]
        self.size = [1 for _ in range(nodes)]

    def union(self, p, q):
        root1, root2 = self.find(p), self.find(q)
        if root1 == root2:
            return
        
        if self.roots[root1] < self.roots[root2]:
            self.roots[root2] = self.roots[root1]
            self.size[root1] += self.size[root2]
            self.size[root2] = 0
        else:
            self.roots[root1] = self.roots[root2]
            self.size[root2] += self.size[root1]
            self.size[root1] = 0
        
        return True
            
    def find(self, r):
        root = r
        
        while root != self.roots[root]:
            root = self.roots[root]

        while r != root:
            new = r
            self.roots[r] = root
            r = new

        return root

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

class Edge:
    def __init__(self, *args) -> None:
        self.start, self.end, self.cost = args

class Graph:
    def __init__(self, nodes) -> None:
        self.graph: list[Edge] = []
        self.node: int = nodes
    
    def add_edge(self, start: int, end: int, cost: int) -> None:
        edge: Edge = Edge(start, end, cost)
        self.graph.append(edge)
    
    def kruskals_mst(self) -> int:
        uf: UnionFind = UnionFind(self.nodes)
        self.graph.sort(key=lambda x: x.cost)
        total_cost: int = 0
        for edge in self.graph:
            if uf.union(edge.start, edge.end):
                total_cost += edge.cost
        return total_cost

if __name__ == '__main__':
    graph: Graph = Graph(4)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)
    print(graph.kruskals_mst())
