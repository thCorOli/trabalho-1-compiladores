import unittest
import sys
sys.path.append('/root/Faculdade/compiladores/trab-1/')
from parser.parser_1 import Parser
from parser.ast_node import ASTNode

class TestParser(unittest.TestCase):

    def test_number(self):
        tokens = [('NUMBER', '42')]
        parser = Parser(tokens)
        result = parser.parse()
        expected = ASTNode('number', '42')
        self.assertEqual(repr(result), repr(expected))

    def test_simple_expression(self):
        tokens = [
            ('IDENTIFIER', 'x'), ('EQUAL', '='), ('NUMBER', '1'), 
            ('PLUS', '+'), ('NUMBER', '2')
        ]
        parser = Parser(tokens)
        result = parser.parse()
        expected = ASTNode('assignment', 'x', [
            ASTNode('op', '+', [
                ASTNode('number', '1'), 
                ASTNode('number', '2')
            ])
        ])
        self.assertEqual(repr(result), repr(expected))

    def test_if_statement(self):
        tokens = [
            ('IF', 'if'), ('LPAREN', '('), ('IDENTIFIER', 'x'), 
            ('EQUAL', '='), ('NUMBER', '1'), ('RPAREN', ')'), 
            ('LBRACE', '{'), ('IDENTIFIER', 'x'), ('EQUAL', '='), 
            ('NUMBER', '2'), ('RBRACE', '}'), ('ELSE', 'else'), 
            ('LBRACE', '{'), ('IDENTIFIER', 'x'), ('EQUAL', '='), 
            ('NUMBER', '3'), ('RBRACE', '}')
        ]
        parser = Parser(tokens)
        result = parser.parse()
        expected = ASTNode('if', '', [
            ASTNode('op', '=', [
                ASTNode('identifier', 'x'),
                ASTNode('number', '1')
            ]),
            ASTNode('block', '', [
                ASTNode('assignment', 'x', [ASTNode('number', '2')])
            ]),
            ASTNode('block', '', [
                ASTNode('assignment', 'x', [ASTNode('number', '3')])
            ])
        ])
        self.assertEqual(repr(result), repr(expected))

    def test_function_call(self):
        tokens = [
            ('IDENTIFIER', 'print'), ('LPAREN', '('), 
            ('IDENTIFIER', 'x'), ('RPAREN', ')')
        ]
        parser = Parser(tokens)
        result = parser.parse()
        expected = ASTNode('function_call', 'print', [
            ASTNode('identifier', 'x')
        ])
        self.assertEqual(repr(result), repr(expected))

if __name__ == '__main__':
    unittest.main()
