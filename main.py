from scanner.tokenizer import Scanner
from parser.parser_1 import Parser

token_specs = [
    ('INT', r'\bint\b', True),  
    ('FLOAT', r'\bfloat\b', True), 
    ('IF', r'\bif\b', True),  
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*', False),  
    ('NUMBER', r'\d+', False),  
    ('PLUS', r'\+', False),  
    ('MINUS', r'-', False),  
    ('EQUAL', r'=', False),
    ('MULTIPLY',r'*',False)
]

scan = Scanner.scan_gen(token_specs)

tokens = scan('float varA = 3 * (5 - 2)')
print(tokens) 
parser = Parser(tokens)
ast = parser.parse()
print('\nSaida Parser\n')
print(ast)