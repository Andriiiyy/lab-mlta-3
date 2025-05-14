import os
from datatypes.edge_list import EdgeList
from datatypes.graph import create_graph

menu = (
    "Оберіть дію:\n"
    "1. Вивести вхідний граф\n"
    "2. Виконати алгоритм Дейкстри\n"
    "3. Виконати алгоритм Флойда\n"
    "4. Візуалізувати граф\n"
)

def main():
    print(menu)
    graph = create_graph()

    item: int = int(input("Оберіть елемент Меню: "))
    match item:
        case 1:
            print("Вхідний граф")
            graph.print()
        case 2:
            select_dijstra(graph)
        case 3:
            print("\nАлгоритм Флойда")
            graph.print_floyd()
        case 4:
            graph.visualize()
    go_main()


def go_main():
    input("Натисніть будь-яку кнопку")
    clear()
    main()

def select_dijstra(graph: EdgeList):
    print("\nАлгоритм Дейкстри")
    vertex: str = input("Оберіть стартову вершину: ")
    node_id: int = graph.get_node_id(vertex)
    if node_id >= 0:
        graph.print_dijstra(node_id)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    main()
