import ply.lex as lex

class AnalizadorLexico:
    def __init__(self, tipo, valor, linea):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea

class Lexer:
    tokens = [
        'PALABRA_RESERVADA',
        'IDENTIFICADOR',
        'NUMERO',
        'OPERADOR',
        'CADENA',
        'SIMBOLO_ESPECIAL',
        'COMENTARIO',
        'MAS',
        'MENOS',
        'POR',
        'DIVIDIDO',
        'DEF',
        'IF',
        'NEWLINE',
        'COMENTARIO_MULTILINEA'
    ]

    # Expresiones regulares  
    t_PALABRA_RESERVADA = r'\b(if|else|while|for|print|true|false|class|int|try|catch|none|and|async|not|or|import|as|def|return)\b'
    t_IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z0-9_]*'
    t_NUMERO = r'\d+'
    t_OPERADOR = r'[+\-*/=]'
    t_CADENA = r'"[^"]*"'
    t_SIMBOLO_ESPECIAL = r'[(),:;{}<=>\[\]]'
    t_COMENTARIO = r'\#.*'
    t_MAS = r'\+'
    t_MENOS = r'-'
    t_POR = r'\*'
    t_DIVIDIDO = r'/'
    t_DEF = r'def'
    t_IF = r'if'
    t_NEWLINE = r'\n+'
    t_COMENTARIO_MULTILINEA = r'/\*(.|\n)*?\*/'

    # Ignorar espacios
    t_ignore = ' '

    # Caracter no reconocido
    def t_error(self, t):
        print(f"Carácter no reconocido: '{t.value[0]}' en la línea {t.lineno}")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def __init__(self, **kwargs):
        self.build(**kwargs)

    def analizar_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            codigo = archivo.read()
            self.lexer.input(codigo)

lexer = Lexer()
lexer.analizar_archivo("codigo.txt")
analizador = lexer.lexer

# Tokens encontrados
def token_final():
    for token in analizador:
        token_obj = AnalizadorLexico(token.type, token.value, token.lineno)
        print(f'{token_obj.tipo}: {token_obj.valor}')
    return analizador