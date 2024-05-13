from tokenizer import scan_gen
token_specs = [
    ('Int', r'\d+'), 
    ('IDENTIFIER',r'int'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'), 
    ('PLUS', r'\+'),
    ('MINUS', r'-'), 
    ('EQUAL', r'=')
]

scan = scan_gen(token_specs)

tokens = scan('varA = var2 + 3 * (5 - 2)')
print(tokens) 