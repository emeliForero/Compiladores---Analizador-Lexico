import ply.yacc as yacc
from AnalizadorLexico import Lexer

class LlamadaFuncion:
    def __init__(self, nombre, argumentos):
        self.nombre = nombre
        self.argumentos = argumentos

class AnalizadorSintactico:
    tokens = Lexer.tokens

    precedence = (
        ('left', 'MAS', 'MENOS'),
        ('left', 'POR', 'DIVIDIDO'),
        ('right', 'UMENOS'),
    )

    def p_expresion_evaluar_binaria(self, t):
        '''expresion : expresion MAS expresion
                     | expresion MENOS expresion
                     | expresion POR expresion
                     | expresion DIVIDIDO expresion'''
        if len(t) == 4:  # Si se trata de una operación binaria
            if t[2] == '+':
                t[0] = t[1] + t[3]
            elif t[2] == '-':
                t[0] = t[1] - t[3]
            elif t[2] == '*':
                t[0] = t[1] * t[3]
            elif t[2] == '/':
                if t[3] == 0:
                    raise ZeroDivisionError("División por cero")
                t[0] = t[1] / t[3]

    def p_expresion_umenos(self, t):
        'expresion : MENOS expresion %prec UMENOS'
        t[0] = -t[2]

    def p_expresion_numero_identificador(self, t):
        '''expresion : NUMERO
                     | IDENTIFICADOR
                     | CADENA
                     | PALABRA_RESERVADA'''
        t[0] = t[1]

    def p_expresion_parentesis(self, t):
        'expresion : "(" expresion ")"'
        t[0] = t[2]

    def p_instruccion_funcion(self, t):
        '''instruccion : DEF IDENTIFICADOR '(' parametros ')' ':' cuerpo_funcion'''
        pass

    def p_parametros(self, t):
        '''parametros : IDENTIFICADOR
                      | parametros ',' IDENTIFICADOR'''
        pass

    def p_cuerpo_funcion(self, t):
        '''cuerpo_funcion : instrucciones'''
        pass

    def p_expresion_condicional(self, t):
        '''expresion : IF expresion ':' cuerpo_condicional'''
        pass

    def p_cuerpo_condicional(self, t):
        '''cuerpo_condicional : instrucciones'''
        pass

    def p_expresion_llamada_funcion(self, t):
        '''expresion : IDENTIFICADOR '(' argumentos ')' '''
        t[0] = LlamadaFuncion(t[1], t[3])

    def p_argumentos(self, t):
        '''argumentos : expresion
                      | argumentos ',' expresion'''
        if len(t) == 2:
            t[0] = [t[1]]
        else:
            t[0] = t[1] + [t[3]]

    def p_comentario(self, t):
        '''comentario : COMENTARIO
                    | COMENTARIO_MULTILINEA'''
        pass

    def p_instrucciones(self, t):
        '''instrucciones : instruccion
                        | comentario
                        | instrucciones instruccion
                        | instrucciones comentario'''
        if len(t) == 2:
            t[0] = [t[1]]
        else:
            t[0] = t[1] + [t[2]]        

    def p_error(self, t):
        if t:
            print(f"Error de sintaxis en la línea {t.lineno}: Token inesperado '{t.value}'")
        else:
            print("Error de sintaxis al final del archivo")
        self.parser.restart()

    def __init__(self):
        # Crear una instancia de la clase Lexer
        lexer = Lexer()
        # Ejecutar el análisis léxico con el archivo "codigo.txt"
        lexer.analizar_archivo("codigo.txt")
        # Obtener el lexer generado
        analizador_lexico = lexer.lexer
        # Crear el parser yacc
        self.parser = yacc.yacc(module=self)
        # Definir el código a analizar
        with open("codigo.txt", "r") as archivo:
            codigo = archivo.read()
        # Ejecutar el análisis sintáctico con el código dado
        self.parser.parse(codigo)

# Crear una instancia de AnalizadorSintactico para ejecutarlo
AnalizadorSintactico()