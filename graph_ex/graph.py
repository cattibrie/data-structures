from queue import Queue, Element

class Graph(object):
    def __init__(self):
        self.graph = dict()

    def __nonzero__(self):
        return not self.isEmpty()

    def isEmpty(self):
        return not self.graph

    def notEmpty(self):
        return not self.isEmpty()

    def add_vertix(self, vert):
        if vert not in self.graph:
            self.graph[vert] = set()

    def has_vertix(self, vert):
        return vert in self.graph

    def add_edge(self, start_v, *neighbors):
        len_n = len(neighbors)
        # Add start vertix to the graph
        self.add_vertix(start_v)
        if not neighbors:
            return
        # Add neighbors to the start vertixes
        for neighbor in neighbors:
            self.graph[start_v].add(neighbor)
        # Add vertixes from the neighbors to the graph
        for vert in neighbors:
            self.add_vertix(vert)
            self.graph[vert].add(start_v)

    def edge_exist(self, start_v, end_v):
        if self.has_vertix(start_v) and self.has_vertix(end_v):
            return start_v in self.graph[end_v]
        return False

    def get_edges(self, vert):
        return self.graph[vert]

    def explore(self, vert, visited, dfs_order):
        dfs_order.append(vert)
        visited.add(vert)
        for neighbor in self.get_edges(vert):
            if  neighbor not in visited:
                self.explore(neighbor, visited, dfs_order)

    def find_connected_vert_dfs(self, vert):
        visited = set()
        dfs_order = []
        self.explore(vert, visited, dfs_order)
        return dfs_order

    def find_connected_vert_bfs(self, vert):
        visited = set()
        queue = Queue()
        queue.add(vert)
        bfs_order = []
        while queue.notEmpty():
            current = queue.getHeadValue()
            bfs_order.append(current)
            visited.add(current)
            for neighbor in self.get_edges(current):
                if neighbor not in visited:
                    queue.add(neighbor)
            queue.pop()
        return bfs_order
