class ASTNode:
    def __init__(self, token_type, value, children=None):
        self.token_type = token_type
        self.value = value
        self.children = children or []

    def __str__(self, level=0):
        ret = "  " * level + f"{self.token_type} {self.value}\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def __repr__(self):
        return self.__str__()