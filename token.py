import re

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

def analizador_lexico(codigo):
    patrones = {
        'PALABRA_RESERVADA': r'\b(if|else|while|for|print)\b',
        'IDENTIFICADOR': r'[a-zA-Z_][a-zA-Z0-9_]*',
        'NUMERO': r'\d+',
        'OPERADOR': r'[+\-*/=]',
        'CADENA': r'\"[^\"]*\"',
        'SIMBOLO_ESPECIAL': r'[(),;{}]',
        'TABULACION': r'\t',
        'COMENTARIO': r'#.*$'
    }

    tokens = []

    while codigo:
        encontrado = False
        for tipo, patron in patrones.items():
            match = re.match(patron, codigo)
            if match and match.start() == 0:
                valor = match.group(0)
                if tipo != 'COMENTARIO' and tipo != 'TABULACION':
                    tokens.append(Token(tipo, valor))
                codigo = codigo[len(valor):]
                encontrado = True
                break

        if not encontrado:
            # Ignorar espacios
            if codigo[0] == ' ':
                codigo = codigo[1:]
            else:
                # Manejar caracteres no reconocidos
                print(f'Error: Carácter no reconocido - "{codigo[0]}"')
                codigo = codigo[1:]

    return tokens

# Ejemplo de uso
codigo = """
# Esto es un comentario
variable1 = 3 + 4 * variable2
if x == 5:
    print("Hola, mundo!")
"""

tokens = analizador_lexico(codigo)

for token in tokens:
    print(f'Tipo: {token.tipo}, Valor: {token.valor}')
