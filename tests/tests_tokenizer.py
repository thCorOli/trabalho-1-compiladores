import unittest
from scanner.tokenizer import scan_gen

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        token_specs = [
            ('NUMBER', r'\d+'), 
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'), 
            ('PLUS', r'\+'),
            ('MINUS', r'-'), 
            ('EQUAL', r'='),
            ('DIVIDE',r'/'),
            ('INT',r'int'),
        ]
        self.scan = scan_gen(token_specs)

    def test_simple_assignment(self):
        result = self.scan("a = 12")
        expected = [('IDENTIFIER', 'a'), ('EQUAL', '='), ('NUMBER', '12')]
        self.assertEqual(result, expected)

    def test_operation(self):
        result = self.scan("a = x / y - 1")
        expected = [('IDENTIFIER', 'a'),('EQUAL', '='),('IDENTIFIER', 'x'), ('DIVIDE', '/'), ('IDENTIFIER', 'y'), ('MINUS', '-'), ('NUMBER', '1')]
        self.assertEqual(result, expected)


    def test_empty_input(self):
        result = self.scan("")
        expected = []
        self.assertEqual(result, expected)

    def test_complex_expression(self):
        result = self.scan("varA = var2 + 3 * (5 - 2)")
        expected = [('IDENTIFIER', 'varA'), ('EQUAL', '='), ('IDENTIFIER', 'var2'), ('PLUS', '+'), ('NUMBER', '3'),('NUMBER', '5'), ('MINUS', '-'), ('NUMBER', '2')]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()