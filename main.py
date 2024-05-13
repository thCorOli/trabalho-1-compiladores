from scanner.tokenizer import scan_gen
from parser.parser_1 import Parser
token_specs = [
    ('NUMBER', r'\d+'), 
    ('IDENTIFIER',r'int'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'), 
    ('PLUS', r'\+'),
    ('MINUS', r'-'), 
    ('EQUAL', r'=')
]

scan = scan_gen(token_specs)

tokens = scan('varA = var2 + 3 * (5 - 2)')
#print(tokens) 
parser = Parser(tokens)
ast = parser.parse()
print(ast)