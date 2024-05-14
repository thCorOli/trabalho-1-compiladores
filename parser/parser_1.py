from parser.ast_node import ASTNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        return self.expression()

    def eat(self, token_type):
        if self.position < len(self.tokens) and self.tokens[self.position][0] == token_type:
            token = self.tokens[self.position]
            self.position += 1
            return token
        raise Exception(f"Expected token {token_type} but found {self.tokens[self.position][0]}")

    def expression(self):
        if self.lookahead('FLOAT') or self.lookahead('INT'):
            type_token = self.eat(self.tokens[self.position][0])  # Handle type declarations
            identifier_token = self.eat('IDENTIFIER')
            self.eat('EQUAL')
            expr_node = self.expr()
            return ASTNode('declaration', type_token[1], [ASTNode('identifier', identifier_token[1]), expr_node])
        return self.expr()

    def lookahead(self, token_type):
        return self.position < len(self.tokens) and self.tokens[self.position][0] == token_type

    def expr(self):
        node = self.term()
        while self.position < len(self.tokens) and self.tokens[self.position][0] in ('PLUS', 'MINUS'):
            op = self.eat(self.tokens[self.position][0])
            right = self.term()
            node = ASTNode('op', op[1], [node, right])
        return node

    def term(self):
        node = self.factor()
        while self.position < len(self.tokens) and self.tokens[self.position][0] in ('MULTIPLY', 'DIVIDE'):
            op = self.eat(self.tokens[self.position][0])
            right = self.factor()
            node = ASTNode('op', op[1], [node, right])
        return node

    def factor(self):
        if self.lookahead('NUMBER'):
            return ASTNode('number', self.eat('NUMBER')[1])
        elif self.lookahead('IDENTIFIER'):
            if self.lookahead_next('LPAREN'):
                return self.function_call()
            if self.lookahead_next('EQUAL'):
                return self.assignment()
            return ASTNode('identifier', self.eat('IDENTIFIER')[1])
        elif self.lookahead('LPAREN'):
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node
        else:
            raise Exception(f"Unexpected token: {self.tokens[self.position]}")

    def lookahead_next(self, token_type):
        return self.position + 1 < len(self.tokens) and self.tokens[self.position + 1][0] == token_type

    def function_call(self):
        ident = self.eat('IDENTIFIER')
        self.eat('LPAREN')
        args = []
        if not self.lookahead('RPAREN'):
            args.append(self.expr())
            while self.lookahead('COMMA'):
                self.eat('COMMA')
                args.append(self.expr())
        self.eat('RPAREN')
        return ASTNode('function_call', ident[1], args)

    def assignment(self):
        ident = self.eat('IDENTIFIER')
        self.eat('EQUAL')
        expr = self.expr()
        return ASTNode('assignment', ident[1], [expr])

    def if_statement(self):
        self.eat('IF')
        self.eat('LPAREN')
        condition = self.expr()
        self.eat('RPAREN')
        true_block = self.block()
        false_block = None
        if self.lookahead('ELSE'):
            self.eat('ELSE')
            false_block = self.block()
        return ASTNode('if', '', [condition, true_block, false_block])

    def block(self):
        statements = []
        self.eat('LBRACE')
        while not self.lookahead('RBRACE'):
            statements.append(self.statement())
        self.eat('RBRACE')
        return ASTNode('block', '', statements)

    def statement(self):
        if self.lookahead('IF'):
            return self.if_statement()
        elif self.lookahead('IDENTIFIER'):
            if self.lookahead_next('EQUAL'):
                return self.assignment()
            else:
                return self.expr()
        elif self.lookahead('LBRACE'):
            return self.block()
        else:
            raise Exception(f"Unsupported or unexpected token: {self.tokens[self.position]}")
