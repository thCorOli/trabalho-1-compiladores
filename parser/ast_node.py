class ASTNode:
    def __init__(self, token_type, value, children=None):
        self.token_type = token_type
        self.value = value
        self.children = children or []

    def __str__(self):
        ret = ""
        stack = [(self, 0)]

        while stack:
            node, level = stack.pop()
            if node is None:
                continue
            ret += "     " * level + f"{node.token_type} {node.value}\n"
            for child in reversed(node.children):
                stack.append((child, level + 1))

        return ret
    
    def __repr__(self):
        return self.__str__()
