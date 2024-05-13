from parser.ast_node import ASTNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        ast = []
        while self.current < len(self.tokens):
            token = self.tokens[self.current]
            ast.append(self.parse_token(token))
            self.current += 1
        return ast

    def parse_token(self, token):
        if token[0] == 'NUMBER':
            return ASTNode('Number', token[1])
        elif token[0] == 'IDENTIFIER':
            return ASTNode('Identifier', token[1])
        elif token[0] in ['PLUS', 'MINUS', 'TIMES', 'DIVIDE','EQUAL']:
            return ASTNode('Operator', token[1])
        else:
            raise ValueError("Unexpected token type")
    