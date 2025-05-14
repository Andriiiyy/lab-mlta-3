import heapq
from math import inf
import networkx as nx
from colorama import Fore
from matplotlib import pyplot as plt
from networkx import DiGraph

from datatypes.node import Node


class EdgeList:
    def __init__(self, list_type: str) -> None:
        self.edge_list: list[tuple[int, int, int]] = []
        self.node_list: list[Node] = []
        allowed_types: list[str] = ["directed", "undirected"]
        if not list_type in allowed_types:
            raise TypeError("Invalid matrix type")
        self.list_type: str = list_type

    def add_node(self, node: Node) -> None:
        self.node_list.append(node)

    def get_node(self, index: int) -> str:
        return self.node_list[index].data

    def check_edge(self, src: int, dest: int) -> int:
        for index, edge in enumerate(self.edge_list):
            if edge == [src, dest]:
                return index
        return -1

    def get_node_id(self, name: str) -> int:
        try:
            return self.node_list.index(Node(name))
        except ValueError:
            return -1

    def add_edge(self, src: int, dest: int, weight: int = 0) -> None:
        if not (0 <= src < len(self.node_list)) or not (0 <= dest < len(self.node_list)):
            raise IndexError("Index is out of bounds")
        self.edge_list.append((src, dest, weight))
        if self.list_type == "undirected":
            self.edge_list.append((dest, src, weight))

    def del_edge(self, src: int, dest: int):
        index: int = self.check_edge(src, dest)
        if index != -1:
            self.edge_list.pop(index)

    def print(self) -> None:
        for edge in self.edge_list:
            print(f"{self.node_list[edge[0]].data} -> {self.node_list[edge[1]].data}, вага {edge[2]}")

    def dijstra(self, src: int) -> dict[int, int]:
        adj: dict[int, list] = self.to_adj_list()
        shortest: dict[int, int] = {}
        min_heap = [[0, src]]

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(min_heap, [w1 + w2, n2])

        for i in range(len(self.node_list)):
            if i not in shortest:
                shortest[i] = -1
        return shortest

    def print_dijstra(self, src: int):
        dijstra: dict[int, int] = self.dijstra(src)
        for key, value in dijstra.items():
            print(f"від {self.get_node(src)} до {self.get_node(key)} – найменший шлях {value}")

    def floyd(self) -> list[list[int]]:
        v: int = len(self.node_list)
        distances: list[list[int]] = [[0 if i == j else inf for j in range(v)] for i in range(v)]

        for edge in self.edge_list:
            src, dest, weight = edge
            distances[src][dest] = weight

        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]

        return distances

    def print_floyd(self):
        print(end="\t")
        for node in self.node_list:
            print(node.data, end="\t")
        print()
        distances: list[list[int]] = self.floyd()
        for i, row in enumerate(distances):
            print(f"{Fore.WHITE}{self.node_list[i].data}", end="\t")
            for element in row:
                if element is inf:
                    print(f"{Fore.RED}X", end="\t")
                else:
                    print(f"{Fore.WHITE}{element}", end="\t")
            print()

    def to_adj_list(self) -> dict[int, list]:
        adj: dict[int, list] = {number: [] for number in range(len(self.node_list))}
        for src, dest, weight in self.edge_list:
            adj[src].append((dest, weight))
        return adj

    def visualize(self):
        nx_graph: DiGraph = nx.DiGraph()

        for edge in self.edge_list:
            src, dest, weight = edge
            nx_graph.add_edge(self.node_list[src].data, self.node_list[dest].data, weight=weight)

        pos = nx.arf_layout(nx_graph, seed=69)
        edges = [(u, v) for (u, v, d) in nx_graph.edges(data=True)]

        nx.draw_networkx_labels(nx_graph, pos, font_family="sans-serif")

        nx.draw_networkx_edges(nx_graph, pos, edgelist=edges)
        edge_labels = nx.get_edge_attributes(nx_graph, "weight")
        nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels)

        ax = plt.gca()
        plt.axis("off")
        plt.show()

