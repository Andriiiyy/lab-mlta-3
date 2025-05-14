class Node:
    def __init__(self, data: str):
        self.data: str = data

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.data == other.data

    def __hash__(self):
        return hash(self.data)
