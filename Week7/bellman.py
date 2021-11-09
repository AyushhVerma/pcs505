class Edge:
    def __init__(self, *args):
        self._from, self.to, self.cost = args

class Graph:
    def __init__(self, nodes):
        self.graph = []
        self.nodes = nodes

    def add_edge(self, *args):
        edge = Edge(*args)
        self.graph.append(edge)

    def get_graph(self):
        return self.graph

    def bellman_ford(self, start):
        dist = [float('inf')] * self.nodes
        dist[start] = 0
        
        for _ in range(self.nodes):
            for edge in self.graph:
                if dist[edge.to] > dist[edge._from] + edge.cost:
                    dist[edge.to] = dist[edge._from] + edge.cost

        for _ in range(self.nodes):
            for edge in self.graph:
                if dist[edge.to] > dist[edge._from] + edge.cost:
                    dist[edge.to] = float('inf')
        
        return dist
