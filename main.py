from scanner.tokenizer import Scanner
from parser.parser_1 import Parser

token_specs = [
    ('INT', r'\bint\b', True),
    ('FLOAT', r'\bfloat\b', True),
    ('IF', r'\bif\b', True),
    ('THEN', r'\bthen\b', True),
    ('ELSE', r'\belse\b', True),
    ('ENDIF', r'\bendif\b', True), 
    ('FOR', r'\bfor\b', True),
    ('TO', r'\bto\b', True),
    ('NEXT', r'\bnext\b', True),
    ('STEP', r'\bstep\b', True),
    ('WHILE', r'\bwhile\b', True),
    ('WEND', r'\bwend\b', True),  
    ('DO', r'\bdo\b', True),
    ('LOOP', r'\bloop\b', True),
    ('FUNCTION', r'\bfunction\b', True),
    ('SUB', r'\bsub\b', True), 
    ('RETURN', r'\breturn\b', True),
    ('PRINT', r'\bprint\b', True),
    ('INPUT', r'\binput\b', True),
    ('LET', r'\blet\b', True),
    ('GOTO', r'\bgoto\b', True),
    ('GOSUB', r'\bgosub\b', True),
    ('DIM', r'\bdim\b', True),
    ('REM', r'\brem\b', True),  
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*', False),
    ('NUMBER', r'\d+', False),
    ('PLUS', r'\+', False),
    ('MINUS', r'-', False),
    ('MULTIPLY', r'\*', False),
    ('DIVIDE', r'/', False),
    ('EQUAL', r'=', False),
    ('LPAREN', r'\(', False),
    ('RPAREN', r'\)', False),
    ('LBRACE', r'\{', False),
    ('RBRACE', r'\}', False),
    ('COMMA', r'\,', False),
    ('SEMICOLON', r'\;', False),
    ('STRING', r'\"[^\"]*\"', False)  
]



scan = Scanner.scan_gen(token_specs)

tokens = scan('float varA = 3 * (5 - 2)')
print('\nSaida Scanner\n')
print(tokens) 
parser = Parser(tokens)
ast = parser.parse()
print('\nSaida Parser\n')
print(ast)