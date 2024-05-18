from parser.ast_node import ASTNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        return self.program()

    def eat(self, token_type):
        if self.position < len(self.tokens) and self.tokens[self.position][0] == token_type:
            token = self.tokens[self.position]
            self.position += 1
            return token
        print(f"Expected token {token_type} but found {self.tokens[self.position][0]} at position {self.position}")
        raise Exception(f"Expected token {token_type} but found {self.tokens[self.position][0]}")

    def lookahead(self, token_type):
        return self.position < len(self.tokens) and self.tokens[self.position][0] == token_type

    def lookahead_next(self, token_type):
        return self.position + 1 < len(self.tokens) and self.tokens[self.position + 1][0] == token_type

    def program(self):
        statements = []
        while self.position < len(self.tokens):
            if self.lookahead('SUB'):
                statements.append(self.subroutine())
            else:
                statements.append(self.statement())
        return ASTNode('program', '', statements)

    def statement(self):
        if self.lookahead('IF'):
            return self.if_statement()
        elif self.lookahead('FOR'):
            return self.for_statement()
        elif self.lookahead('WHILE'):
            return self.while_statement()
        elif self.lookahead('SUB'):
            return self.subroutine()
        elif self.lookahead('FUNCTION'):
            return self.function()
        elif self.lookahead('IDENTIFIER'):
            if self.lookahead_next('EQUAL'):
                return self.assignment()
            else:
                return self.expr()
        elif self.lookahead('PRINT'):
            return self.print_statement()
        elif self.lookahead('RETURN'):
            return self.return_statement()
        elif self.lookahead('DIM'):
            return self.dim_statement()
        else:
            raise Exception(f"Unsupported or unexpected token: {self.tokens[self.position]}")

    def if_statement(self):
        self.eat('IF')
        condition = self.expr()
        self.eat('THEN')
        true_block = self.block()
        false_block = None
        if self.lookahead('ELSE'):
            self.eat('ELSE')
            false_block = self.block()
        self.eat('END')
        self.eat('IF')
        return ASTNode('if', '', [condition, true_block, false_block])

    def for_statement(self):
        self.eat('FOR')
        init = self.assignment()
        self.eat('TO')
        end = self.expr()
        step = None
        if self.lookahead('STEP'):
            self.eat('STEP')
            step = self.expr()
        body = self.block()
        self.eat('NEXT')
        return ASTNode('for', '', [init, end, step, body])

    def while_statement(self):
        self.eat('WHILE')
        condition = self.expr()
        body = self.block()
        self.eat('WEND')
        return ASTNode('while', '', [condition, body])

    def subroutine(self):
        self.eat('SUB')
        sub_name = self.eat('IDENTIFIER')
        self.eat('LPAREN')
        params = self.parameters()
        self.eat('RPAREN')
        self.eat('AS')
        return_type = self.eat('IDENTIFIER')  # Assuming return type
        body = self.block()
        self.eat('END')
        self.eat('SUB')
        return ASTNode('subroutine', sub_name[1], [params, ASTNode('type', return_type[1]), body])

    def function(self):
        self.eat('FUNCTION')
        func_name = self.eat('IDENTIFIER')
        self.eat('LPAREN')
        params = self.parameters()
        self.eat('RPAREN')
        self.eat('AS')
        return_type = self.eat('IDENTIFIER')  # Assuming return type
        body = self.block()
        self.eat('END')
        self.eat('FUNCTION')
        return ASTNode('function', func_name[1], [params, ASTNode('type', return_type[1]), body])

    def parameters(self):
        params = []
        while not self.lookahead('RPAREN'):
            if self.lookahead('DIM'):
                self.eat('DIM')
            param_name = self.eat('IDENTIFIER')[1]
            if self.lookahead('AS'):
                self.eat('AS')
                param_type = self.eat(self.tokens[self.position][0])[1]
                params.append(ASTNode('param', param_name, [ASTNode('type', param_type)]))
            else:
                params.append(ASTNode('param', param_name))
            if self.lookahead('COMMA'):
                self.eat('COMMA')
        return ASTNode('parameters', '', params)

    def block(self):
        statements = []
        while self.position < len(self.tokens) and not (self.lookahead('END') or self.lookahead('ELSE') or self.lookahead('NEXT') or self.lookahead('WEND')):
            statements.append(self.statement())
        return ASTNode('block', '', statements)

    def assignment(self):
        ident = self.eat('IDENTIFIER')
        self.eat('EQUAL')
        expr = self.expr()
        return ASTNode('assignment', ident[1], [expr])

    def print_statement(self):
        self.eat('PRINT')
        expr = self.expr()
        return ASTNode('print', '', [expr])

    def return_statement(self):
        self.eat('RETURN')
        expr = self.expr()
        return ASTNode('return', '', [expr])

    def dim_statement(self):
        self.eat('DIM')
        ident = self.eat('IDENTIFIER')
        self.eat('AS')
        data_type = self.eat(self.tokens[self.position][0])[1]
        return ASTNode('dim', ident[1], [ASTNode('type', data_type)])

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
        elif self.lookahead('STRING'):
            return ASTNode('string', self.eat('STRING')[1])
        elif self.lookahead('BYTE'):
            return ASTNode('type', self.eat('BYTE')[1])
        else:
            raise Exception(f"Unexpected token: {self.tokens[self.position]}")

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
