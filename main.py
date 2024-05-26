from assets.utils import read_file
from scanner.tokenizer import Scanner
from parser_1.parser_1 import Parser
from assets.token_specs import ts


scan = Scanner.scan_gen(ts)
content = read_file("models/parser/parser.txt")
tokens = scan(content)
parser = Parser(tokens)
ast = parser.parse()
print(ast)
