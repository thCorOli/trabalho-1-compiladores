import sys
sys.path.append('/root/Faculdade/compiladores/trab-1/')
from parser.parser_1 import Parser
from scanner.tokenizer import Scanner
import unittest

class TestParser(unittest.TestCase):
    def setUp(self) :
        token_specs = [
            ('NUMBER', r'\d+'), 
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'), 
            ('PLUS', r'\+'),
            ('MINUS', r'-'), 
            ('EQUAL', r'='),
            ('DIVIDE',r'/'),
            ('INT',r'int'),
        ]
        self.scan = Scanner.scan_gen(token_specs)
        
        
    def test_simple_assignment(self):
        result = self.scan("a = 12")
        parser = Parser.parse(result)
        print(parser)
        expected = []
        self.assertEqual(result, expected)

    def test_operation(self):
        result = self.scan("a = x / y - 1")
        parser = Parser.parse(result)
        print(parser)
        expected = []
        self.assertEqual(result, expected)


    def test_empty_input(self):
        result = self.scan("")
        parser = Parser.parse(result)
        print(parser)
        expected = []
        self.assertEqual(result, expected)

    def test_complex_expression(self):
        result = self.scan("varA = var2 + 3 * (5 - 2)")
        parser = Parser.parse(result)
        print(parser)
        expected = []
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()