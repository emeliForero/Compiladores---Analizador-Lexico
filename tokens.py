import ply.lex as lex

class Token:
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
        'COMENTARIO'
    ]

    # Expresiones regulares  
    t_PALABRA_RESERVADA = r'\b(if|else|while|for|print|true|false|class|int|try|catch|none|and|async|not|or|import|as|def|return)\b'
    t_IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z0-9_]*'
    t_NUMERO = r'\d+'
    t_OPERADOR = r'[+\-*/=]'
    t_CADENA = r'\"[^\"]*\"'
    t_SIMBOLO_ESPECIAL = r'[(),:;{}[\]]'
    t_COMENTARIO = r'\#.*'

    # Ignorar espacios
    t_ignore = ' '

    # Caracter no reconocido
    def t_error(self, t):
        print(f"Carácter no reconocido: '{t.value[0]}' en la línea {t.lineno}")
        t.lexer.skip(1)

    # Saltos de línea
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

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

#Tokens encontrados
for token in lexer.lexer:
    token_obj = Token(token.type, token.value, token.lineno)
    #print(f'Tipo: {token_obj.tipo}, Valor: {token_obj.valor}, Línea: {token_obj.linea}')
    print(f'{token_obj.tipo}: {token_obj.valor}')

