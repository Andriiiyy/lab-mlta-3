from pprint import pprint

from datatypes.node import Node
from datatypes.edge_list import EdgeList

def create_graph():
    graph = EdgeList("directed")
    nodes = ["A", "B", "C", "D", "E", "F"]
#             0    1    2    3    4    5
    for node in nodes:
        graph.add_node(Node(node))

    graph.add_edge(0, 1, 3)
    graph.add_edge(0, 2, 6)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 5, 5)
    graph.add_edge(3, 5, 4)
    graph.add_edge(5, 4, 7)

    return graph


def main():
    graph = create_graph()
    graph.print_floyd()

if __name__ == '__main__':
    main()
