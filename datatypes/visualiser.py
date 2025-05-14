import networkx as nx
from datatypes.node import Node
import matplotlib.pyplot as plt
import imageio

class Visualiser:
    def __init__(self, node_list: list[Node], adj_matrix: list[list[int]], graph_type: str):
        self.node_list = [node.data for node in node_list]
        self.adj_matrix = adj_matrix
        self.graph_type = graph_type
        self.graph = nx.Graph()
        self.images: list[str] = []

    def create_graph(self) -> None:
        if self.graph_type == "directed":
            self.graph = nx.DiGraph()
        elif self.graph_type == "undirected":
            self.graph = nx.Graph()

    def add_nodes(self) -> None:
        self.graph.add_nodes_from(self.node_list)
        mapping = {i: node for i, node in enumerate(self.node_list)}
        self.graph = nx.relabel_nodes(self.graph, mapping)

    def add_edges(self) -> None:
        for i, row in enumerate(self.adj_matrix):
            for j, element in enumerate(row):
                if element == 1:
                    self.graph.add_edge(self.node_list[i], self.node_list[j])

    def create_figure(self, order: list[int], step) -> None:
        self.create_graph()
        self.add_nodes()
        self.add_edges()
        color_map = []
        for node in self.graph:
            if self.node_list.index(node) in order and self.node_list.index(node) == 0:
                color_map.append('lime')
                continue
            if self.node_list.index(node) in order:
                color_map.append('lightblue')
            else:
                color_map.append('grey')
        plt.figure(figsize=(6, 5))
        nx.draw(self.graph, pos=nx.shell_layout(self.graph), node_color=color_map, with_labels=True, node_size=700, font_size=10, edge_color='black')
        image = f"./media/step_{step}.png"
        plt.savefig(image)
        self.images.append(image)
        plt.close()

    def create_gif(self, gif_name: str) -> None:
        with imageio.get_writer(f"./media/{gif_name}", mode='I', fps=1) as writer:
            for image in self.images:
                writer.append_data(imageio.imread(image))
