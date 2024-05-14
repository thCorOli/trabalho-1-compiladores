class ASTNode:
    def __init__(self, node_type, value=None, children=None):
        self.type = node_type
        self.value = value
        self.children = children if children is not None else []

    def __repr__(self):
        return f"Arvore Sintatica:\n Nó ({self.type},{repr(self.value)})\n Filhos -> {self.children}\n"
    
    def add_child(self, node):
        self.children.append(node)