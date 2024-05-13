import ply.lex as lex
import ply.yacc as yacc

# Lista de nomes de tokens. É essencial para o funcionamento do PLY.
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN'
)

# Regras de expressões regulares para tokens simples.
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Uma regra para números (vamos tratar todos como float para simplicidade).
def t_NUMBER(t):
    r'\d+(\.\d*)?'
    t.value = float(t.value)
    return t

# Uma regra para contabilizar números de linha.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Uma string contendo caracteres ignorados (espaços e tabs).
t_ignore = ' \t'

# Uma regra de erro para tokens inválidos.
def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir o lexer.
lexer = lex.lex()

# Regras de precedência para resolver ambiguidades envolvendo operadores não associativos.
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('nonassoc', 'UMINUS'),
)

# Definição das regras do parser.

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]

def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = p[1] * p[3]

def p_expression_divide(p):
    'expression : expression DIVIDE expression'
    if p[3] == 0:
        print("Erro: Divisão por zero.")
        p[0] = 0
    else:
        p[0] = p[1] / p[3]

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    if p:
        print("Erro de sintaxe na entrada!")
    else:
        print("Erro de sintaxe no fim do arquivo!")

# Construir o parser.
parser = yacc.yacc()

# Teste do parser
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
