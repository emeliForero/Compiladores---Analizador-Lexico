import ply.yacc as yacc
from AnalizadorLexico import Lexer, AnalizadorLexico

#https://docs.python.org/es/3.9/library/html.parser.html?highlight=sintactico

class AnalizadorSintactico:
     
    tokens = Lexer.tokens
    
    precedence = (
        ('left','MAS','MENOS'),
        ('left','POR','DIVIDIDO'),
        ('right','UMENOS'),
        )
    
    def p_expresion_evaluar(t):
     'expresion : expresion MAS expresion'
     #   ^            ^      ^    ^
     #  t[0]         t[1]   t[2] t[3]
 
     t[0] = t[1] + t[3]





