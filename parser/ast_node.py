class ASTNode:
    def __init__(self, node_type, value=None, children=None):
        self.type = node_type
        self.value = value
        self.children = children if children is not None else []

    def __repr__(self):
        return f"ASTNode({self.type}, {repr(self.value)}, {self.children})"

    def add_child(self, node):
        self.children.append(node)