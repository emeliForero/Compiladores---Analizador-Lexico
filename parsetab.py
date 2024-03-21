
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftPORDIVIDIDOrightUMENOSCADENA COMENTARIO COMENTARIO_MULTILINEA DEF DIVIDIDO IDENTIFICADOR IF MAS MENOS NEWLINE NUMERO OPERADOR PALABRA_RESERVADA POR SIMBOLO_ESPECIALexpresion : expresion MAS expresion\n                     | expresion MENOS expresion\n                     | expresion POR expresion\n                     | expresion DIVIDIDO expresionexpresion : MENOS expresion %prec UMENOSexpresion : NUMERO\n                     | IDENTIFICADOR\n                     | CADENA\n                     | PALABRA_RESERVADAexpresion : "(" expresion ")"instruccion : DEF IDENTIFICADOR \'(\' parametros \')\' \':\' cuerpo_funcionparametros : IDENTIFICADOR\n                      | parametros \',\' IDENTIFICADORcuerpo_funcion : instruccionesexpresion : IF expresion \':\' cuerpo_condicionalcuerpo_condicional : instruccionesexpresion : IDENTIFICADOR \'(\' argumentos \')\' argumentos : expresion\n                      | argumentos \',\' expresioncomentario : COMENTARIO\n                    | COMENTARIO_MULTILINEAinstrucciones : instruccion\n                        | comentario\n                        | instrucciones instruccion\n                        | instrucciones comentario'
    
_lr_action_items = {'MENOS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,25,26,27,28,29,30,32,33,34,35,36,45,46,],[2,10,2,-6,-7,-8,-9,2,2,2,2,2,2,-5,2,10,10,-1,-2,-3,-4,10,-10,-17,2,-15,-16,-22,-23,-20,-21,10,-24,-25,-11,-14,]),'NUMERO':([0,2,7,8,9,10,11,12,14,26,],[3,3,3,3,3,3,3,3,3,3,]),'IDENTIFICADOR':([0,2,7,8,9,10,11,12,14,26,31,38,42,],[4,4,4,4,4,4,4,4,4,4,37,39,44,]),'CADENA':([0,2,7,8,9,10,11,12,14,26,],[5,5,5,5,5,5,5,5,5,5,]),'PALABRA_RESERVADA':([0,2,7,8,9,10,11,12,14,26,],[6,6,6,6,6,6,6,6,6,6,]),'(':([0,2,4,7,8,9,10,11,12,14,26,37,],[7,7,14,7,7,7,7,7,7,7,7,38,]),'IF':([0,2,7,8,9,10,11,12,14,26,],[8,8,8,8,8,8,8,8,8,8,]),'$end':([1,3,4,5,6,13,17,18,19,20,23,25,27,28,29,30,32,33,35,36,45,46,],[0,-6,-7,-8,-9,-5,-1,-2,-3,-4,-10,-17,-15,-16,-22,-23,-20,-21,-24,-25,-11,-14,]),'MAS':([1,3,4,5,6,13,15,16,17,18,19,20,22,23,25,27,28,29,30,32,33,34,35,36,45,46,],[9,-6,-7,-8,-9,-5,9,9,-1,-2,-3,-4,9,-10,-17,-15,-16,-22,-23,-20,-21,9,-24,-25,-11,-14,]),'POR':([1,3,4,5,6,13,15,16,17,18,19,20,22,23,25,27,28,29,30,32,33,34,35,36,45,46,],[11,-6,-7,-8,-9,-5,11,11,11,11,-3,-4,11,-10,-17,-15,-16,-22,-23,-20,-21,11,-24,-25,-11,-14,]),'DIVIDIDO':([1,3,4,5,6,13,15,16,17,18,19,20,22,23,25,27,28,29,30,32,33,34,35,36,45,46,],[12,-6,-7,-8,-9,-5,12,12,12,12,-3,-4,12,-10,-17,-15,-16,-22,-23,-20,-21,12,-24,-25,-11,-14,]),')':([3,4,5,6,13,15,17,18,19,20,21,22,23,25,27,28,29,30,32,33,34,35,36,39,40,44,45,46,],[-6,-7,-8,-9,-5,23,-1,-2,-3,-4,25,-18,-10,-17,-15,-16,-22,-23,-20,-21,-19,-24,-25,-12,41,-13,-11,-14,]),':':([3,4,5,6,13,16,17,18,19,20,23,25,27,28,29,30,32,33,35,36,41,45,46,],[-6,-7,-8,-9,-5,24,-1,-2,-3,-4,-10,-17,-15,-16,-22,-23,-20,-21,-24,-25,43,-11,-14,]),',':([3,4,5,6,13,17,18,19,20,21,22,23,25,27,28,29,30,32,33,34,35,36,39,40,44,45,46,],[-6,-7,-8,-9,-5,-1,-2,-3,-4,26,-18,-10,-17,-15,-16,-22,-23,-20,-21,-19,-24,-25,-12,42,-13,-11,-14,]),'DEF':([24,28,29,30,32,33,35,36,43,45,46,],[31,31,-22,-23,-20,-21,-24,-25,31,-11,31,]),'COMENTARIO':([24,28,29,30,32,33,35,36,43,45,46,],[32,32,-22,-23,-20,-21,-24,-25,32,-11,32,]),'COMENTARIO_MULTILINEA':([24,28,29,30,32,33,35,36,43,45,46,],[33,33,-22,-23,-20,-21,-24,-25,33,-11,33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([0,2,7,8,9,10,11,12,14,26,],[1,13,15,16,17,18,19,20,22,34,]),'argumentos':([14,],[21,]),'cuerpo_condicional':([24,],[27,]),'instrucciones':([24,43,],[28,46,]),'instruccion':([24,28,43,46,],[29,35,29,35,]),'comentario':([24,28,43,46,],[30,36,30,36,]),'parametros':([38,],[40,]),'cuerpo_funcion':([43,],[45,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expresion","S'",1,None,None,None),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_evaluar_binaria','AnalizadorSintactico.py',19),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_evaluar_binaria','AnalizadorSintactico.py',20),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_evaluar_binaria','AnalizadorSintactico.py',21),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_evaluar_binaria','AnalizadorSintactico.py',22),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_umenos','AnalizadorSintactico.py',36),
  ('expresion -> NUMERO','expresion',1,'p_expresion_numero_identificador','AnalizadorSintactico.py',40),
  ('expresion -> IDENTIFICADOR','expresion',1,'p_expresion_numero_identificador','AnalizadorSintactico.py',41),
  ('expresion -> CADENA','expresion',1,'p_expresion_numero_identificador','AnalizadorSintactico.py',42),
  ('expresion -> PALABRA_RESERVADA','expresion',1,'p_expresion_numero_identificador','AnalizadorSintactico.py',43),
  ('expresion -> ( expresion )','expresion',3,'p_expresion_parentesis','AnalizadorSintactico.py',47),
  ('instruccion -> DEF IDENTIFICADOR ( parametros ) : cuerpo_funcion','instruccion',7,'p_instruccion_funcion','AnalizadorSintactico.py',51),
  ('parametros -> IDENTIFICADOR','parametros',1,'p_parametros','AnalizadorSintactico.py',55),
  ('parametros -> parametros , IDENTIFICADOR','parametros',3,'p_parametros','AnalizadorSintactico.py',56),
  ('cuerpo_funcion -> instrucciones','cuerpo_funcion',1,'p_cuerpo_funcion','AnalizadorSintactico.py',60),
  ('expresion -> IF expresion : cuerpo_condicional','expresion',4,'p_expresion_condicional','AnalizadorSintactico.py',64),
  ('cuerpo_condicional -> instrucciones','cuerpo_condicional',1,'p_cuerpo_condicional','AnalizadorSintactico.py',68),
  ('expresion -> IDENTIFICADOR ( argumentos )','expresion',4,'p_expresion_llamada_funcion','AnalizadorSintactico.py',72),
  ('argumentos -> expresion','argumentos',1,'p_argumentos','AnalizadorSintactico.py',76),
  ('argumentos -> argumentos , expresion','argumentos',3,'p_argumentos','AnalizadorSintactico.py',77),
  ('comentario -> COMENTARIO','comentario',1,'p_comentario','AnalizadorSintactico.py',84),
  ('comentario -> COMENTARIO_MULTILINEA','comentario',1,'p_comentario','AnalizadorSintactico.py',85),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','AnalizadorSintactico.py',89),
  ('instrucciones -> comentario','instrucciones',1,'p_instrucciones','AnalizadorSintactico.py',90),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','AnalizadorSintactico.py',91),
  ('instrucciones -> instrucciones comentario','instrucciones',2,'p_instrucciones','AnalizadorSintactico.py',92),
]