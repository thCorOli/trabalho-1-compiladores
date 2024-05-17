from scanner.tokenizer import Scanner
from parser.parser_1 import Parser
from assets.token_specs import ts

# lê as especificações e gera o automato inicial
scan = Scanner.scan_gen(ts)

# lê o código fornecido
with open('code.txt', 'r', encoding='utf-8') as file:
    conteudo = file.read()
print('\n\nCódigo:\n')
print(conteudo)

# gera a lista de tokens presentes no codigo
tokens = scan(conteudo)
print('\n\nSaida Scanner:\n')
print(tokens)

# gera a arvore
parser = Parser(tokens)
ast = parser.parse()
print('\n\nSaida Parser:\n')
print(ast)
