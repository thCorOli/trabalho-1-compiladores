ts = [
    ('INT', r'(?i)\bint\b', True),
    ('FLOAT', r'(?i)\bfloat\b', True),
    ('IF', r'(?i)\bif\b', True),
    ('THEN', r'(?i)\bthen\b', True),
    ('ELSE', r'(?i)\belse\b', True),
    ('ENDIF', r'(?i)\bendif\b', True), 
    ('FOR', r'(?i)\bfor\b', True),
    ('TO', r'(?i)\bto\b', True),
    ('NEXT', r'(?i)\bnext\b', True),
    ('STEP', r'(?i)\bstep\b', True),
    ('WHILE', r'(?i)\bwhile\b', True),
    ('WEND', r'(?i)\bwend\b', True),  
    ('DO', r'(?i)\bdo\b', True),
    ('LOOP', r'(?i)\bloop\b', True),
    ('FUNCTION', r'(?i)\bfunction\b', True),
    ('SUB', r'(?i)\bsub\b', True), 
    ('END', r'(?i)\bend\b', True),
    ('RETURN', r'(?i)\breturn\b', True),
    ('PRINT', r'(?i)\bprint\b', True),
    ('INPUT', r'(?i)\binput\b', True),
    ('LET', r'(?i)\blet\b', True),
    ('GOTO', r'(?i)\bgoto\b', True),
    ('GOSUB', r'(?i)\bgosub\b', True),
    ('DIM', r'(?i)\bdim\b', True),
    ('REM', r'(?i)\brem\b', True),  
    ('AS', r'(?i)\bas\b', True),
    ('BYTE', r'(?i)\bbyte\b', True),
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